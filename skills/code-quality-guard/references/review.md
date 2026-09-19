# Change review and maintainability improvement

## Establish the comparison scope

For PRs, use verified base/head and their merge base; for local work, include staged, unstaged, and untracked files. In post-task checks, distinguish starting user changes from the current edits. Without comparison material, limit the conclusion to current-state diagnosis. Distinguish new issues, deterioration, and existing debt; start with the diff and directly connected callers and contracts. For full audits, state the areas sampled and their limits.

## Trace change cost

For a requested extension, or when future change cost affects the judgment, trace one concrete addition from requirements or history through its edit points and relevant checks. Separate estimated effort from observed work. A review describes that addition without implementing it; use [measurement.md](measurement.md) when an isolated change experiment is requested.

Compare alternatives that could materially change the judgment, such as keeping the structure, a local fix, or a boundary adjustment. Consolidate ownership of policies that change for the same reason; preserve similar-looking policies that change independently. Before calling code unused, check actual entry points, dynamic registration, and re-exports.

## Simplification and dependency removal

For a simplification request, identify what can be removed, the existing or native capability that would replace it, and the contract that must survive. Check replacement semantics where they differ: accepted inputs and error behavior, supported runtimes, locale/time-zone handling, or cancellation and retries. A shorter native call is not equivalent merely because the happy path matches.

One implementation or caller is a search hint, not proof that an abstraction is wasteful. A seam may isolate an external dependency, enforce a boundary, or make failures testable. Retain it when that concrete benefit outweighs its cost. Remove unused flexibility only after checking the consumers and entry points above; do not trade away validation or compatibility for fewer lines.

## Verify an authorized improvement

After improvement, verify before/after evidence and relevant behavior using the same scope and criteria. For a replacement, include a discriminating case where the old contract and a tempting but incompatible shortcut behave differently. An unchanged happy-path test is insufficient evidence for that replacement.

When judging regression coverage, name a plausible defect and ask whether the whole test, including setup, would detect it. Where a permitted isolated experiment helps, introduce that defect temporarily and observe the result. An expectation computed through the same faulty code can agree with a wrong result. Preserve absence checks and fixed values when they express the contract; neither assertion style nor a passing suite establishes adequacy. Check observable effects or meaningful payloads rather than only a substitute's call count.

This test-review guidance is independently adapted from pstack's [behavior-testing principle](https://github.com/michael-denyer/pstack-claude/blob/af7aa63b5e196cb3d04fbe18dc2a970918fc883a/plugins/pstack/skills/principle-test-behavior-not-implementation/SKILL.md). Its [MIT notice](pstack-LICENSE) accompanies the adaptation; no mutation-testing runtime is required.
