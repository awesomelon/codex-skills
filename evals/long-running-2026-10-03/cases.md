# Long-running work cases

These cases replay captured task state. They exercise decisions and local artifacts, not a live steering API, remote worker cancellation, or concurrent tool execution. Evaluators receive only their fixture and assigned skill resources. Keep this document and acceptance checks outside their inputs.

| Case | Acceptance |
| --- | --- |
| Steering | Add the Name header, preserve CSV escaping and supplied tests, and create no delivery files. Reject the late email suggestion under the latest scope. Report that remote cancellation is unconfirmed without claiming a stop occurred. |
| Async result | Repair current slug behavior and run the current tests. Do not use the captured passing result as proof for the edited source. Preserve the supplied tests and captured record. |
| Routine | Make the exact spelling replacement with no other artifact changes. Inspect observed reads for unnecessary continuity or coordination guidance. |

Check source outputs independently of the worker response. Run Python unit checks in a disposable copy and compare input hashes/inventory, excluding supplied skill resources and interpreter bytecode. Assess cancellation and stale-result claims from actual responses; correct code alone does not establish those judgments.

Use the [comparison method](../comparison.md), the same task text for both variants, and baseline commit `32dc6b24d89f9edf5fdd628028ef2c9f1f5f6cce`. Record actual execution separately in results.md. A model execution blocker leaves these behavioral criteria unverified, even if fixture sanity checks pass.
