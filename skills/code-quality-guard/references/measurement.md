# Evidence for quality comparisons

## Comparable conditions

Record the baseline commit/snapshot, target files and languages, tools with versions and configuration, and excluded paths. Use the same conditions before and after. Separate product code, tests, generated code, vendor files, and lockfiles; do not count file moves or renames as improvements. Include added and deleted files. Do not invent deltas without a baseline.

Prefer analyzers, lint, type checks, and test tools already in the project. Do not use automatic fixes or snapshot-update options during a review. If a tool is unavailable, report AST complexity or clone rate as unmeasured with qualitative evidence, rather than estimating by eye or regex. Do not add dependencies or CI simply to populate metrics unless separately requested.

Compare two implementations against the same requirements, tests, and scope. Allow ties or withheld judgment when the difference is unclear. If order or author labels could affect the conclusion, consider hiding labels and reversing the order. This reassessment does not replace a correctness oracle and is not needed for every single-implementation review.

## Signals suited to the question

| Signal | Evidence to collect | Limits of interpretation |
| --- | --- | --- |
| Change volume | Added/deleted lines, changed files, new public APIs and dependencies | Git diff lines are not SLOC. Distinguish added tests and required exception handling. Lower LOC is not itself the objective. |
| Duplication | Clone locations/rates reported by an analyzer; edit points for the same policy | Sharing similar-looking code can increase coupling if it changes for different reasons. |
| Complexity | Supported analyzer results for per-function CC/SLOC, nesting, and major hotspots | Repository averages can hide a changed critical path. Splitting functions may increase navigation cost. |
| Coupling and state | Policy owners, public entry points, actual calls, events, caches, and state write paths | Import counts alone do not describe runtime coupling or state ownership. |
| Understanding and verification cost | Symbols traversed to find intent, required fixtures/environments, relevant regression paths | File counts or coverage alone are not quality scores. Check that tests protect external behavior. |

Attach units, denominators, and raw output or a reproducible command to numbers. Prioritize changed and directly affected areas; use whole-project aggregates as context. Do not present arbitrary weighted sums of signals with different units as objective quality.

## Judgment criteria

Explain the cost, risk, and evidence for relevant issues. These perspectives help select what matters; they are neither a fixed report template nor instrumented measurements.

- **Policy and responsibility:** Does one policy change require synchronized edits across independent implementations? Establish the shared reason for change through contracts or actual consumers.
- **Simplicity and clarity:** Do abstractions, options, and indirection serve current requirements? Compare the contracts lost by removal with the cost of understanding them.
- **State and side effects:** Can the authoritative state and update paths be traced? Distinguish intentional lifetimes, such as independently edited drafts, from duplicated state.
- **Ease of change and verification:** Where are the logical edit points and regression checks for a realistic policy change? Distinguish inferred cost from files, errors, and time observed in an actual experiment.

Explain confidence using code paths, contracts, and reproductions, not unsupported percentages. Lack of source access or runnable tests is not a reason for a favorable score.
