# Full skill audit — 2026-09-14

> English translation of a historical record. [Original at the pre-translation commit](https://github.com/awesomelon/codex-skills/blob/ce11c34e3d1da77140087300218b776594bb65cf/docs/skill-audit-2026-09-14.md). Reported runs, hashes, and counts describe the original work, not this translation.

Baseline: `2e561f747302c6d86bb5844424175b7835be2459`. Audited all three skills, including the new `code-quality-guard`: their SKILL.md files, UI metadata, every reference, repository AGENTS.md, two always-loaded guidance examples, two request templates, and existing evaluation records. The latest source was copied into a separate local workspace with no initial user changes.

[OpenAI's Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) informed checks of invocation precision, relevant reference loading, and excessive process, validation, or stopping demands. The changes below are audit judgments applying those criteria to this repository.

## Findings and improvements

| Area | Observed problem | Change |
| --- | --- | --- |
| Always-loaded examples | Required architecture review before and after all code/configuration/dependency work, regardless of impact. This could override narrower skill descriptions. | Apply to changes in responsibilities, dependency direction, shared state, or public API design, or explicit architecture reviews. Reuse evidence and avoid extra review for unrelated local edits. |
| Skill path in examples | The personal example assumed one fixed installation folder, different from the actual location in the session. | Use the session-provided location. If missing, continue with available code/guidance and state limits without implicitly requiring installation or settings changes. |
| New quality description | Mixed selection conditions with details about correctness, cost, duplication, and complexity. | Reduced to maintainability review/improvement, before/after comparison, and exclusions. Retained judgments in the body. |
| Quality comparison reference | Ordinary before/after comparison also loaded scoring, A/B comparison, and special metrics. Four-stage judgment wording encouraged a fixed report. | Separated common comparison into measurement.md and scores/alternative implementations/source calculations into scoring.md. Kept perspectives without fixed labels. |
| Architecture/React bodies | Before/after quality comparison referred through another installed skill. Although not mandatory, standalone criteria could be direct. | Stated same-scope/same-criteria comparison and evidence reuse in each body without adding dependencies. |
| New-skill request template | Required insufficient-input, permission, and failure-handling evaluations regardless of capability. | Cover representative requests and likely non-invocation; select other cases only when relevant. |
| Actual quality execution | The initial evaluation repeated passing baseline tests to save report output. | Reuse results on the same code/conditions, without rerunning merely for records absent a new edit, failure, or uncertainty. Reevaluate only that case. |

## Preserved guidance

Kept skill roles, read-only requests, user-requested implementation through verification, and evidence-based conclusions. Also retained architectural consumer/state/dependency judgments and React draft preservation, request ordering, cache isolation, and version-specific API conditions. Domain references were not shortened simply because they were long.

At the time of this audit, UI metadata, invocation examples, and selection settings were appropriate and unchanged. Repository AGENTS.md already selected documents/checks conditionally and constrained remote scope, so it remained unchanged. The initial-publication template applies to explicit first-publication requests where account and remote verification matter; it was preserved. Installer and validator were unchanged.

Scoring and source formulas were moved into a new reference without changing their substance. This audit did not update React or metric source versions or newly validate effects claimed by those sources.

## Reading size

Character counts use Python `len(text)`, including whitespace/newlines. These are not token, speed, or accuracy measurements.

| Document | Before | After |
| --- | ---: | ---: |
| Quality skill description | 92 | 60 |
| General-comparison measurement.md | 2,600 | 1,563 |
| architecture-guard SKILL.md | 1,462 | 1,439 |
| react-quality-guard SKILL.md | 1,483 | 1,463 |
| code-quality-guard SKILL.md | 1,889 | 1,954 |

The quality body grew slightly to route references and address repeated checks observed in evaluation. The goal was relevant guidance for the current task, not minimizing every file. Specialized comparison reads the additional reference.

## Actual behavioral evaluation

Used Codex CLI 0.154.0 on macOS, requesting `gpt-6-astra` with `medium` reasoning. A separate model snapshot identifier was not verified. Each run used a new temporary folder and independent one-shot conversation. User configuration was excluded, but existing authentication and personal-skill discovery remained available. This was not a completely isolated account or empty installation environment.

Evaluators received only the skill and actual TASK input, without expected conclusions, findings, solutions, or prior results. Edits were limited to temporary inputs; network, package installation, and GitHub operations were prohibited. Model execution itself used its connection. Ran three explicit-invocation cases and one implicit case using example guidance, then repeated only the revised quality case once.

| Case | Observed result | References read |
| --- | --- | --- |
| [Initial quality improvement](../evals/skill-audit-2026-09-14/outputs/quality.md) | Archive-policy edit points went from 3 to 1; independent pin policy retained. Existing 7 tests passed before/after, but baseline checks ran twice. This motivated the rerun guidance. | measurement.md |
| [Quality reevaluation](../evals/skill-audit-2026-09-14/outputs/quality-retest.md) | Same policy improvement and public-function preservation. Existing 7 tests ran once before and once after, passing both times. No invented complexity/clone measurements. | measurement.md |
| [Architecture review](../evals/skill-audit-2026-09-14/outputs/architecture.md) | Explained prohibited core-to-feature dependency and hidden billing-state coupling. Did not flag the allowed exception; all input hashes were preserved. | review.md |
| [React improvement](../evals/skill-audit-2026-09-14/outputs/react.md) | Changed only DocumentPicker.tsx. Removed shared-array sorting and an unnecessary Effect, preserving public props/input/selection. Actual calculation checks passed. | react-correctness.md, performance.md |
| [Local volume fix](../evals/skill-audit-2026-09-14/outputs/local-change.md) | With example AGENTS.md and three skills available, changed only volume.mjs and passed supplied tests. Did not read skill bodies/references or add an architecture report. | None |

Fewer checks in reevaluation are an observation from this sample, not proof of repeatability or a controlled A/B improvement. The quality run attempted Git status in a non-Git input folder, then continued using the supplied snapshot. React runs reported absent runtime dependencies and type checking.

Saved [commands and exit codes](../evals/skill-audit-2026-09-14/outputs/commands.json), [requests and before/after/skill hashes](../evals/skill-audit-2026-09-14/outputs/manifest.json), responses, check output, and patches in the same folder. Temporary absolute file links in responses were normalized to filenames. Attachment filenames in original quality reports refer to run-time locations; saved check records and patches establish actual output and source changes. The initial quality SKILL.md was also preserved.

## Validation and limits

- Repository `scripts/validate.py`: all three skills passed structure, metadata, and internal references.
- Official `quick_validate.py`: all three passed. Checked UI YAML, invocation examples, and automatic-selection settings. PyYAML 6.0.3 ran in a disposable virtual environment.
- Copy installation in a macOS temporary folder: all three skills installed, with every source file matching, including scoring.md. No real personal installation folder was used.
- Implementation checks: 7 quality tests passed before/after; React calculation checks and volume-range tests passed. TASK files, supplied tests, and skill copies retained their hashes in every run.
- Verified patch reapplication, final source hashes, documentation links, and whitespace. Directly compared AGENTS.md with the baseline copy; unchanged.

The installer/validator were unchanged, so their full suite was not repeated. React rendering, browser interaction, type checking, build, and performance were unverified because inputs lacked execution environments. Scores, A/B/source-metric calculations, missing-skill behavior, automatic invocation for public API changes, multiple models, large repositories, and desktop automatic selection were outside actual execution. The full new scenario set is not claimed to pass.

Work used branch `feature/skill-audit-2026-09-14`. Installed skills, global guidance, and the current app project were unchanged. At the time of this record, remote publication was to follow a separate request after audit completion.
