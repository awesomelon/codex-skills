from pathlib import Path
import json
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate import validate


class UIMetadataTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="skill ui ")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.skill = self.root / "skills" / "example"
        (self.skill / "agents").mkdir(parents=True)
        (self.skill / "SKILL.md").write_text(
            "---\nname: example\ndescription: A focused workflow\n---\n# Example\n",
            encoding="utf-8",
        )
        self.ui = self.skill / "agents" / "openai.yaml"

    def write_field(self, field, value):
        self.ui.write_text(
            f"interface:\n  {field}: {json.dumps(value)}\n", encoding="utf-8"
        )

    def test_ui_file_and_individual_fields_remain_optional(self):
        self.assertEqual(len(validate(self.root)), 1)
        self.write_field("display_name", "Example")
        self.assertEqual(len(validate(self.root)), 1)

    def test_valid_metadata_preserves_explicit_only_policy_and_dependencies(self):
        contents = (
            'interface:\n  display_name: "Example"\n'
            '  short_description: "Review one concrete engineering task"\n'
            '  default_prompt: "Use $example for the requested work."\n'
            'policy:\n  allow_implicit_invocation: false\n'
            'dependencies:\n  tools:\n    - type: "mcp"\n      value: "github"\n'
        )
        self.ui.write_text(contents, encoding="utf-8")
        self.assertEqual(len(validate(self.root)), 1)
        self.assertEqual(self.ui.read_text(encoding="utf-8"), contents)

    def test_renamed_or_partial_skill_invocations_fail(self):
        for prompt in ("Use $old-name.", "Use $example-extra.", "Use example.", "Use $$example."):
            with self.subTest(prompt=prompt):
                self.write_field("default_prompt", prompt)
                with self.assertRaisesRegex(ValueError, r"must invoke \$example"):
                    validate(self.root)

    def test_punctuation_after_skill_invocation_is_valid(self):
        self.write_field("default_prompt", "Use $example: review this code.")
        self.assertEqual(len(validate(self.root)), 1)

    def test_invocation_policy_requires_a_boolean(self):
        for value in ('"false"', "yes", "0", "", "null"):
            with self.subTest(value=value):
                self.ui.write_text(f"policy:\n  allow_implicit_invocation: {value}\n")
                with self.assertRaisesRegex(ValueError, "boolean invocation policy"):
                    validate(self.root)
        for value in ("true", "false"):
            self.ui.write_text(f"policy:\n  allow_implicit_invocation: {value}\n")
            self.assertEqual(len(validate(self.root)), 1)

    def test_ui_strings_are_nonempty_and_short_description_has_documented_bounds(self):
        for value in ("", "  ", None, 42):
            with self.subTest(value=value):
                self.write_field("display_name", value)
                with self.assertRaisesRegex(ValueError, "nonempty UI string"):
                    validate(self.root)
        for size in (24, 65):
            self.write_field("short_description", "a" * size)
            with self.assertRaisesRegex(ValueError, "25-64"):
                validate(self.root)
        for size in (25, 64):
            self.write_field("short_description", "a" * size)
            self.assertEqual(len(validate(self.root)), 1)

    def test_ambiguous_or_malformed_known_fields_fail(self):
        samples = (
            ('interface:\n  display_name: "Example\n', "JSON-quoted"),
            ('interface:\n display_name: "Example"\n', "indentation"),
            ('interface:\n  display_name: "One"\n  display_name: "Two"\n', "Duplicate"),
        )
        for contents, message in samples:
            with self.subTest(contents=contents):
                self.ui.write_text(contents)
                with self.assertRaisesRegex(ValueError, message):
                    validate(self.root)


if __name__ == "__main__":
    unittest.main()
