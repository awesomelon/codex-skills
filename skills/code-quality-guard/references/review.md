# Change review and maintainability improvement

## Establish the comparison scope

For PRs, use verified base/head and their merge base; for local work, include staged, unstaged, and untracked files. In post-task checks, distinguish starting user changes from the current edits. Without comparison material, limit the conclusion to current-state diagnosis. Distinguish new issues, deterioration, and existing debt; start with the diff and directly connected callers and contracts. For full audits, state the areas sampled and their limits.

## Trace change cost

For a requested extension, or when future change cost affects the judgment, trace one concrete addition from requirements or history through its edit points and relevant checks. Separate estimated effort from observed work. A review describes that addition without implementing it; use [measurement.md](measurement.md) when an isolated change experiment is requested.

Compare keeping the structure, a local fix, and a boundary adjustment. Consolidate ownership of policies that change for the same reason; preserve similar-looking policies that change independently. Before calling code unused, check actual entry points, dynamic registration, and re-exports.

## Verify an authorized improvement

After improvement, verify before/after evidence and relevant behavior using the same scope and criteria.
