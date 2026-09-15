# Skill audit follow-up — 2026-09-15

Baseline: `144188c65d99ecc88d2b267fb895bf7aa262afe5` on `awesomelon/codex-skills/main`, after the preceding audit was merged in PR #8.

The [OpenAI article](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) recommends precise selection descriptions, conditional reading, and boundaries that let the agent finish the requested work. This follow-up applies those principles to remaining instruction conflicts and the requested TypeScript naming change. The findings are instruction analysis, not measured model or performance regressions.

## Findings and changes

| Finding | Baseline evidence | Change |
| --- | --- | --- |
| Planning/review boundaries prohibit requested deliverables | AGENTS.md, architecture, React, code-quality, and snippets prohibit documentation or file changes during planning/review. | Preserve assessed material while allowing explicitly requested plans or reports. Align all five independently installable skills, repository guidance, and both snippets. |
| Planning can finish before its requested artifact exists | Architecture preflight calls the design judgment complete. | Include any requested plan artifact in completion. |
| UI selection can suggest unrequested implementation | React says to assess, then complete improvements. TypeScript lists modeling and input validation together for every request. | Default to assessment without implementation edits; complete requested changes with relevant verification. Align the code-quality UI wording too. |
| Always-loaded snippets have a broader trigger | The architecture description names contracts between modules, but snippets mention public API design and shared state more broadly. | Match snippet and README triggers to module boundaries, dependency direction, state ownership, and inter-module contracts. |
| TypeScript naming differs from the collection | Folder, frontmatter, display name, and invocation use typescript-best-practices / TypeScript Best Practices. | Rename to typescript-quality-guard / TypeScript Quality Guard, including README commands and the evaluation directory. |
| Renaming leaves installed entries behind | The installers discover current directories and preserve renamed/removed installations. | Document replacement of old links/copies, preserving local edits outside discovery paths and retaining mode/destination options. No automatic migration is claimed. |

The TypeScript description now anchors input validation to TypeScript. Preserve all four TypeScript references, compiler/runtime examples, and historical evaluation evidence byte-for-byte. Existing routers, technical guidance, attribution, and the TanStack license remain intact. Matching scope wording across independent skill packages is intentional: each must work without the repository's AGENTS.md or another skill.

The README explains subset installation beside the full-collection example. Installer defaults and code are unchanged. No compatibility alias, new skill, mandatory agent delegation, or generic framework is added.

## Rename map

| Before | After |
| --- | --- |
| skills/typescript-best-practices/ | skills/typescript-quality-guard/ |
| name: typescript-best-practices | name: typescript-quality-guard |
| TypeScript Best Practices | TypeScript Quality Guard |
| $typescript-best-practices | $typescript-quality-guard |
| --skill typescript-best-practices | --skill typescript-quality-guard |
| evals/typescript-best-practices/ | evals/typescript-quality-guard/ |

The relocated historical results retain their original name because they describe the pre-rename run. They do not validate the revised instructions or installation.

## Validation

The first attempt had no usable execution environment and stopped before GitHub publication. On resumption, the environment was available and `main` still matched the pinned baseline. Validation below describes this resumed revision.

- `python3 scripts/validate.py`: all five skills passed metadata, portable-content, and local-reference checks.
- The bundled skill-creator `quick_validate.py`: all five skills passed.
- Parsed every UI YAML file; checked short descriptions, matching invocation names, and preserved automatic-selection settings.
- Verified all four TypeScript reference files and the relocated historical result against baseline bytes; verified project/global snippet parity.
- Eleven installer CLI invocations passed on Linux, covering discovery, link/copy dry runs, standalone link/copy installation, repeated installation, and documented migration from a broken link and a locally edited managed copy. Installed contents matched source; backup assertions preserved source/copy edits and old management metadata. See [installation output](../evals/skill-audit-2026-09-15-followup/installation.json).
- An independent architecture planning request created only the requested `docs/export-plan.md`; all three fixture source files retained their hashes. The plan addresses actual module dependencies, distinct filenames, CSV compatibility, JSON output, and proposed checks. See [saved plan](../evals/skill-audit-2026-09-15-followup/export-plan.md).

- An independent React review using the revised UI prompt returned supported findings while retaining both fixture file hashes and creating no files. See [raw review output](../evals/skill-audit-2026-09-15-followup/react-review.txt). This evaluates review scope, not React runtime behavior.

The [run manifest](../evals/skill-audit-2026-09-15-followup/manifest.json) records exact requests, input/output hashes, skill hashes, and evaluation limits.

The scenario catalogs also cover paired UI review/implementation requests, saved plans/reports, snippet selection, and renamed standalone discovery. Expectations are not pass records; execution evidence and remaining limits are recorded separately.

## Limits

This revision was not run on macOS. Installer and validator implementations are unchanged, so the full installer regression suite is not newly required. The focused migration checks do not constitute a new macOS certification.

Independent explicit-invocation examples do not establish automatic selection quality, all-scenario coverage, behavior on other models, or measured token/latency improvements. No such gains are claimed. Existing historical compiler/runtime results are not new executions of those examples.
