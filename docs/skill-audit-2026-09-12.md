# Skill audit and improvements — 2026-09-12

> English translation of a historical record. [Original at the pre-translation commit](https://github.com/awesomelon/codex-skills/blob/ce11c34e3d1da77140087300218b776594bb65cf/docs/skill-audit-2026-09-12.md). Reported runs, hashes, and counts describe the original work, not this translation.

Baseline commit: `2a17c3950824ab6547bc498df4cd9818c1727bcc`. Scope: both complete skills, repository `AGENTS.md`, invocation snippets, and the add-skill request template.

The user-designated [OpenAI article](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) informed concise/discriminating descriptions, relevant references, outcome-oriented instructions, and risk-proportionate validation. No specific model was required.

## Findings and changes

| Finding | Improvement |
| --- | --- |
| Both descriptions repeated detailed checks from their bodies | Kept selection-relevant purpose and likely exclusions |
| Architecture body, preflight, and review repeated scope/reporting/validation guidance | Kept ownership, dependencies, contracts, and intervention criteria in the body; retained stage-specific judgments in references |
| Four preflight output items and fixed review classifications encouraged report templates for small tasks | Preserved evidence and conclusions while allowing the format to follow the request and task size |
| React entry guidance implied checking all versions, lockfiles, builds, routers, and Compiler every time | Inspect environment only when it affects API support, bundles, or memo decisions; reuse supplied context |
| Repository guidance and the add-skill template required the full installer suite even for wording-only skill changes | Tie structure checks to skill changes, installer tests to code changes, and behavioral evaluation to significant instruction changes |
| Always-loaded snippets repeated investigation/reporting steps from the skill | Retained the then-existing preflight/completion policy, invocation path, and review-only boundary |

Preserved purpose, explicit required checks, read-only requests, and remote write scope. Also preserved private-repository requirements, existing user changes, the no-force-push rule, and macOS scope. Installer, validator, and test code were unchanged, as were `agents/openai.yaml` display names, invocation examples, and automatic-selection policy.

Kept all four React references. Draft preservation, uncertainty about omitted API internals, memo defaults, Effect Events, React 18 transitions, and server-cache conditions had been useful domain-specific criteria in earlier evaluation. They were not removed simply for length or replaced with generic checklists. The initial-publication template remained as a record of how to repeat already completed work.

## Length comparison

Unicode character counts use Python `len(text)`. SKILL.md counts include frontmatter and newlines. These are not token counts, execution speed, or model-quality improvements.

| Target | Before | After | Reduction |
| --- | ---: | ---: | ---: |
| architecture-guard SKILL.md | 2,720 | 1,367 | 49.7% |
| react-quality-guard SKILL.md | 2,219 | 1,391 | 37.3% |
| Architecture description | 89 | 64 | 28.1% |
| React description | 131 | 80 | 38.9% |
| Repository AGENTS.md | 1,124 | 975 | 13.3% |

The two SKILL.md files together decreased from 4,939 to 2,758 characters. This audit and evaluation records live outside installed skills.

## Behavioral evaluation

Copied revised skills and original inputs into separate temporary folders. Three independent agents without conversation history received only the skill path and respective TASK.md. They did not receive expected findings, solutions, or other evaluation outputs. All runs used explicit invocation; no separate model-version identifier was collected.

| Input | Observed result | References read |
| --- | --- | --- |
| [Current architecture review](../evals/skill-audit-2026-09-12/fixtures/architecture/TASK.md) | Identified core-to-feature dependency and hidden billing-state coupling. Did not flag the permitted adapter exception or claim regressions without a baseline | review.md |
| [React review](../evals/react-quality-guard/fixtures/review/TASK.md) | Found tenant caching and draft loss after refetch failure. Did not assert missing updates inside an opaque API; proposed preserving draft, memo, and save state | react-correctness.md, performance.md |
| [React implementation](../evals/react-quality-guard/fixtures/implementation/TASK.md) | Changed only DocumentPicker, removing source-array mutation, derived state, and an Effect. Preserved display/public props/input/selection and completed available calculation checks | react-correctness.md, performance.md |

References and commands were confirmed with agents afterward without additional execution. Before/after hashes verified unchanged inputs in both reviews and changes to only one implementation file. Evidence is saved in the [architecture review](../evals/skill-audit-2026-09-12/outputs/architecture-review.md), [React review](../evals/skill-audit-2026-09-12/outputs/react-review.md), [implementation report](../evals/skill-audit-2026-09-12/outputs/react-implementation.md), [implementation code](../evals/skill-audit-2026-09-12/outputs/DocumentPicker.tsx), and [skill/input hashes](../evals/skill-audit-2026-09-12/outputs/manifest.json).

These three samples met scope, reference-selection, and evidence-level criteria. This was not a controlled A/B performance comparison with the prior skills. It does not establish all-scenario success, automatic discovery/non-invocation accuracy, or repeatability. Portions of the newly added small-task and stopping scenarios beyond these samples remain unexecuted.

## Execution checks and limits

Executed in a Linux container:

- Passed both skills' `quick_validate.py`, repository `scripts/validate.py`, and UI YAML checks.
- Ran all 24 installer tests once as required by instructions at audit start; all passed. Did not repeat them for subsequent documentation edits.
- Nine [Node checks](../evals/skill-audit-2026-09-12/outputs/check-picker.mjs) extracting the actual calculation from the new implementation passed. They covered sorting, search, source immutability, empty input, new props, and element identity. Existing checks were reused for this output.
- Verified unchanged review inputs and skill-copy hashes, implementation edit scope, and relative Markdown links in distribution files.

React rendering, type checks, browser interactions, and performance profiling were not run. macOS installation and automatic Codex invocation remain unverified. The user's installed skills and global guidance were unchanged. The earlier [React authoring evaluation](../evals/react-quality-guard/results.md) and [initial publication validation](validation.md) remain historical records.

To reproduce, copy each input folder into its own workspace and ask the respective skill to perform TASK.md. Preserve original inputs and separately record outputs, changed files, and skill version. From the repository root, run calculation checks with `node evals/skill-audit-2026-09-12/outputs/check-picker.mjs`.
