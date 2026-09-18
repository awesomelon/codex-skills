---
name: multi-agent-guard
description: Coordinate parallel investigation, review, or implementation when requested or when independent workstreams justify delegation.
---

# Multi-Agent Guard

Use real subagents to resolve independent questions or deliver bounded changes, then integrate their evidence and work. This skill coordinates work; it does not replace domain-specific judgment or require other skills to be installed.

## Choose useful delegation

Permission to use multiple agents is not a requirement to spawn them for every task. Delegate when independent investigation, distinct review perspectives, or separable implementation can materially help. Keep tightly dependent steps together; do not manufacture roles for a trivial edit. Choose concurrency for the available work and runtime limits, not a fixed agent count.

When delegation is useful and available, perform it rather than only describing a team. If the runtime cannot spawn agents, state that limit and continue with supported work; sequential self-review is not independent or multi-agent execution. Do not change models, permissions, global configuration, or install tooling just to enable delegation.

## Bound each assignment

Keep one coordinator responsible for the requested outcome and final integration. Give each worker the relevant baseline revision and starting user changes, a concrete question or deliverable, allowed paths and write scope, shared contracts, and the evidence needed to accept its result. Share necessary source context, not an indiscriminate copy of the whole conversation. Use [workflows.md](references/workflows.md) for a task brief or a relevant review, investigation, or implementation pattern.

Read-only requests remain read-only for every worker; only explicitly requested deliverable paths may be written. Assign relevant specialist guidance only where it helps, not every installed skill to every worker. The coordinator handles complementary work instead of repeating the same investigation. Further delegation needs coordinator agreement on the additional scope and capacity.

For writes, assign one owner per shared artifact. Different files can still share a contract, generated output, cache, test database, or server. Use isolated worktrees when useful and supported; they prevent filesystem collisions, not semantic conflicts. Settle shared interfaces before dependent edits, and serialize overlapping work when safe isolation is unavailable. Preserve unrelated user changes; a worker must not commit, publish, or merge outside the user's authorization.

## Reconcile and verify

Collect the assigned results or explicitly account for failed, canceled, or blocked work. A handoff identifies the inspected revision, changed paths or patch, findings with file/symbol evidence and consequences, checks actually run with their conditions, and remaining gaps. A missing check is not a pass. Retry only when there is a concrete reason it can succeed; narrow or complete a failed assignment locally when appropriate.

Verify material worker claims against the relevant code or test evidence. Merge duplicate root causes; settle disagreements with contracts or a discriminating check, not votes or averaged scores. Recheck stale findings after relevant edits. For implementation, inspect the combined diff and verify affected cross-boundary behavior on the integrated state; isolated green checks do not prove the combination works. Reuse checks only when their code, dependencies, and conditions remain applicable.

Finish with the implemented result or requested assessment, actual delegation and coverage, verification, and unresolved risks. Do not claim parallel execution, speedups, cost savings, or independent evaluation without evidence. Stop when the requested outcome is sufficiently verified, rather than expanding the team for optional cleanup.

Consult [sources.md](references/sources.md) when verifying or updating this guidance, not as a prerequisite for each use.
