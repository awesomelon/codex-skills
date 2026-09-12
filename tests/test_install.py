from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from install import MARKER, discover, install
from validate import validate


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="skills test ")
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / "checkout"
        self.dest = self.base / "home" / ".agents" / "skills"
        self.source = self.add_skill("example")
        self.target = self.dest / "example"

    def add_skill(self, name):
        path = self.root / "skills" / name
        (path / "references").mkdir(parents=True)
        (path / "SKILL.md").write_text(
            f"---\nname: {name}\ndescription: Test workflow\n---\n"
            "# Test\n[Reference](references/check.md)\n", encoding="utf-8")
        (path / "references" / "check.md").write_text("original\n", encoding="utf-8")
        return path

    def symlink(self, link, source):
        try:
            link.symlink_to(source, target_is_directory=True)
        except OSError:
            self.skipTest("This platform does not allow directory symlinks")

    def run_install(self, mode="copy", **kwargs):
        return install(self.root, self.dest, mode, **kwargs)

    def test_copy_installs_complete_skill_and_leaves_source_unchanged(self):
        self.run_install()
        self.assertTrue((self.target / "references/check.md").is_file())
        self.assertTrue((self.target / MARKER).is_file())
        self.assertFalse((self.source / MARKER).exists())

    def test_repeated_copy_is_unchanged(self):
        self.run_install()
        self.assertIn("unchanged:", self.run_install()[0])

    def test_managed_copy_updates_and_removes_obsolete_reference(self):
        self.run_install()
        (self.source / "references/check.md").unlink()
        (self.source / "new.md").write_text("new", encoding="utf-8")
        result = self.run_install()
        self.assertIn("update:", result[0])
        self.assertFalse((self.target / "references/check.md").exists())
        self.assertTrue((self.target / "new.md").exists())

    def test_locally_edited_copy_is_preserved(self):
        self.run_install()
        file = self.target / "SKILL.md"
        file.write_text("local change", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Locally edited"):
            self.run_install()
        self.assertEqual(file.read_text(), "local change")

    def test_local_extra_file_is_preserved(self):
        self.run_install()
        (self.target / "notes.md").write_text("local notes", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Locally edited"):
            self.run_install()
        self.assertTrue((self.target / "notes.md").exists())

    def test_local_empty_directory_is_preserved(self):
        self.run_install()
        (self.target / "local-empty").mkdir()
        with self.assertRaisesRegex(ValueError, "Locally edited"):
            self.run_install()

    def test_existing_unmanaged_directory_is_preserved(self):
        self.target.mkdir(parents=True)
        (self.target / "notes").write_text("keep", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Not a managed"):
            self.run_install()
        self.assertEqual((self.target / "notes").read_text(), "keep")

    def test_broken_link_is_not_overwritten(self):
        self.dest.mkdir(parents=True)
        self.symlink(self.target, self.base / "missing")
        with self.assertRaisesRegex(ValueError, "Existing link"):
            self.run_install()
        self.assertTrue(self.target.is_symlink())

    def test_link_install_is_repeatable(self):
        probe = self.base / "probe"
        self.symlink(probe, self.source)
        probe.unlink()
        self.run_install(mode="link")
        self.assertEqual(self.target.resolve(), self.source.resolve())
        self.assertIn("unchanged:", self.run_install(mode="link")[0])

    def test_same_link_cannot_silently_switch_to_copy(self):
        self.dest.mkdir(parents=True)
        self.symlink(self.target, self.source)
        with self.assertRaises(ValueError):
            self.run_install(mode="copy")
        self.assertEqual(self.target.resolve(), self.source.resolve())

    def test_source_link_is_rejected(self):
        self.symlink(self.source / "external", self.base)
        with self.assertRaisesRegex(ValueError, "Links/reparse"):
            self.run_install()
        self.assertFalse(self.dest.exists())

    def test_unknown_or_traversal_name_is_rejected(self):
        for name in ("missing", "../example", "/tmp"):
            with self.subTest(name=name):
                with self.assertRaisesRegex(ValueError, "Unknown skill"):
                    self.run_install(names=[name])
        self.assertFalse(self.dest.exists())

    def test_dry_run_writes_nothing(self):
        self.assertIn("DRY RUN", self.run_install(dry_run=True)[0])
        self.assertFalse(self.dest.exists())

    def test_self_installation_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "outside"):
            install(self.root, self.root / "skills", "copy")
        self.assertFalse((self.source / MARKER).exists())

    def test_new_skill_is_picked_up_without_install_script_changes(self):
        self.run_install()
        self.add_skill("another")
        self.run_install()
        self.assertTrue((self.dest / "another/SKILL.md").exists())

    def test_selection_does_not_install_other_skills(self):
        self.add_skill("another")
        self.run_install(names=["example"])
        self.assertFalse((self.dest / "another").exists())

    def test_unrelated_installed_skill_is_untouched(self):
        other = self.dest / "foreign"
        other.mkdir(parents=True)
        (other / "data").write_text("do not touch", encoding="utf-8")
        self.run_install()
        self.assertEqual((other / "data").read_text(), "do not touch")

    def test_conflicts_are_detected_before_any_install(self):
        self.add_skill("aaa")
        self.target.mkdir(parents=True)
        with self.assertRaises(ValueError):
            self.run_install()
        self.assertFalse((self.dest / "aaa").exists())

    def test_failed_replacement_restores_previous_copy(self):
        self.run_install()
        original = (self.target / "SKILL.md").read_bytes()
        (self.source / "SKILL.md").write_text("changed", encoding="utf-8")
        rename = Path.rename

        def fail_staging(path, destination):
            if path.name == "staging":
                raise OSError("simulated replacement failure")
            return rename(path, destination)

        with patch.object(Path, "rename", fail_staging):
            with self.assertRaisesRegex(OSError, "simulated replacement"):
                self.run_install()
        self.assertEqual((self.target / "SKILL.md").read_bytes(), original)

    def test_failed_restoration_keeps_backup(self):
        self.run_install()
        original = (self.target / "SKILL.md").read_bytes()
        (self.source / "SKILL.md").write_text("changed", encoding="utf-8")
        rename = Path.rename

        def fail_staging_and_restore(path, destination):
            if path.name in ("staging", "backup"):
                raise OSError("simulated I/O failure")
            return rename(path, destination)

        with patch.object(Path, "rename", fail_staging_and_restore):
            with self.assertRaisesRegex(OSError, "previous copy preserved"):
                self.run_install()
        copies = list(self.dest.parent.glob(".codex-skills-*/backup/SKILL.md"))
        self.assertEqual(len(copies), 1)
        self.assertEqual(copies[0].read_bytes(), original)

    def test_valid_package_metadata_and_references(self):
        self.assertEqual(list(discover(self.root)), ["example"])
        self.assertIn("PASS example", validate(self.root)[0])

    def test_broken_reference_fails_validation(self):
        (self.source / "references/check.md").unlink()
        with self.assertRaisesRegex(ValueError, "Broken/escaping"):
            validate(self.root)

    def test_escaping_reference_fails_validation(self):
        outside = self.root / "secret.md"
        outside.write_text("outside", encoding="utf-8")
        skill = self.source / "SKILL.md"
        skill.write_text(skill.read_text().replace("references/check.md", "../../secret.md"), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Broken/escaping"):
            validate(self.root)

    def test_name_mismatch_fails_validation(self):
        skill = self.source / "SKILL.md"
        skill.write_text(skill.read_text().replace("name: example", "name: different"), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "mismatch"):
            validate(self.root)


if __name__ == "__main__":
    unittest.main()
