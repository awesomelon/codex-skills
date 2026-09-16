# Astra skill refinement — 2026-09-16

Baseline: `8d59c883a8e5b1ada712c76f9feb051c16cef2fa` in `awesomelon/codex-skills`.

## Basis and scope

The user-designated [Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) was retrieved and read in this session. It favors precise discovery descriptions, conditional detail, and task-appropriate completion over elaborate fixed procedures. These principles guide this revision; shorter text alone is not evidence of better behavior.

Two independent agents inspected the five skill entrypoints and relevant references, and researched upstream examples. The existing collection already follows most of the article. Preserve its domain guidance and independently installable work boundaries; no new installed skill is justified by the findings.

## Changes

| Finding | Revision |
| --- | --- |
| TypeScript's description mentions review only for input validation, while its existing cases cover type review. | Explicitly include designing and reviewing types. |
| Query design is supported by existing case 16 but absent from its description. | Include design while retaining the Query-specific scope and exclusions. |
| Architecture implementation always requires a final change review, duplicating the separate review workflow. | Require verification of affected boundaries and contracts; retain the review route when review is requested. |
| Parameter-design advice is loaded for every TypeScript task. | Move that advice unchanged to the existing type-modeling reference. |
| The collection has an add-skill prompt but no reusable prompt for the user's recurring improvement task. | Add `prompts/improve-skills.md`, outside skill discovery, with source-based findings and independent evaluation guidance. Record the required article in repository instructions. |

These are instruction-analysis findings, not measured baseline model failures. The metadata edits make existing supported use cases explicit; they do not establish improved automatic selection. React and code-quality packages, installer behavior, UI invocation policies, and historical evidence remain unchanged.

## External ideas considered

The research agent read these primary sources on 2026-09-16. No upstream implementation or instruction block was copied.

| Source | Use in this revision |
| --- | --- |
| [Ponytail](https://github.com/DietrichGebert/ponytail/blob/main/skills/ponytail/SKILL.md) | Existing code-quality guidance already prefers small changes and justified abstractions. Keep that guidance; do not import blanket coding activation or compression as a goal. |
| [ECC skill-stocktake](https://github.com/affaan-m/ECC/blob/main/skills/skill-stocktake/SKILL.md) | The improvement prompt asks for concrete reasons to change a skill and permits keeping effective guidance. Avoid fixed batches and repeated approval steps. |
| [ECC agent-eval](https://github.com/affaan-m/ECC/blob/main/skills/agent-eval/SKILL.md) | Use realistic tasks, observable outcomes, and separate evidence from scenario expectations, without introducing another runner. |
| [pstack context-window](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-guard-the-context-window/SKILL.md) | Keep small common constraints in the entrypoint and conditional parameter guidance in its reference. Do not impose fixed turn budgets or mandatory delegation. |

The [pstack mirror notice](https://github.com/backnotprop/pstack/blob/main/MIRROR.md) identifies `cursor/plugins/pstack` as upstream. Source links identify what was consulted; they are not a promise that future upstream revisions will match this audit.

## Evidence

See [structural results](../evals/astra-refinement-2026-09-16/structural-results.json) for actual commands, output, baseline, and entrypoint hashes. All five packages passed the repository validator and the current bundled skill-creator validator on macOS with Python 3.12. PyYAML was installed only in a disposable validation directory. Installer and validator implementations did not change, so their regression suite and installation tests were not repeated.

Behavioral execution and its limitations are recorded separately in [evaluation results](../evals/astra-refinement-2026-09-16/results.md).
