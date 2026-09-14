# Architecture review: comparison scope and evidence

## Comparison scope

- For PR or commit reviews, use the user-specified scope and verified base/head. Review PR changes from their merge base. Do not assume `main`, `HEAD~1`, or a remote-tracking branch without evidence.
- Include staged, unstaged, and untracked files in local-change reviews. Compare completed work with the starting state to distinguish existing user changes from the current implementation. Include committed work when it is part of the requested scope.
- Without comparison material, report a current-state diagnosis. State inspected boundaries, samples, and unreviewed areas; do not claim the absence of regressions from the current state alone.

## Evidence that reduces false positives

Read the diff with relevant callers. Check whether aliases, re-exports, type-only dependencies, generated code, or dynamic registration make visible paths differ from actual dependencies. Compare documented exceptions and gradual migrations with their allowed scope. Moving a file alone does not resolve a dependency problem.

Distinguish new issues, worsened issues, and unrelated existing debt. Explain the connection when existing debt directly blocks the change. Group findings with the same root cause. For weakly supported candidates, name the contract or caller to check rather than declare a defect.

## Severity and conclusion

Match the user's requested output format. A finding needs the supporting file/symbol, trigger and impact, smallest remedy, and verification method.

Ground blockers in actual paths, such as mandatory boundary violations, broken consumer compatibility, or authorization/data-integrity risks. Maintainability problems may also block completion when they seriously undermine a core boundary. Taste differences or hypothetical scalability are not blockers.

Choose validation sufficient to judge the issue. Do not use automatic-fix options in review-only work. State the limitation when existing failures cannot be separated from failures introduced by the change.

Distinguish significant unresolved issues, evidence still needed for a judgment, and no significant issues found within the reviewed scope. Discuss regressions only with comparison material and sufficient relevant validation. Do not turn unavailable checks or a narrow sample into project-wide quality assurance.
