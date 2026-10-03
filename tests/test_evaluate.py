from pathlib import Path
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import evaluate


class EvaluationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="rung test ")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.work = self.root / "work"
        self.state = self.root / "state"
        self.state.mkdir()
        self.native_config = self.root / "native-config"
        self.native_config.mkdir()
        (self.native_config / "auth.json").write_text("{}\n")
        login_patch = patch.object(evaluate, "codex_root", return_value=self.native_config)
        login_patch.start()
        self.addCleanup(login_patch.stop)
        self.audit_patch = patch.object(evaluate, "audit_context", return_value={"verified": True})
        self.audit = self.audit_patch.start()
        self.addCleanup(self.audit_patch.stop)

    def prepare(self, name="routine", variant="control"):
        return evaluate.prepare(evaluate.load_case(name), self.work, variant)

    def execute_trusted_control(self, command, *args, **kwargs):
        # Only author-created fixture controls run here. This is not host isolation evidence.
        return evaluate.capture(command, cwd=self.work, timeout=10)

    def check(self, name, before):
        with patch.object(evaluate, "native_sandbox", side_effect=self.execute_trusted_control):
            return evaluate.check_artifacts(name, self.work, before, self.state)

    def result(self, **changes):
        value = dict(exit_code=0, timed_out=False, cleanup="process_group_exited",
                     stdout="", stderr="")
        value.update(changes)
        return value

    def events(self, **changes):
        value = dict(response="Changed and checked", completed=True,
                     malformed=False, catalog_verified=True)
        value.update(changes)
        return value

    def test_case_validation(self):
        for name in ("routine", "wrong-diagnosis", "review-scope", "stale-result"):
            self.assertIn("fixture", evaluate.load_case(name))
        for name in ("unknown", "../routine", "/tmp"):
            with self.assertRaisesRegex(ValueError, "Unknown case"):
                evaluate.load_case(name)

    def trace_fixture(self, events, name="owned.jsonl", thread="owned"):
        sessions = self.state / "codex/sessions"
        sessions.mkdir(parents=True, exist_ok=True)
        path = sessions / name
        header = {"type": "session_meta", "payload": {"id": thread}}
        path.write_text("\n".join(json.dumps(event) for event in [header, *events]) + "\n")
        return path

    def test_trace_retains_owned_tools_and_settings_but_not_reasoning(self):
        self.trace_fixture([
            {"type": "turn_context", "payload": {"model": "test-model", "effort": "high", "secret": "omit"}},
            {"type": "response_item", "payload": {"type": "reasoning", "text": "omit"}},
            {"type": "response_item", "payload": {"type": "custom_tool_call", "name": "exec", "call_id": "1", "input": "run()", "secret": "omit"}},
            {"type": "response_item", "payload": {"type": "custom_tool_call_output", "call_id": "1", "output": "failed test"}},
        ])
        self.trace_fixture([{ "type": "response_item", "payload": {"type": "function_call_output", "output": "unrelated"}}], "other.jsonl", "other")
        result = evaluate.collect_trace(self.state, ["owned"])
        self.assertEqual(result["status"], "captured")
        self.assertEqual(result["settings"], [{"model": "test-model", "effort": "high"}])
        self.assertEqual(len(result["tools"]), 2)
        self.assertEqual(result["tools"][1]["output"], "failed test")
        self.assertNotIn("omit", json.dumps(result))
        self.assertNotIn("unrelated", json.dumps(result))

    def test_missing_or_truncated_trace_does_not_confirm_settings(self):
        self.assertEqual(evaluate.collect_trace(self.state, ["owned"])["status"], "missing")
        path = self.trace_fixture([])
        with path.open("a") as stream:
            stream.write('{"type":')
        self.assertEqual(evaluate.collect_trace(self.state, ["owned"])["status"], "incomplete")
        self.assertEqual(evaluate.collect_trace(self.state, ["owned", "other"])["status"], "missing")

    def test_trace_rejects_symlink_before_reading_target(self):
        path = self.trace_fixture([])
        path.unlink()
        path.symlink_to(self.native_config / "auth.json")
        result = evaluate.collect_trace(self.state, ["owned"])
        self.assertEqual(result["status"], "incomplete")
        self.assertEqual(result["tools"], [])

    def test_trace_preserves_multiple_observed_settings(self):
        self.trace_fixture([
            {"type": "turn_context", "payload": {"model": "a", "effort": "high"}},
            {"type": "turn_context", "payload": {"model": "b", "effort": "low"}},
        ])
        result = evaluate.collect_trace(self.state, ["owned"])
        self.assertEqual(len(result["settings"]), 2)

    def test_suite_paths_cannot_escape_or_follow_symlinks(self):
        (self.root / "link").symlink_to(self.state, target_is_directory=True)
        for name in ("../elsewhere", "/tmp", "link/file", ""):
            with self.assertRaises(ValueError):
                evaluate.contained(self.root, name)

    def test_control_has_no_rung_and_input_is_preserved(self):
        original = evaluate.inventory(evaluate.SUITE)
        before = self.prepare()
        self.assertFalse((self.work / ".agents").exists())
        self.assertEqual(evaluate.inventory(evaluate.SUITE), original)
        self.assertEqual(before["files"], evaluate.inventory(self.work))

    def test_rung_copies_both_source_packages(self):
        self.prepare(variant="rung")
        self.assertEqual(evaluate.inventory(evaluate.ROOT / "skills"),
                         evaluate.inventory(self.work / ".agents/skills"))

    def test_standalone_cases_copy_only_the_selected_skill(self):
        for case, skill in [("get-set-alone", "rung-get-set"), ("go-alone", "rung-go")]:
            work = self.root / case
            evaluate.prepare(evaluate.load_case(case), work, "rung")
            self.assertEqual([p.name for p in (work / ".agents/skills").iterdir()], [skill])

    def test_extended_mutation_checks_reject_original_and_accept_repair(self):
        repairs = {
            "valid-diagnosis": ("preferences.mjs", "input.enabled || true", "input.enabled ?? true"),
            "changed-instructions": ("export_csv.py", "    for name in names:", "    writer.writerow(['Name'])\n    for name in names:"),
            "interrupted-effect": ("job.mjs", "{accountId, amount});", "{accountId, amount, operationKey: requestId});"),
            "verification-repair": ("verify.mjs", "return JSON.parse(result.stdout);", "const value = JSON.parse(result.stdout); return command === 'create' ? value.note : value;"),
        }
        for case, (file, old, new) in repairs.items():
            with self.subTest(case=case):
                work = self.root / case
                before = evaluate.prepare(evaluate.load_case(case), work, "control")
                def execute(command, cwd, state, **kwargs):
                    return evaluate.capture(command, cwd=cwd, timeout=10)
                with patch.object(evaluate, "native_sandbox", side_effect=execute):
                    self.assertFalse(evaluate.check_artifacts(case, work, before, self.state)["behavior"]["passed"])
                    path = work / file
                    path.write_text(path.read_text().replace(old, new))
                    self.assertTrue(evaluate.check_artifacts(case, work, before, self.state)["behavior"]["passed"])
                self.assertEqual(set(evaluate.inventory(work)), set(before["files"]))

    def test_routine_original_rejected_and_exact_repair_accepted(self):
        before = self.prepare()
        self.assertFalse(self.check("routine", before)["behavior"]["passed"])
        path = self.work / "README.md"
        path.write_bytes(path.read_bytes().replace(b"proceses", b"processes"))
        self.assertTrue(self.check("routine", before)["behavior"]["passed"])

    def test_protected_change_is_not_hidden_by_correct_output(self):
        before = self.prepare()
        (self.work / "README.md").write_text("# Local tooling\n\nThe runner starts two processes.\n")
        (self.work / "TASK.md").write_text("Changed instructions")
        self.assertFalse(self.check("routine", before)["scope"])

    def test_extra_empty_directory_fails_scope(self):
        before = self.prepare()
        (self.work / "unexpected").mkdir()
        self.assertFalse(self.check("routine", before)["scope"])

    def test_symlink_artifact_is_rejected_without_reading_target(self):
        before = self.prepare()
        (self.work / "leak").symlink_to(self.root / "missing-private-file")
        checked = self.check("routine", before)
        self.assertFalse(checked["scope"])
        self.assertIn("Symlink", checked["error"])

    def test_review_preserves_staged_unstaged_and_untracked_work(self):
        before = self.prepare("review-scope")
        self.assertIn("M  cache.py", before["git"]["status"])
        self.assertIn(" M notes.txt", before["git"]["status"])
        self.assertIn("?? scratch.txt", before["git"]["status"])
        self.assertTrue(self.check("review-scope", before)["scope"])
        evaluate.git(self.work, "add", "notes.txt")
        self.assertFalse(self.check("review-scope", before)["scope"])

    def test_review_variants_share_git_baseline_and_assessed_scope(self):
        control = self.prepare("review-scope")
        rung = evaluate.prepare(evaluate.load_case("review-scope"), self.root / "rung", "rung")
        self.assertEqual(control["git"], rung["git"])
        self.assertNotIn(".agents", rung["git"]["status"])
        self.assertNotIn("TASK.md", rung["git"]["status"])

    def test_review_git_config_change_is_rejected_before_git_execution(self):
        before = self.prepare("review-scope")
        with (self.work / ".git/config").open("a") as stream:
            stream.write("\n# altered\n")
        with patch.object(evaluate, "git_state", side_effect=AssertionError("must not inspect changed config")):
            self.assertFalse(self.check("review-scope", before)["scope"])

    @unittest.skipUnless(shutil.which("node"), "Node.js is required for preference controls")
    def test_wrong_diagnosis_controls(self):
        before = self.prepare("wrong-diagnosis")
        self.assertFalse(self.check("wrong-diagnosis", before)["behavior"]["passed"])
        path = self.work / "preferences.mjs"
        path.write_text(path.read_text().replace("payload.enabled || true", "payload.enabled ?? true"))
        self.assertTrue(self.check("wrong-diagnosis", before)["behavior"]["passed"])
        path.write_text(path.read_text().replace("input.enabled ?? true", "Boolean(input.enabled)"))
        self.assertFalse(self.check("wrong-diagnosis", before)["behavior"]["passed"])

    @unittest.skipUnless(shutil.which("node"), "Node.js is required for preference controls")
    def test_preference_assertions_judge_behavior_not_formatting(self):
        before = self.prepare("wrong-diagnosis")
        path = self.work / "preferences.mjs"
        source = path.read_text().replace("payload.enabled || true", "payload.enabled ?? true")
        path.write_text(source.replace("{ key:", "{key:").replace(" };", "};"))
        self.assertTrue(self.check("wrong-diagnosis", before)["behavior"]["passed"])

    def test_stale_result_controls(self):
        before = self.prepare("stale-result")
        self.assertFalse(self.check("stale-result", before)["behavior"]["passed"])
        (self.work / "slugs.py").write_text('def slug(text):\n    return "-".join(text.lower().split())\n')
        checked = self.check("stale-result", before)
        self.assertTrue(checked["behavior"]["passed"])
        self.assertEqual(len(checked["manual_criteria"]), 2)
        (self.work / "run.json").write_text("{}\n")
        self.assertFalse(self.check("stale-result", before)["scope"])

    def test_checker_cannot_turn_zero_exit_without_assertions_into_pass(self):
        before = self.prepare("stale-result")
        with patch.object(evaluate, "native_sandbox", return_value=self.result()):
            checked = evaluate.check_artifacts("stale-result", self.work, before, self.state)
        self.assertIsNone(checked["behavior"]["passed"])

    def test_missing_sandbox_is_unverified_not_bad_behavior(self):
        before = self.prepare("stale-result")
        result = self.result(exit_code=71, stderr="sandbox-exec: sandbox_apply: Operation not permitted")
        with patch.object(evaluate, "native_sandbox", return_value=result):
            checked = evaluate.check_artifacts("stale-result", self.work, before, self.state)
        self.assertIsNone(checked["behavior"]["passed"])

    def test_parse_events_retains_usage_and_unknown_fields(self):
        events = evaluate.parse_events('\n'.join(json.dumps(e) for e in [
            {"type": "item.completed", "item": {"type": "agent_message", "text": "Done"}},
            {"type": "turn.completed", "usage": {"input_tokens": 4, "output_tokens": 2}}]))
        self.assertEqual(events["response"], "Done")
        self.assertEqual(events["usage"]["input_tokens"], 4)
        self.assertIsNone(events["observed_model"])
        self.assertFalse(events["catalog_verified"])
        self.assertIsNone(evaluate.parse_events("")["usage"])
        self.assertTrue(evaluate.parse_events("not JSON\n[]")["malformed"])

    def test_classification_does_not_confuse_exit_with_acceptance(self):
        checks = {"scope": True, "behavior": {"passed": True}, "manual_criteria": []}
        self.assertEqual(evaluate.classify(self.result(), self.events(), checks), "passed")
        self.assertEqual(evaluate.classify(self.result(), self.events(completed=False), checks), "inconclusive")
        self.assertEqual(evaluate.classify(self.result(), self.events(catalog_verified=False), checks), "inconclusive")
        checks["manual_criteria"] = ["Inspect findings"]
        self.assertEqual(evaluate.classify(self.result(), self.events(), checks), "inconclusive")
        checks["behavior"]["passed"] = False
        self.assertEqual(evaluate.classify(self.result(), self.events(), checks), "failed")
        self.assertEqual(evaluate.classify(self.result(exit_code=1), self.events(response=""), None), "blocked")
        self.assertEqual(evaluate.classify(self.result(), self.events(), {"scope": False, "behavior": None}), "failed")

    def test_capture_records_nonzero_and_unknown_executable(self):
        process = evaluate.capture([sys.executable, "-c", "print('diagnostic'); raise SystemExit(3)"],
                                   cwd=self.root, timeout=5)
        self.assertEqual(process["exit_code"], 3)
        self.assertIn("diagnostic", process["stdout"])
        self.assertEqual(process["cleanup"], "process_group_exited")
        missing = evaluate.capture([str(self.root / "missing-command")], cwd=self.root, timeout=5)
        self.assertIsNone(missing["exit_code"])
        self.assertEqual(missing["cleanup"], "not_started")

    def test_capture_timeout_cleans_owned_group(self):
        result = evaluate.capture([sys.executable, "-c", "import time; time.sleep(10)"],
                                  cwd=self.root, timeout=0.05)
        self.assertTrue(result["timed_out"])
        self.assertEqual(result["cleanup"], "process_group_exited")
        self.assertNotEqual(result["exit_code"], 0)

    def test_capture_interrupt_retains_output_and_cleanup_state(self):
        process = Mock(pid=432165, returncode=-9)
        process.communicate.side_effect = [KeyboardInterrupt, ("partial response", "interrupted")]
        with patch.object(evaluate.subprocess, "Popen", return_value=process), patch.object(
                evaluate.os, "killpg", side_effect=[None, ProcessLookupError]):
            result = evaluate.capture(["fake-process"], cwd=self.root, timeout=1)
        self.assertTrue(result["interrupted"])
        self.assertEqual(result["stdout"], "partial response")
        self.assertEqual(result["cleanup"], "process_group_exited")

    def test_cleanup_timeout_is_explicitly_unconfirmed(self):
        process = Mock(pid=432165, returncode=-9)
        process.communicate.side_effect = [
            subprocess.TimeoutExpired("fake-process", 1),
            subprocess.TimeoutExpired("fake-process", 5, output=b"partial", stderr=b"open pipe")]
        with patch.object(evaluate.subprocess, "Popen", return_value=process), patch.object(
                evaluate.os, "killpg", side_effect=[None, ProcessLookupError]):
            result = evaluate.capture(["fake-process"], cwd=self.root, timeout=1)
        self.assertEqual(result["cleanup"], "unconfirmed")
        self.assertEqual(result["stdout"], "partial")
        process.stdout.close.assert_called_once()

    def test_model_command_retains_sandbox_and_does_not_override_home(self):
        self.prepare()
        command = evaluate.model_command("codex", self.work, self.state, None, None)
        self.assertNotIn("--dangerously-bypass-approvals-and-sandbox", command)
        self.assertIn('--ignore-user-config', command)
        self.assertIn('approval_policy="never"', command)
        self.assertTrue(any('permissions.rung_eval.filesystem=' in arg for arg in command))
        self.assertNotIn("--model", command)

    def test_child_state_and_native_login_leave_original_configuration_unchanged(self):
        old_environment = dict(os.environ)
        env = evaluate.runtime_environment(self.state)
        self.assertEqual(env["CODEX_HOME"], str(self.state / "codex"))
        self.assertEqual(dict(os.environ), old_environment)
        original = self.native_config / "auth.json"
        reference = self.state / "codex/auth.json"
        with self.assertRaisesRegex(RuntimeError, "stop"):
            with evaluate.native_auth(self.state):
                self.assertTrue(reference.is_symlink())
                self.assertEqual(reference.resolve(), original)
                raise RuntimeError("stop")
        self.assertFalse(reference.exists())
        self.assertEqual(original.read_text(), "{}\n")

    def test_context_audit_rejects_contamination_and_malformed_messages(self):
        self.audit_patch.stop()
        self.work.mkdir()
        for name in ("rung-get-set", "rung-go"):
            (self.work / ".agents/skills" / name).mkdir(parents=True)
        def messages(text):
            return json.dumps([{"type":"message", "role":"developer", "content":[{"type":"input_text", "text":text}]}])
        for output, variant, verified in [
            (messages("No selected skill"), "control", True),
            (messages("rung-go and rung-get-set"), "control", False),
            (messages("rung-go and rung-get-set"), "rung", True),
            (messages("rung-go"), "rung", False),
            ("[{}]", "control", False), ("[]", "control", False)]:
            with self.subTest(output=output, variant=variant), patch.object(evaluate, "capture", return_value=self.result(stdout=output)):
                result = evaluate.audit_context("codex", self.work, self.state, "task", variant, "model", "high")
                self.assertEqual(result["verified"], verified)

    def test_unverified_context_prevents_model_execution(self):
        self.audit.return_value = {"verified":False}
        with patch.object(evaluate, "preflight", return_value={"status":"ready_for_probe", "binary":"codex"}), patch.object(evaluate, "capture") as invoke:
            record = evaluate.run_attempt("routine", "control", self.root / "attempt", 1)
        invoke.assert_not_called()
        self.assertFalse(record["model_attempted"])
        self.assertEqual(record["outcome"], "blocked")

    def test_missing_native_login_is_recorded_without_model_execution(self):
        (self.native_config / "auth.json").unlink()
        with patch.object(evaluate, "preflight", return_value={"status":"ready_for_probe", "binary":"codex"}), patch.object(evaluate, "capture") as invoke:
            record = evaluate.run_attempt("routine", "control", self.root / "attempt", 1)
        invoke.assert_not_called()
        self.assertEqual(record["outcome"], "blocked")
        self.assertIn("login is unavailable", record["runtime_error"])

    def test_preflight_fails_closed_before_model_on_unsupported_os(self):
        self.work.mkdir()
        with patch.object(evaluate.platform, "system", return_value="Linux"), patch.object(evaluate, "native_sandbox") as invoke:
            value = evaluate.preflight(self.work, self.state)
        self.assertEqual(value["status"], "blocked")
        invoke.assert_not_called()

    def test_blocked_attempt_record_and_report(self):
        out = self.root / "attempt"
        with patch.object(evaluate, "preflight", return_value={"status": "blocked", "reason": "Unavailable"}):
            value = evaluate.run_attempt("routine", "control", out, 1)
        self.assertFalse(value["model_attempted"])
        self.assertEqual(value["outcome"], "blocked")
        report = evaluate.report([out / "record.json"])
        self.assertEqual(report["attempts"], 1)
        self.assertEqual(report["outcomes"]["blocked"], 1)
        self.assertIsNone(report["cost_per_successful_task"])
        with self.assertRaises(FileExistsError):
            evaluate.run_attempt("routine", "control", out, 1)

    def test_review_artifact_export_does_not_create_an_embedded_repository(self):
        out = self.root / "attempt"
        with patch.object(evaluate, "preflight", return_value={"status": "blocked", "reason": "Unavailable"}):
            record = evaluate.run_attempt("review-scope", "control", out, 1)
        self.assertIn("M  cache.py", record["before"]["git"]["status"])
        self.assertTrue((out / "artifacts/cache.py").is_file())
        self.assertFalse((out / "artifacts/.git").exists())

    def test_startup_failure_is_not_a_model_quality_failure(self):
        out = self.root / "attempt"
        readiness = {"status": "ready_for_probe", "binary": "codex"}
        with patch.object(evaluate, "preflight", return_value=readiness), patch.object(
                evaluate, "capture", return_value=self.result(exit_code=1, stderr="initialization failure")):
            record = evaluate.run_attempt("routine", "control", out, 1)
        self.assertTrue(record["model_attempted"])
        self.assertEqual(record["outcome"], "blocked")
        self.assertTrue(record["checks"]["scope"])
        self.assertIsNone(record["checks"]["behavior"])

    def test_failed_process_does_not_hide_unauthorized_writes(self):
        def failed_process(command, **kwargs):
            (kwargs["cwd"] / "TASK.md").write_text("unauthorized change")
            return self.result(exit_code=1)

        with patch.object(evaluate, "preflight", return_value={"status": "ready_for_probe", "binary": "codex"}), patch.object(
                evaluate, "capture", side_effect=failed_process):
            record = evaluate.run_attempt("routine", "control", self.root / "attempt", 1)
        self.assertEqual(record["outcome"], "failed")
        self.assertFalse(record["checks"]["scope"])

    def test_duplicate_report_inputs_cannot_inflate_attempt_count(self):
        path = self.root / "record.json"
        path.write_text('{"schema_version":1,"outcome":"passed"}')
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            evaluate.report([path, path])

    def test_successful_process_with_correct_artifact_and_catalog_evidence(self):
        out = self.root / "attempt"

        def fake_model(command, **kwargs):
            path = kwargs["cwd"] / "README.md"
            path.write_bytes(path.read_bytes().replace(b"proceses", b"processes"))
            return self.result(stdout='{"type":"item.completed","item":{"type":"agent_message","text":"Done"}}\n{"type":"turn.completed"}')

        with patch.object(evaluate, "preflight", return_value={"status": "ready_for_probe", "binary": "codex"}), patch.object(
                evaluate, "capture", side_effect=fake_model):
            record = evaluate.run_attempt("routine", "rung", out, 1)
        self.assertTrue(record["checks"]["behavior"]["passed"])
        self.assertEqual(record["outcome"], "passed")
        self.assertIn("$rung-go", record["wrapper"])
        self.assertNotIn("$rung", record["task"])

    def test_unconfirmed_cleanup_retains_workspace_without_accepting_artifacts(self):
        out = self.root / "attempt"
        with patch.object(evaluate, "preflight", return_value={"status": "ready_for_probe", "binary": "codex"}), patch.object(
                evaluate, "capture", return_value=self.result(cleanup="unconfirmed")):
            record = evaluate.run_attempt("routine", "control", out, 1)
        retained = Path(record["retained_workspace"])
        self.addCleanup(shutil.rmtree, retained.parent)
        self.assertTrue(retained.is_dir())
        self.assertFalse((out / "artifacts").exists())
        self.assertEqual(record["outcome"], "inconclusive")
        self.assertIsNone(record["checks"])

    def test_record_schema_and_output_reuse_are_rejected(self):
        path = self.root / "bad.json"
        path.write_text('{"schema_version":99,"outcome":"passed"}')
        with self.assertRaises(ValueError):
            evaluate.report([path])
        evaluate.write_json(self.root / "immutable.json", {"original": True})
        with self.assertRaises(FileExistsError):
            evaluate.write_json(self.root / "immutable.json", {"replacement": True})


if __name__ == "__main__":
    unittest.main()
