---
name: craftflow-set
description: Investigate, design, plan, or review engineering work without changing the assessed material. Use for diagnosis, technical strategy, audits, and quality assessments.
---

# CraftFlow Set

Establish what should change or assess what already exists. Follow the requested outcome: a review need not produce a plan, and a plan need not repeat a completed review. Preserve assessed code and records; write only requested deliverables. A request to implement or fix authorizes execution through Go without requiring another assessment or approval.

## Ground the judgment

Trace the symptom, intended outcome, affected consumers, and constraints. Separate observations from causal hypotheses and current behavior from intended policy. Reuse settled decisions; investigate available facts before asking for consequential user-owned choices, with evidence and a recommendation. Continue independent work while a choice remains blocked.

For diagnosis, design, or planning, compare credible alternatives, including keeping the current design or making a local repair. Explain the mechanism, compatibility, maintenance cost, and evidence that could reject the proposal. Identify dependencies, contract ownership, and acceptance evidence where needed. A short recommendation can be the entire plan; no fixed document set is required.

For review, establish the actual base, head, and local changes; use the merge base for PRs. Without comparison material, report current-state findings rather than invented regressions. Include affected consumers, attempt to disprove findings, and merge duplicate causes. Connect each supported issue to its location, trigger, consequence, evidence, and smallest justified remedy; keep weak findings as questions.

Separate correctness from maintainability and measured performance. File size, repeated syntax, passing tests, or a preferred pattern alone does not justify a redesign. Preserve independently changing policies and useful complexity.

## Read only for the unresolved question

| Question | Guidance |
| --- | --- |
| Behavior, symptoms, or traces | [Investigation](references/workflow/investigation.md) |
| Priorities and problem selection | [Problem selection](references/workflow/problem-selection.md) |
| Uncertain work, adoption, or rollout | [Execution strategy](references/workflow/execution-strategy.md) |
| Intent gaps and requirements-to-work traceability | [Change intent](references/workflow/spec-driven-changes.md) |
| Design boundaries and alternatives | [Architecture preflight](references/architecture/preflight.md) |
| Existing architecture and dependency direction | [Architecture review](references/architecture/review.md) |
| Maintainability or regression coverage | [Review criteria](references/quality/review.md) |
| Shared-rule ownership | [Shared rules](references/quality/implementation.md) |
| Before/after evidence or an authorized isolated experiment | [Measurement](references/quality/measurement.md) |
| Explicitly requested scores or source metrics | [Scoring](references/quality/scoring.md), [metrics](references/quality/earendil-metrics.md) |

Go owns optional React, Query, TypeScript, refactoring, and runtime-verification references. Resolve its location through the host's catalog, including any plugin prefix; use its reference table only to find relevant documents. Reading execution guidance does not authorize edits. Set works alone: use project contracts and authoritative technical documentation when optional resources are unavailable.

## Finish at the requested endpoint

Use relevant non-mutating checks and respect stricter no-write requests. Distinguish proposed checks from actual execution, failed assertions from checks that never ran, and fresh evidence from stale results. Zero tests or a matching SHA under changed runtime/local conditions does not establish completion.

For plans, report the recommendation, rationale, uncertainty, and usable next action. For reviews, report supported findings by importance, coverage, actual checks, and remaining uncertainty. Scores summarize judgment; they are not measurements and cannot offset correctness failures. Stop after sufficient assessment. Implementation, delegated edits, delivery, and monitoring require a request for that work. [Attribution](references/sources.md) records provenance.
