from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate import validate


class YAMLValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="skill yaml ")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.skill = self.root / "skills" / "example"
        (self.skill / "agents").mkdir(parents=True)
        self.write_description("Review code quality")

    def write_description(self, value):
        (self.skill / "SKILL.md").write_text(
            f"---\nname: example\ndescription: {value}\n---\n# Example\n",
            encoding="utf-8",
        )

    def test_unquoted_mapping_separator_is_rejected(self):
        self.write_description("Review: code quality")
        with self.assertRaisesRegex(ValueError, "Invalid YAML"):
            validate(self.root)

    def test_quoted_colon_and_yaml_escaped_quotes_are_valid(self):
        for value in ('"Review: code quality"', "'Review developers'' code'"):
            with self.subTest(value=value):
                self.write_description(value)
                self.assertEqual(len(validate(self.root)), 1)

    def test_nonstring_descriptions_are_rejected(self):
        for value in ("true", "123", "null", "[]", "{}", '"  "'):
            with self.subTest(value=value):
                self.write_description(value)
                with self.assertRaisesRegex(ValueError, "nonempty strings"):
                    validate(self.root)

    def test_malformed_yaml_in_dependency_fields_is_rejected(self):
        (self.skill / "agents/openai.yaml").write_text("dependencies:\n  tools: [\n")
        with self.assertRaisesRegex(ValueError, "Invalid YAML"):
            validate(self.root)

    def test_duplicate_sections_and_nested_dependency_keys_are_rejected(self):
        for text in (
            'interface:\n  display_name: "First"\ninterface:\n  short_description: "Review a concrete engineering task"\n',
            'dependencies:\n  tools:\n    - type: "mcp"\n      type: "other"\n',
        ):
            with self.subTest(text=text):
                (self.skill / "agents/openai.yaml").write_text(text)
                with self.assertRaisesRegex(ValueError, "Duplicate YAML key"):
                    validate(self.root)

    def test_ui_root_and_known_sections_must_be_mappings(self):
        for text in ("[]\n", "interface: []\n", "policy: false\n"):
            with self.subTest(text=text):
                (self.skill / "agents/openai.yaml").write_text(text)
                with self.assertRaisesRegex(ValueError, "mapping"):
                    validate(self.root)

    def test_unsafe_yaml_tags_are_rejected(self):
        self.write_description('!!python/object/apply:builtins.str [123]')
        with self.assertRaisesRegex(ValueError, "Invalid YAML"):
            validate(self.root)

    def test_inline_or_quoted_known_keys_cannot_bypass_ui_conventions(self):
        for text in (
            'interface: {default_prompt: "Use $old-name."}\n',
            'interface:\n  "default_prompt": "Use $old-name."\n',
            'policy: {allow_implicit_invocation: "false"}\n',
        ):
            with self.subTest(text=text):
                (self.skill / "agents/openai.yaml").write_text(text)
                with self.assertRaisesRegex(ValueError, "indentation"):
                    validate(self.root)


if __name__ == "__main__":
    unittest.main()
