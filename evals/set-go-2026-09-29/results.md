# Set/Go consolidation — 2026-09-29

Set combines the former planning and review endpoints; Go retains the former build workflow. Exactly two discoverable skill roots remain. No mandatory sequence or old-name aliases are introduced. Technical references and source licenses remain available, with duplicate root notices deduplicated when merging plan and review. Plugin version 0.4.0 and English/Korean documentation describe the new catalog and migration.

The supplied Astra authoring article was read locally for this revision. Set uses one shared assessment boundary and a question-to-reference table instead of loading both former workflows for every request. Go can execute a clear request directly.

## Fresh execution

Two fresh agents independently received only the Set package, their task folder, and instructions to carry out `TASK.md`, inspect only those supplied folders, and report resources/checks. Optional Go was unavailable. No expected findings, parent diagnosis, sibling output, or prior conversation was supplied. Model/runtime settings were inherited without overrides.

| Case | Observed result | Parent verification |
| --- | --- | --- |
| [Design assessment](plan-task.md) | Compared alternatives, separated session reuse from offline export, challenged unmeasured caching benefits, and identified expiry policy. Proposed measurement without claiming execution. | Read [actual response](plan-response.md); all task hashes unchanged. |
| [Migration review](review-task.md) | Found incompatible collection fields and stale evidence; distinguished historical worker status and current-state findings. Ran non-writing Node assertions, reporting failures rather than completion. | Compared [response](review-response.md) with source; all five input files unchanged. |

[Manifest](manifest.json) records tested skill/input hashes, task wrappers, and post-run hashes. Task wording comes from the previous [planning](../three-skills-2026-09-28/plan-task.md) and [review](../three-skills-2026-09-28/review-task.md) cases, with the explicit skill name changed to Set. Review source fixtures remain at [handoffs](../engineering-orchestrator/fixtures/handoffs/) in the manifest's base revision. The full planning artifact is saved in the task file.

Go's execution instructions were renamed and optional-resource pointers updated; no new implementation procedure was introduced. The previous [build run](../three-skills-2026-09-28/results.md) remains historical evidence, not a fresh Go run.

## Structural checks and limits

- `python3 scripts/validate.py`: both skills pass metadata, UI, portable-content, and local-reference checks.
- `bash scripts/install.sh --list`: exactly `craftflow-go` and `craftflow-set`.
- Temporary standalone copy installation: exactly two folders; all 58 payload files byte-identical to source. No actual user installation or configuration changed.
- Maintained relative Markdown links resolve; original legal-notice bytes remain present. Historical evaluation records were not rewritten.
- Installer/validator code did not change; prior unit-test totals are not presented as a new test run.

These are two explicit-invocation smoke cases on Linux. They do not establish automatic selection, plugin-host installation, optional cross-skill reference loading, comparative quality, cost, or reliability. Native Codex plugin execution and macOS installation were not tested.
