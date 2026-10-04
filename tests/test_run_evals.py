"""Runner accounting and process controls, without credentials or model requests."""

import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("run_evals", ROOT / "scripts/run_evals.py")
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


class RunnerTests(unittest.TestCase):
    def test_nonzero_exit_is_retained(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            result = runner.execute([sys.executable, "-c", "raise SystemExit(7)"], root, root / "logs", 2)
            self.assertEqual(result["exit_code"], 7)
            self.assertEqual(result["execution_status"], "completed")

    def test_timeout_is_not_success(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            result = runner.execute([sys.executable, "-c", "import time; time.sleep(30)"], root, root / "logs", .1)
            self.assertEqual(result["execution_status"], "timed_out")
            self.assertIsNone(result["exit_code"])

    def test_missing_cli_is_launch_failure(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            result = runner.execute([str(root / "missing")], root, root / "logs", 1)
            self.assertEqual(result["execution_status"], "launch_failed")

    def test_symlink_input_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "alias").symlink_to(ROOT / "README.md")
            with self.assertRaises(ValueError):
                runner.inventory(root)

    def test_usage_only_from_completion(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "stdout.jsonl").write_text('not json\n{"type":"turn.failed"}\n')
            info = runner.metadata(root)
            self.assertIsNone(info["usage"])
            self.assertFalse(info["turn_completed"])
            self.assertTrue(info["turn_failed"])

    def test_blocked_preflight_preserves_all_unstarted_attempts(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "evidence"
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

    def test_artifact_pass_still_needs_response_review(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "evidence"
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
