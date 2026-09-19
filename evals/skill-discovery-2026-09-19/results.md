# Discovery and UI metadata audit — 2026-09-19

Baseline: `90832a76688a28984b5b29c52d7bb140529dbf38` in `awesomelon/codex-skills`.

## Findings and changes

All seven entrypoints, UI files, repository authoring rules, and selected execution references were inspected. Their task boundaries and conditional references already substantially follow the designated [OpenAI Astra article](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra), freshly retrieved for this audit. No domain skill body, discovery description, invocation policy, or installer implementation needed a supported change.

- Four UI default prompts repeated scope, reporting, and verification rules already present in their independently installed skill bodies. Architecture, Code Quality, React, and Query now use short task starters that invoke their current names. The bodies retain review-only scope and implementation completion criteria.
- The validator accepted a prompt invoking a retired skill name and a quoted string in the boolean invocation policy. This was reproduced in a disposable package. It now checks supplied UI names/descriptions/prompts and policy fields using the repository's documented single-line conventions. Metadata and individual fields remain optional; dependency declarations and full YAML schema validation remain outside its scope.
- Seven regression tests cover valid and malformed metadata, current-name invocation, policy types, optional fields, description bounds, and preservation of unrelated configuration. The shell installer remains Python-free; no new dependencies or runtime hooks were added.

The four changed UI files total **1,270 → 933 UTF-8 bytes**, a **26.5% reduction**. This is not a reduction in the discovery list, which is unchanged, or a measured token, latency, or quality improvement. Evaluation files stay outside the installed skills.

## Current upstream review

The following default-branch heads were resolved through GitHub on 2026-09-19. Inspection was selective, not a complete audit of every repository. Sources supplied ideas and comparisons; no external scripts or skill packages were copied.

| Source and inspected material | Resolved head | Decision |
| --- | --- | --- |
| [OpenAI skill creator](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.system/skill-creator/SKILL.md) | `49f948f` · June 24 | Retain concise instructions, conditional resources, and consistent UI metadata. Prefer the freshly retrieved Astra article when older authoring advice is more prescriptive. |
| [Anthropic skill creator](https://github.com/anthropics/skills/blob/34040c9c568585f6929bedeaad110ad08f079624/skills/skill-creator/SKILL.md) | `34040c9` · September 10 | Use realistic positive and adjacent negative requests to inspect discovery. Do not import Claude-specific broad triggering, fixed evaluation counts, or an evaluation runtime. |
| [Vercel React Best Practices](https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/react-best-practices/SKILL.md) | `063bee9` · August 28 | Same head as the existing React baseline; retain task-specific local adaptations. No new React-rule audit or wholesale refresh was needed. |
| [Cursor pstack entrypoint](https://github.com/cursor/plugins/blob/032be146865d973682535de75f2287da438550bf/pstack/skills/poteto-mode/SKILL.md) | `032be14` · September 18 | Same head as the existing adaptation. Keep conditional orchestration; do not import its mandatory skill cascades or platform-specific mode. |
| [ECC verification loop](https://github.com/affaan-m/ECC/blob/07756cee15788a54506031462794ad645719b028/skills/verification-loop/SKILL.md) | `07756ce` · September 19 | The inspected blob is unchanged from the previous audit. Retain actual-check evidence, without universal build/lint/security phases, coverage targets, or periodic rechecking. |
| [Ponytail review](https://github.com/DietrichGebert/ponytail/blob/e3ba2aa6f1e6f0bc4d69eb09c9f0d0a93af56156/skills/ponytail-review/SKILL.md) | `e3ba2aa` · September 14 | The inspected blob is unchanged. Retain contract-preserving simplification; do not adopt net deleted lines as the quality objective. |

The current [OpenAI Build skills documentation](https://learn.chatgpt.com/docs/build-skills) was also fetched. It distinguishes name/description discovery from loading the body and recommends clear, front-loaded scope. The installed OpenAI skill-creator's `references/openai_yaml.md` supplied UI field constraints. JSON quoting and two-space indentation are this repository's supported subset, not claims about every valid Codex YAML file.

## Executed checks

| Check | Actual outcome and limits |
| --- | --- |
| Metadata-only selection | A fresh, unforked subagent received only [catalog.json](catalog.json) and [queries.json](queries.json). Its [normalized selections](selections.json) covered all ten relevant requests and left all six adjacent exclusions unselected. Selecting both quality and refactoring for one restructuring request was reasonable overlap, not a demonstrated error. No description was rewritten just to change this result. |
| Short Code Quality UI prompt + read-only review | A fresh subagent used the standalone revised skill and existing policy fixture. It reported the repeated archive policy, preserved independent pinning, distinguished correctness from change cost, and reported seven passing fixture tests. Parent hash comparison confirmed that every supplied file remained unchanged. |
| Short React UI prompt + implementation | A separate fresh subagent used the existing picker fixture and changed only `DocumentPicker.tsx`. It removed redundant derived state and in-place prop sorting without changing public props, display text, or handlers. It reported eleven calculation checks; the parent independently ran the existing nine-assertion derivation check against the saved result. [Code](DocumentPicker.tsx), [check](check-picker.mjs), [output](derivation-check.txt). |
| Structural validators | All seven source packages passed both the repository validator and the installed OpenAI skill-creator's `quick_validate.py`. |
| Regression suite | `bash -n scripts/install.sh` and `python3 -m unittest discover -s tests -v`: 57 tests passed, including seven new metadata tests. |
| Standalone copy installation | In a disposable destination, all seven copied packages matched source contents and passed UI validation. No actual user installation was changed. |

The source-package validator initially rejected installed-copy management markers, as designed. The installation check was corrected to compare source files and call the UI validator on installed copies; it did not remove those markers or change the installer.

Input/output hashes and execution limits are in [manifest.json](manifest.json). [Task prompts](prompts.json) identify the existing fixtures and normalize only workspace paths. Skill files were identical before and after the forward runs; only the React task fixture changed. The parent provided raw tasks and inputs, without expected findings or earlier answers.

These were one metadata-only selection pass and two explicit UI-prompt task runs, not live automatic invocation, a controlled before/after behavior comparison, or a statistical benchmark. Architecture and Query UI prompts were inspected and structurally validated but not independently executed. The runner was Linux; macOS installation, React rendering, TypeScript compilation, browser interactions, and general speed/token improvements remain unmeasured.
