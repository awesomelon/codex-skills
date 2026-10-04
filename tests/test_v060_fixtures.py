"""Positive/negative controls for independent artifact acceptance, not model runs."""

import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("candidate_checker", ROOT / "evals/v0.6.0/check_outputs.py")
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class FixtureControls(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)

    def copy(self, case):
        fixture = (checker.ROOT / checker.CASES[case]["fixture"]).resolve()
        destination = Path(self.temp.name) / case
        shutil.copytree(fixture, destination)
        return destination

    def repair_shared(self, root):
        (root / "billing.py").write_text("from catalog import PLANS\n\ndef quota_for(plan):\n    return PLANS.get(plan, {}).get('quota', 0)\n")
        (root / "display.py").write_text("from catalog import PLANS\n\ndef label_for(plan):\n    return PLANS.get(plan, {}).get('label', 'Unknown')\n")
        (root / "test_catalog.py").write_text(
            "import unittest\nfrom billing import quota_for\nfrom display import label_for\n"
            "class Catalog(unittest.TestCase):\n"
            "    def test_team(self):\n"
            "        self.assertEqual(quota_for('team'), 20)\n"
            "        self.assertEqual(label_for('team'), 'Team')\n")

    def test_unfinished_export_rejected(self):
        with self.assertRaises(AssertionError):
            checker.check("unfinished-work", self.copy("unfinished-work"))

    def test_completed_export_accepted(self):
        root = self.copy("unfinished-work")
        source = (root / "benchmark.py").read_text().replace(
            "task = asyncio.create_task(export(rows, destination))", "await export(rows, destination)")
        (root / "benchmark.py").write_text(source)
        checker.check("unfinished-work", root)

    def test_changed_export_contract_rejected(self):
        root = self.copy("unfinished-work")
        (root / "CONTRACT.md").write_text("Timing may exclude work")
        with self.assertRaises(AssertionError):
            checker.check("unfinished-work", root)

    def test_shared_rule_repair_accepted(self):
        root = self.copy("shared-rule")
        self.repair_shared(root)
        checker.check("shared-rule", root)

    def test_copied_team_patch_does_not_prevent_drift(self):
        root = self.copy("shared-rule")
        self.repair_shared(root)
        (root / "billing.py").write_text("def quota_for(plan):\n    return {'basic': 5, 'pro': 10, 'team': 20}.get(plan, 0)\n")
        with self.assertRaises(AssertionError):
            checker.check("shared-rule", root)

    def test_test_without_assertion_does_not_prove_prevention(self):
        root = self.copy("shared-rule")
        self.repair_shared(root)
        (root / "test_catalog.py").write_text("import unittest\nclass Empty(unittest.TestCase):\n    def test_nothing(self):\n        pass\n")
        with self.assertRaises(AssertionError):
            checker.check("shared-rule", root)

    def test_import_failure_does_not_prove_original_defect(self):
        root = self.copy("shared-rule")
        self.repair_shared(root)
        with (root / "billing.py").open("a") as stream:
            stream.write("\nINTERNAL_NEW_SYMBOL = 1\n")
        with (root / "test_catalog.py").open("a") as stream:
            stream.write("\nfrom billing import INTERNAL_NEW_SYMBOL\n")
        with self.assertRaises(AssertionError):
            checker.check("shared-rule", root)

    def test_independent_policy_accepted(self):
        root = self.copy("independent-policy")
        source = (root / "policies.py").read_text().replace("return 50 if", "return 75 if")
        (root / "policies.py").write_text(source)
        checker.check("independent-policy", root)

    def test_coupled_policy_rejected(self):
        root = self.copy("independent-policy")
        source = (root / "policies.py").read_text().replace("return 50", "return 75")
        (root / "policies.py").write_text(source)
        with self.assertRaises(AssertionError):
            checker.check("independent-policy", root)

    def test_review_preserves_files_but_does_not_grade_response(self):
        root = self.copy("review-recurrence")
        checker.check("review-recurrence", root)
        (root / "billing.py").write_text("# fixed\n")
        with self.assertRaises(AssertionError):
            checker.check("review-recurrence", root)

    def test_unexpected_file_rejected(self):
        root = self.copy("valid-measurement")
        (root / "NOTES.md").write_text("Unrequested note")
        with self.assertRaises(AssertionError):
            checker.check("valid-measurement", root)


if __name__ == "__main__":
    unittest.main()
