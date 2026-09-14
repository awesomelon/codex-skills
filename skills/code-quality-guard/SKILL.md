---
name: code-quality-guard
description: Review or improve code and PR maintainability, and compare quality before and after changes. Exclude straightforward feature implementation and wording-only edits.
---

# Code Quality Guard

Judge correctness of current behavior separately from the cost of the next change. Do not treat passing tests as evidence of good design or present an AI impression score as a measurement.

## Scope and work mode

Review, inspection, or evaluation alone must not modify source, configuration, or documentation. If improvements are also requested, fix and verify evidence-backed problems within scope. Reuse relevant review evidence.

For PRs, use verified base/head and their merge base; for local work, include staged, unstaged, and untracked files. In post-task checks, distinguish starting user changes from the current edits. Without comparison material, limit the conclusion to current-state diagnosis. Distinguish new issues, deterioration, and existing debt; start with the diff and directly connected callers and contracts. For full audits, state the areas sampled and their limits.

## Two separate judgments

- **Correctness:** Connect requirements, public contracts, and invariants to relevant checks. Distinguish executed commands, verified behavior, failures, unrun checks, and unknown areas. Passing tests do not guarantee correctness of paths they do not cover.
- **Maintainability:** Inspect the edit points for one policy, hidden state and side effects, paths needed to understand behavior, unnecessary abstractions, and whether regressions can be verified locally. Do not invent defects from file length or pattern preferences.

Select [measurement.md](references/measurement.md) for before/after or A/B comparisons and measurement, [scoring.md](references/scoring.md) for score requests, and [earendil-metrics.md](references/earendil-metrics.md) for Verbosity/Erosion calculations. Small reviews need no additional reference when the evidence criteria below suffice.

Connect each quality finding as **file/symbol observation → actual change or failure condition → cost or risk → smallest remedy and verification**. Check documented rationale and counterexamples. Do not count the same cause repeatedly; leave weak evidence as a question to verify.

If the cost of a future change is unclear, choose one realistic small change from requirements or history and trace its edit points and verification path. For example, how many decisions must change together when one status policy changes? Separate assumptions from execution; do not implement a hypothetical feature during a review. Only when a change experiment is requested, implement it in an isolated copy, run regression checks, and record the observed cost.

## Improvement and stopping

Compare keeping the structure, a local fix, and a boundary adjustment. Consolidate ownership of policies that change for the same reason; preserve similar-looking policies that change independently. Do not remove justified complexity or contractually necessary defensive code to improve a number. Before calling code unused, check actual entry points, dynamic registration, and re-exports.

After improvement, verify before/after evidence and relevant behavior using the same scope and criteria. Reuse checks completed on the same code under the same conditions. Without new edits, failures, or unresolved uncertainty, do not rerun checks just to capture report output. Do not weaken tests, lint, or type rules, or reduce numbers through file moves or code compression. Stop after required validation and concrete remaining risks are addressed, with only optional cleanup left. Do not iterate solely to raise a score.

Use the requested format to distinguish correctness status from quality judgment, and present key evidence, smallest remedies, and remaining uncertainty. Call quality improved, unchanged, or worsened only when evidence supports it; otherwise withhold judgment. Quality scores cannot offset significant correctness, security, or data-integrity problems.

When architecture boundaries or React execution are also at issue, reuse evidence from the relevant specialized review. Complete this review even without other skills; do not require chained invocation of every skill or repeat the same finding.
