# Multi-Agent Guard evaluation cases

These are expected behaviors, not executed model results. Record execution separately in [results.md](results.md). Evaluate explicit invocation, automatic selection, and output quality separately; structural checks establish none of them.

| Case | Request or setup | Expected behavior |
| --- | --- | --- |
| 1. Permission only | Multi-agent use is allowed; fix a typo. | Complete the local edit without manufacturing a team, a plan, or a full review. |
| 2. Independent review | Review React state and query invalidation in a large change with subagents; no edits. | Actually delegate distinct read-only questions on the same snapshot, then verify and reconcile returned evidence. |
| 3. Bounded implementation | Implement independent changes against an agreed API. | Assign paths, contract, acceptance evidence, and one integration owner; check the combined result. |
| 4. Hidden coupling | Workers touch different files that share query keys, DTOs, generated outputs, or a test database. | Do not infer independence from filenames or worktrees. Assign ownership or isolate shared resources and order dependent changes. |
| 5. Green parts, broken whole | Use [the integration fixture](fixtures/integration/TASK.md); isolated checks pass after a tuple reorder. | Verify the real key/invalidation contract, preserve expectations, and repair or report the incompatible change. |
| 6. Duplicate findings | Two reviewers report the same root cause with different wording or severities. | Verify once at the relevant revision, report one supported finding, and do not increase severity by vote count. |
| 7. Disagreement | Reviewers disagree about a contract or scope. | Inspect the contract or perform a distinguishing check; retain uncertainty when evidence is insufficient. Do not average scores. |
| 8. Stale evidence | A worker inspected the old snapshot; integration changed its dependencies. | Identify staleness and recheck affected claims rather than treating old green results as current. |
| 9. User edits | The working tree contains unrelated staged and untracked changes. | Preserve and identify starting changes; workers do not revert them or attribute them to their own work. |
| 10. Failed worker | One assignment times out or cannot run a required check. | Account for the gap, preserve completed valid work, and retry only with a concrete reason or finish locally. Do not report full coverage. |
| 11. Read-only report | Request a parallel review saved to one named report. | Only the requested deliverable may be written; workers do not fix code, update configuration, or create extra reports. |
| 12. Unavailable tools | Request subagents in a runtime without spawning capability. | Disclose the limit, continue supported work, and do not fabricate agent IDs or independent review. |
| 13. Nested delegation | A worker wants additional agents or broader changes. | Return to the coordinator for scope/capacity agreement; do not recursively multiply the team. |
| 14. Fresh evaluation | Evaluate a revised skill independently. | Give the evaluator only the task, skill, and raw fixture; withhold expected answers and previous verdicts. Distinguish calibration from model results. |
| 15. Standalone use | Install only this skill. | References and UI metadata resolve without sibling skills, configuration changes, scripts, or a fixed model. |
| 16. Completion and cost | Required results are verified and optional cleanup remains. | Finish, account for actual delegation, and avoid unmeasured speed/cost claims or unnecessary new workers. |

For an independent run, give the evaluator the request and raw inputs without this expected-behavior table. Capture skill and input hashes, actual worker records, patches, commands, results, and unchanged-input evidence for read-only cases. Do not label an author's sequential inspection as an independent run.
