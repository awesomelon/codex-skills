# Independent execution — Astra refinement

These results concern the revision identified by [manifest hashes](manifest.json), based on `8d59c883a8e5b1ada712c76f9feb051c16cef2fa`. They do not relabel earlier scenarios as passing runs. The [structural record](structural-results.json) covers all five packages separately.

## Method

Two new evaluators received no parent conversation history, audit findings, proposed fixes, or expected answers. One received a disposable boundary task and the standalone architecture skill. The other received three read-only tasks and a local catalog of the five revised skills. The second evaluator handled its three tasks in one context; they are not three independent sessions. Models inherited the parent settings; the spawn tool did not return an exact backend identifier.

The parent assessed the returned responses, inspected the implementation diff, and checked preserved fixture content. Reference lists and final test totals below come from evaluator reports. Full tool transcripts were not exported. The manifest distinguishes parent observations from evaluator reports.

## Outcomes

| Task | Observed result | Limits |
| --- | --- | --- |
| [Boundary implementation](fixtures/boundary/TASK.md) | Removed the shared-to-feature import by passing tenant from both consumers. Only three implementation files changed. Existing labels, tenant switching, frozen record inputs, session API, and test assertions were preserved. Baseline and post-change `node --test` each passed 1 test, 0 failed. | Two patch attempts were denied by automatic approval review. Execution resumed after explicit user approval. This does not establish uninterrupted persistence. |
| [Type review](fixtures/types/TASK.md) | Selected TypeScript type-modeling and narrowing guidance. Correctly recognized that the explicit string return annotation already rejects a new unhandled object variant; did not invent a missing compile-time exhaustiveness check. Identified returning an unexpected runtime object as a conditional limitation, not a demonstrated input-path failure. Preserved independent optional progress. | Source reasoning only; no compiler or runtime execution was available or claimed. |
| [Query design](../design-extension-2026-09-15/fixtures/query-design/TASK.md) | Selected Query cache/key, mutation, and prefetch guidance. Proposed tenant/status-specific keys, compatible all-records calls, shared options/preloader inputs, list-prefix and counts invalidation, and retention of complete detail updates. Kept screen presentation/polling local and distinguished active refetches from inactive invalidation. | Design only; no Query runtime or endpoint verification. |
| [Wording review](fixtures/wording/TASK.md) | Identified “Syncronized” → “Synchronized”; selected no skill or reference. | One catalog-assisted negative control, not production automatic-selection measurement. |

The architecture evaluator read `references/review.md` for current-state diagnosis rather than `preflight.md`. It did not report a separate final PR-review phase. Reading that reference is compatible with the skill's diagnosis route; this evaluation does not prove that the revised wording reduces reference reads.

The read-only evaluator reported unchanged hashes for all 39 supplied files, including skill packages. Its attempted temporary report write was denied by automatic approval review; it returned the completed response in chat without retrying the write. No fixture edit was reported. The parent independently compared the Query inputs to the existing repository fixture; complete per-file before hashes for the other read-only tasks were not returned by the evaluator.

## Reproduction and interpretation

Copy a fixture into a disposable directory and provide only its TASK.md, raw inputs, and the relevant standalone skill or catalog. For the boundary case, the original test deliberately passes even while the architectural dependency is wrong: behavior checks must be combined with inspection of dependency ownership. [The saved patch](boundary-implementation.patch) records the actual three-file output; keep it and this results document out of evaluator input.

The metadata edits and parameter-reference relocation are small instruction refinements. Untagged requests in a supplied catalog exercise the evaluator's selection judgment; they do not measure real Codex discovery, truncation, selection rates, or before/after improvement. No timing, token-efficiency, generalized model-quality, or performance gain is claimed. The new maintenance prompt was reviewed for scope and source requirements, not run as another recursive optimization task.

No installed skills or actual application files were changed. Installer behavior, regression tests, and runtime configuration were outside this revision.
