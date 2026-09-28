---
name: craftflow-plan
description: Investigate a problem, choose priorities, or design and plan a change without implementing it. Use for diagnosis, technical strategy, and planning requests.
---

# CraftFlow Plan

Choose the right problem and a feasible scope of change. Start at the unresolved decision; reuse established requirements and evidence. Preserve the assessed code and existing records; write only requested deliverables. A clear implementation request belongs to build and needs no preliminary planning ceremony.

## Decide what matters

Trace the symptom, intended outcome, affected consumers, and constraints. Distinguish observations from causal hypotheses and current implementation from intended policy. Investigate facts available in the project; ask only for consequential user-owned choices that remain unsettled, with evidence and a recommendation. Continue independent analysis while a choice is blocked.

Compare credible alternatives at the necessary depth, including keeping the current design or making a local repair. Explain which mechanism would improve the outcome, the cost and compatibility implications, and what evidence could reject the proposal. File length or pattern preference alone does not justify a redesign.

For dependent work, specify checkable outcomes, prerequisites, shared contract ownership, and acceptance evidence. Use existing task artifacts when useful and authorized. Include rollout and recovery only where the change requires them. A short recommendation can be a complete plan; do not generate a document set or fixed task graph by default.

## Read for the current decision

| Decision | Guidance |
| --- | --- |
| Explain behavior, a symptom, or a trace | [Investigation](references/workflow/investigation.md) |
| Choose which problem deserves investment | [Problem selection](references/workflow/problem-selection.md) |
| Sequence uncertain work, adoption, or rollout | [Execution strategy](references/workflow/execution-strategy.md) |
| Resolve intent gaps and maintain requirements-to-work traceability | [Change intent](references/workflow/spec-driven-changes.md) |
| Choose module boundaries and compare designs | [Architecture preflight](references/architecture/preflight.md) |

When technical detail from another advertised CraftFlow skill would settle a question, resolve its location through the current catalog; plugin prefixes and paths vary. Read only that reference as supporting guidance, retaining this task's planning scope. No other installed skill is required: use project contracts and primary technical documentation when needed.

Finish with the recommendation, rationale, significant uncertainty, and a usable next action or requested plan. Describe proposed checks separately from checks actually run. Implementation, delegated edits, delivery, and monitoring are not authorized by a planning request. Source history is in [attribution](references/sources.md).
