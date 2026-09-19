---
name: refactoring-guard
description: Plan, perform, or review behavior-preserving refactoring using Martin Fowler's principles. Use for restructuring existing code, not feature design or formatting alone.
---

# Refactoring Guard

Improve the ease of understanding and changing existing code while preserving observable behavior. Use Martin Fowler's small, verified transformations as the working method. This skill works alone; it does not require a general quality audit or another skill.

## Respect the requested work

For review, explanation, or planning, inspect and recommend without editing the assessed code. Write a plan or report only when requested. For implementation, complete the requested refactoring and relevant verification.

Keep refactoring and behavior changes distinct: adding a feature, correcting an existing bug, changing validation, or improving performance can need different expectations. If both are requested, separate their edits and checks so each result can be assessed. A refactoring request alone does not authorize a newly discovered bug fix. Preserve current behavior, describe the issue, and continue any independent in-scope work.

## Establish what must stay the same

Inspect the affected implementation, callers, and relevant checks before editing. Identify the observable results that the proposed change could affect: return values, errors, public signatures, stored data, and the order or number of externally visible effects. Include mutation, evaluation order, asynchronous completion, or cancellation when the code depends on them; do not turn this into an unrelated system audit.

Run the smallest relevant existing checks to establish a starting result. Reuse results already obtained for the same code and conditions. If those checks fail before edits, distinguish an existing failure from this change; establish a passing check for the affected behavior before making a substantive transformation. Do not repair unrelated failures or weaken expectations to obtain a pass.

When coverage is missing, add focused tests of current externally observable behavior before a risky change. Include meaningful errors and edge cases, not assertions about private helper names or the proposed decomposition. If tests cannot run, use available static checks and direct reasoning only for a small, mechanically verifiable edit. Narrow or defer changes whose behavior cannot be established and state the verification limit. Do not claim behavior preservation from compilation alone.

## Choose a useful transformation

Connect a concrete difficulty to the proposed change: what is hard to understand, what current change requires repeated edits, and how this transformation helps. A code smell is a reason to investigate, not an automatic defect. File length, repeated syntax, a switch statement, or a metric alone does not justify splitting code or adding a design pattern.

Prefer readability and maintainability over LOC or the smallest diff. Keep code together when it must be understood and changed together. An extraction can remain in the same file; create another file when independent change, reuse, or testing makes the additional navigation worthwhile.

Use the transformation that addresses the observed problem. Extract a named calculation when it reveals intent; inline a helper when its name adds no understanding; move a function when its use of data supports the move. Similar expressions need not represent the same business rule. Preserve separate policies when their reasons to change differ, and avoid structures for hypothetical future requirements.

For an unfamiliar technique, consult the relevant entry in Fowler's catalog linked in [sources.md](references/sources.md). Do not load the whole catalog or require a fixed number of techniques.

## Make and verify small changes

Choose a sequence in which each completed transformation can be checked. Change one responsibility at a time, update affected callers, and run the relevant checks before building on it. A small change means an understandable, verifiable transformation, not an arbitrary line limit or a required commit per edit.

Independent transformations may run in parallel with disjoint write ownership and stable, agreed shared contracts. Give shared types, exports, generated outputs, and test fixtures one owner; worktrees do not remove semantic dependencies. Serialize dependent transformations and verify affected behavior on the integrated result. Delegation does not authorize bug fixes or relax review-only restrictions.

Preserve public APIs used outside the editable code. An internal rename can update all known callers; a published API may need the old entry point retained until an explicitly requested migration. Do not assume a repository search finds external consumers. Moving expressions must preserve evaluation count and order; extracting computation must not move writes or calls across failures or asynchronous work.

If a check fails after a transformation, investigate that transformation and repair it or undo only your own affected edits before proceeding. Do not keep layering changes on a new failure, change expected outputs to fit the refactoring, or discard existing user work.

Use fast focused checks during the work and the repository's required broader checks at completion. Repeat passed checks only after relevant edits, failures, or unresolved uncertainty. When preparing for a requested feature, refactor only enough to make that concrete addition clearer; keep its new behavior and tests distinguishable.

## Finish with evidence

Review the complete change for accidental behavior changes and unnecessary scope. Stop when the requested structural problem is addressed and relevant checks are complete; optional cleanup is not a reason to keep expanding the task.

Report what became easier to understand or change, the behavior preserved, and actual verification results. Distinguish passing checks, pre-existing failures, and unrun checks with reasons. For review or planning, provide the relevant file/symbol, evidence, proposed transformation, and verification approach without claiming implementation or test execution.

The [source record](references/sources.md) separates Fowler's principles from this skill's practical guidance for agent work.
