# Refactoring Guard validation

Date: 2026-09-18. Environment: macOS, Darwin 27.0.0 arm64. Repository starting commit: `78e68252c851408edf9ba50507ecbf6138766bd5`.

## Scope and source review

Added an independently installable [Refactoring Guard](../../skills/refactoring-guard/SKILL.md), UI metadata, primary-source attribution, the README catalog entry, and [15 evaluation cases](cases.md). Existing skill instructions, installer code, and validator code were not changed.

Read the Fowler pages and OpenAI authoring article listed in [sources.md](../../skills/refactoring-guard/references/sources.md) directly for this revision. The separate skill addresses the sequence and verification of behavior-preserving edits. The existing code-quality skill retains general maintainability assessment and shared-rule design.

## Author assessment

This is an assessment of written guidance against the cases, not an independent model run or a claim that code refactoring was executed.

| Cases | Assessment |
| --- | --- |
| 1, 15 | Selection text identifies existing-code restructuring. UI metadata retains automatic selection, and the standalone copy was checked. Actual automatic selection remains untested. |
| 2, 3 | Review and planning preserve assessed code, while an explicitly requested plan can be written. A long cohesive parser does not by itself justify extraction. |
| 4, 5, 12 | Instructions identify externally observable results and effects, require focused current-behavior tests for risky changes with missing coverage, and preserve evaluation and asynchronous ordering. No billing, import, or asynchronous example was executed in this run. |
| 6, 13 | Starting failures and new regressions have separate handling; progress depends on establishing relevant behavior rather than changing expectations. Existing user edits must survive any undo. |
| 7, 8 | Existing defects are reported without silently correcting them. A requested feature may proceed separately from preparatory refactoring and its checks. |
| 9, 10, 11 | The guidance allows separate policies and function inlining, and accounts for consumers beyond the repository when considering public API renames. |
| 14 | Completion depends on the requested structural result and relevant verification, with no metric target or repeated checks for unchanged conditions. |

## Executed checks

- `python3 scripts/validate.py`: passed for all six skills. Also passed with Python 3.11.16, meeting the repository's Python 3.10+ development requirement; the shell's default Python was 3.9.6.
- `skill-creator/scripts/quick_validate.py skills/refactoring-guard`: passed using a disposable Python 3.11.16 environment with PyYAML 6.0.3. Initial attempts with existing Python installations reported missing PyYAML; the dependency was installed only in the temporary environment.
- `bash scripts/install.sh --list`: listed all six skills, including `refactoring-guard`.
- `bash scripts/install.sh --skill refactoring-guard --mode copy --dest <temporary-directory>/installed-skills`: passed on macOS. Compared every installed skill file byte for byte with its source.
- Parsed `agents/openai.yaml` and checked the display name, short-description length, explicit skill invocation, default automatic-selection policy, and absence of companion dependencies: passed.
- Changed-document local links and Markdown fences: passed.
- `git diff --check`: passed.
- Compared `AGENTS.md` byte for byte with its pre-edit copy: unchanged.

Instruction and scenario SHA-256 values at assessment time:

| File | SHA-256 |
| --- | --- |
| `skills/refactoring-guard/SKILL.md` | `af08acb8d343cd9a1fa3d1eca65650f142bf7d729ba72fe7d289bb965d4a47d9` |
| `skills/refactoring-guard/agents/openai.yaml` | `919207e814bb1330cb4cc5e62e06cf0ae22e09bf046b1b2309b1eddede3335c3` |
| `skills/refactoring-guard/references/sources.md` | `b336ea67d33537e7191e442fa0879d025056517c4dfb4154cabfb6dfb2781723` |
| `evals/refactoring-guard/cases.md` | `921784ddc6202d404de0c4f8df6852f743705be0001924b2504835a1807ac83d` |

## Limits

No independent model evaluation, automatic-selection experiment, or application refactoring was run; behavioral cases remain proposed scenarios. Structural checks and installation do not establish model execution quality. No installer or validator implementation changed, so their full test suites were not rerun. User-installed skills and Codex settings were not modified.
