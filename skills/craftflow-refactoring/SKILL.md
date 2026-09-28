---
name: craftflow-refactoring
description: Plan, perform, or review behavior-preserving refactoring using Martin Fowler's principles. Use for restructuring existing code, not feature design or formatting alone.
---

# CraftFlow Refactoring

Carry out or assess behavior-preserving structural transformations. Reuse an established diagnosis and chosen transformation; when none is supplied, identify the local difficulty using the criteria below. No preceding quality audit or other skill is required.

## Scope and useful changes

For review, explanation, or planning, preserve the assessed code and write only requested deliverables. For implementation, complete the requested refactoring and relevant verification. A discovered bug or behavior change is separate work unless its correction was also requested; report it and continue independent in-scope work.

Identify the actual difficulty, affected callers, and observable contract before choosing a transformation. Values, errors, public signatures, stored data, and effect order/count matter when the affected code depends on them. Keep a refactoring distinguishable from a requested feature or bug fix so each can be assessed against its own expectations.

Choose a transformation that resolves the identified difficulty. File length or repeated syntax alone does not justify splitting; preserve independently changing policies even when their expressions match. Balance easier local reasoning and verification against added navigation.

## Choose the relevant depth

Review and planning can use the criteria above and the affected contract directly. For substantive implementation, read [transformations.md](references/transformations.md) for baseline checks, external consumers, effect sequencing, and recovery from regressions. Consult it during review only when one of those risks needs closer analysis. A small mechanically clear rename needs no full execution workflow.

For unfamiliar mechanics, consult the relevant Fowler catalog entry linked in [sources.md](references/sources.md), not the whole catalog. Extract, inline, and move are alternatives chosen by the difficulty they resolve, not a required sequence or target count.

## Completion

Finish when the requested structural difficulty is resolved and required verification is complete. Reuse results for unchanged code and conditions; new edits, failures, or unresolved uncertainty justify rechecking. Continue authorized work through verification without stopping for optional cleanup or an intermediate approval.

For implementation, report the supported improvement, behavior preserved, and actual checks, separating pre-existing failures and unrun checks. For review or planning, give evidence, a justified transformation if any, and the relevant verification approach without claiming edits or execution. Preserve scope and user changes throughout.
