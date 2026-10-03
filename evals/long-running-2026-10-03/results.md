# Long-running work refinement — 2026-10-03

Baseline: `32dc6b24d89f9edf5fdd628028ef2c9f1f5f6cce` (v0.5.4). Candidate package: v0.5.5. This work follows the user's request to implement the preceding review. At evaluation time, no commit, remote publication, installation, or user configuration change had been performed. Release preparation is recorded below separately.

## Changes and source basis

Go's continuity reference now reconciles changed instructions with active work and distinguishes steering from cancellation. Its coordination reference covers pending tool results, dependent decisions, and input identity. The entrypoint adds conditional routing without changing its description or invocation policy. Get Set and the technical reference library remain unchanged. The README and current scenario catalog reflect the added use cases.

The [GPT-6 practical guide](https://openai.com/ko-KR/index/practical-guide-building-gpt-6/) and [Astra authoring article](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) were fetched and read during the preceding review in this conversation. Extracted source hashes appear in the manifest. Host features remain outside this skills-only plugin. The new [model guide](../../docs/model-selection.md) and [comparison method](../comparison.md) distinguish requested settings, observed settings, and missing measurements.

These changes address an instruction gap identified in review. They do not respond to a newly demonstrated model failure, and no behavioral or efficiency improvement is established below.

## Attempted model evaluation

Three [cases](cases.md) were prepared: a narrowed export task with a late worker response, an edited slug function with a stale passing test record, and an exact spelling correction. Each variant is intended to receive the same task and input files plus its standalone Go package. Expected outcomes and `check_outputs.py` stay outside evaluator input. The event histories are replay fixtures, not connected workers or live asynchronous tools.

The first baseline steering invocation used Codex CLI `0.159.0-alpha.3`, an ephemeral session, `--ignore-user-config`, a workspace-write sandbox, and explicit Go invocation. It exited 1 before a model response with:

```text
Error: failed to initialize in-process app-server client: Read-only file system (os error 30)
```

A diagnostic retry supplied temporary `sqlite_home` and `log_dir` overrides with strict configuration checking. It failed with the same initialization error. A file-syscall trace could not start because ptrace is prohibited; it produced no additional model execution. A network-enabled retry request was interrupted before execution and produced no output files; it is not counted as an executed attempt. After the user asked to continue, the configuration retry ran under the normal sandbox.

The [manifest](manifest.json) preserves both executed invocation records, elapsed whole-attempt time, exit status, and captured initialization errors. No resolved model, reasoning effort, usage, or billing data was returned; these values remain `null`. Requested model and effort were inherited defaults. The two elapsed observations measure initialization failure, not model response speed.

| Case | Baseline | Candidate |
| --- | --- | --- |
| Steering | Blocked before model execution; one diagnostic retry also blocked. | Not run because the execution prerequisite remained unavailable. |
| Async result | Not run. | Not run. |
| Routine | Not run. | Not run. |

There are zero completed model evaluations and no baseline/candidate comparison. No task success rate, discovery rate, typical latency, token savings, or cost per successful task is established. Do not count the two initialization failures as evidence that either skill version produced an incorrect answer.

## Local acceptance-check validation

[check_outputs.py](check_outputs.py) checks the file inventory and protected input bytes, runs supplied tests plus independent edge assertions, and verifies that the checks did not change the task artifacts. The steering assertions include CSV quoting, CRLF, Unicode, empty names, and an empty download. Slug assertions include mixed whitespace, a non-breaking space, empty input, and an existing hyphen. Response claims about pending work, stale evidence, and resource reads still need separate inspection.

Eight checks ran in disposable directories, as recorded in [fixture-checks.json](fixture-checks.json):

| Input | Observed result |
| --- | --- |
| Each of the three original fixtures | Rejected, as intended: missing CSV header, incorrect whitespace normalization, or unchanged spelling. |
| Each of three author-created positive controls | Accepted: add `writer.writerow(["Name"])` before the CSV rows; use `"-".join(text.lower().split())` for slugs; make the exact spelling replacement. |
| Correct CSV output with a changed handoff record | Rejected for changing a protected input. |
| Correct spelling with an extra output file | Rejected for an unexpected file inventory. |

These are hand-authored checker controls, not independent model outputs. They establish that the proposed artifact acceptance checks discriminate these cases. They do not validate the new skill instructions, actual resource selection, live cancellation, asynchronous progress, or the handling of a status question/compaction.

## Reproduce the comparison when the host is available

Use six fresh disposable task directories, one for each case/variant. Copy only `fixtures/<case>/` into each task directory. Obtain baseline `skills/rung-go/` from the stated Git revision and candidate `skills/rung-go/` from the reviewed working tree; copy the assigned package to `.agents/skills/rung-go/`. Do not provide this report, the cases table, saved responses, or parent acceptance checks to the evaluator. Keep output logs outside the task directory.

Use the same host configuration for both variants, with recorded model/effort and permissions. A CLI invocation matching the initial attempt is:

```bash
codex exec --ignore-user-config --ephemeral --skip-git-repo-check \
  --sandbox workspace-write --color never --json \
  -C /absolute/path/to/disposable-task \
  -o /absolute/path/outside-task/response.txt \
  'Carry out TASK.md using the supplied rung-go skill in .agents/skills/rung-go/SKILL.md.'
```

Capture events, stderr, exit status, elapsed time, and exposed runtime/usage metadata. Then run `python3 check_outputs.py CASE /absolute/path/to/disposable-task` outside the evaluator session and inspect the response against the non-artifact criteria. Follow the [comparison method](../comparison.md); one successful pair still does not establish reliability. If both variants pass, report no demonstrated improvement on that case.

## Structural validation

See [structural-checks.json](structural-checks.json) for the final local commands and results. Installer and validator code were unchanged, so their regression suites were not rerun. Structural validation does not prove host installation or model behavior. The behavioral verification gap remains explicit for this candidate.

## Release preparation

The user subsequently authorized committing and publishing the change. A fresh GitHub inspection found `main` still at the baseline revision and the latest published release at v0.5.4, so v0.5.5 requires no integration or version adjustment. Existing validation applies to the unchanged skill and fixture bytes. The release notes must retain the blocked model-evaluation result and distinguish checker controls from model runs. GitHub CI and publication outcomes are recorded on the actual commit and release; they are not inferred from this preparation record. Existing installed skills and user configuration remain outside this release operation.
