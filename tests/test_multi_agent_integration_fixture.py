"""Calibrate a cross-worker contract fixture; this does not invoke an agent."""
from __future__ import annotations

from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

FIXTURE = Path(__file__).resolve().parents[1] / "evals/multi-agent-guard/fixtures/integration"
NODE = shutil.which("node")


@unittest.skipUnless(NODE, "An existing Node.js 18+ runtime is needed for fixture calibration")
class IntegrationFixtureTests(unittest.TestCase):
    def setUp(self) -> None:
        version = subprocess.run(
            [NODE, "--version"], text=True, capture_output=True, check=True, timeout=10
        ).stdout.strip()
        if int(version.lstrip("v").split(".")[0]) < 18:
            self.skipTest("Node.js 18+ is required")
        temporary = tempfile.TemporaryDirectory(prefix="multi-agent-fixture-")
        self.addCleanup(temporary.cleanup)
        self.work = Path(temporary.name) / "fixture"
        shutil.copytree(FIXTURE, self.work)

    def run_checks(self, *names: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [NODE, "--test", *names], cwd=self.work, text=True,
            capture_output=True, check=False, timeout=20,
        )

    def assert_passes(self, *names: str) -> None:
        result = self.run_checks(*names)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_baseline_contract_passes(self) -> None:
        self.assert_passes("keys.test.mjs", "invalidation.test.mjs", "integration.test.mjs")

    def test_green_isolated_checks_miss_an_incompatible_tuple(self) -> None:
        source = self.work / "keys.mjs"
        before = source.read_text(encoding="utf-8")
        self.assertEqual(before.count("['document', tenantId, documentId]"), 1)
        source.write_text(
            before.replace("['document', tenantId, documentId]", "['document', documentId, tenantId]"),
            encoding="utf-8",
        )
        # No test edits: intentionally incomplete isolated checks remain green.
        self.assert_passes("keys.test.mjs", "invalidation.test.mjs")
        result = self.run_checks("integration.test.mjs")
        output = result.stdout + result.stderr
        self.assertNotEqual(result.returncode, 0, output)
        self.assertIn("reader keys remain invalidatable", output)
        self.assertIn("ERR_ASSERTION", output)
        source.write_text(before, encoding="utf-8")
        self.assert_passes("keys.test.mjs", "invalidation.test.mjs", "integration.test.mjs")

    def test_compatible_changes_in_both_modules_pass(self) -> None:
        (self.work / "keys.mjs").write_text(
            "const resource = 'document';\n"
            "export function documentKey(tenantId, documentId) {\n"
            "  return [resource, tenantId, documentId];\n}\n", encoding="utf-8",
        )
        (self.work / "invalidation.mjs").write_text(
            "export function shouldInvalidate(key, tenantId, documentId) {\n"
            "  const [resource, tenant, document] = key;\n"
            "  return resource === 'document' && tenant === tenantId && document === documentId;\n"
            "}\n", encoding="utf-8",
        )
        self.assert_passes("keys.test.mjs", "invalidation.test.mjs", "integration.test.mjs")


    def test_integrated_check_rejects_coordinated_public_contract_break(self) -> None:
        # The producer and consumer agree, but the published tuple is still broken.
        source = self.work / "keys.mjs"
        source.write_text(
            source.read_text(encoding="utf-8").replace(
                "['document', tenantId, documentId]", "['document', documentId, tenantId]"
            ), encoding="utf-8",
        )
        consumer = self.work / "invalidation.mjs"
        consumer.write_text(
            consumer.read_text(encoding="utf-8").replace(
                "key[1] === tenantId && key[2] === documentId",
                "key[2] === tenantId && key[1] === documentId",
            ), encoding="utf-8",
        )
        # The unchanged behavioral integration test still passes for this pair.
        behavior = subprocess.run(
            [NODE, "--test", "--test-name-pattern=reader keys", "integration.test.mjs"],
            cwd=self.work, text=True, capture_output=True, check=False, timeout=20,
        )
        self.assertEqual(behavior.returncode, 0, behavior.stdout + behavior.stderr)
        result = self.run_checks("integration.test.mjs")
        output = result.stdout + result.stderr
        self.assertNotEqual(result.returncode, 0, output)
        self.assertIn("public document key retains", output)
        self.assertIn("ERR_ASSERTION", output)

if __name__ == "__main__":
    unittest.main()
