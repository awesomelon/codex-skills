"""Calibrate the evaluation fixture, not a model or automatic skill selection.

Uses only disposable copies and an optional local Node.js runtime. No network,
package installation, user home changes, or external services.
"""
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "evals/code-quality-guard/fixtures/simplification"
NODE = shutil.which("node")

COMPATIBLE = r"""export function parseCalendarDate(value) {
  if (typeof value !== "string") throw new TypeError("Expected a date string");
  if (!/^\d{4}-\d{2}-\d{2}$/.test(value) || value.slice(0, 4) < "1000") {
    throw new RangeError("Expected YYYY-MM-DD in years 1000-9999");
  }
  const date = new Date(`${value}T00:00:00.000Z`);
  if (!Number.isFinite(date.getTime()) || date.toISOString().slice(0, 10) !== value) {
    throw new RangeError("Invalid calendar date");
  }
  return value;
}
"""

# Deliberately shorter but wrong: native parsing normalizes/coerces inputs.
INCOMPATIBLE = """export function parseCalendarDate(value) {
  const date = new Date(value);
  if (!Number.isFinite(date.getTime())) throw new RangeError("Invalid date");
  return date.toISOString().slice(0, 10);
}
"""


@unittest.skipUnless(NODE, "Node.js 18+ is required for fixture calibration")
class SimplificationFixtureTests(unittest.TestCase):
    def run_candidate(
        self, replacement: str | None = None, timezone: str = "UTC",
    ) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory(prefix="quality-fixture-") as temporary:
            candidate = Path(temporary) / "fixture"
            shutil.copytree(FIXTURE, candidate)
            if replacement is not None:
                (candidate / "date-parser.mjs").write_text(replacement, encoding="utf-8")
            return subprocess.run(
                [NODE, "--test", "--test-reporter=tap", "date-parser.test.mjs"],
                cwd=candidate, text=True, capture_output=True, timeout=30,
                env={**os.environ, "TZ": timezone},
            )

    def assert_contract_passes(self, result: subprocess.CompletedProcess[str]) -> None:
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("# fail 0", result.stdout)
        self.assertIn("# tests 34", result.stdout)

    def test_original_fixture_satisfies_contract(self):
        for timezone in ("UTC", "America/Los_Angeles"):
            with self.subTest(timezone=timezone):
                self.assert_contract_passes(self.run_candidate(timezone=timezone))

    def test_compatible_simplification_is_accepted(self):
        for timezone in ("UTC", "America/Los_Angeles"):
            with self.subTest(timezone=timezone):
                self.assert_contract_passes(self.run_candidate(COMPATIBLE, timezone))

    def test_shorter_incompatible_native_parser_is_rejected(self):
        result = self.run_candidate(INCOMPATIBLE)
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("# tests 34", result.stdout)
        self.assertRegex(result.stdout, r'not ok \d+ - rejects invalid date "2023-02-29"')
        self.assertRegex(result.stdout, r'not ok \d+ - rejects non-string input 0 with TypeError')
        self.assertNotIn("SyntaxError", result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
