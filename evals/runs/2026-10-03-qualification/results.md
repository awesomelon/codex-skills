# Rung 1.0 stability qualification

All 13 frozen contract attempts satisfied independent scope/artifact assertions and coordinator adjudication of their responses and actual tool evidence. Two additional explicit installed-plugin tasks also passed. The skill payload is unchanged from 0.5.5. These results support the adopted bounded stability contract; they do not establish comparative superiority or a reliability rate.

## Policy and execution

After the [24-attempt pilot](../2026-10-03-native-pilot/results.md) showed correct artifacts in both arms, the maintainer approved stability and compatibility as the release basis. The [adopted policy](../../../docs/rung-1.0-design.md#adopted-release-policy) supersedes the original comparative-gain blocker and broad host proposal. This decision occurred before this batch.

[plan.json](plan.json) froze 13 cases, one repetition each, a 13-invocation ceiling, no retries, at most two concurrent contract attempts, a 240-second limit, exact runner/suite/skill hashes, and separate installed-task lanes. All 13 records match the frozen runner and suite inventories. Every contract trace captured observed `gpt-6-astra` / `high` on macOS 27.0.1 arm64 with Codex CLI 0.160.0. Processes exited successfully with confirmed owned process-group exit. No failed model attempts were discarded or replaced. The installed tasks used two additional invocations; no diagnostic model invocation was needed.

All tasks used fresh synthetic fixtures without coordinator assertions in their input. The comparison and contract lanes used source skills under `.agents/skills`; the installed lane used the native 1.0 plugin cache. Temporary state and model filesystem permissions separated credentials, source/checkers, and task artifacts. Existing user configuration and installed skills were not modified. The runner is repository development tooling, not part of the skills-only plugin runtime.

## Contract results

| Case | Observed result |
| --- | --- |
| Wrong diagnosis | Correct decoder repair; stale encoder diagnosis rejected; actual failing/passing checks and local-only limit reported |
| Valid diagnosis | Applicable encoder diagnosis reused; focused repair and actual tests; production confirmation not invented |
| Review scope | Cross-tenant cache issue found; staged, unstaged, untracked files and Git state preserved |
| Undefined outcome | Parsing identified as the measured lead; duplicate support report distinguished; target and cache policy not invented |
| Quality evidence | Mean/p95 mismatch, 0.8% failure rate, monthly availability gap, and scoped audit acceptance handled correctly |
| Shared responsibility | Shared archive rule distinguished from independent pin policy; seven tests run; no edits or measured-performance claim |
| Interrupted effect | Stable request identity prevents duplicate effects; separate request IDs remain separate; restart/write-failure checks recorded |
| Verification repair | Driver/docs repaired while product/contract remain unchanged; the exposed remove failure is reported honestly |
| Changed instructions | CSV header completed with escaping preserved; late email work rejected; disconnected cancellation remains unconfirmed |
| Stale result | Earlier passing snapshot rejected as current proof; current failing tests repaired and rerun |
| Get Set alone | Correct read-only review with only Get Set installed |
| Go alone | Direct exact correction with only Go installed and no preceding assessment |
| Routine | Exact wording correction with no unrelated changes |

[adjudication.json](adjudication.json) maps each case to its immutable record hash, outcome, and reason. The coordinator inspected response semantics, actual tool calls/outputs, final artifacts, and independent assertions. This is author adjudication, not independent blinded review. Raw automated outcomes remain one `passed` routine case and twelve `inconclusive` cases requiring that manual step. Passing manual assessment does not rewrite raw classifications.

The verification-repair fixture intentionally leaves a product test failing: the authorized endpoint is a valid verifier plus an accurate defect report, not an unauthorized product repair. Its independent checker rejects the broken product and accepts a corrected disposable copy. Interrupted-effect checks also use disposable copied data, leaving saved artifacts intact.

## Distribution

[installed-lifecycle.json](installed-lifecycle.json) records local marketplace installation, enabled-state/version inspection, 0.5.5 → 1.0.0 replacement, restoration to 0.5.5, 1.0.0 reinstallation, and removal. Installed skills matched source bytes at every step; unrelated test preferences/data were preserved. Both versions have identical skill bytes. Version checks establish replacement of the manifest/cache path, not changed behavior between those payloads.

[installed-review-scope.json](installed-review-scope.json) and [installed-routine.json](installed-routine.json) capture actual reads of the 1.0 cached Get Set and Go entrypoints, observed model settings, correct results, and preserved task scope. These use explicit catalog names and do not measure implicit discovery. The pre-publication lifecycle uses a local marketplace; the final GitHub installation is verified separately after publishing the immutable release commit and retained as a release asset.

Two pre-model fixture diagnostics were corrected while preparing this lane: a quoted dotted permission override was replaced with a full filesystem-map override, and an unrelated preference was placed at TOML root rather than under a plugin table. Neither involved a model invocation, real user configuration, or a change to plugin behavior.

[shell-installation.json](shell-installation.json) records real macOS Bash 3.2 listing, dry run without writes, selected link, both managed copies, repeat, update, previous-byte restoration, and refusal to overwrite edited copies. All destinations are temporary. The unchanged Python compatibility installer is covered by deterministic regression tests.

## Repository checks and limits

[validation.json](validation.json) records final structural validation, Bash syntax, and the complete deterministic regression suite against the runner/checker/package hashes. The tests include positive/negative fixture controls, native-login-reference cleanup without reading credentials, path isolation, inventory/Git preservation, trace filtering, and standalone selection. They validate the tooling and package, not universal model behavior.

The source skill bytes are identical to 0.5.5 and the frozen plan. License notices and portable references remain bundled. Assigned `.agents` copies are unchanged and omitted from Git to keep `skills/` as the single maintained source; their hashes and source revision remain in every record. Raw task artifacts and tool evidence are preserved.

Desktop activation, automatic selection, live steering/cancellation/pause/resume, and compaction reliability are outside the qualified launch claim. The replay cases remain replay evidence. Other OS/model profiles are unverified for model behavior. No cost or performance advantage is claimed. The 24 pilot attempts, two observability diagnostics, 13 contract attempts, and two installed tasks are separate denominators.

## Gate disposition

| Adopted gate | Evidence and disposition |
| --- | --- |
| Stable behavior and critical boundaries | 13/13 coordinator-adjudicated contract passes; no observed unauthorized artifact change or unsupported material verification claim |
| Independent entrypoints | Get Set-only and Go-only tasks pass; portable references validated |
| Distribution and recovery | Native local lifecycle, two installed tasks, and real macOS standalone operations pass; final remote byte verification follows publication |
| Package integrity | Structural validation, Bash syntax, full regression suite, and unchanged skill payload |
| Documentation and scope | Stable compatibility contract, migration/recovery procedure, grounded examples, and explicit unqualified host mechanisms |
| Comparative gain | Not a release gate under the maintainer's adopted policy; no demonstrated gain is reported |

A publication record is complete only after the final remote installation matches the intended bytes. No wider host or reliability claim is implied by this gate table.
