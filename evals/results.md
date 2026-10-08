# Tact validation results

## Tact 0.0.8 test-authoring boundary

Date: 2026-10-08. [Requests, inputs, skill hashes, raw tool events, responses, and parent checks](runs/2026-10-08-test-authoring.json) cover six fresh Codex CLI contexts using the revised skill. Plain fix and fix-plus-verification requests changed only the implementation, ran existing tests, and observed the expiry boundary directly. An explicit regression-test request added the equality case, which failed before the fix and passed afterward. A behavior change conflicting with an existing expectation preserved the test and requested that specific update after implementing and checking the new behavior. A project with no suite and a note suggesting a throwaway assertion script used direct observations without authoring tests. A test-execution-only request reported the existing failure without editing any project file.

Parent review covered final artifacts and recorded commands, including inline and temporary-code paths. All six cases met their scope expectations, unrelated notes were preserved, and all supplied skill copies matched the final source. These are one-run observations without a baseline comparison or a measured reliability rate. Earlier multi-turn authorization, browser E2E, and snapshot-specific workflows were not executed. Filesystem read isolation was not enforced. The no-suite evaluator made one unsuccessful attempt to remove a nonexistent Python cache after its behavioral checks; the raw record retains that failure.

Repository structure, Skill Creator validation, and all six existing semantic controls passed on macOS using Python 3.12 for the Python validators. Both Claude manifests passed strict validation. Local-source installation into fresh temporary Codex and Claude Code configurations reported version 0.0.8, and all seven installed skill files matched the evaluated source. The initial sandboxed behavioral CLI launch failed to initialize; the six recorded contexts then ran through approved execution with child workspace-write sandboxes. These checks do not establish automatic skill selection, Claude model behavior, published marketplace updates, or real-service integration. Installed user skills and configuration were not changed by installation tests.

## Tact 0.0.7 documentation cleanup revision

Date: 2026-10-08. [Requests, inputs, raw tool events, responses, and parent checks](runs/2026-10-08-documentation-cleanup.json) cover two fresh CLI contexts using the revised skill. The cleanup case moved the unique retry-budget constraint into the maintained guide, deleted the redundant draft and completed work log, and repaired the README links without adding a document. Both decision records, the useful recovery guide, implementation, and unrelated notes remained unchanged. The read-only variant recommended consolidation without changing any file. Parent checks confirmed the exact changed file set, all local documentation links, and matching final skill hashes.

Repository structure and Skill Creator validation passed with Python 3.12 and PyYAML 6.0.3 on macOS; the initial default Python attempt lacked PyYAML. These are one-run observations per case, without a baseline comparison or reliability measurement. Filesystem read isolation was not enforced, and the cleanup evaluator used an extra temporary hash snapshot. Automatic selection, installation, and publication were not tested during the behavioral evaluation.

Subsequent package checks in the same evidence record installed 0.0.7 into empty temporary Codex and Claude Code configurations on macOS, with all seven skill files matching the evaluated source. Claude manifests passed strict validation; both host manifests, marketplace paths, and the README version were aligned. These local-source checks do not establish published marketplace updates or model behavior.

## Tact 0.0.6 evidence and scope revision

Date: 2026-10-08. [Report and raw evidence](runs/2026-10-08-evidence/report.md) cover six fresh CLI contexts: indirect consumers, rejected debugging hypotheses, original decision scope, incomplete performance measurements, a routine typo, and an unchanged external-input boundary. Parent artifact checks confirmed scope and final skill hashes; the debugging regressions fail on the original and pass on the repair. Structure checks passed on Python 3.12. These are single-run observations, not a baseline comparison or measured improvement rate. Subsequent [package verification](runs/2026-10-08-release/report.md) confirmed temporary macOS installation in Codex and Claude Code with matching skill files. User installations were preserved.

## Tact 0.0.4 decision documentation revision

Date: 2026-10-07. The [focused evaluation](runs/2026-10-07-decisions-focus/report.md) covers the 0.0.4 decision-documentation source: two fresh contexts produced a useful proposal without an implementation checklist and reused adequate existing rationale without creating a new record. Structural checks passed. The [initial five-case evaluation and installation evidence](runs/2026-10-07-decisions/report.md) cover the earlier candidate; they do not validate the revised bytes. Neither run establishes general reliability or a measured improvement rate.

## Tact 0.0.3 communication revision

Date: 2026-10-06. [Report and raw evidence](runs/2026-10-06-communication/report.md) cover flexible presentation, specific engineering claims, stable terminology, and requested formats. One fresh evaluator context and three behavioral follow-ups met the reviewed expectations. Structural checks and temporary macOS standalone/plugin installation passed. These observations are not a baseline comparison or a general reliability measurement.

## Tact 0.0.2 release

Date: 2026-10-04. This report covers the 0.0.2 release inputs. Evaluation used isolated copies and did not modify the previously installed 0.0.1 package.

### Executed behavior

Four evaluators received fresh contexts with the task, raw inputs, and a copy of the candidate skill. Expected findings and parent acceptance checks were not supplied. The readiness evaluator then received two follow-up requests. All work used disposable paths; the parent inspected outputs and checked protected input hashes.

| Case | Observed outcome | Evidence |
| --- | --- | --- |
| Implementation | Replaced repeated accumulation with direct construction, fixed omitted zero timeout, preserved the contract, added regressions. Parent rerun confirmed the added regression fails on the exact original source and all four tests pass on the result. | [Response](runs/2026-10-04-integration/implementation/response.md), [commands](runs/2026-10-04-integration/implementation/commands.txt), [patch](runs/2026-10-04-integration/implementation/change.patch). |
| Read-only review | Found unchecked JSON assertions and a module mock that bypassed the implementation. Identified imprecise types and reflection separately, retained the legitimate external-input guard, and did not change assessed files. | [Response](runs/2026-10-04-integration/review/response.md), [commands](runs/2026-10-04-integration/review/commands.txt). |
| Readiness | Declined a readiness claim based on stale unit results, zero selected tests, and unrun production integration. Preserved the 14-day and 30/600-second conditions and rollback limits. | [Response](runs/2026-10-04-integration/readiness/response.md), [commands](runs/2026-10-04-integration/readiness/commands.txt). |
| Routine edit | Changed only the requested typo and returned a one-sentence result without a plan artifact, dependency change, or extra test suite. | [Response](runs/2026-10-04-integration/routine/response.md), [commands](runs/2026-10-04-integration/routine/commands.txt). |
| JSON-only follow-up | Returned parseable JSON with exactly the requested keys and no chat formatting, preserving the missing evidence and scoped values. | [Raw response](runs/2026-10-04-integration/readiness/json-response.txt). |
| Detailed follow-up | Delivered the requested explanation of evidence, conditions, rollback, and readiness without offering to explain later or performing external work. Did not invent the unspecified inclusive/exclusive 14-day boundary. | [Raw response](runs/2026-10-04-integration/readiness/detailed-response.md). |

[Run metadata and hashes](runs/2026-10-04-integration/summary.json) identify the exact instruction and input bytes. Raw responses retain their original Korean wording and temporary-path references. [Starting inputs](runs/2026-10-04-integration/inputs/) and the implementation artifacts are retained separately.

### Other checks

- `python3 scripts/validate.py` passed for the six-file skill package and all internal references, using `/opt/anaconda3/bin/python3` with PyYAML 6.0.3.
- `node --test evals/semantic-controls.mjs` passed all six controls on Node.js 24.21.0. [Raw output](runs/2026-10-04-integration/semantic-controls.txt). These are semantic examples, not model evaluations.
- Temporary standalone and Codex plugin installation passed for 0.0.2 with Codex CLI 0.158.0. Installed skill bytes matched the candidate. [Installation evidence](runs/2026-10-04-integration/installation.json).
- Maintained-file whitespace and document links were checked. The raw original-regression failure log retains Node's whitespace unchanged. The installer and validator implementations were unchanged; their 62-test regression suite was not repeated for this instruction-only change.

### Limits

These are four explicit-invocation smoke cases plus two follow-ups, not six independent trials or a measured improvement over 0.0.1. There was no baseline comparison, repeated sampling, automatic-selection measurement, or enforced cross-workspace read isolation. Evaluators inherited the session configuration; the exact resolved model identifier, token usage, and cost were not captured.

Effect-specific guidance was checked as instruction coverage, not executed against an Effect application. TypeScript runtime examples used Node's support; no TypeScript compiler or Vitest suite was run. No linter was installed. These limits do not turn the observed task outcomes into evidence for every rule or future task.
