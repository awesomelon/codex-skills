---
name: pstack
description: Run pstack engineering workflows for evidence-led debugging, measured optimization, multi-step delivery, and resuming interrupted work. Routine edits and standalone domain reviews do not need this workflow.
---

# Pstack

Turn an engineering request into a verifiable outcome. Adapted from Lauren Tan's pstack for Codex; this skill coordinates work rather than imposing a coding style or replacing domain expertise.

## Select the work

Establish the requested result and what would demonstrate it. Distinguish investigation, planning, review, implementation, and delivery from the user's words and existing authorization. Inspection or skill selection alone does not authorize edits to the assessed material. Write requested reports or plans without changing their subject.

Read the one reference that fits the immediate task. Add another only when the work reaches that decision. A small task can use this entrypoint alone; do not manufacture phases, prototypes, a plan document, or a review panel.

| Current decision | Guidance |
| --- | --- |
| Explain behavior, reconstruct rationale, diagnose without fixing | [Investigation](references/investigation.md) |
| Reproduce and fix a bug, implement a feature, refactor, or prototype | [Changes](references/changes.md) |
| Measure and improve performance, or inspect a trace | [Performance](references/performance.md) |
| Review a diff, inspect PR status, prepare delivery, or land an authorized change | [Review and delivery](references/review-and-delivery.md) |
| Delegate independent work or compare competing approaches | [Coordination](references/coordination.md) |
| Continue a long task, resume prior work, or pause for handoff | [Continuity](references/continuity.md) |

For a new task, select again. Do not install a sticky mode, change global instructions, or carry the previous task's edit/delivery permissions into unrelated work. The source and adaptation record is in [sources.md](references/sources.md); read it for provenance or maintenance, not every task.

## Keep evidence attached to the work

Inspect the relevant implementation, consumers, and existing verification path. For a change, note the starting revision and local changes so a failure can be attributed correctly. For a multi-step task, use a brief plan of independently checkable outcomes; the user's requested endpoint determines the last step.

Choose evidence that can distinguish success from a plausible failure. A unit test can prove a calculation; it cannot establish visual parity, real network cancellation, or production latency. Prefer a cheap reproduction or discriminating experiment to guessing at an observable fact. Ask about missing product decisions when they materially affect the result; continue independent work while waiting.

Complete authorized edits and required checks. Reuse evidence for unchanged code and conditions. New edits, failures, or unresolved concerns justify further verification; repeating a passing suite alone adds no confidence. Remove or revise only your own changes that were motivated by a disproven hypothesis. If repeated attempts fail for the same reason, revisit the assumed mechanism before adding another workaround.

## Fit the Codex environment

Use tools and skills actually available in the current session. Do not invent a Cursor command, custom agent, connector, or background loop. For independent work where delegation materially helps, use the available subagent capability as described in [Coordination](references/coordination.md); otherwise proceed locally. Keep the configured model and permission settings unless the user requests a change.

This skill works alone. When an installed specialist skill matches a concrete decision, use its guidance and reuse its evidence. Do not require a chain of architecture, quality, language, and framework skills for every change. Unavailable tooling limits the corresponding claim, not every other useful part of the task.

## Finish at the requested endpoint

Report the outcome, the evidence that supports it, and material limits. Link actual files, commands/results, or inspected remote artifacts where useful. Keep observed facts, causal hypotheses, and design judgments distinguishable. A missing check stays unverified; a delegate's summary is not independent proof.

Stop when the requested result and relevant verification are complete. PR creation, posting comments, merging, deployment, recurring monitoring, and cleanup are task-specific actions, not automatic final steps. Continue actions already authorized by the user without requesting the same permission again.
