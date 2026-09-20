# Specification-driven concept evaluation — 2026-09-20

## Corrected scope

The user requested OpenSpec's concepts rather than a connection to its CLI. This revision removes the CLI adapter and setup guide, replacing them with conditional [spec-driven change guidance](../../skills/engineering-orchestrator/references/spec-driven-changes.md) and a [concept mapping](../../docs/spec-driven-changes.md). The guidance separates accepted behavior, proposed deltas, implementation design, tasks, and evidence while reusing existing project artifacts. It does not prescribe a tool, schema, folder hierarchy, document set, or approval pipeline.

ECC-derived acceptance and shared-contract guidance stays intact. The seven skill descriptions, UI metadata, plugin manifest, and installer implementations are unchanged. The earlier [CLI-adapter evaluation](../contracts-openspec-2026-09-20/results.md) remains a historical record, with pinned links to removed resources; it is not counted as current validation.

## Method and inputs

Three fresh agents received the revised Engineering Orchestrator, isolated raw project artifacts, and one ordinary engineering request. They did not receive OpenSpec CLI captures, generated skills, a tool schema, expected findings, other agents' responses, or parent acceptance checks. Each was restricted to its own project and read-only skill resources, with no further delegation or external services. Model/tools inherited the session defaults without overrides; exact model build, token use, cost, and agent timings were not measured.

The starting repository revision is `19605a4388bfd46b090372f3959f0541c357d32a`, which contains the merged follow-up #27 on the open #26 branch. [The input manifest](inputs/manifest.json) records the revised skill/resource hashes and every initial project file. Both substantive tasks used the existing [migration source fixture](../engineering-orchestrator/fixtures/migration), plus ordinary current-behavior, change, and work notes. All work items were incorrectly checked complete even though the source still implemented v1.

## Observed outcomes

| Request | Observed result | Parent verification |
| --- | --- | --- |
| Finish the documented change, verify, and reconcile existing records | Implemented v2 export and v1/v2 import; preserved compatibility and unrelated guarantees; updated current-behavior.md and work.md after verification. | Withheld migration checks passed 6/6. Independent Unicode and caller-nonmutation checks passed. Only the three implementation modules, existing tests, and two authorized records changed. |
| Review completion and propose the remaining plan in the response only | Rejected stale checked tasks, distinguished intended behavior from v1 source and accepted baseline, and connected outstanding work to observable checks. | All eight project files and skill resources remained byte-for-byte unchanged. Findings agree with the supplied source. |
| Correct a README typo | Corrected only `pakage` to `package`. | Exact expected README content; no additional file or directory. |

The implementation agent reported 5 failures in its expanded test suite before implementation and 8/8 passing afterward. These are agent-reported execution details retained in [the response](outputs/implementation-response.md) and [result patch](outputs/implementation.patch). The parent's independent evidence is in [commands](outputs/commands.json), [six-check output](outputs/acceptance.txt), [preserved-guarantee output](outputs/preserved-guarantees.txt), and [artifact hashes](outputs/artifact-checks.json).

The coordinator inspected the updated specification and confirmed that v2 export and dual-version import are recorded while the original unaffected-guarantees paragraph is preserved. The existing work record describes the stale handoff and actual implementation/verification evidence; no duplicate backlog or new document hierarchy was created. [Review excerpts](outputs/review-response.md) preserve the reasoning and its execution limits. The tiny agent's final response was: "Corrected `pakage` to `package` in README.md. Verified that this was the only content change. Supplied skill resources were preserved; no delegation or external services were used."

## Structure and distribution

All seven skills passed the repository validator, and the revised coordinator passed Skill Creator validation. [Structural records](outputs/structure.json) also record a search that found no operational OpenSpec commands, generated-skill invocations, or removed local-reference links in maintained skill/documentation surfaces. Historical evaluation captures and upstream provenance remain distinguishable from current instructions.

The parent updated the disposable standalone copy from the preceding evaluation. The existing installer removed the old adapter reference and copied the new concept reference; every source file matched the updated copy. See [copy-update evidence](outputs/copy-update.json). No user installation or host configuration was changed. Authored-content whitespace and changed-document local-link checks passed. The raw implementation patch retains whitespace-only diff context lines and is excluded from the authored-content whitespace check.

## Reproduction and limits

Recreate implementation/review projects from the migration fixture, omitting its TASK.md. Add [current-behavior.md](inputs/current-behavior.md), [change.md](inputs/change.md), and [work.md](inputs/work.md), plus notes.txt containing `Unrelated local note: retain export column order for the next release.` followed by a newline. Supply the [implementation request](inputs/implementation-request.md) or [review request](inputs/review-request.md), the revised skill location, and the isolation constraints above. For the tiny case, create README.md containing `# Document exchange`, a blank line, and `This pakage exchanges documents.` with a final newline; supply [the tiny request](inputs/tiny-request.md).

Keep the expected outcomes and parent checks out of the worker workspace. To verify the recorded implementation without a new model run, apply the saved implementation patch to the reconstructed starting project and rerun the commands in outputs/commands.json with MIGRATION_PROJECT set to its path.

These are single-run checks of explicit invocation on Linux. They do not establish automatic discovery, comparative success rates, cost improvements, macOS behavior, or recovery from requirements changed mid-run. Case 41 in the [scenario catalog](../engineering-orchestrator/cases.md) remains unexecuted. Real OpenSpec CLI compatibility is outside the corrected product scope, not an outstanding integration task.
