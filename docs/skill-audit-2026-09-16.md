# Skill audit follow-up — 2026-09-16

Baseline: `247aac97db443fa4e38e7836cf253b9d5ae806b2` on `awesomelon/codex-skills/main`, including the merged TypeScript naming and task-boundary follow-up in PR #9.

## Source and scope

The user-designated [Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) could not be retrieved in this session: the canonical URL and alternate forms returned cache-miss errors. This is **not a fresh line-by-line verification of that article**. The repository's [previously recorded interpretation](https://github.com/awesomelon/codex-skills/blob/247aac97db443fa4e38e7836cf253b9d5ae806b2/docs/skill-audit-2026-09-15-followup.md) was cross-checked against accessible current OpenAI documentation:

- [Build skills](https://learn.chatgpt.com/docs/build-skills): discovery uses names and descriptions; the full entrypoint is read when a skill is selected. Use task-specific guidance and progressive disclosure.
- [Model guidance](https://developers.openai.com/api/docs/guides/latest-model): audit conflicting skill instructions, finish the requested work, and calibrate verification to the change rather than repeating checks without a reason.

Inspected all five `SKILL.md` entrypoints, repository `AGENTS.md`, README, the code-quality skill's complete existing references and UI metadata, installer/validator source, and the previous follow-up audit. This is an instruction/routing audit, not a new technical correctness audit of every React, Query, or TypeScript reference. No new measured model defect is claimed.

## Findings and changes

| Finding | Evidence at the baseline | Change |
| --- | --- | --- |
| Change-specific guidance is loaded for every code-quality task | The entrypoint includes PR merge-base selection, mixed local-change scope, hypothetical extensions, and unused-code checks even for a small current-state review. | Move those decisions to `references/review.md`, selected for change review, full audit, improvement, or future-change analysis. Keep small current-state reviews self-contained. |
| Selection metadata omits an existing work mode | The code-quality body supports improvement, while its description names design, implementation, review, and comparison but not improvement. | Explicitly name maintainability improvement and keep routine-edit exclusions in the body. Automatic-selection effects remain unmeasured. |
| The first installation and update examples select everything | README recommends installing only recurring needs, but its main command examples invoke the all-skills default. | Lead with discovery, a selected-skill dry run and install, and an update retaining that selection. Preserve the explicit all-skills option and existing installer behavior. |

The other four entrypoints already route by relevant decisions. Keep them unchanged rather than rewrite working guidance to meet a length target. Keep `AGENTS.md`, UI prompts, the four existing code-quality references, installer and validator implementations, TypeScript naming, and historical execution evidence unchanged. Repeated work-mode boundaries across independently installable skills remain intentional. No shared runtime dependency, new skill, compatibility alias, mandatory subagent workflow, or auto-migration is introduced.

## Preserved decisions

The entrypoint still separates correctness from maintainability; preserves assessed material while allowing requested reports; completes authorized implementation and relevant checks; preserves necessary defensive code and checking rules; rejects metric gaming; reuses sufficient checks; and withholds unsupported quality claims. Its safety and stopping rules do not depend on loading the new review reference.

The relocated guidance retains verified PR base/head and merge-base selection, staged/unstaged/untracked scope, starting user changes, audit sampling limits, estimated-versus-observed change cost, independent policy ownership, dynamic registration/re-exports, and comparable before/after verification. Existing implementation guidance still handles shared-policy design independently. Scenario 11 reflects routing, cases 19–21 cover the relocated decisions, and the other 17 existing cases remain byte-for-byte unchanged. These cases are expectations, **not newly passing model runs**.

## Size and tradeoff

Counts are Unicode code points, including frontmatter and whitespace, not tokens:

| Surface | Before | After |
| --- | ---: | ---: |
| Code-quality entrypoint | 4,408 | 3,044 |
| Discovery description | 143 | 93 |
| Entrypoint plus the new review reference | 4,408 | 4,412 |

The entrypoint is 30.94% shorter. A task that also loads the new reference sees approximately the same text volume and an additional file read; this is not a universal speedup. The purpose is to avoid loading change-specific detail for tasks that do not need it, not to delete useful judgment criteria. No token, latency, model-quality, or automatic-selection improvement was measured.

## Validation and limits

See [structural execution results](../evals/skill-audit-2026-09-16/structural-results.json) for command output, Git blob hashes, counts, and explicit scope.

A direct clone failed because the execution environment could not resolve github.com. The changed skill package and supporting validation files were reconstructed from GitHub connector reads; original bytes were checked against their fetched Git blob SHAs. No placeholder references or fabricated source files were used.

Executed on Linux:

- The unchanged `python3 scripts/validate.py` passed for the complete **code-quality-guard package in this partial checkout**, not for all five packages.
- YAML parsing, matching UI invocation, all eight skill-local links, existing reference/UI byte preservation, and four relocated decision-paragraph comparisons passed.
- Checked retained entrypoint boundaries, unchanged evaluation cases, README link-change scope, text hygiene, and recorded content hashes. These are mechanical checks, not evidence that a model obeys the instructions.

Not run: the all-five-package validator, official skill-creator validator, the full installer/validator regression suite, shell installation, macOS/Bash 3.2 execution, fresh Codex behavioral cases, automatic selection, or controlled model A/B evaluation. Installer and validator source were not changed. Fresh-session cases 11 and 19–21 and a full-checkout structural run remain advisable before merging; keep the proposed change as a draft PR until those checks are resolved. Earlier execution results are not relabeled as validation of this revision.
