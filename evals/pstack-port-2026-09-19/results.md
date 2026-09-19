# pstack-claude adaptation and validation — 2026-09-19

Compared `awesomelon/codex-skills` at `197a5205c050f88a5529e9853fff9860598d109a` with the user-designated [pstack-claude port](https://github.com/michael-denyer/pstack-claude/tree/af7aa63b5e196cb3d04fbe18dc2a970918fc883a). Two read-only comparison agents inspected orchestration/runtime and specialist-guard material; the coordinator checked the selected source and target files.

## Decisions

- Add conditional runtime-verification guidance: identify the actual instance/build, exercise public paths, independently inspect promised effects, check dry-run behavior, and preserve evidence after cleanup.
- Extend delivery guidance with an expected-head condition at the service write, pending/future merge reconciliation, and confirmation in the intended destination. The [GitHub CLI manual](https://cli.github.com/manual/gh_pr_merge) and local CLI help were checked; their queue behavior explains why a merge command can return before landing.
- Extend Code Quality Guard's existing review reference with defect-oriented test assessment, including shared faulty expectations, meaningful payloads, and valid absence assertions.
- Retain existing reproduction, scoped delegation, retry diagnosis, checkpoint reconciliation, and selective expertise. Do not duplicate them across guards. Do not import automatic routing hooks, named model panels, mandatory worktrees, a Bun store/watcher, or a new checkpoint CLI.

The [official Astra authoring article](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) was freshly fetched. Both discovery descriptions remain unchanged. The orchestrator entrypoint adds one conditional reference row; detail stays in the relevant references. The port's MIT notice remains in standalone installs, including the adapted test-review guidance. This is a focused instruction improvement, not a measured token or latency optimization.

## Behavioral observations

Two fresh agents received only a copied skill, their raw fixture, and execution boundaries; they did not receive expected outcomes. A prior comparison agent then reviewed the test fixture without receiving its expected answers. That third run is independent of the implementation but is **not** a fresh-context evaluation. Inputs and skill copies match the final source and remained unchanged; hashes are in [manifest.json](outputs/manifest.json). Task prompts are saved beside the results.

| Scenario | Observed result | Evidence |
| --- | --- | --- |
| Notes CLI runtime | Drove eight real CLI invocations. Confirmed persisted add/list and normal export, then detected all three dry-run data/log mutations despite success exit codes and unchanged export targets. Removed disposable data and retained evidence. | [Report](outputs/runtime/report.md), [commands and snapshots](outputs/runtime/commands-and-results.json) |
| Offline delivery review | Identified missing expected-head protection, retarget/base limits, already-enabled auto-merge without suitable gates, unsafe retargeting, and queued-versus-merged confusion. Performed no forge action. | [Coordinator-recorded delegate response](outputs/delivery-response.md) |
| Regression-test review | Found the shared incorrect total expectation and unverified email body, while retaining the meaningful denied-send absence test. Existing three tests passed despite both defects. | [Coordinator-recorded delegate response](outputs/test-response.md), [parent command evidence](outputs/test-checks.json) |

The coordinator inspected runtime commands/snapshots and confirmed cleanup. For the test-review fixture, the coordinator independently ran the original suite and checked the wrong total/body in disposable copies. Removing the inactive-user rejection in another isolated copy made the existing absence test fail, demonstrating its defect-detection value.

The delivery agent's report-file write was rejected by automatic approval review; its conclusions were returned in the conversation and recorded here by the coordinator as part of this requested repository change. It did not create the requested report. The test reviewer ran the read-only suite in the supplied input directory using `-B`, rather than the requested scratch working directory; hashes confirm no changes, and the coordinator's recorded rerun used a separate copy. These limits are not hidden as fully compliant runs.

## Packaging and limits

- `python3 scripts/validate.py`: all seven skills passed metadata, portability, and local-reference checks.
- Skill Creator `quick_validate.py`: both changed skills passed.
- The shell installer installed both changed skills into a disposable destination, updated a changed provenance file, and reported both unchanged on the final dry run. All installed files matched final source bytes, excluding only management markers. Standalone references and licenses were present.
- Checks ran on this macOS host with Python 3.9.6 and the native shell installer. Installer/validator implementation did not change, so the unrelated full test suite was not rerun.

These cases assess explicit invocation and the supplied artifacts. They do not prove automatic discovery, comparative model quality, a live merge race, UI/service driving, or performance gains. Intentionally faulty fixtures remain faulty. Published evidence normalizes local paths and omits machine environment metadata; original records remain outside Git. Source hashes are unchanged and published output hashes are recorded after normalization. Actual user installation is a separate delivery action after commit/PR creation, not an installation test.
