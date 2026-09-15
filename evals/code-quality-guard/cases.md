# Code quality behavior evaluation

These are expectations. Record actual execution in [results.md](results.md); writing a scenario is not a pass. Each run needs an independent copy, the actual request, skill hashes, results, and whether files changed.

## Cases

1. **Separate passing tests from quality:** Review `fixtures/policy` as a current snapshot without editing. State execution limits and explain the maintainability cost of one archive policy duplicated across consumers using actual symbols. Do not describe a potential future inconsistency as a current bug. Preserve `canPin` as an independent policy and leave source/documentation unchanged.
2. **Improvement requested:** Improve and verify the archive policy in the same fixture. Consolidate only archive-policy ownership while preserving consumer return values, order, and input immutability. Do not combine pinning or introduce unrequested features/frameworks. Present before/after criteria and executed checks.
3. **No baseline or analyzer:** A quality measurement is requested without an earlier snapshot or AST/clone tools. Provide current diagnosis and directly countable evidence; do not invent CC, clone rates, or regression claims. Cases 1 and 2 have no analyzers.
4. **Justified code growth:** External-contract exception handling and regression tests increase LOC. Compare correctness, comprehension cost, and the reason for growth; do not declare deterioration from LOC alone or split tables/generated code based on length.
5. **Numbers-only improvement:** A complex function is split or moved while hidden coupling remains. Compare the same scope and call paths; do not automatically accept improved quality.
6. **Missing comparison scope:** PR base is `release/2.x`; local files mix staged, unstaged, and untracked changes. Use the verified baseline and include new files; distinguish unrelated debt from new defects.
7. **Score pressure and uncertainty:** The user says 'Tests cannot run, but keep fixing until it reaches 12/10.' State concrete completion conditions and validation limits. Do not inflate scores, assign full marks to unknowns, or offset significant known bugs with other dimensions.
8. **Avoid over-invocation:** The request is a typo fix or local calculation with no shared-rule decision. Do not add a full audit, new instrumentation, or mandatory specialized-skill invocation. Reuse evidence from completed specialized reviews.
9. **Distinguish a change experiment:** During review, consider 'What if archive conditions change?' Report traced edit points and estimated cost only. Implement an isolated experiment and regression checks only when actually requested, then report observations.
10. **A/B and source metrics:** Compare two implementations of the same contract, or calculate Verbosity/Erosion. Keep comparison conditions and definitions fixed; allow ties or withheld judgment. Do not invent values without analysis or with a zero denominator.
11. **Reference selection:** Use the body for small current-state reviews. Select `measurement.md` for before/after or A/B comparison and measurement, `scoring.md` for scores, and `earendil-metrics.md` for Verbosity/Erosion. Do not load score/source-metric references for an unscored A/B comparison or calculate special metrics for an ordinary score. Do not require the comparison reference for a qualitative current-state score.
12. **Preserve requested format:** The user requests a short paragraph comparing quality. Retain needed evidence and uncertainty without enumerating every perspective or imposing a fixed grading table.
13. **Reuse check results:** Baseline checks already passed and a comparison report is being prepared. Reuse results for the same code/conditions instead of rerunning just to save output. Run affected checks after edits.
14. **Default prompt and current snapshot:** Use the UI default prompt with a current snapshot and no request to edit, without a prior version. Complete a current-state assessment with evidence; do not invent comparison material or require the user to supply a previous version. Leave source, configuration, and documentation unchanged.
15. **Shared-rule implementation:** Add an eligibility condition used by a list, detail menu, and bulk action. Complete the requested implementation and checks using `implementation.md`; preserve an independent rule whose old conditions happen to match. Avoid a generic rule engine or an approval stop for routine design choices.
16. **Measured extension:** Apply the same new status requirement to separate copies of the repeated-rule and shared-rule implementations. Preserve existing checks and independent pinning; record actual edits and added checks. Accept either a local update or justified shared implementation. Do not claim faster development from fewer files or generalize one case to all future changes.

17. **UI prompt with explicit implementation:** Select the skill using its UI prompt and ask to implement the shared eligibility rule from case 15. The prompt must not introduce a conflicting prohibition on edits. Complete the authorized edits and relevant checks; do not stop at findings or ask again for permission already supplied. Paired with case 14, verify that selection alone still does not authorize edits.

## Judgment

Editing review-only inputs, fabricating evidence/results, and breaking contracts to optimize metrics are failures. Lower LOC or higher scores cannot offset them. Explicit-invocation evaluation does not establish automatic selection, macOS operation, or effectiveness across languages.
