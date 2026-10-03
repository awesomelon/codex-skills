# Native CLI feasibility and comparison pilot

The frozen 24-attempt pilot completed on macOS with Codex CLI 0.160.0. Both arms produced correct artifacts and preserved the assessed scope in all 12 attempts per arm. The inspected responses also made the expected diagnosis, review, and stale-evidence decisions. These cases show no demonstrated additional benefit from Rung. They do not qualify a 1.0 release.

Subsequently, the maintainer adopted a stability-and-compatibility policy and completed the [separate qualification batch](../2026-10-03-qualification/results.md). The status statements below describe this earlier pilot milestone.

## Inputs and boundaries

[plan.json](plan.json) freezes the four cases, source/checker hashes, requested `gpt-6-astra` / `high` profile, 24-invocation ceiling, 180-second attempt limit, and run order. There were three repetitions per case and arm, with no automatic retries. The Rung skill payload matches 0.5.5; no instruction repair or distinct candidate arm was justified by the pilot.

Each attempt used a new temporary workspace and child CLI state. Control inputs contained no Rung package; Rung inputs contained the two current skills and an explicit invocation wrapper. Pre-turn prompt audits passed for all attempts. Native command sandbox probes denied source/private-state reads and outside writes while allowing the workspace. Global configuration and installed skills were not changed. Model tools could not access the native authentication reference or original Codex state.

Requested settings are known for all 24 attempts. Their ephemeral CLI event stream did not expose resolved settings; those remain unknown in these records. Later trace diagnostics observed Astra/high in separate sessions, which does not retroactively establish the earlier sessions' settings. The comparison is an engineering pilot under a fixed request, not a model-specific reliability estimate.

## Outcomes

| Case | Control artifact/scope checks | Rung artifact/scope checks | Response assessment |
| --- | --- | --- | --- |
| Routine wording | 3/3 | 3/3 | Exact correction with preserved surrounding bytes |
| Wrong diagnosis | 3/3 | 3/3 | All identify the stale encoder diagnosis and repair the decoder; unavailable production confirmation disclosed |
| Review scope | 3/3 | 3/3 | All identify cross-tenant cache reuse and preserve staged, unstaged, and untracked work |
| Stale result | 3/3 | 3/3 | All reject the earlier snapshot as evidence for current source and produce the correct repair |

The raw classifications are six `passed` routine attempts and eighteen `inconclusive` attempts requiring manual criteria. [author-assessment.json](author-assessment.json) records the coordinator's response assessment and hashes of the original records. It is not an independent blinded judgment. Incomplete CLI tool events prevent full adjudication of every verification claim, so the eighteen cases have not been relabeled as fully passed. Artifact correctness and semantic response assessment are narrower findings.

The provider's reported usage is retained in each record. No price or complete cost model was recorded. No token, time, cost-saving, or statistical superiority claim follows from this pilot. The artifact ceiling in these fixtures makes simply repeating them uninformative for the proposed usefulness gate.

## Tool observability repair

Some CLI JSON streams omitted code-mode tool calls, including commands described in model responses. [trace-probe.json](trace-probe.json) records a separate, read-only diagnostic showing a failing test command in the evaluation-owned session while the CLI stream contains no corresponding command event. This establishes an observability gap, not fabricated verification and not proof that any particular unseen historical command ran.

The runner now retains only tool calls/outputs and observed model/effort from the session matching its current thread identifier. It rejects symlink paths and marks missing, truncated, or ambiguous traces. It does not export reasoning items or unrelated session metadata. This requires temporary session persistence inside the isolated child state; the state is deleted after confirmed group cleanup.

The separate [trace-smoke record](trace-smoke/record.json) captures ten tool items, observed `gpt-6-astra` / `high`, the two pre-repair test failures, and all three post-repair tests passing. Independent artifact and scope assertions also pass. The response correctly distinguishes the earlier captured snapshot. This author-adjudicated diagnostic satisfies the stale-result criteria, but is not part of the frozen 24-attempt denominator and is not a held-out qualification case.

The batch ceiling was 24 comparison attempts. Two subsequent model invocations were narrowly scoped observability diagnostics, retained separately above; they were not added as retries or favorable comparison samples.

## Distribution and repository checks

[local-distribution.json](local-distribution.json) records native local-marketplace registration, installation/enabled listing, removal/reinstallation using a temporary manifest version, restoration of 0.5.5, and final removal. Installed skill bytes matched source at each step, and an unrelated preference and file in the isolated state were preserved. The temporary `1.0.0-rc.1` manifest used unchanged skill bytes; it is not a release candidate or published version. This verifies the local CLI package lifecycle, not loaded task behavior, desktop activation, implicit discovery, or installation from a final published revision.

[checker-controls.json](checker-controls.json) records native positive/negative fixture controls. [validation.json](validation.json) records current structural validation, Bash syntax, and the full deterministic repository test suite. These checks validate tooling and packaging, not model usefulness. The [initial execution record](../2026-10-03-pilot/results.md) retains earlier startup failures and earlier validation snapshots without rewriting them.

## Grounded examples

These examples use synthetic fixtures and explicitly invoked source skills, not installed-plugin discovery:

- Assessment: [Rung review repetition 1](06-review-scope-rung-r1/record.json) identified the staged cache key's tenant-isolation regression. The independent preservation check confirms unchanged files, HEAD, index, status, and Git configuration. The fixture has no application consumers or full product test suite.
- Implementation: [Rung diagnosis repetition 1](04-wrong-diagnosis-rung-r1/record.json) rejected the obsolete encoder diagnosis, repaired the decoder, and passed the independent false/true/default checks without modifying supplied tests. Production/browser confirmation was unavailable; complete historical command fidelity has the limitation described above.

## Release decision

The package remains 0.5.5. Commit/publication was requested after completion, and completion has not been claimed. The design's usefulness gate is not met by this pilot; a maintainer decision is pending on retaining that gate versus explicitly adopting a stability-focused release claim. Do not expand sampling to search for favorable outcomes or silently lower the gate.

The full frozen qualification suite, independent-skill cases, installed-host task/discovery behavior, required live-continuity checks, desktop lane or explicit scope decision, and final published-payload verification remain open. No user installation was replaced. No version bump, commit, tag, push, or release was performed for this incomplete milestone.
