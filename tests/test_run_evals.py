"""Runner accounting and process controls, without credentials or model requests."""

import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import sys
import tempfile
import textwrap
from types import SimpleNamespace
import unittest
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("run_evals", ROOT / "scripts/run_evals.py")
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


class RunnerTests(unittest.TestCase):
    def test_nonzero_exit_is_retained(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp).resolve()
            result = runner.execute([sys.executable, "-c", "raise SystemExit(7)"], root, root / "logs", 2)
            self.assertEqual(result["exit_code"], 7)
            self.assertEqual(result["execution_status"], "completed")

    def test_timeout_is_not_success(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp).resolve()
            result = runner.execute([sys.executable, "-c", "import time; time.sleep(30)"], root, root / "logs", .1)
            self.assertEqual(result["execution_status"], "timed_out")
            self.assertIsNone(result["exit_code"])

    def test_missing_cli_is_launch_failure(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp).resolve()
            result = runner.execute([str(root / "missing")], root, root / "logs", 1)
            self.assertEqual(result["execution_status"], "launch_failed")

    def test_symlink_input_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp).resolve()
            (root / "alias").symlink_to(ROOT / "README.md")
            with self.assertRaises(ValueError):
                runner.inventory(root)

    def test_usage_only_from_completion(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp).resolve()
            (root / "stdout.jsonl").write_text('not json\n{"type":"turn.failed"}\n')
            info = runner.metadata(root)
            self.assertIsNone(info["usage"])
            self.assertFalse(info["turn_completed"])
            self.assertTrue(info["turn_failed"])

    def test_blocked_preflight_preserves_all_unstarted_attempts(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp).resolve() / "evidence"
            args = mock.Mock(baseline=str(ROOT), candidate=str(ROOT), output=str(output),
                             case=["routine"], repeat=2, timeout=1, codex="codex")

            def fail(argv, cwd, logs, timeout):
                logs.mkdir(parents=True)
                (logs / "stdout.jsonl").write_text('{"type":"turn.failed"}\n')
                (logs / "stderr.txt").write_text("401 Unauthorized")
                return {"exit_code": 1, "execution_status": "completed"}

            with mock.patch.object(runner, "execute", side_effect=fail) as execute:
                self.assertEqual(runner.run(args), 2)
                self.assertEqual(execute.call_count, 1)
            report = json.loads((output / "summary.json").read_text())
            self.assertEqual(len(report["attempts"]), 4)
            self.assertTrue(all(a["outcome"] == "not_run" for a in report["attempts"]))
            self.assertEqual(report["preflight"]["outcome"], "blocked")
            self.assertEqual(report["counts"], {"not_run": 4})
            self.assertTrue((output / "bundle/evals/v0.6.0/cases.json").is_file())

    def test_artifact_pass_still_needs_response_review(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp).resolve() / "evidence"
            args = mock.Mock(baseline=str(ROOT), candidate=str(ROOT), output=str(output),
                             case=["routine"], repeat=1, timeout=3, codex="codex")
            real_execute = runner.execute

            def fake_cli(argv, cwd, logs, timeout):
                if argv[0] != "codex":
                    return real_execute(argv, cwd, logs, timeout)
                logs.mkdir(parents=True)
                response = Path(argv[argv.index("-o") + 1])
                response.write_text("READY" if logs.name == "preflight" else "Done")
                (logs / "stdout.jsonl").write_text('{"type":"turn.completed","usage":{"input_tokens":1}}\n')
                (logs / "stderr.txt").write_text("")
                if logs.name != "preflight":
                    readme = cwd / "README.md"
                    readme.write_bytes(readme.read_bytes().replace(b"proceses", b"processes"))
                return {"exit_code": 0, "execution_status": "completed"}

            with mock.patch.object(runner, "execute", side_effect=fake_cli):
                self.assertEqual(runner.run(args), 1)
            report = json.loads((output / "summary.json").read_text())
            self.assertTrue(all(a["artifact_outcome"] == "passed" for a in report["attempts"]))
            self.assertTrue(all(a["outcome"] == "inconclusive" for a in report["attempts"]))
            self.assertEqual(report["attempts"][0]["variant"], "baseline")

    def make_sources(self, root, case_id="routine"):
        """A disposable repository, so mutation controls never touch real inputs."""
        # Match production REPO normalization, including macOS /var -> /private/var.
        root = root.resolve()
        repo = root / "repository"
        catalog = repo / "evals/v0.6.0/cases.json"
        catalog.parent.mkdir(parents=True)
        case = next(case for case in json.loads(runner.CATALOG.read_text())["cases"]
                    if case["id"] == case_id)
        catalog.write_text(json.dumps({"cases": [case]}))
        shutil.copy2(ROOT / "evals/v0.6.0/check_outputs.py", catalog.parent / "check_outputs.py")
        shutil.copy2(ROOT / "evals/v0.6.0/review.md", catalog.parent / "review.md")
        source = (ROOT / "evals/v0.6.0" / case["fixture"]).resolve()
        fixture = (catalog.parent / case["fixture"]).resolve()
        shutil.copytree(source, fixture)
        if case_id in runner.LEGACY_CASES:
            shutil.copy2(ROOT / runner.LEGACY_CHECKER, repo / runner.LEGACY_CHECKER)
        for variant in ("baseline", "candidate"):
            shutil.copytree(ROOT / "skills", root / variant / "skills")
        candidate_skill = root / "candidate/skills/rung-go/SKILL.md"
        candidate_skill.write_text(candidate_skill.read_text() + "\nCandidate test marker.\n")
        args = SimpleNamespace(baseline=str(root / "baseline"), candidate=str(root / "candidate"),
                               output=str(root / "evidence"), case=[case_id], repeat=2,
                               timeout=3, codex=str(root / "fake-codex"))
        return repo, catalog, fixture, args

    def fake_cli(self, root, preflight="pass", attempt="pass"):
        """Use a real child process for the adapter; it never calls a model."""
        root = root.resolve()
        executable = root / "fake-codex"
        executable.write_text(
            f"#!{sys.executable}\n" + textwrap.dedent("""\
            import json
            from pathlib import Path
            import sys
            if '--version' in sys.argv:
                print('fake-codex 1.0')
                raise SystemExit(0)
            workspace = Path(sys.argv[sys.argv.index('-C') + 1])
            response = Path(sys.argv[sys.argv.index('-o') + 1])
            stage = 'preflight' if response.parent.name == 'preflight' else 'attempt'
            """) + f"with Path({str(root / 'calls.jsonl')!r}).open('a') as stream:\n" +
            "    stream.write(json.dumps({'stage': stage, 'workspace': str(workspace), 'prompt': sys.argv[-1]}) + '\\n')\n" +
            "if stage == 'preflight':\n" + textwrap.indent(preflight, "    ") + "\n" +
            "else:\n" + textwrap.indent(attempt, "    ") + "\n" +
            "response.write_text('READY' if stage == 'preflight' else 'Done')\n" +
            "print(json.dumps({'type': 'turn.completed', 'usage': {'input_tokens': 1}}))\n")
        executable.chmod(0o755)

    def test_temporary_parent_alias_is_normalized_without_allowing_input_symlinks(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp).resolve()
            canonical = root / "private/folders"
            canonical.mkdir(parents=True)
            alias = root / "var"
            alias.symlink_to(canonical.parent, target_is_directory=True)
            aliased_root = alias / "folders"
            repo, catalog, fixture, args = self.make_sources(aliased_root)
            self.assertEqual(repo, canonical / "repository")
            self.assertEqual(catalog, repo / "evals/v0.6.0/cases.json")
            self.assertEqual(fixture.relative_to(repo),
                             Path("evals/long-running-2026-10-03/fixtures/routine"))
            self.assertEqual(Path(args.output), canonical / "evidence")
            # Real CLI arguments may also arrive through the OS-level parent alias.
            args.baseline = str(aliased_root / "baseline")
            args.candidate = str(aliased_root / "candidate")
            args.output = str(aliased_root / "evidence")
            args.repeat = 1
            self.fake_cli(aliased_root, attempt="readme = workspace / 'README.md'\n"
                          "readme.write_bytes(readme.read_bytes().replace(b'proceses', b'processes'))")
            with mock.patch.object(runner, "REPO", repo), mock.patch.object(runner, "CATALOG", catalog):
                self.assertEqual(runner.run(args), 1)
            report = json.loads((canonical / "evidence/summary.json").read_text())
            self.assertEqual(report["source_paths"]["baseline"], str(canonical / "baseline"))
            self.assertTrue(all(item["artifact_outcome"] == "passed" for item in report["attempts"]))

            readme = fixture / "README.md"
            moved = fixture / "original.md"
            readme.rename(moved)
            readme.symlink_to(moved)
            args.output = str(aliased_root / "rejected-evidence")
            with mock.patch.object(runner, "REPO", repo), mock.patch.object(runner, "CATALOG", catalog), \
                    mock.patch.object(runner, "execute") as execute:
                with self.assertRaisesRegex(ValueError, "Symlink"):
                    runner.run(args)
                execute.assert_not_called()
            self.assertFalse(Path(args.output).exists())

    def test_original_mutations_after_freeze_do_not_change_cases_or_checks(self):
        for case_id in ("routine", "valid-measurement"):
            with self.subTest(case=case_id), tempfile.TemporaryDirectory() as temp:
                root = Path(temp).resolve()
                repo, catalog, fixture, args = self.make_sources(root, case_id)
                original_fixture = runner.inventory(fixture)
                original_skills = runner.inventory(root / "baseline/skills")
                original_candidate = runner.inventory(root / "candidate/skills")
                original_review = hashlib.sha256((catalog.parent / "review.md").read_bytes()).hexdigest()
                original_catalog = hashlib.sha256(catalog.read_bytes()).hexdigest()
                original_checker = hashlib.sha256((catalog.parent / "check_outputs.py").read_bytes()).hexdigest()
                changes = f"""\
Path({str(catalog)!r}).write_text('{{"cases": []}}')
Path({str(catalog.parent / 'check_outputs.py')!r}).write_text('raise SystemExit(77)')
Path({str(catalog.parent / 'review.md')!r}).write_text('changed response rubric')
for path in Path({str(fixture)!r}).rglob('*'):
    if path.is_file():
        path.write_text('changed original fixture')
for variant in ('baseline', 'candidate'):
    Path({str(root)!r}, variant, 'skills/rung-go/SKILL.md').write_text('changed original skill')
"""
                if case_id == "routine":
                    changes += f"Path({str(repo / runner.LEGACY_CHECKER)!r}).write_text('raise SystemExit(78)')\n"
                solve = ("readme = workspace / 'README.md'\n"
                         "readme.write_bytes(readme.read_bytes().replace(b'proceses', b'processes'))"
                         if case_id == "routine" else "pass")
                self.fake_cli(root, preflight=changes, attempt=solve)
                with mock.patch.object(runner, "REPO", repo), mock.patch.object(runner, "CATALOG", catalog):
                    self.assertEqual(runner.run(args), 1)
                output = Path(args.output)
                report = json.loads((output / "summary.json").read_text())
                self.assertEqual(report["catalog_hash"], original_catalog)
                self.assertEqual(report["checker_hash"], original_checker)
                self.assertEqual(report["skill_hashes"]["baseline"], original_skills)
                self.assertEqual(report["skill_hashes"]["candidate"], original_candidate)
                self.assertEqual(report["review_hash"], original_review)
                self.assertEqual(report["review_source_path"], str(catalog.parent / "review.md"))
                self.assertEqual(report["evaluation_bundle"]["review"], "evals/v0.6.0/review.md")
                self.assertEqual(report["fixture_hashes"][case_id], original_fixture)
                self.assertEqual(report["catalog_source_path"], str(catalog))
                self.assertEqual(report["checker_source_path"], str(catalog.parent / "check_outputs.py"))
                self.assertEqual(report["fixture_source_paths"][case_id], str(fixture))
                self.assertEqual(report["source_paths"]["baseline"], str(root / "baseline"))
                self.assertEqual(report["host"]["cli_version"], "fake-codex 1.0")
                self.assertEqual(report["counts"], {"inconclusive": 4})
                self.assertEqual(runner.inventory(output / "bundle"), report["evaluation_bundle"]["file_hashes"])
                self.assertNotEqual(runner.inventory(fixture), original_fixture)
                self.assertNotEqual(runner.inventory(root / "baseline/skills"), original_skills)
                for attempt in report["attempts"]:
                    self.assertEqual(attempt["fixture_hashes"], original_fixture)
                    self.assertEqual(attempt["input_pairing"], "verified")
                    if case_id == "routine":
                        skill = ".agents/skills/rung-go/SKILL.md"
                        self.assertEqual(attempt["input_hashes"][skill],
                                         report["skill_hashes"][attempt["variant"]]["rung-go/SKILL.md"])
                    self.assertEqual(attempt["artifact_outcome"], "passed")
                    self.assertEqual(attempt["review_status"], "pending")
                    self.assertEqual(attempt["checked_output_hashes"], attempt["output_hashes"])
                    self.assertIn(str(output / "bundle" / report["evaluation_bundle"]["checker"]),
                                  attempt["checker"]["command"])
                    self.assertEqual(attempt["prompt"], report["attempts"][0]["prompt"])
                calls = [json.loads(line) for line in (root / "calls.jsonl").read_text().splitlines()]
                self.assertEqual([call["stage"] for call in calls], ["preflight"] + ["attempt"] * 4)
                if case_id == "routine":
                    self.assertIn(runner.LEGACY_CHECKER.as_posix(), report["evaluation_bundle"]["file_hashes"])

    def test_frozen_bundle_mutation_blocks_before_case_invocation(self):
        for target in ("fixture", "checker", "catalog", "legacy-checker", "skill", "symlink"):
            with self.subTest(target=target), tempfile.TemporaryDirectory() as temp:
                root = Path(temp).resolve()
                repo, catalog, fixture, args = self.make_sources(root)
                output = Path(args.output)
                paths = {
                    "fixture": output / "bundle" / fixture.relative_to(repo) / "README.md",
                    "checker": output / "bundle/evals/v0.6.0/check_outputs.py",
                    "catalog": output / "bundle/evals/v0.6.0/cases.json",
                    "legacy-checker": output / "bundle" / runner.LEGACY_CHECKER,
                    "skill": output / "sources/baseline/skills/rung-go/SKILL.md",
                    "symlink": output / "bundle" / fixture.relative_to(repo) / "README.md",
                }
                path = paths[target]
                mutation = f"Path({str(path)!r}).write_text('tampered frozen input')"
                if target == "symlink":
                    mutation = (f"Path({str(path)!r}).unlink()\n"
                                f"Path({str(path)!r}).symlink_to({str(fixture / 'README.md')!r})")
                self.fake_cli(root, preflight=mutation)
                with mock.patch.object(runner, "REPO", repo), mock.patch.object(runner, "CATALOG", catalog):
                    self.assertEqual(runner.run(args), 2)
                report = json.loads((output / "summary.json").read_text())
                self.assertEqual(report["input_integrity"]["status"], "blocked")
                self.assertEqual(report["counts"], {"blocked": 1, "not_run": 3})
                self.assertTrue(all(item["execution_status"] == "not_run" for item in report["attempts"]))
                self.assertFalse(any("checker" in item for item in report["attempts"]))
                self.assertEqual(len((root / "calls.jsonl").read_text().splitlines()), 1)

    def test_checker_mutation_during_model_call_blocks_before_check(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp).resolve()
            repo, catalog, fixture, args = self.make_sources(root)
            frozen_checker = Path(args.output) / "bundle/evals/v0.6.0/check_outputs.py"
            self.fake_cli(root, attempt=f"Path({str(frozen_checker)!r}).write_text('raise SystemExit(0)')")
            with mock.patch.object(runner, "REPO", repo), mock.patch.object(runner, "CATALOG", catalog):
                self.assertEqual(runner.run(args), 2)
            report = json.loads((Path(args.output) / "summary.json").read_text())
            self.assertEqual(report["counts"], {"blocked": 1, "not_run": 3})
            self.assertEqual(report["attempts"][0]["execution_status"], "completed")
            self.assertNotIn("checker", report["attempts"][0])
            self.assertEqual(len((root / "calls.jsonl").read_text().splitlines()), 2)

    def test_checker_mutation_after_final_check_is_not_reported_as_verified(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp).resolve()
            repo, catalog, fixture, args = self.make_sources(root)
            args.repeat = 1
            checker = catalog.parent / "check_outputs.py"
            checker.write_text(
                "from pathlib import Path\n"
                "counter = Path.cwd().parent / 'checker-count.txt'\n"
                "count = int(counter.read_text()) + 1 if counter.exists() else 1\n"
                "counter.write_text(str(count))\n"
                "if count == 2:\n"
                "    Path(__file__).write_text('changed during final check')\n")
            self.fake_cli(root)
            with mock.patch.object(runner, "REPO", repo), mock.patch.object(runner, "CATALOG", catalog):
                self.assertEqual(runner.run(args), 2)
            report = json.loads((Path(args.output) / "summary.json").read_text())
            self.assertEqual(report["counts"], {"inconclusive": 1, "blocked": 1})
            self.assertEqual(report["input_integrity"]["status"], "blocked")
            self.assertEqual(report["attempts"][0]["artifact_outcome"], "passed")
            self.assertEqual(report["attempts"][1]["checker"]["exit_code"], 0)
            self.assertNotIn("artifact_outcome", report["attempts"][1])

    def test_pairing_drift_in_second_workspace_blocks_before_second_model_call(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp).resolve()
            repo, catalog, fixture, args = self.make_sources(root)
            self.fake_cli(root, attempt="readme = workspace / 'README.md'\n"
                          "readme.write_bytes(readme.read_bytes().replace(b'proceses', b'processes'))")
            copytree = shutil.copytree
            workspaces = []

            def drifting_copy(source, destination, *positional, **kwargs):
                result = copytree(source, destination, *positional, **kwargs)
                if Path(destination).parent == Path(args.output) / "work":
                    workspaces.append(destination)
                    if len(workspaces) == 2:
                        (Path(destination) / "README.md").write_text("mismatched input")
                return result

            with mock.patch.object(runner, "REPO", repo), mock.patch.object(runner, "CATALOG", catalog), \
                    mock.patch.object(runner.shutil, "copytree", side_effect=drifting_copy):
                self.assertEqual(runner.run(args), 2)
            report = json.loads((Path(args.output) / "summary.json").read_text())
            self.assertEqual(report["counts"], {"inconclusive": 1, "blocked": 1, "not_run": 2})
            self.assertEqual(report["attempts"][0]["artifact_outcome"], "passed")
            self.assertEqual(report["attempts"][1]["execution_status"], "not_run")
            self.assertIn("pairing drift", report["attempts"][1]["input_error"])
            self.assertEqual(len((root / "calls.jsonl").read_text().splitlines()), 2)

    def test_wrong_variant_skill_copy_is_rejected_before_model_call(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp).resolve()
            repo, catalog, fixture, args = self.make_sources(root)
            self.fake_cli(root, attempt="readme = workspace / 'README.md'\n"
                          "readme.write_bytes(readme.read_bytes().replace(b'proceses', b'processes'))")
            copytree = shutil.copytree

            def wrong_skill_copy(source, destination, *positional, **kwargs):
                if Path(source) == Path(args.output) / "sources/candidate/skills/rung-go":
                    source = Path(args.output) / "sources/baseline/skills/rung-go"
                return copytree(source, destination, *positional, **kwargs)

            with mock.patch.object(runner, "REPO", repo), mock.patch.object(runner, "CATALOG", catalog), \
                    mock.patch.object(runner.shutil, "copytree", side_effect=wrong_skill_copy):
                self.assertEqual(runner.run(args), 2)
            report = json.loads((Path(args.output) / "summary.json").read_text())
            self.assertEqual(report["counts"], {"inconclusive": 1, "blocked": 1, "not_run": 2})
            self.assertIn("Skill or fixture input pairing drift", report["attempts"][1]["input_error"])
            self.assertEqual(len((root / "calls.jsonl").read_text().splitlines()), 2)

    def test_source_change_while_freezing_fails_before_any_cli_call(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp).resolve()
            repo, catalog, fixture, args = self.make_sources(root)
            copytree = shutil.copytree

            def changing_copy(source, destination, *positional, **kwargs):
                result = copytree(source, destination, *positional, **kwargs)
                if Path(source) == root / "baseline/skills":
                    (Path(source) / "rung-go/SKILL.md").write_text("changed during copy")
                return result

            with mock.patch.object(runner, "REPO", repo), mock.patch.object(runner, "CATALOG", catalog), \
                    mock.patch.object(runner.shutil, "copytree", side_effect=changing_copy), \
                    mock.patch.object(runner.subprocess, "run") as subprocess_run, \
                    mock.patch.object(runner, "execute") as execute:
                with self.assertRaisesRegex(ValueError, "changed while freezing"):
                    runner.run(args)
                subprocess_run.assert_not_called()
                execute.assert_not_called()

    def test_symlink_sources_rejected_before_any_cli_call(self):
        for target in ("skill-root", "fixture-root", "fixture-file", "checker", "legacy-checker"):
            with self.subTest(target=target), tempfile.TemporaryDirectory() as temp:
                root = Path(temp).resolve()
                repo, catalog, fixture, args = self.make_sources(root)
                paths = {"skill-root": root / "baseline/skills", "fixture-root": fixture,
                         "fixture-file": fixture / "README.md",
                         "checker": catalog.parent / "check_outputs.py",
                         "legacy-checker": repo / runner.LEGACY_CHECKER}
                path = paths[target]
                moved = path.with_name(path.name + "-original")
                path.rename(moved)
                path.symlink_to(moved, target_is_directory=moved.is_dir())
                with mock.patch.object(runner, "REPO", repo), mock.patch.object(runner, "CATALOG", catalog), \
                        mock.patch.object(runner, "execute") as execute:
                    with self.assertRaisesRegex(ValueError, "Symlink"):
                        runner.run(args)
                    execute.assert_not_called()
                self.assertFalse(Path(args.output).exists())

    def test_output_cannot_overwrite_source_or_evidence(self):
        args = mock.Mock(baseline=str(ROOT), candidate=str(ROOT), output=str(ROOT / "evals/output"),
                         case=["routine"], repeat=1, timeout=1)
        with self.assertRaises(ValueError):
            runner.run(args)
        with tempfile.TemporaryDirectory() as temp:
            args.output = temp
            with self.assertRaises(ValueError):
                runner.run(args)


if __name__ == "__main__":
    unittest.main()
