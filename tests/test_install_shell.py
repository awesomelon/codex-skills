"""Exercise the shell CLI in temporary paths; Python is only the test runner."""
from pathlib import Path
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from install import install as legacy_install


class ShellInstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="shell skills 한글 ")
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / "checkout"
        self.dest = self.base / "user" / ".agents" / "skills"
        (self.root / "scripts").mkdir(parents=True)
        self.script = self.root / "scripts/install.sh"
        shutil.copyfile(Path(__file__).resolve().parents[1] / "scripts/install.sh", self.script)
        self.bin = self.base / "bin"
        self.bin.mkdir()
        # No Python, Node, Ruby, jq, GNU realpath, or external package manager.
        for name in ("cat", "dirname", "shasum", "cp", "mv", "mktemp", "rm", "mkdir", "ln"):
            executable = shutil.which(name)
            if not executable:
                self.skipTest(f"Missing test utility: {name}")
            (self.bin / name).symlink_to(executable)
        self.env = dict(os.environ, PATH=str(self.bin))
        self.source = self.add_skill("example")
        self.target = self.dest / "example"

    def add_skill(self, name):
        skill = self.root / "skills" / name
        (skill / "references").mkdir(parents=True)
        (skill / "SKILL.md").write_text(f"---\nname: {name}\ndescription: Example\n---\n")
        (skill / "references/check.md").write_text("original\n")
        return skill

    def run_cli(self, *args, ok=True, dest=None):
        result = subprocess.run(
            ["/bin/bash", str(self.script), "--dest", str(dest or self.dest), *args],
            cwd=self.base, env=self.env, text=True, capture_output=True, timeout=20,
        )
        if ok:
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        return result

    def snapshot(self, folder):
        if not folder.exists():
            return None
        result = {}
        for path in folder.rglob("*"):
            name = str(path.relative_to(folder))
            if path.is_symlink():
                result[name] = ("link", os.readlink(path))
            elif path.is_dir():
                result[name] = ("dir",)
            else:
                result[name] = ("file", path.read_bytes())
        return result

    def test_python_free_link_install_repeat_and_live_update(self):
        self.run_cli()
        self.assertEqual(self.target.resolve(), self.source.resolve())
        self.assertIn("unchanged:", self.run_cli().stdout)
        (self.source / "references/check.md").write_text("updated")
        self.assertEqual((self.target / "references/check.md").read_text(), "updated")

    def test_legacy_python_link_is_reused(self):
        legacy_install(self.root, self.dest, "link")
        self.assertIn("unchanged:", self.run_cli().stdout)

    def test_list_dry_run_and_help_do_not_write(self):
        before = self.snapshot(self.base)
        self.assertEqual(self.run_cli("--list").stdout.strip(), "example")
        self.assertIn("DRY RUN", self.run_cli("--dry-run", "--mode", "copy").stdout)
        self.run_cli("--help")
        self.assertEqual(self.snapshot(self.base), before)

    def test_repeated_selection_and_new_skill_discovery(self):
        self.add_skill("another")
        result = self.run_cli("--skill", "example", "--skill", "example")
        self.assertEqual(result.stdout.count("install:"), 1)
        self.assertFalse((self.dest / "another").exists())
        self.run_cli()
        self.assertTrue((self.dest / "another").is_symlink())

    def test_bad_arguments_fail_without_writes(self):
        before = self.snapshot(self.base)
        for args in [("--skill", "../example"), ("--skill", "unknown"), ("--skill",),
                     ("--mode", "other"), ("--unknown",), ("--dest", "")]:
            with self.subTest(args=args):
                self.run_cli(*args, ok=False)
        self.assertEqual(self.snapshot(self.base), before)

    def test_preflight_blocks_entire_selection_on_foreign_directory(self):
        self.add_skill("aaa")
        self.target.mkdir(parents=True)
        (self.target / "local.txt").write_text("keep")
        before = self.snapshot(self.base)
        self.run_cli(ok=False)
        self.assertEqual(self.snapshot(self.base), before)

    def test_foreign_and_broken_links_are_preserved(self):
        self.dest.mkdir(parents=True)
        for location in [self.base, self.base / "missing"]:
            with self.subTest(location=location):
                self.target.symlink_to(location)
                self.run_cli(ok=False)
                self.assertEqual(os.readlink(self.target), str(location))
                self.target.unlink()

    def test_relative_link_to_same_source_is_reused(self):
        self.dest.mkdir(parents=True)
        self.target.symlink_to(os.path.relpath(self.source, self.dest))
        self.assertIn("unchanged:", self.run_cli().stdout)

    def test_copy_update_deletes_obsolete_source_files_only(self):
        before = self.snapshot(self.root)
        self.run_cli("--mode", "copy")
        self.assertFalse(self.target.is_symlink())
        self.assertEqual(self.snapshot(self.root), before)
        self.assertIn("unchanged:", self.run_cli("--mode", "copy").stdout)
        (self.source / "references/check.md").unlink()
        (self.source / "new.md").write_text("new")
        self.assertIn("update:", self.run_cli("--mode", "copy").stdout)
        self.assertFalse((self.target / "references/check.md").exists())
        self.assertEqual((self.target / "new.md").read_text(), "new")

    def test_local_copy_edits_additions_and_deletions_are_preserved(self):
        mutations = [
            lambda: (self.target / "SKILL.md").write_text("local edit"),
            lambda: (self.target / "notes").write_text("local notes"),
            lambda: (self.target / "empty").mkdir(),
            lambda: (self.target / "references/check.md").unlink(),
        ]
        for mutate in mutations:
            with self.subTest(mutate=mutate):
                if self.target.exists():
                    shutil.rmtree(self.target)
                self.run_cli("--mode", "copy")
                mutate()
                before = self.snapshot(self.base)
                self.run_cli("--mode", "copy", ok=False)
                self.assertEqual(self.snapshot(self.base), before)

    def test_legacy_copy_preserved_with_migration_message(self):
        legacy_install(self.root, self.dest, "copy")
        before = self.snapshot(self.base)
        result = self.run_cli("--mode", "copy", ok=False)
        self.assertIn("Legacy Python copy preserved", result.stderr)
        self.assertEqual(self.snapshot(self.base), before)

    def test_cannot_silently_switch_install_mode(self):
        self.run_cli()
        self.run_cli("--mode", "copy", ok=False)
        self.assertTrue(self.target.is_symlink())
        self.target.unlink()
        self.run_cli("--mode", "copy")
        self.run_cli(ok=False)
        self.assertFalse(self.target.is_symlink())

    def test_source_symlink_fifo_and_metadata_are_rejected(self):
        bad = self.source / "bad"
        for kind in ("symlink", "fifo", "marker", "legacy"):
            with self.subTest(kind=kind):
                if kind == "symlink":
                    bad.symlink_to(self.base)
                elif kind == "fifo":
                    os.mkfifo(bad)
                else:
                    bad = self.source / (".codex-skills-install.v2" if kind == "marker" else ".codex-skills-install.json")
                    bad.write_text("invalid")
                self.run_cli(ok=False)
                self.assertFalse(self.dest.exists())
                bad.unlink()

    def test_copy_handles_hidden_empty_and_unusual_filenames(self):
        (self.source / "empty").mkdir()
        (self.source / ".hidden").write_text("hidden")
        unusual = self.source / "한글 newline\n$(touch should-not-exist)`echo oops`.md"
        unusual.write_text("original")
        self.run_cli("--mode", "copy")
        self.assertEqual((self.target / unusual.name).read_text(), "original")
        self.assertTrue((self.target / "empty").is_dir())
        self.assertIn("unchanged:", self.run_cli("--mode", "copy").stdout)
        (self.target / unusual.name).write_text("local")
        self.run_cli("--mode", "copy", ok=False)
        self.assertFalse((self.base / "should-not-exist").exists())

    def test_destination_overlap_and_symlink_ancestor_are_rejected(self):
        alias = self.base / "alias"
        alias.symlink_to(self.root)
        for dest in [self.root, self.root / "new/subdir", alias / "new", self.root / "new/../skills"]:
            with self.subTest(dest=dest):
                before = self.snapshot(self.root)
                self.run_cli(dest=dest, ok=False)
                self.assertEqual(self.snapshot(self.root), before)

    def test_destination_symlink_and_parent_resolution(self):
        actual = self.base / "elsewhere" / "nested"
        actual.mkdir(parents=True)
        alias = self.base / "alias"
        alias.symlink_to(actual)
        self.run_cli(dest=alias / "../installed")
        self.assertTrue((actual.parent / "installed/example").is_symlink())
        self.assertFalse((self.base / "installed").exists())

    def test_newline_destination_alias_fails_without_writes(self):
        actual = self.base / "newline\n"
        actual.mkdir()
        alias = self.base / "alias"
        alias.symlink_to(actual)
        before = self.snapshot(self.base)
        self.run_cli(dest=alias / "skills", ok=False)
        self.assertEqual(self.snapshot(self.base), before)

    def test_invalid_marker_is_never_executed(self):
        self.run_cli("--mode", "copy")
        marker = self.target / ".codex-skills-install.v2"
        marker.write_text("$(touch injected)\n")
        before = self.snapshot(self.base)
        self.run_cli("--mode", "copy", ok=False)
        self.assertEqual(self.snapshot(self.base), before)

    def test_unrelated_skill_is_untouched(self):
        other = self.dest / "unrelated"
        other.mkdir(parents=True)
        (other / "notes").write_text("keep")
        self.run_cli()
        self.assertEqual((other / "notes").read_text(), "keep")

    def inject_mv_failure(self, restoration=False):
        real_mv = shutil.which("mv")
        (self.bin / "mv").unlink()
        # shell quoting for the executable path; no user input or credentials.
        quoted = "'" + real_mv.replace("'", "'\\''") + "'"
        pattern = "*/staging|*/backup" if restoration else "*/staging"
        (self.bin / "mv").write_text(
            f'#!/bin/bash\ncase "$1" in {pattern}) exit 73 ;; esac\nexec {quoted} "$@"\n'
        )
        (self.bin / "mv").chmod(0o755)

    def test_failed_replacement_restores_previous_copy(self):
        self.run_cli("--mode", "copy")
        before = self.snapshot(self.target)
        (self.source / "SKILL.md").write_text("upstream update")
        self.inject_mv_failure()
        self.run_cli("--mode", "copy", ok=False)
        self.assertEqual(self.snapshot(self.target), before)
        self.assertFalse(list(self.dest.parent.glob(".codex-skills.*")))

    def test_failed_first_copy_leaves_no_partial_install(self):
        self.inject_mv_failure()
        self.run_cli("--mode", "copy", ok=False)
        self.assertFalse(self.target.exists())
        self.assertFalse(list(self.dest.parent.glob(".codex-skills.*")))

    def test_failed_restore_leaves_backup_outside_discovery(self):
        self.run_cli("--mode", "copy")
        before = self.snapshot(self.target)
        (self.source / "SKILL.md").write_text("upstream update")
        self.inject_mv_failure(restoration=True)
        result = self.run_cli("--mode", "copy", ok=False)
        backups = list(self.dest.parent.glob(".codex-skills.*/backup"))
        self.assertEqual(len(backups), 1)
        self.assertEqual(self.snapshot(backups[0]), before)
        self.assertIn(str(backups[0]), result.stderr)


if __name__ == "__main__":
    unittest.main()
