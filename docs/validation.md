# Validation records

> English translation of a historical record. [Original at the pre-translation commit](https://github.com/awesomelon/codex-skills/blob/ce11c34e3d1da77140087300218b776594bb65cf/docs/validation.md). Reported runs, hashes, and counts describe the original work, not this translation.

The installation entry point moved to shell on 2026-09-13. See [shell installer validation](shell-installer-validation.md) for the current installation/validation workflow.

The records below describe their respective publication stages. Subsequent audits of both skill bodies and separate behavioral evaluations are in the [2026-09-12 audit](skill-audit-2026-09-12.md).

Validation date: 2026-09-12. The existing package was revalidated in a Linux container while publishing it to GitHub.

## Work performed

- Reused all four original architecture-guard files: SKILL.md, agents/openai.yaml, and two references, without content changes.
- `python scripts/validate.py`: passed basic frontmatter conventions and skill-local relative references.
- `python -m unittest discover -s tests -v`: passed 24 tests covering installation, updates, collisions, user-change preservation, recovery, and validation.
- Exercised actual CLI list, preview, link, copy, reinstall, and exit codes against temporary user paths.
- Parsed original skill YAML, checked relative Markdown references across distribution files, and verified ZIP integrity.
- Verified that the user-created `awesomelon/codex-skills` repository was private, had an empty initial history, and allowed writes.
- Replaced the initial ZIP-only README with installation/update instructions for the existing repository. Preserved original skill bodies, references, installer, and tests.

## macOS scope

- Made installation/update guidance and future work instructions specific to macOS.
- Removed OS-dependent installer defaults and used symbolic links by default. Retained explicit copy mode for independent project copies.
- Revalidated default CLI link installation, repeated execution, structure, and the existing 24 tests in Linux temporary paths after the change. Skill bodies and references were unchanged.

Both link and copy paths ran on Linux, which does not replace execution on macOS. Recovery tests inject I/O errors; they do not guarantee recovery from every storage failure.

## React quality skill

The [separate record](../evals/react-quality-guard/results.md) covers `react-quality-guard` structure, installation, behavioral evaluation, and limits. Existing `architecture-guard` and installer code were unchanged.

## Not executed or completed

- GitHub Actions CI was neither configured nor run. These results are local execution records.
- The user's ~/.agents/skills, ~/.codex/AGENTS.md, and config.toml were unchanged.
- Actual Codex discovery, automatic/explicit invocation, before/after skill execution, and review quality were not verified.
- The 12 cases in `evals/architecture-guard/cases.md` were model-behavior scenarios, not pass records.
- `validate.py` is neither a general YAML parser nor an official Codex validator. It does not validate external URL availability, every Markdown form, or semantic instruction conflicts.

## Rerun

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Record actual macOS Codex validation separately after installation on a Mac, checking the invocation list and behavioral scenarios.
