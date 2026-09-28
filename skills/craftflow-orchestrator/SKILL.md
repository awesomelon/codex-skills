---
name: craftflow-orchestrator
description: Select engineering priorities, plan dependent work, and coordinate delivery or resumption through verified integration. Routine edits and standalone domain reviews need no orchestration.
---

# CraftFlow Orchestrator

Coordinate the engineering decisions needed to deliver the requested outcome: problem, scope, dependencies, and integration evidence. Start at the unresolved decision; an established problem needs no new discovery phase. Planning, investigation, and review preserve the assessed material; write only requested deliverables. Implementation and external delivery follow the user's existing authorization.

## Coordinate the outcome

For dependent work, keep one compact plan of outcomes, dependencies, owners, and acceptance evidence using the existing task mechanism. Reconcile the starting revision and local edits. Settle blocking shared contracts before dependent implementation; update the plan when evidence changes the work. A small explicit invocation can be handled directly without a plan or new document.

Keep short or tightly coupled work local. Delegate when independent investigation, separable implementation, or a distinct review perspective warrants its cost. Honor requested parallelism within available capabilities; if delegation is unavailable, continue feasible work locally without reconfiguring the runtime. Use [coordination](references/coordination.md) for assignments, shared ownership, recovery, and accepting handoffs.

Select expertise by the concrete decision and the current catalog's descriptions and resource locations, including plugin prefixes. Load only the relevant skill or reference and pass its usable location to the responsible worker. Skills are guidance, not workers: one worker may use several skills, and standalone specialists need no coordinator. Use [expertise boundaries](references/expertise.md) when responsibilities overlap; reuse findings rather than adding a full review sequence. Missing specialists need only be reported when they limit the result.

## Integrate and finish

Inspect accepted artifacts and verify the behavior where their contracts meet. Reuse applicable evidence; refresh checks made stale by integration or new findings and run required gates. Use [verification evidence](references/verification.md) for runtime claims, ambiguous command results, and evidence validity. Specialist checks alone do not establish integration.

Complete authorized work to its requested endpoint, accounting for blocked or canceled outcomes and remaining owned workers/processes. Report the integrated result, actual checks, and material gaps. Stop when the outcome and relevant verification are complete; delivery and future monitoring are not automatic final stages.

## Task-specific guidance

Read only the guidance needed for the unresolved decision. These references do not form a required pipeline.

| Subtask decision | Guidance |
| --- | --- |
| Discover worthwhile problems, challenge a proposed solution, or prioritize competing opportunities | [Problem selection](references/problem-selection.md) |
| Turn an uncertain or cross-team initiative into a feasible plan, rollout, and outcome check | [Execution strategy](references/execution-strategy.md) |
| Explain behavior, diagnose a symptom, or interpret a trace without fixing | [Investigation](references/investigation.md) |
| Reproduce and fix, implement, migrate, refactor, or compare prototypes | [Changes](references/changes.md) |
| Resolve material intent gaps and keep requirements, tasks, and completion evidence aligned | [Spec-driven changes](references/spec-driven-changes.md) |
| Verify a running UI, CLI, or service; distinguish a real pass from missing or stale evidence | [Verification evidence](references/verification.md) |
| Measure and improve performance against a workload | [Performance](references/performance.md) |
| Review a diff, inspect PR status, or perform authorized delivery | [Review and delivery](references/review-and-delivery.md) |
| Resume, checkpoint, or pause coordinated work | [Continuity](references/continuity.md) |
| Retrieve an applicable project lesson or preserve verified reasoning not recoverable from the implementation | [Learning](references/learning.md) |

Read [sources](references/sources.md) only for provenance or maintaining this adaptation.
