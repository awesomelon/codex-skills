---
name: craftflow-code-quality
description: Assess maintainability, choose improvements, and design or implement shared business rules.
---

# CraftFlow Code Quality

Separate correctness of current behavior from the cost of the next change. Passing tests do not establish good design; AI impression scores are not measurements.

Judge structure by the cost of understanding, changing, and verifying a responsibility. Keep rules that change together close; separate independent policies when the benefit outweighs added navigation. File length and diff size alone establish neither quality nor a need to split.

## Scope and routing

For planning, review, or explanation, preserve the assessed material and write only requested deliverables. Implementation requests include needed design decisions, edits, and relevant verification. Routine local, wording-only, or formatting-only edits need no separate quality review.

| Requested work | Guidance |
| --- | --- |
| Shared-rule design or implementation; deciding what to reuse | [implementation.md](references/implementation.md) |
| PR/change review, full audit, maintainability improvement, or tracing a future change | [review.md](references/review.md) |
| Before/after or A/B comparison, measurement, or an isolated extension experiment | [measurement.md](references/measurement.md) |
| A quality score | [scoring.md](references/scoring.md) |
| Verbosity/Erosion calculations | [earendil-metrics.md](references/earendil-metrics.md) |

Small current-state reviews can use the evidence criteria below. Select references for unresolved decisions, not every row. Once a behavior-preserving transformation is chosen, refactoring expertise can guide its execution without another quality audit. This skill can also implement a supported improvement alone; reuse any existing diagnosis and verification.

## Evidence and completion

For correctness, connect requirements, public contracts, and invariants to relevant checks. Distinguish executed commands, verified behavior, failures, unrun checks, and unknown areas; passing tests do not cover untested paths. For maintainability, inspect policy edit points, hidden state and side effects, paths needed to understand behavior, unnecessary abstractions, and local verifiability. Pattern preferences alone do not establish defects.

Connect each finding as **file/symbol observation → actual change or failure condition → cost or risk → smallest remedy and verification**. Check rationale and counterexamples. Verify received findings against the assessed code and merge duplicate causes; reviewer agreement is not evidence. Leave weak evidence as a question. Without a baseline, diagnose the current state rather than inventing regressions.

Preserve justified complexity and contractually necessary defensive code. Do not weaken tests, lint, or type rules, or game metrics through file moves or code compression. Quality scores cannot offset significant correctness, security, or data-integrity problems.

Complete authorized changes and required verification. Reuse sufficient checks for unchanged code and conditions; repeat them when new edits, failures, or unresolved uncertainty require it, not solely to capture report output. Stop when concrete in-scope risks are addressed and only optional cleanup remains, not when a score rises. Use the requested format to separate correctness, quality judgment, evidence, remedies, and uncertainty; withhold improvement claims when unsupported.
