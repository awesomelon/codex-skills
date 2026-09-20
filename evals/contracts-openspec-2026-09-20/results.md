# ECC and OpenSpec integration evaluation — 2026-09-20

## Change and source basis

This revision keeps the seven existing skills and their discovery metadata. It adds acceptance and shared-contract guidance to Engineering Orchestrator, a conditional boundary-contract reference to Architecture Guard, and an optional OpenSpec adapter. It does not install upstream bundles, copy generated OpenSpec skills, configure models or hooks, or add a new runtime. The [source record](../../skills/engineering-orchestrator/references/sources.md) pins the inspected ECC/OpenSpec revisions; the [setup guide](../../docs/openspec.md) separates optional installation from skill operation.

The OpenAI Astra authoring article was fetched during this revision. Only task-relevant details were added behind existing references or a conditional route. Source review and structure checks are separate from observed task behavior.

## Method

Six fresh agents received an explicit skill invocation, an isolated project, and read-only skill resources. Two cases were paired: baseline and candidate migration, and baseline and candidate OpenSpec status review. Two additional candidate runs covered a tiny edit and a proposal-only request. Agents received no expected findings, other outputs, or parent acceptance suite. They were restricted to their own project/resources, local work, no further delegation, and no external services.

Baseline skills came from `92b32fa458ae347e14c9a829a159737b1eafcbb2` (the still-open plugin PR #26 at the start of this work). Both variants used the same task text, starting source, optional Architecture Guard catalog entry, and session-configured model/tools with no model override. Exact model build, token usage, cost, and agent elapsed time were not exported or measured. One run per variant is a bounded smoke comparison, not a reliability or performance benchmark.

[Input manifest](inputs/manifest.json) records initial project and resource hashes. Candidate behavioral instructions match the delivered revision; only the provenance reference `references/sources.md` was expanded after snapshots were supplied. That provenance-only edit was not a new behavioral run. [Artifact checks](outputs/artifact-checks.json) record final paths/hashes and preserved resource bytes.

The OpenSpec fixture contains **synthetic CLI captures** shaped from the inspected upstream workflow, with a custom requirements/tracking layout. They are not outputs of a live CLI invocation. The agents were explicitly told the CLI was unavailable. These cases test interpretation, scope preservation, and evidence judgment; they do not certify CLI compatibility.

## Observed results

| Case | Baseline | Candidate | Independent evidence |
| --- | --- | --- | --- |
| Shared-contract migration | Implemented v2 output and v1/v2 import; local agent tests reported 6/6. | Implemented the same required behavior; local agent tests reported 6/6. | Parent's withheld suite passed 6/6 on each result. Only contract, producer, consumer, and tests changed; unrelated note preserved. |
| Checked OpenSpec tasks with old implementation | Rejected recorded completion and identified producer, consumer, and coverage gaps. | Rejected recorded completion, identified the same gaps, and explicitly distinguished supplied captures from refreshed CLI state. | All nine project files and skill resources unchanged in both runs. Starting-code acceptance checks independently fail the missing v2/default behaviors. |
| Tiny edit beside an OpenSpec directory | Not rerun; no paired conclusion. | Corrected exactly one word. | Only README.md changed, with exact expected bytes. The OpenSpec configuration was unchanged and no new artifacts appeared. |
| Proposal-only request | Not rerun; no paired conclusion. | Produced the requested proposal with acceptance criteria and implementation/verification work; reported the stale completion state. | Only proposal.md was added. All nine existing files and skill resources remained unchanged. |

Both paired variants passed the applicable outcome criteria. This supports compatibility with those tasks, not superiority of the added guidance. The proposal is detailed for a small fixture; no claim is made about reduced planning overhead. [Saved response excerpts](outputs/responses.md) preserve agent reports; they are not complete tool traces.

The parent used the existing [acceptance suite](../engineering-orchestrator/acceptance.test.mjs), withheld from implementing agents, against the original fixture and both resulting implementations. The original passes 1/6; both implementations pass 6/6. It checks literal v2 output, archive defaults/preservation, order, legacy/current imports, assembled round trips, and unsupported versions. See [command records](outputs/acceptance-commands.json), [starting output](outputs/starting-acceptance.txt), [baseline output](outputs/baseline-migration-acceptance.txt), and [candidate output](outputs/candidate-migration-acceptance.txt).

## Structural and copy checks

- `python3 scripts/validate.py`: all seven skills passed metadata, UI, portable-content, and local-reference checks.
- Skill Creator's `quick_validate.py`: both changed skills passed.
- Shell installer copied both changed skills into a disposable destination. Every source file, including new references and upstream notices, matched its copy. The only additional file was the installer's existing ownership marker. [Installation record](outputs/installation.json) notes an initial comparison assertion that incorrectly counted this marker as a source mismatch, and its correction without reinstalling.
- Authored-document whitespace checks passed. The full staged diff also flags whitespace in raw Node failure output and an upstream license's terminal blank line; those evidence/notice bytes are retained unchanged and excluded from the authored-document check. Installer and validator implementations were unchanged, so their full historical unit suite was not rerun.

Checks ran on Linux; versions are in the artifact record. They do not establish macOS execution or native Codex discovery.

## Reproduction

Use the repository revision containing this report for candidate instructions and the pinned baseline revision above for baseline instructions. The recorded candidate source-provenance hash differs as described above; behavioral files and notices can be checked against the manifest. Recreate fresh workspaces and compare the same requests with equivalent model/tool settings.

- Migration: copy the existing [migration fixture](../engineering-orchestrator/fixtures/migration), omitting its TASK.md. Add notes.txt containing `Unrelated local note: retain export column order for the next release.` followed by a newline. Supply [the migration request](inputs/migration.md) and the two skill locations.
- Status review and proposal: copy [the status fixture](fixtures/status-review) and supply [the review request](inputs/status-review.md) or [the proposal request](inputs/proposal.md). Treat captured relative paths as project-relative, as explicitly stated in those requests.
- Tiny edit: create README.md containing `# Document exchange`, a blank line, and `This pakage exchanges documents.` with a trailing newline. Add openspec/config.yaml containing `schema: spec-driven` and a newline. Supply [the tiny request](inputs/tiny.md).

For every run, provide the chosen Engineering Orchestrator resource location. For all but the tiny case, make Architecture Guard available by its actual resource path and description. Restrict writes to the task workspace and keep skill resources unchanged. Do not supply this report, expected cases, other runs, or the acceptance suite to the worker.

To reproduce the saved migration outputs without invoking a model, apply [baseline-migration.patch](outputs/baseline-migration.patch) or [candidate-migration.patch](outputs/candidate-migration.patch) to a fresh original fixture and run:

```bash
MIGRATION_PROJECT=/path/to/result node --test evals/engineering-orchestrator/acceptance.test.mjs
```

## Remaining coverage

The [scenario catalog](../engineering-orchestrator/cases.md) also includes unresolved intent, blocked CLI states, manual spec changes during resume, ambiguous change/store selection, concurrent shared-spec writers, and sync/archive preservation. Those branches were not executed here. Likewise untested: real OpenSpec 1.13.1 installation/generated skills, native plugin discovery, external stores/worksets, standalone Architecture Guard selection, and repeated model sampling. Optional setup commands were documented but not run against user settings or repositories.
