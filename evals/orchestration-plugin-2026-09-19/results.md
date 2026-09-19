# Engineering orchestration package evaluation — 2026-09-19

## Change and method

The repository now presents engineering orchestration as independently usable skills packaged together for Codex. The existing coordinator keeps its task-adaptive workflow. This revision adds catalog-based resource resolution and a conditional expertise-boundary reference; it preserves all six specialist entrypoints and their invocation policies. The root plugin manifest points to the original seven skill folders.

Four fresh agents received only their raw task, an isolated workspace, and a skill catalog. They did not receive expected findings, this report, previous responses, or the coordinator's acceptance tests. Each run explicitly invoked the coordinator. Names in the supplied catalog were qualified with `codex-skills:` and its entrypoint was stored separately from specialists. This is a simulated catalog test, not a native plugin-loader test. Agents were instructed to use only the task workspace and supplied resources, with no external services.

The starting repository revision was `3ef8837f4bc0a8b4721360e7f85228870c6fdf4f`. [Input hashes](inputs/before.json) record every supplied task and resource, including the revised skill. [Catalog](inputs/catalog.json) records the exact names, descriptions, and paths. Absolute temporary paths are historical identifiers, not installation instructions. [Artifact checks](outputs/artifact-checks.json) record final changed-file hashes and read-only invariants.

## Observed task behavior

| Run and cases | Observed result | Evidence and limit |
| --- | --- | --- |
| Tiny edit — case 4 | Corrected exactly `pakage` to `package`. Loaded the coordinator without specialist references or a review cascade. | [Request](inputs/tiny.md), [response](outputs/tiny-response.md); parent verified exact resulting content and the only changed path. This tests explicit invocation, not natural non-selection. |
| Multi-domain planning — cases 27–28 | Selected architecture, TypeScript, React, and TanStack Query guidance. Kept legacy import, rejected a type cast as validation, preserved user drafts, and assigned shared contracts before dependent work. | [Request](inputs/planning.md), [response excerpts](outputs/planning-response.md); no files changed. Checks were proposed, not executed. No UI/API implementation was requested or evaluated. |
| Conflicting handoffs — case 22 | Reproduced the `documents`/`entries` mismatch, rejected stale completion evidence, and distinguished a historical timeout from live worker state. | [Request](inputs/handoffs.md), [response](outputs/handoffs-response.md); source and checkpoint hashes remained unchanged. No real worker recovery was attempted. |
| Resume locally — case 29 | Inspected restored v1 files despite a completed checkpoint, finished the v2 migration, retained legacy imports and the unrelated note, and updated the checkpoint. | [Request](inputs/resume.md), [response](outputs/resume-response.md), [result patch](outputs/resume.patch); task-disabled delegation was respected. This does not simulate tools actually being absent. |

The evaluator judged all four runs acceptable for these bounded tasks. Tool/resource lists in agent responses are agent-reported, not a complete independently captured execution trace. Filesystem preservation and the final migration behavior were independently checked by the parent. No repeated sampling or before/after model comparison was performed.

The resume agent reported 7/7 local tests passing after its added coverage first failed 6 cases. Separately, the parent ran the existing [acceptance suite](../engineering-orchestrator/acceptance.test.mjs), withheld from the agent. The starting fixture passed 1/6 checks; the final implementation passed **6/6**, covering the exact v2 envelope, row order, archive defaults, v1/v2 import, assembled round trips, and unsupported versions. See [acceptance output](outputs/acceptance.txt) and [command record](outputs/acceptance.json). These checks verify fixture behavior, not general orchestration reliability.

## Structural and installation checks

| Check | Result |
| --- | --- |
| `python3 scripts/validate.py` | All 7 skills passed metadata, UI, portable-content, and local-reference checks. |
| Plugin Creator's `validate_plugin.py` against the repository root | Passed the supported manifest/skill ingestion checks. |
| Skill Creator's `quick_validate.py` on the revised coordinator | Passed. |
| Shell installer `--list` and installation to temporary link/copy destinations | The 7 linked skills matched the manifest's skills directory. Every standalone coordinator copy file matched its source; copied skill validation passed. |
| Parent artifact checks | Planning and handoff inputs unchanged; shared skill resources unchanged; exactly the intended tiny edit and five migration files changed; unrelated note preserved. |

[Installation output](outputs/installation.json) retains commands, results, and the manifest hash. The existing installer and validators were not modified; the full historical repository suite was not rerun. The new package reuses the same skill sources, so targeted installation checks addressed the changed distribution boundary.

## Reproduction and remaining scope

Recreate disposable workspaces from the existing [migration](../engineering-orchestrator/fixtures/migration) and [handoff](../engineering-orchestrator/fixtures/handoffs) fixtures. For resume, add [the supplied checkpoint](inputs/resume-checkpoint.json), `notes.txt` containing `Unrelated local note: retain export column order for the next release.` followed by a newline, and the matching request. Tiny-edit input is `# Document Exchange`, a blank line, then `This pakage exchanges documents.` with a final newline. Planning needs only its request. Copy current skills into read-only task resources and regenerate the catalog's absolute locations.

Give each fresh agent its corresponding `inputs/*.md` request and resource catalog. Withhold expected case behavior and the parent acceptance suite. To verify the recorded implementation instead, apply [resume.patch](outputs/resume.patch) to the reconstructed resume workspace, then run:

```bash
MIGRATION_PROJECT=/path/to/resume node --test evals/engineering-orchestrator/acceptance.test.mjs
```

Execution took place on Linux with runtime versions in the artifact-check record. Native Codex plugin installation, automatic skill selection, real no-subagent capability fallback, macOS execution, and directory publication were not tested. No personal marketplace or host configuration was modified. Follow the [host installation guide](../../docs/plugin.md) to test the package in a fresh Codex conversation before distributing it as host-verified.

The authoring and packaging basis is documented in the [plugin guide](../../docs/plugin.md#basis). The previous [coordinated migration evaluation](../engineering-orchestrator/results.md) remains historical evidence for delegated execution; it is not counted as a fresh run of this revision.
