# Follow-up skill audit — 2026-09-14

> English translation of a historical record. [Original at the pre-translation commit](https://github.com/awesomelon/codex-skills/blob/ce11c34e3d1da77140087300218b776594bb65cf/docs/skill-audit-2026-09-14-followup.md). Reported runs, hashes, and counts describe the original work, not this translation.

Baseline: `9fda923949502a7ab5f6a8e35950cb3056109da2`. The previous audit [PR #2](https://github.com/awesomelon/codex-skills/pull/2) was already merged into main. Read all three skill bodies/references/UI metadata, AGENTS.md, always-loaded examples, request templates, README, and evaluation cases to address remaining issues.

[OpenAI's article on skills and prompts](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) recommends specific invocation boundaries, reading only relevant material, and reducing duplicate or excessive procedures. The changes below apply those principles; they are not measured model-performance improvements.

## Findings and changes

| Area | Remaining issue | Remedy |
| --- | --- | --- |
| Quality references | Unscored A/B comparison still loaded scoring.md; ordinary score requests also exposed Earendil formulas. | Moved A/B criteria to measurement.md and special metrics to earendil-metrics.md. Limited scoring.md to scoring and conditionally linked common measurement criteria. |
| Add-skill request | macOS, installer, folder, and validation conventions were maintained in both AGENTS.md and the template. | Kept common rules in AGENTS.md and retained purpose, invocation boundaries, work scope, and completion conditions in the prompt. Preserved temporary installation checks and completion through a PR. |
| UI metadata | Architecture wording suggested both pre/post review; the default quality prompt requested before/after evidence every time. | Described architectural review subjects and made the default quality request usable with current-code evidence. Preserved automatic-selection policy and read-only scope. |
| Installation guidance | GitHub reported a public repository while README asserted private visibility and required GitHub CLI/authentication. | Removed the incorrect assertion and documented public HTTPS clone. Repository visibility was not changed. |

Existing architecture/React criteria, requested implementation through verification, read-only boundaries, data/contract protection, and metric limitations were appropriate and retained. AGENTS.md, installer/validator code, installed personal skills, and global settings were unchanged. Earlier audits remain historical records.

## Document size

Python `len(text)` counts include whitespace/newlines. Reference totals exclude SKILL.md and describe that reading path, not actual tokens or speed. Old scoring.md required measurement.md as common conditions, so both count in the old total.

| Material | Before | After |
| --- | ---: | ---: |
| Complete add-skill template | 1,239 | 794 |
| Qualitative current-state scoring references | 2,709 | 366 |
| Unscored A/B comparison references | 2,709 | 1,728 |

General before/after measurement.md grew from 1,563 to 1,728 characters by receiving the A/B paragraph. Special-metric requests read their dedicated document and common measurement conditions. Reducing every reading path was not the goal.

## Validation

- Repository `python3 scripts/validate.py`: all three skills passed structure/internal references.
- Official `quick_validate.py`: all three passed. Checked UI YAML description lengths, explicit-invocation examples, and existing selection policy.
- Linux temporary copy installation with `bash scripts/install.sh --mode copy --dest <temporary-path>`: all 15 source files, including the new reference, matched installed content. This was not macOS hardware validation.
- Ran one unscored A/B comparison in an independent fresh conversation. Prepared alternatives using the existing archive-policy fixture and existing improvement patch; provided only the skill, contract, and request. The response reported measurement.md use, 7 existing tests passing in each implementation, and preservation of independent pinning. Independently verified unchanged hashes for all 15 input files. Saved the [actual response](../evals/code-quality-guard/outputs/ab-routing-review.md) and [request/hashes/check record](../evals/code-quality-guard/outputs/ab-routing-manifest.json). Reference use and test results rely on the evaluator response; the raw tool trace was not saved separately.

New score, special-metric, and UI-default behavior received static review and updated scenarios only. The unchanged installer/validator did not trigger another full suite. Desktop automatic selection, multiple models/repeated-run stability, response time, and token savings were not measured.
