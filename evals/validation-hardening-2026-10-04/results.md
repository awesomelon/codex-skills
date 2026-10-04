# Validation hardening — 2026-10-04

Status: deterministic validation passed; model execution is blocked before a response. This change strengthens repository evaluation tooling and adds challenge fixtures. It does not change installed skill instructions, metadata, plugin version, or historical results.

## Why this changed

At starting revision `c3e84a5568181a57dc37e047c38da2ad38614486`, the runner recorded a checker hash before preflight but later executed the live repository checker and copied live fixtures for each attempt. Editing the source during a batch could change the checked bytes or paired task inputs after their recorded identity was established.

The runner now freezes the catalog, selected fixtures, current and required legacy checkers, optional response rubric, and both skill trees before preflight. The report records original source paths separately from the frozen content hashes. Cases and checks use frozen copies. Integrity checks cover copying, per-attempt input pairing, and state before and after independent checks. A changed frozen dependency blocks the run rather than becoming an artifact pass. The response rubric is frozen for later manual review; raw attempt outcomes remain inconclusive until that review is separately recorded.

The dependency closure is explicit and repository-local. It is not a generalized dependency scanner, an immutable filesystem, or a security sandbox. The existing limitation on cross-workspace read isolation remains disclosed.

## Challenge coverage

The existing ten cases already cover fast failures, incomplete asynchronous work, configuration/noise, valid measurement, shared-rule drift, independent policies, review-only recurrence, routine edits, steering, and stale results. They were not added again.

Three variants were authored after the released skill instructions:

- `lazy-materialization`: time completed generator consumption, preserve duplicate/order/empty-input behavior, and propagate partial-generation errors.
- `valid-cached-control`: accept a supported warm-cache improvement within its stated scope rather than treating every cache hit as invalid evidence. Artifact checks preserve files; the response judgment remains a manual rubric criterion.
- `renamed-registry`: prevent the same shared-owner failure in a delivery-service domain. The checker changes existing registry values and adds two services, verifies zero-day and unknown fallbacks, and requires a real regression test to reject the original defect.

These are holdouts from instruction design, not secret benchmarks. They are inspectable repository fixtures; accessing the independent rubric/checker contaminates a claimed blinded trial. No skill instructions were tuned to these cases.

## Actual validation

Host: Linux, Python 3.12.14, Node.js 24.19.0, Codex CLI 0.159.2.

- `python3 -m unittest discover -s tests -v`: **101 tests passed, no skips**. The previous 84 tests remain; eight new runner tests and nine new fixture controls were added. [Full output](evidence/unit-tests.txt).
- Sixteen total runner tests include actual local fake-CLI subprocesses. They prove that changing original catalog/checkers/fixtures/rubric/skills after freezing leaves the frozen attempts intact; frozen tampering, symlinks, wrong-variant copying, and fixture pairing drift block invocation or checking. A checker mutated during the last check cannot be reported as verified merely because it exits zero. These controls do not call a model.
- Twenty fixture controls pass, including positive repairs and negative mutations for the new cases. [Focused output](evidence/fixture-controls.txt).
- `python3 scripts/validate.py`: both skills passed metadata and portable-reference validation. [Output](evidence/structural-validation.txt).
- `bash -n scripts/install.sh` and `git diff --check`: passed.

The [source manifest](evidence/source-manifest.json) identifies the skill and evaluation sources for this run. No macOS local execution, host installation, automatic discovery, or live steering/cancellation test was performed for this change. Remote CI is reported separately on the pull request for its exact head commit.

## Actual model attempt

A bounded direct initialization probe and the completed runner's preflight both exited 1 with:

> Error: failed to initialize in-process app-server client: Read-only file system (os error 30)

Neither received a model response. This is the current blocker, distinct from the prior release's HTTP 401. No host authentication, credentials, or permissions were changed to bypass it. [Direct probe](evidence/direct-preflight.json), [direct stderr](evidence/direct-preflight-stderr.txt), [runner stderr](evidence/runner-preflight-stderr.txt).

The runner compared v0.5.5 source `0925ce0ac0bc3ddbd56f722d9e86befb20486098` with the unchanged v0.6.0 skill bytes at `c3e84a5`, planning one pair for each of 13 cases. Its 39-file evaluation bundle and both skill snapshots passed input-integrity checks. All **26 planned case attempts remain `not_run`**, with no model successes or failures. [Frozen hashes and attempt accounting](evidence/comparison.json).

No behavior, latency, token, cost, discovery, or reliability gain is claimed. Preflight elapsed time measures failed initialization only. Requested model settings remain host defaults and observed settings/usage remain unknown. When a supported host is available, rerun from a new output directory, review actual responses using the frozen rubric, and retain failures as well as successes before making any comparative claim.

## Source review

The current [pstack snapshot](https://github.com/cursor/plugins/tree/e43c7ee26e0038c6c1fa8380dd34ce86ff94cb2a/pstack) is identical to Rung's latest pin. Rung already selectively covers its benchmark and recurring-error principles. This change therefore tests transfer and evidence integrity instead of importing another workflow.

[OpenAI's skill-evaluation guidance](https://developers.openai.com/blog/eval-skills) supports separating explicit invocation, discovery, negative controls, and actual tool evidence. Its [Astra authoring guidance](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) supports keeping entrypoints concise and loading detail conditionally. Real-host discovery remains separate future work; this runner still uses explicit invocation.
