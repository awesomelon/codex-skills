# Carry out a behavior-preserving change

## Establish the baseline

Inspect the affected implementation, consumers, and existing verification path. Run or reuse the smallest relevant checks for the starting state. If they fail, distinguish a pre-existing failure from this change and obtain a passing focused check for the affected behavior before a substantive transformation. Do not repair unrelated failures or weaken expectations to obtain a pass.

When coverage is missing, add focused checks of the current observable behavior before a risky change, including meaningful errors and effects rather than private helper names. If execution is unavailable, static checks and direct reasoning support only a small mechanically verifiable edit. Narrow or defer changes whose behavior cannot be established and state the limit; compilation alone does not prove preservation.

## Preserve the affected contracts

Preserve public APIs used outside the editable code. A repository search cannot establish that a published API has no external consumers. Internal renames can update all known callers; retain an external entrypoint until a breaking migration is requested.

Moving or extracting expressions must preserve mutation, evaluation count/order, asynchronous completion, and cancellation where relevant. Do not move writes or calls across a failure or asynchronous boundary, parallelize effects, or add retries merely as cleanup.

For independently implementable transformations, assign disjoint writes and settle shared contracts first. Give shared types, exports, generated outputs, and fixtures one owner. Worktrees isolate files, not semantic dependencies; verify the integrated behavior. Delegation does not expand edit scope or authorize incidental bug fixes.

## Transform and verify

Use a sequence of understandable changes that can be checked before dependent work accumulates. Update the affected callers with each transformation. Small means verifiable, not a line limit, a single file, or a required commit per edit.

When a check fails after a transformation, investigate that change and repair it or undo only your affected edits before building further. Preserve other work and the original expectations rather than fitting tests to the refactor.

Use focused checks during the work and the repository's required broader checks at completion. For a refactor preparing a concrete feature, simplify only enough to support that addition and keep its new behavior and expectations distinguishable.
