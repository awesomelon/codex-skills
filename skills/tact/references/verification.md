# Evidence before completion

A completion statement is a claim about an artifact or behavior. Before making it, identify the observation that would establish it, run the relevant check when needed, inspect its actual output and exit status, and state only what that evidence supports. Confidence, an intended test command, or a worker's success report cannot substitute for the observation.

## Match the check to the claim

| Claim | Evidence needed |
| --- | --- |
| Tests passed | The relevant tests actually executed with no failing assertions; identify skipped or unselected coverage. |
| Build succeeded | The build command completed successfully for the relevant configuration. Lint alone is insufficient. |
| The bug is fixed | Exercise the reported failure condition and observe the corrected behavior. |
| A regression test protects the fix | Demonstrate failure against the original behavior and success against the corrected behavior. |
| Performance improved | Correct, completed work under comparable conditions, with the measured path, units, run count, and observed variation. |
| The task is complete | Inspect the final artifact against the requested outcomes, including relevant integration boundaries and required project gates. |

For a regression check, use a disposable copy of the original behavior when a comparison is needed. Do not revert user changes or disturb a shared checkout to obtain a failing result. For a refactor, compare the affected behavior and checks before and after; keep existing valid baseline evidence when available.

Inspect the full relevant result, not just a green summary. Zero selected tests, every relevant case skipped, a wrapper hiding a failing child, or a mocked answer without an exercised integration leaves that behavior unverified. Do not loosen assertions, suppress diagnostics, or redefine the expected result just to pass.

## Assess performance evidence when relevant

Before reporting or using a measured speedup, inspect what the timed region executes and what it counts as success. Confirm that asynchronous or lazy work completed there and that outputs are correct; fast failures and skipped work are not improvements. Compare equivalent workloads and relevant build, configuration, cache, and concurrency conditions. For an adoption decision, resolve material configuration differences or leave the comparison inconclusive. Repeat or interleave runs when warmup, noise, or drift could decide the result; a gap within observed variation does not establish a win. Relate a microbenchmark to the user-visible path before generalizing. A requested rough estimate can use one labeled run, but still needs correct completed work. Do not impose a fixed run count or infer a bottleneck without evidence.

## Verify the relevant final state

Confirm which code, local changes, build, dependencies, configuration, and runtime/data conditions the evidence covers. A matching commit hash alone does not establish equivalence. Rerun affected checks when these inputs change, including after integrating delegated work. Inspect the worker's artifact and verify the boundary it changes.

Reuse an already-observed result only when those material conditions remain applicable. Do not rerun unchanged checks merely to repeat a completion sentence; do not use an earlier passing run for a subsequently changed implementation. Focused checks support focused claims and do not replace mandatory project gates.

## Report the actual state

Distinguish a passed check, a failed assertion, an unrun check, and an inconclusive attempt. Resolve in-scope failures. If a dependency or permission blocks verification, identify the blocked observation and what is still unknown; do not call the overall task complete when that observation is required.

Check the evidence before saying "fixed", "done", "passing", or expressing satisfaction that implies those claims, including in a commit, PR, or release report. A narrow observed success can be reported while broader work remains, with its scope explicit. Verification does not itself authorize a commit, publication, or live mutation.
