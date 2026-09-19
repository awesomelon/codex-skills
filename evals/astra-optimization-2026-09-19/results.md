# Astra optimization evaluation — 2026-09-19

This record covers the first four runs identified by [manifest hashes](outputs/manifest.json), based on `02b3906e4a45cc4ea151df19c379248da30d62a7`, and the renamed workflow identified by [final manifest hashes](outputs/final-manifest.json). [Baseline hashes](outputs/baseline.json) were saved before editing. Scenario additions in each skill's `cases.md` describe intended behavior; they are not additional executed tests.

## Method

Five fresh evaluators received no parent history, audit rationale, proposed edits, or expected answers. Each received one task, raw fixture inputs, and the relevant candidate skill path in a disposable directory. The fifth ran after the requested rename. They inherited the parent model configuration; the spawn tool did not expose an exact backend identifier. No evaluator received the evaluation report or another evaluator's response.

This tests **explicitly invoked candidate skills**. There were no baseline model runs, automatic-discovery runs, or repeated statistical trials. Task restrictions are part of the inputs, so successful scope preservation cannot be attributed to the skill alone. Evaluator reference-read lists and original command reports are self-reported in saved responses; full tool transcripts were not exported. Parent command records, patch inspection, and file comparisons independently verify the observable artifacts.

## Observed outcomes

| Task | Result | References read beyond the entrypoint |
| --- | --- | --- |
| [Refactoring](fixtures/refactoring/TASK.md) | Unified repeated receipt construction and completion into one path while preserving the API, data, failure propagation, and effect order. Existing 8 tests passed before and after. Only `checkout.mjs` changed; TASK.md and tests were preserved. | `references/transformations.md` |
| [TypeScript](fixtures/typescript/TASK.md) | Added the existing `LoadOptions` annotation to the local object. Baseline compilation produced TS2345; the result compiled successfully with strict checks and no emitted files. Runtime expressions and exported functions were unchanged; only `options.ts` changed. | None |
| [Query SSR review](fixtures/query-ssr/TASK.md) | Identified cross-request account leakage from the shared server client/key and missing browser freshness configuration. Proposed request isolation and browser `staleTime`, distinguished elapsed freshness from mount time, and stated integration limits. Files remained unchanged. | `references/server-rendering.md`, `references/cache-and-keys.md`; no offline/persistence reference |
| [Trace diagnosis](fixtures/trace/TASK.md) | Separated the 300 ms debounce and 502 ms request interval from 9 ms filtering and CPU sample share. Did not claim the request's internal cause or production latency. Proposed a discriminating timing observation without edits, instrumentation, or benchmarks. | `references/investigation.md`; no performance workflow |
| [Renamed workflow](fixtures/trace-renamed/TASK.md) | Resolved `$engineering-workflow` using the supplied skill path, gave the same supported interval diagnosis and uncertainty, and left all files unchanged. This is explicit invocation, not automatic discovery or a cross-platform compatibility test. | `references/investigation.md`; no performance workflow |

The parent independently reran the original and refactored Node fixture: **8 passed, 0 failed** in both. Checks cover express/standard receipts, immutable input, empty orders, errors at each service boundary, and a pending reservation. These are fixture-level behavior checks, not an exhaustive proof of all consumers.

The parent also reproduced the original TypeScript diagnostic and successful candidate compilation using the existing **TypeScript 6.0.3** compiler read-only. The fixture's runtime expressions were inspected, not executed. Node was **v24.16.0**. [Command records](outputs/behavior-checks.json) contain exact commands, exit codes, and output. Implementation artifacts are [refactoring.patch](outputs/refactoring.patch) and [typescript.patch](outputs/typescript.patch).

The parent compared complete file sets and bytes for all three read-only runs, preserved task/test inputs, and the candidate skill packages against their pre-dispatch hashes. No evaluator edits to these inputs were observed; [final integrity checks](outputs/final-integrity.json) also record reference preservation and current documentation links. Saved original responses: [refactoring](outputs/refactoring-response.md), [TypeScript](outputs/typescript-response.md), [SSR](outputs/query-ssr-response.md), [trace](outputs/trace-response.md), and [renamed workflow](outputs/trace-renamed-response.md). The first four records retain the skill names used at execution time; they have not been rewritten to claim a later candidate was evaluated.

## Structural validation and limits

The repository validator and bundled skill-creator `quick_validate.py` passed all seven packages on macOS using Python 3.12.14. The official validator used PyYAML 6.0.3 already isolated in a temporary validation directory. `git diff --check` passed. See [initial structural commands](outputs/structural-results.json) and [rename checks](outputs/rename-checks.json). The rename checks include an actual standalone copy installation in a disposable destination, a second metadata validation there, byte comparison against source, absence of an old-name alias, and license preservation. These checks establish package integrity, not model quality.

Architecture migration wording, qualitative quality comparisons, React reporting, automatic selection, refactoring failure recovery, and real SSR/runtime integration were not executed in this evaluation. The full installer regression suite was not repeated because the installer and validator implementation did not change. The [text-size record](outputs/text-size.json) measures bytes only.

To reproduce a candidate task, copy its fixture and the identified skill package into a disposable directory, use TASK.md as the request, and keep expected outcomes, saved responses, and audit documents outside evaluator input. Supply a compatible existing TypeScript compiler for that case; do not install into or edit the real application.
