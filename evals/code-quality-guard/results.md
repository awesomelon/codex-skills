# Code Quality Guard execution records

> English translation of a historical record. [Original at the pre-translation commit](https://github.com/awesomelon/codex-skills/blob/ce11c34e3d1da77140087300218b776594bb65cf/evals/code-quality-guard/results.md). Reported runs, hashes, and counts describe the original work, not this translation.

2026-09-13 UTC. Baseline repository commit: `364b33ac502bfcde54eb3508798c3d68ee346a7c`. Requests and SHA-256 hashes of the actual evaluated skills/fixtures are in [manifest.json](outputs/manifest.json).

## Scope and method

Two independent agents in fresh conversations received separate copies of the skill and [document-policy fixture](fixtures/policy/TASK.md) only. No prior conversation, expected answer, or scenario catalog was supplied. Agents inherited the parent model settings; an exact version was not exposed. Environment: Linux, Node.js 24.19.0, Python 3.12.14, Bash 5.2.21.

| Run | Observed result | Judgment |
| --- | --- | --- |
| Case 1: read-only quality review | Distinguished 7/7 passing tests from the maintainability issue of three policy definitions. Did not exaggerate it into a current bug; preserved independent pinning and all input hashes. | Passed this case |
| Case 2: improvement and validation | Consolidated archive policy into one function. Edited three product files and added one; contract/tests unchanged. Existing 7 tests passed before/after and public functions were preserved. | Passed this case |
| Case 3 conditions: no history/analyzers | Neither run invented CC or clone rates. Review stayed at current-state diagnosis; improvement compared with its starting snapshot. | Observed in both runs |

Only temporary absolute file links were normalized in the [review response](outputs/review.md) and [improvement response](outputs/improve.md). Reapplied the [implementation patch](outputs/implementation.patch) to the fixture and verified all resulting file hashes. Reducing archive-policy edit points from 3 to 1 is directly observed code evidence, not a future-policy experiment or development-time measurement.

## Package checks

- `python3 scripts/validate.py`: all three skills passed metadata, portable contents, and internal references.
- `quick_validate.py skills/code-quality-guard`: basic skill validation passed.
- `bash scripts/install.sh --list`: discovered the new skill.
- Installed only the new skill in temporary link/copy targets and reran each; checked installation, idempotence, and file-content preservation.
- `node --test evals/code-quality-guard/fixtures/policy/policy.test.mjs`: original fixture passed 7/7.
- `git diff --check`: no whitespace errors.

Installer and validator were unchanged. Real home directories and Codex configuration were not test targets.

## Limits

Cases 4–10, combined architecture/React invocation, automatic selection, macOS hardware, other languages, and large repositories were not executed in these initial runs. Two explicitly supplied cases do not establish general quality gains or automatic-invocation accuracy. AST/clone analysis and source Verbosity/Erosion calculations were not run. This skill supplies judgment guidance, not an enforced CI gate or automatic grader.

## Follow-up reference-selection evaluation — 2026-09-14

After the records above, ran one independent unscored A/B comparison. It completed with `measurement.md` under the new routing and reported 7 existing tests passing for both A and B. It produced neither scores nor unmeasured complexity/clone rates. Independently verified unchanged before/after hashes for all 15 inputs.

See the [response](outputs/ab-routing-review.md), [request/hashes/check record](outputs/ab-routing-manifest.json), and [follow-up audit](../../docs/skill-audit-2026-09-14-followup.md). This was one explicit-invocation run; reference use and checks are recorded from the response. Score/special-metric calculations, UI-default behavior, and automatic selection were not executed.
