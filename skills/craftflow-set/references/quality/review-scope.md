# Review scope and findings

Use the requested comparison and verify its base and head; use the merge base for PRs. Do not assume `main`, `HEAD~1`, or a remote-tracking branch. Include staged, unstaged, and untracked files in local-change reviews, plus committed work within scope. Distinguish starting user changes from the implementation being assessed.

Without comparison material, report current-state findings rather than regressions. State inspected boundaries, samples, and unreviewed areas. Distinguish new issues, worsened issues, and existing debt; explain when existing debt directly blocks the change.

Trace affected consumers and attempt to disprove material findings. Group duplicate causes and keep weak candidates as questions about the missing contract or caller. Each supported finding needs its location, trigger, consequence, evidence, smallest justified remedy, and a suitable verification method. Match the requested output format.

Ground severity in affected contracts and consequences. A broken core boundary can be significant; style preferences and hypothetical scale alone are not blockers. Choose checks sufficient to judge the issue, and state when failures cannot be attributed to the change. Distinguish supported issues, missing evidence, and no significant issues found within the inspected scope; a narrow sample or unavailable check does not establish project-wide quality.
