# Astra authoring audit follow-up — 2026-09-29

Base revision: `3838bfb49b9e327a2b1357a94b29fba8713d860c`. The [OpenAI authoring article](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) was fetched directly in the preceding audit in this conversation. This source verification is separate from earlier repository audit interpretations.

## Changes

Go checks whether an existing diagnosis or reproduction still applies before repeating investigation. An unavailable original environment does not block a sufficiently supported, authorized local fix; confirmation on that target remains explicitly unverified. Stale evidence still calls for a discriminating check.

Set's common comparison, evidence, severity, and reporting criteria now live in one [review reference](../../skills/craftflow-set/references/quality/review-scope.md). Its entrypoint and architecture/quality references link there, while domain-specific criteria remain in their respective files. Read-only scope remains in the entrypoint. The README and current [scenario catalog](../set-go-2026-09-29/cases.md) reflect these behaviors. The package version is 0.4.1; the marketplace identity and source path are unchanged.

## Fresh execution

Three independent, ephemeral Codex CLI invocations ran in temporary macOS workspaces with copies of the current Set and Go packages under `.agents/skills`. Each received only the wrapper recorded in the [manifest](manifest.json), its task and raw fixture, and the available resources. Neither task nor wrapper named a skill. The wrapper requested a record of resources actually read. The audit conclusions, expected scenarios, sibling responses, and coordinator acceptance checks were not supplied. Host-level resources could also be advertised; this was not an isolated two-entry global catalog.

Codex CLI 0.157.1 ran with `--ignore-user-config`, no model override, and ephemeral sessions. The resolved model and reasoning configuration were not independently captured. This is behavioral smoke evidence, not an Astra-specific reliability claim. Implementation cases used a workspace-write sandbox; review used read-only. No user skills or Codex configuration were installed or changed.

| Case | Observed behavior | Independent acceptance |
| --- | --- | --- |
| [Valid diagnosis](valid-diagnosis-response.md) | Selected Go and read `changes.md` and `verification.md`. Checked the source hash against prior evidence, repaired the encoder, and completed local verification while reporting production/browser confirmation unavailable. It still ran a cheap local red/green check. | Only `preferences.mjs` changed; tests and skill files unchanged. Parent reran all 3 Node tests successfully. |
| [Stale diagnosis](stale-diagnosis-response.md) | Selected Go, rejected the old encoder diagnosis against current source, and used a direct encode/decode observation to locate the decoder failure before repairing it. Reported the unavailable production confirmation. | Only `preferences.mjs` changed; the already-correct encoder and test assertions were preserved. Parent reran all 3 Node tests successfully. |
| [Combined review](review-response.md) | Selected Set, read the common review scope plus architecture/quality criteria, then consulted Go's Query references. Identified the shared tenant cache key and missing request-state presentation as current-state findings, with proposed verification and no implementation. | All supplied source/task and skill hashes unchanged; no new workspace files. Parent checked the findings against the supplied source. Read-only sandbox also enforced the edit boundary. No browser/runtime check was run. |

[Execution records](execution.json) preserve observed commands, exit codes, read-output hashes, relevant test output, file changes, and web-search events. [Baseline checks](baseline-checks.json) record one failed and two passed assertions in each implementation fixture. [Acceptance](acceptance.json) records the parent's final checks; implementation patches are saved for the [valid](valid-diagnosis.patch) and [stale](stale-diagnosis.patch) cases. The manifest records input, resource, response, and post-run hashes.

## Structural verification and limits

- Repository structure checker: both skills pass metadata, UI, portable-content, and local-reference checks using Python 3.11 and the pinned PyYAML 6.0.3 in a temporary virtual environment. The system Python initially lacked PyYAML; no user Python environment was modified.
- Plugin Creator's `validate_plugin.py`: passed for version 0.4.1.
- Local link and package/marketplace consistency checks, plus `git diff --check`, are recorded in [structural checks](structural-checks.json).
- Installer and validator implementation did not change, so their full regression suites were not rerun.

These three unpaired cases demonstrate observed local skill selection and one cross-skill reference path. They do not establish selection reliability across other wording/catalogs, a before/after quality improvement, token or cost savings, marketplace/plugin-host discovery, or production correctness. The unavailable environment was the original production/browser surface; local Node execution was available. Fully execution-blocked repairs, PR merge-base selection, and staged/unstaged/untracked review coverage remain scenario expectations rather than newly executed results.
