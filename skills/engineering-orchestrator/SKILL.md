---
name: engineering-orchestrator
description: Orchestrate engineering work across dependent tasks, specialist skills, and agents through verified integration. Use for coordinated delivery, explicit orchestration, or resuming multi-part work; routine edits and standalone domain reviews need no orchestration.
---

# Engineering Orchestrator

Own the requested outcome from task decomposition through integration. Choose which work stays local, which expertise to load, and which independent work to delegate. The coordinator remains responsible for the final artifact and evidence.

## Frame and divide the work

Establish the requested endpoint, scope, starting revision/local edits, and evidence of completion. Planning, investigation, and review preserve the assessed material; write only requested deliverables. Selecting this skill does not authorize implementation or external delivery.

For work that needs coordination, keep a compact plan of outcomes, dependencies, owners, and acceptance evidence. Use the existing task/plan mechanism; create a durable document only when useful and in scope. A small explicit invocation can be handled directly.

Decompose by independently checkable outcomes, not arbitrary file counts or fixed roles. Identify shared contracts, generated artifacts, state, and test resources before parallel writes. Settle blocking contracts first and assign a single owner to each shared artifact. Separate ready work from work awaiting a decision or upstream result.

## Select execution and expertise

Keep short or tightly coupled work local. Delegate when independent investigation, separable implementation, or a distinct review perspective is worth its coordination cost. Honor requested parallelism within available capabilities; do not manufacture workers or reconfigure the runtime when delegation is unavailable.

Use available skill descriptions to select expertise for a concrete subtask. Load only the relevant skill or reference, and pass its usable location and purpose to the responsible worker. A skill provides guidance; it is not an agent. Multiple skills can serve one worker, and one skill can serve several disjoint tasks. No fixed panel or full guard sequence is required. If a specialist skill is unavailable, use the relevant guidance below and report only limitations that affect the result.

Read [coordination](references/coordination.md) when delegating, changing ownership, or integrating delegated results. Keep useful complementary work local while workers run.

## Reconcile and finish

Update the plan when a result changes a dependency, contract, or hypothesis. Unblock dependent work from inspected artifacts, not completion messages alone. Preserve unrelated edits; revise or undo only your own affected work when evidence rejects an approach.

Integrate accepted results and verify the behavior where their contracts meet. Individual passing checks do not prove the combined result. Reuse evidence for unchanged artifacts and conditions; rerun only required checks and those made stale by integration or new findings. Resolve disagreements through source evidence or a discriminating check, not agent agreement.

Complete authorized work to the requested endpoint, accounting for blocked or canceled tasks and active workers. Report the integrated outcome, actual verification, and material gaps. Stop when the outcome and relevant verification are complete; publishing, merging, deployment, and monitoring follow the user's existing authorization, not an automatic final stage.

## Task-specific guidance

Read only what the current subtask needs. These references support execution and do not impose a fixed pipeline or require other installed skills.

| Subtask decision | Guidance |
| --- | --- |
| Explain behavior, diagnose a symptom, or interpret a trace without fixing | [Investigation](references/investigation.md) |
| Reproduce and fix, implement, migrate, refactor, or compare prototypes | [Changes](references/changes.md) |
| Measure and improve performance against a workload | [Performance](references/performance.md) |
| Review a diff, inspect PR status, or perform authorized delivery | [Review and delivery](references/review-and-delivery.md) |
| Resume, checkpoint, or pause coordinated work | [Continuity](references/continuity.md) |

Read [sources](references/sources.md) only for provenance or maintaining this adaptation.
