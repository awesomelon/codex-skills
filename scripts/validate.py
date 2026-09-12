#!/usr/bin/env python3
"""Check this repository's simple frontmatter convention and local reference paths.

Not a general YAML parser or an official Codex validator. No model is invoked.
"""
from __future__ import annotations

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

from install import ROOT, discover


def validate(root: Path = ROOT) -> list[str]:
    results = []
    for name, folder in discover(root).items():
        text = (folder / "SKILL.md").read_text(encoding="utf-8")
        lines = text.splitlines()
        if not lines or lines[0] != "---" or "---" not in lines[1:]:
            raise ValueError(f"Missing frontmatter: {name}")
        end = lines.index("---", 1)
        fields = {}
        for line in lines[1:end]:
            # This collection intentionally uses only single-line name/description.
            match = re.fullmatch(r"(name|description):\s*(.+)", line)
            if not match or match[1] in fields:
                raise ValueError(f"Use one single-line name and description in {name}")
            value = match[2].strip()
            if value.startswith(('"', "'")):
                if len(value) < 2 or value[-1] != value[0]:
                    raise ValueError(f"Unclosed metadata quote: {name}")
                value = value[1:-1]
            if not value or value in ("|", ">", "|-", ">-"):
                raise ValueError(f"Use a nonempty single-line metadata value: {name}")
            fields[match[1]] = value
        if fields.get("name") != name or not fields.get("description"):
            raise ValueError(f"Frontmatter name/description mismatch: {name}")
        if len(fields["description"]) > 1024:
            raise ValueError(f"Description is too long: {name}")
        for doc in folder.rglob("*.md"):
            for target in re.findall(r"!?\[[^\]\n]*\]\(([^)\n]+)\)", doc.read_text(encoding="utf-8")):
                target = target.strip().strip("<>")
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                resolved = (doc.parent / unquote(parsed.path)).resolve()
                if not resolved.is_relative_to(folder) or not resolved.is_file():
                    raise ValueError(f"Broken/escaping reference in {doc}: {target}")
        results.append(f"PASS {name}: basic metadata, portable contents, local references")
    return results


def main() -> int:
    try:
        print("\n".join(validate()))
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
