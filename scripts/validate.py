#!/usr/bin/env python3
"""Check repository metadata conventions and local reference paths.

Parses YAML safely and checks repository conventions. Not an official
Codex schema validator. No model is invoked.
"""
from __future__ import annotations

from pathlib import Path
import json
import re
import sys
from urllib.parse import unquote, urlsplit

import yaml

from install import ROOT, discover


class UniqueKeyLoader(yaml.SafeLoader):
    """Reject ambiguous duplicate keys instead of silently taking the last value."""

    def construct_mapping(self, node, deep=False):
        keys = set()
        for key_node, _ in node.value:
            if key_node.tag == "tag:yaml.org,2002:merge":
                continue
            key = self.construct_object(key_node, deep=deep)
            try:
                if key in keys:
                    raise ValueError(f"Duplicate YAML key: {key}")
                keys.add(key)
            except TypeError as exc:
                raise ValueError("YAML mapping keys must be scalar values") from exc
        return super().construct_mapping(node, deep=deep)


def yaml_mapping(text: str, path: Path) -> dict:
    try:
        value = yaml.load(text, Loader=UniqueKeyLoader)
    except (yaml.YAMLError, ValueError) as exc:
        raise ValueError(f"Invalid YAML in {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"Expected a YAML mapping in {path}")
    return value


def validate_ui_metadata(folder: Path, name: str) -> None:
    """Check YAML syntax and known fields in our single-line UI metadata.

    UI metadata and its fields remain optional. Unrelated fields (including
    dependency declarations) are left to the host's schema validation.
    """
    path = folder / "agents" / "openai.yaml"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    section = None
    seen = set()
    string_fields = {"display_name", "short_description", "default_prompt"}
    for line in text.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if not line[0].isspace():
            section = line.split(":", 1)[0]
            continue
        match = re.fullmatch(r"\s+(\w+):\s*(.*)", line)
        if not match:
            continue
        field, raw = match.groups()
        is_string = section == "interface" and field in string_fields
        is_policy = section == "policy" and field == "allow_implicit_invocation"
        if not (is_string or is_policy):
            continue
        key = (section, field)
        if key in seen:
            raise ValueError(f"Duplicate UI metadata field in {name}: {field}")
        seen.add(key)
        if not line.startswith("  " + field + ":"):
            raise ValueError(f"Use two-space UI field indentation in {name}: {field}")
        if is_policy:
            if raw.strip() not in {"true", "false"}:
                raise ValueError(f"Use a boolean invocation policy in {name}")
            continue
        try:
            value = json.loads(raw)
        except ValueError as exc:
            raise ValueError(f"Use a JSON-quoted single-line UI string in {name}: {field}") from exc
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"Use a nonempty UI string in {name}: {field}")
        if field == "short_description" and not 25 <= len(value) <= 64:
            raise ValueError(f"UI short_description must be 25-64 characters in {name}")
        if field == "default_prompt" and not re.search(
            rf"(?<![\w$])\${re.escape(name)}(?![\w-])", value
        ):
            raise ValueError(f"UI default_prompt must invoke ${name}")
    metadata = yaml_mapping(text, path)
    for section in ("interface", "policy"):
        if section in metadata and not isinstance(metadata[section], dict):
            raise ValueError(f"UI {section} must be a mapping in {name}")
        known = string_fields if section == "interface" else {"allow_implicit_invocation"}
        for field in metadata.get(section, {}):
            if field in known and (section, field) not in seen:
                raise ValueError(f"Use two-space UI field indentation in {name}: {field}")


def validate(root: Path = ROOT) -> list[str]:
    results = []
    for name, folder in discover(root).items():
        text = (folder / "SKILL.md").read_text(encoding="utf-8")
        lines = text.splitlines()
        if not lines or lines[0] != "---" or "---" not in lines[1:]:
            raise ValueError(f"Missing frontmatter: {name}")
        end = lines.index("---", 1)
        seen = set()
        for line in lines[1:end]:
            # This collection intentionally uses only single-line name/description.
            match = re.fullmatch(r"(name|description):\s*(.+)", line)
            if not match or match[1] in seen:
                raise ValueError(f"Use one single-line name and description in {name}")
            if match[2].strip() in ("|", ">", "|-", ">-"):
                raise ValueError(f"Use a nonempty single-line metadata value: {name}")
            seen.add(match[1])
        fields = yaml_mapping("\n".join(lines[1:end]), folder / "SKILL.md")
        if any(not isinstance(fields.get(key), str) or not fields[key].strip()
               for key in ("name", "description")):
            raise ValueError(f"Use nonempty strings for name and description in {name}")
        if fields.get("name") != name or not fields.get("description"):
            raise ValueError(f"Frontmatter name/description mismatch: {name}")
        if len(fields["description"]) > 1024:
            raise ValueError(f"Description is too long: {name}")
        validate_ui_metadata(folder, name)
        for doc in folder.rglob("*.md"):
            for target in re.findall(r"!?\[[^\]\n]*\]\(([^)\n]+)\)", doc.read_text(encoding="utf-8")):
                target = target.strip().strip("<>")
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                resolved = (doc.parent / unquote(parsed.path)).resolve()
                if not resolved.is_relative_to(folder) or not resolved.is_file():
                    raise ValueError(f"Broken/escaping reference in {doc}: {target}")
        results.append(f"PASS {name}: basic metadata, UI fields, portable contents, local references")
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
