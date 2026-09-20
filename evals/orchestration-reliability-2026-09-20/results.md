# Validation hardening and orchestration evidence — 2026-09-20

Starting revision: `7fae44bf1da3d13a8d28bfeec781d9b686bf657a`.

## Changes supported by the audit

The repository validator accepted an invalid YAML description (`Review: code quality`). It now safely parses frontmatter and UI YAML, rejects duplicate keys and non-string required metadata, and prevents inline or quoted known UI keys from bypassing the repository's formatting checks. Eight regression tests cover these failures and valid quoted descriptions. PyYAML is a pinned development dependency; the Bash installer remains Python-free.

The new GitHub Actions workflow runs the validator, installer syntax check, and unit suite on Linux/Python 3.10 and macOS/Python 3.13. It uses read-only repository permissions, no model credentials, and disposable installer destinations. Workflow configuration, remote job execution, and native Codex installation are separate claims.

All seven skill bodies, references, discovery descriptions, and invocation policies were retained. The designated [OpenAI Astra article](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) was retrieved during the preceding audit. The forward runs below found no behavioral failure requiring another instruction. Evaluation evidence and development checks improve confidence without expanding installed guidance.

## Paired requirement-change task

Two fresh agents received separate, identical copies of the existing [migration fixture](../engineering-orchestrator/fixtures/migration), excluding TASK.md, plus the shared files in `inputs/`. One had only the project and standard runtimes; the other additionally received a read-only copy of Engineering Orchestrator. Neither received expected findings, acceptance tests, other outputs, or this report. Further delegation and external resources were disabled equally. Model and reasoning settings inherited the session defaults with no overrides; exact backend build, tokens, costs, and timings were not measured.

Both first received [phase one](inputs/phase-one.md), which requested a verified exporter handoff while preserving the importer. After each completed that handoff, the parent independently ran its local tests and verified that consumer.mjs was unchanged. Both passed 6 tests. [Phase-one hashes and results](outputs/phase-one.json) retain the intermediate evidence.

Both then received the same [changed contract](inputs/phase-two.md): wire `isArchived`, in-memory `archived`, and preserved v1 compatibility. This is a requirement change at an explicit handoff during an unfinished migration, not an interruption during a tool call or a test of multiple concurrent writers.

| Result | Without the skill | With the skill |
| --- | --- | --- |
| Initial exporter handoff | 6 local tests passed; importer unchanged | 6 local tests passed; importer unchanged |
| Final local tests, independently rerun | 10/10 | 10/10 |
| Withheld final acceptance tests | 5/5 | 5/5 |
| Unrelated note | Preserved byte for byte | Preserved byte for byte |
| Requirements and work record | Revised contract and completed integration recorded | Revised contract, superseded handoff, and completed integration recorded |

The parent inspected the implementations and records and ran [independent acceptance checks](changed-contract.test.mjs), including exact producer and consumer expectations rather than relying only on round trips. [Baseline patch](outputs/baseline.patch), [skill patch](outputs/candidate.patch), acceptance logs, final records, and hashes are retained in `outputs/`.

Both variants met the task. This single pair provides **no evidence of a success-rate advantage from the skill**, and cannot establish equivalence across other tasks. The common request already supplies clear acceptance conditions and resource boundaries; successful compliance cannot be attributed solely to skill guidance.

## Live delayed-writer recovery

A third fresh agent received the skill, [recovery request](inputs/recovery.md), the original migration fixture, and a timed-out checkpoint plus an owned-worker record. A real [delayed writer](late_worker.py) remained active in a managed execution session, ready to overwrite producer.mjs when released. It supported a project-local cooperative stop and acknowledgement. The evaluator could inspect its actual script and owned controls, but not the parent acceptance suite.

The agent requested a cooperative stop and observed the acknowledgement before implementation. The parent confirmed the managed session's exit code 0 and supplied that runtime fact. The agent then completed v2 export/v1-v2 import and reconciled the checkpoint. Parent checks found 8/8 local tests and 6/6 withheld migration acceptance tests passing. Releasing the old writer after completion produced no late-write marker and left producer.mjs unchanged. The note and supplied skill resources were preserved. See [verification](outputs/verification.json), [patch](outputs/recovery.patch), [checkpoint](outputs/recovery-checkpoint.json), and [worker record](outputs/recovery-worker.json).

Initial setup attempts exposed tool-local process namespaces: detached child processes did not persist, and process IDs could not safely identify a worker across commands. Those attempts were stopped before the evaluator made mutations. The corrected fixture used a managed foreground session and cooperative file controls; its initial hashes are recorded in [manifest.json](outputs/manifest.json). This run establishes one cooperative recovery path, not forced termination, native subagent cancellation, capacity exhaustion, or recovery when shutdown cannot be confirmed.

## Repository checks

- `python3 scripts/validate.py`: all seven packages passed.
- `/bin/bash -n scripts/install.sh`: passed.
- `python3 -m unittest discover -s tests -v`: 65 tests passed on Linux, including eight new YAML regression tests.
- Actual Bash link and copy installation in disposable destinations: all seven packages matched source bytes. [Installation record](outputs/installation.json).
- Workflow YAML parsed and its intended triggers, two-runner matrix, and read-only permission were inspected. This local check is not a GitHub Actions execution result.

## Reproduce and remaining scope

For either paired variant, copy the existing migration fixture without TASK.md, then add inputs/requirements.md, inputs/work.md, and inputs/notes.txt. Submit phase-one.md and phase-two.md in order with the same resource limits. Supply the skill only to the skill variant. Keep expected checks and saved outputs outside worker input. For replay without a model, apply the corresponding final patch with `git apply --unidiff-zero` and run:

```bash
MIGRATION_PROJECT=/absolute/path/to/project node --test evals/orchestration-reliability-2026-09-20/changed-contract.test.mjs
```

For recovery, start late_worker.py only against a dedicated copy, retain its managed execution session, and supply its stop/release/acknowledgement paths through worker.json. Never use process IDs from another tool namespace. Give the worker a five-minute maximum lifetime and account for its termination before cleaning up. The saved recovery patch reproduces application/requirements/work changes; worker and checkpoint records are separate runtime evidence.

These are three bounded model runs, with two turns per paired variant. They are not repeated sampling, a speed benchmark, natural skill discovery, or a native plugin-loader test. macOS host installation and automatic invocation remain unverified in this session. Follow [the plugin guide](../../docs/plugin.md) to record host version, advertised names, actual resource loads, requests, and outcomes in fresh conversations. CI cannot substitute for those host observations.
