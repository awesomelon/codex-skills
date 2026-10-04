"""Controls for post-release challenge fixtures, not fresh model evaluations."""

import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("holdout_checker", ROOT / "evals/v0.6.0/check_outputs.py")
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class HoldoutControls(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)

    def copy(self, case):
        fixture = (checker.ROOT / checker.CASES[case]["fixture"]).resolve()
        destination = Path(self.temp.name) / case
        shutil.copytree(fixture, destination)
        return destination

    def repair_lazy(self, root):
        source = (root / "benchmark.py").read_text()
        source = source.replace('    elapsed = perf_counter() - start\n    report = "\\n".join(lines)',
                                '    report = "\\n".join(lines)\n    elapsed = perf_counter() - start')
        (root / "benchmark.py").write_text(source)

    def repair_registry(self, root):
        (root / "estimates.py").write_text(
            "from registry import SERVICES\n\ndef days_for(code):\n"
            "    return SERVICES.get(code, {}).get('days')\n")
        (root / "labels.py").write_text(
            "from registry import SERVICES\n\ndef label_for(code):\n"
            "    return SERVICES.get(code, {}).get('label', 'Unavailable')\n")
        (root / "test_services.py").write_text(
            "import unittest\nfrom estimates import days_for\nfrom labels import label_for\n"
            "class Services(unittest.TestCase):\n"
            "    def test_next_day(self):\n"
            "        self.assertEqual(days_for('next_day'), 1)\n"
            "        self.assertEqual(label_for('next_day'), 'Next day')\n")

    def test_lazy_work_outside_timer_rejected(self):
        with self.assertRaises(AssertionError):
            checker.check("lazy-materialization", self.copy("lazy-materialization"))

    def test_lazy_completed_work_accepted(self):
        root = self.copy("lazy-materialization")
        self.repair_lazy(root)
        checker.check("lazy-materialization", root)

    def test_lazy_wrong_report_rejected(self):
        root = self.copy("lazy-materialization")
        self.repair_lazy(root)
        source = (root / "benchmark.py").read_text().replace('"\\n".join(lines)', '" ".join(lines)')
        (root / "benchmark.py").write_text(source)
        with self.assertRaises(AssertionError):
            checker.check("lazy-materialization", root)

    def test_lazy_swallowed_error_rejected(self):
        root = self.copy("lazy-materialization")
        self.repair_lazy(root)
        source = (root / "benchmark.py").read_text().replace(
            '    report = "\\n".join(lines)',
            '    try:\n        report = "\\n".join(lines)\n    except ValueError:\n        report = ""')
        (root / "benchmark.py").write_text(source)
        with self.assertRaises(AssertionError):
            checker.check("lazy-materialization", root)

    def test_cached_control_preserves_source_without_grading_answer(self):
        root = self.copy("valid-cached-control")
        checker.check("valid-cached-control", root)
        (root / "EVIDENCE.md").write_text("Measurements replaced")
        with self.assertRaises(AssertionError):
            checker.check("valid-cached-control", root)

    def test_renamed_registry_accepted(self):
        root = self.copy("renamed-registry")
        self.repair_registry(root)
        checker.check("renamed-registry", root)

    def test_renamed_copied_patch_rejected(self):
        root = self.copy("renamed-registry")
        self.repair_registry(root)
        (root / "estimates.py").write_text(
            "def days_for(code):\n    return {'ground': 5, 'pickup': 0, 'next_day': 1}.get(code)\n")
        with self.assertRaises(AssertionError):
            checker.check("renamed-registry", root)

    def test_renamed_zero_value_fallback_rejected(self):
        root = self.copy("renamed-registry")
        self.repair_registry(root)
        source = (root / "estimates.py").read_text().replace("get('days')", "get('days') or None")
        (root / "estimates.py").write_text(source)
        with self.assertRaises(AssertionError):
            checker.check("renamed-registry", root)

    def test_renamed_assertion_free_regression_rejected(self):
        root = self.copy("renamed-registry")
        self.repair_registry(root)
        (root / "test_services.py").write_text(
            "import unittest\nclass Empty(unittest.TestCase):\n    def test_empty(self):\n        pass\n")
        with self.assertRaises(AssertionError):
            checker.check("renamed-registry", root)


if __name__ == "__main__":
    unittest.main()
