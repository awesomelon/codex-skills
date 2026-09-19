---
name: engineering-workflow
description: Coordinate evidence-led debugging, measured optimization, multi-step delivery, and resuming interrupted work. Routine edits and standalone domain reviews do not need this workflow.
---

# Engineering Workflow

Coordinate an engineering request toward a verifiable outcome. This skill works alone; installed specialist skills are optional when their expertise helps a concrete decision.

## Scope and routing

Establish the requested result and the evidence that would demonstrate it. Investigation, planning, and review preserve the assessed material; write only requested deliverables. Implementation includes authorized edits and relevant verification. Skill selection alone does not change the requested scope.

Read the reference for the immediate decision, adding another only when that decision arises. A small task can use this entrypoint alone. Do not manufacture a plan document, prototype, or review panel merely to follow a workflow.

| Current decision | Guidance |
| --- | --- |
| Explain behavior or rationale; diagnose a symptom or supplied trace without fixing | [Investigation](references/investigation.md) |
| Reproduce and fix a bug, implement a feature, refactor, or prototype | [Changes](references/changes.md) |
| Measure and improve performance against a workload | [Performance](references/performance.md) |
| Review a diff, inspect PR status, prepare delivery, or land an authorized change | [Review and delivery](references/review-and-delivery.md) |
| Delegate useful independent work or compare competing approaches | [Coordination](references/coordination.md) |
| Continue a long task, resume prior work, or pause for handoff | [Continuity](references/continuity.md) |

Select again for a new task; this is not a sticky mode or permission to change global configuration. Use the current session's actual capabilities. Missing tooling limits the corresponding claim, not every other useful part of the task.

## Evidence and completion

Inspect the relevant implementation, consumers, and existing verification path. For changes, establish the starting revision and local edits. For multi-step work, keep a brief plan of checkable outcomes ending at the user's requested endpoint.

Choose evidence that distinguishes success from a plausible failure on the affected surface. Unit tests cannot establish visual parity or production latency. Prefer a discriminating observation to guessing at an observable fact; ask about material product choices that evidence cannot settle.

Complete authorized work and required checks. Reuse evidence for unchanged code and conditions; recheck after relevant edits, failures, or unresolved concerns. When a hypothesis fails, revise or undo only your affected changes and reconsider the mechanism before layering on another workaround. Continue independent work while a dependent decision or capability is missing.

Report the supported outcome, actual evidence, and material limits, distinguishing observations from hypotheses and design judgments. Stop when the requested outcome and relevant verification are complete. Publishing, messaging, merging, deployment, monitoring, and cleanup are task-specific actions, not automatic final steps; existing authorization for the requested action need not be asked for again.

Read [sources.md](references/sources.md) only for provenance or maintaining the adaptation.
