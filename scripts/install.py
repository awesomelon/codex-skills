#!/usr/bin/env python3
"""Install this collection without overwriting unrelated or locally edited skills.

Python 3.10+, standard library only. Never runs git, network requests, or skill code.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import stat
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
COLLECTION = "awesomelon/codex-skills"
MARKER = ".codex-skills-install.json"
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


def indirect(path: Path) -> bool:
    """Reject junctions/reparse points as well as symbolic links during copying."""
    try:
        info = path.lstat()
    except FileNotFoundError:
        return False
    return stat.S_ISLNK(info.st_mode) or bool(
        getattr(info, "st_file_attributes", 0)
        & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)
    )


def fingerprint(folder: Path) -> str:
    """Hash names and contents, including empty dirs; ignore only our root marker."""
    if indirect(folder) or not folder.is_dir():
        raise ValueError(f"Not a regular directory: {folder}")
    digest = hashlib.sha256()
    for path in sorted(folder.rglob("*")):
        if indirect(path):
            raise ValueError(f"Links/reparse points inside a skill are not supported: {path}")
        if path == folder / MARKER:
            continue
        relative = path.relative_to(folder).as_posix()
        if path.is_dir():
            record = [relative, "directory"]
        elif path.is_file():
            record = [relative, hashlib.sha256(path.read_bytes()).hexdigest()]
        else:
            raise ValueError(f"Not a regular skill file: {path}")
        digest.update(json.dumps(record, ensure_ascii=True).encode("utf-8") + b"\n")
    return digest.hexdigest()


def discover(root: Path = ROOT) -> dict[str, Path]:
    folder = root / "skills"
    if not folder.is_dir():
        raise ValueError(f"Missing skills directory: {folder}")
    found = {}
    for path in sorted(folder.iterdir()):
        if path.name.startswith("."):
            continue
        if indirect(path) or not path.is_dir() or not (path / "SKILL.md").is_file():
            raise ValueError(f"Each skills/ entry must be a regular skill directory: {path}")
        if not NAME.fullmatch(path.name) or len(path.name) > 64:
            raise ValueError(f"Invalid skill directory name: {path.name}")
        if (path / MARKER).exists():
            raise ValueError(f"Do not commit installation metadata into skills/: {path}")
        fingerprint(path)
        found[path.name] = path.resolve()
    if not found:
        raise ValueError("No skills found")
    return found


def disposition(source: Path, target: Path, mode: str) -> str:
    if target.is_symlink():
        if mode == "link" and target.resolve() == source:
            return "unchanged"
        raise ValueError(f"Existing link is not this installation; preserved: {target}")
    if indirect(target):
        raise ValueError(f"Existing junction/reparse point is preserved: {target}")
    if not target.exists():
        return "install"
    if mode != "copy" or not target.is_dir():
        raise ValueError(f"Existing path is preserved: {target}")
    try:
        metadata = json.loads((target / MARKER).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise ValueError(f"Not a managed copy; move it to a backup first: {target}") from exc
    if not isinstance(metadata, dict) or any(
        metadata.get(key) != value
        for key, value in {"version": 1, "collection": COLLECTION, "skill": source.name}.items()
    ):
        raise ValueError(f"Foreign installation metadata; preserved: {target}")
    actual = fingerprint(target)
    if actual != metadata.get("sha256"):
        raise ValueError(f"Locally edited copy; preserve/merge your edits before updating: {target}")
    return "unchanged" if actual == fingerprint(source) else "update"


def copy_skill(source: Path, target: Path) -> None:
    # Stage and backup live outside the skill-discovery directory, on the same volume.
    temporary = Path(tempfile.mkdtemp(prefix=".codex-skills-", dir=target.parent.parent))
    staging, backup = temporary / "staging", temporary / "backup"
    try:
        shutil.copytree(source, staging)
        metadata = {
            "version": 1, "collection": COLLECTION,
            "skill": source.name, "sha256": fingerprint(staging),
        }
        (staging / MARKER).write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
        disposition(source, target, "copy")  # Recheck before touching an existing copy.
        if target.exists():
            target.rename(backup)
        try:
            staging.rename(target)
        except OSError:
            if backup.exists():
                try:
                    backup.rename(target)
                except OSError as restore_error:
                    raise OSError(f"Restore failed; previous copy preserved at {backup}") from restore_error
            raise
        # Delete only a known, unedited prior managed copy after successful replacement.
        if backup.exists():
            shutil.rmtree(backup)
    finally:
        # On restoration failure, leave the backup intact instead of cleaning it away.
        if not backup.exists():
            shutil.rmtree(temporary)


def install(root: Path, destination: Path, mode: str, names: list[str] | None = None,
            dry_run: bool = False) -> list[str]:
    if mode not in {"link", "copy"}:
        raise ValueError("mode must be link or copy")
    skills = discover(root)
    selected = list(dict.fromkeys(names or skills.keys()))
    unknown = set(selected) - skills.keys()
    if unknown:
        raise ValueError("Unknown skill(s): " + ", ".join(sorted(unknown)))
    destination = destination.expanduser().resolve()
    # Prevent self-installation or staging/backup within the source checkout.
    repository = root.resolve()
    if destination == repository or repository in destination.parents:
        raise ValueError("Installation destination must be outside the skills source repository")
    plans = []
    for name in selected:
        source = skills[name]
        target = destination / name
        if target == repository or target in repository.parents:
            raise ValueError(f"Destination overlaps source checkout: {target}")
        plans.append((source, target, disposition(source, target, mode)))
    messages = []
    # Validate every selected destination first; fail before installing on known conflicts.
    for source, target, action in plans:
        messages.append(f"{'DRY RUN ' if dry_run else ''}{action}: {target} ({mode})")
        if dry_run or action == "unchanged":
            continue
        destination.mkdir(parents=True, exist_ok=True)
        if mode == "link":
            target.symlink_to(source, target_is_directory=True)
        else:
            copy_skill(source, target)
    return messages


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dest", type=Path, default=Path.home() / ".agents" / "skills")
    parser.add_argument("--mode", choices=("link", "copy"),
                        default="copy" if os.name == "nt" else "link")
    parser.add_argument("--skill", action="append", help="Install only this skill; repeatable")
    parser.add_argument("--dry-run", action="store_true", help="Inspect without modifying anything")
    parser.add_argument("--list", action="store_true", help="List available skills")
    args = parser.parse_args()
    try:
        if args.list:
            print("\n".join(discover()))
        else:
            for message in install(ROOT, args.dest, args.mode, args.skill, args.dry_run):
                print(message)
            if not args.dry_run:
                print("Installation complete. Verify in Codex; restart it if the skill is not visible.")
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
