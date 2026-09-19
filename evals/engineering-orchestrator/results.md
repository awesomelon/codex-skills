# Engineering Orchestrator validation — 2026-09-19

This revision changes `engineering-workflow` into an orchestration entrypoint: outcomes and dependencies, relevant skill selection, bounded agent assignments, ownership recovery, and verified integration. Existing investigation, change, performance, delivery, and continuity references remain conditional support. The designated [Astra article](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) was fetched for this revision; the original upstream MIT notice is unchanged.

## Method

Two fresh agents received only a copied skill, a raw task fixture, and execution boundaries. Neither received the expected-behavior catalog, another agent's conclusions, or the coordinator's acceptance checks. Both used the runtime's inherited model settings. The implementation run could delegate within its disposable project; the diagnosis run was strictly read-only. Inputs, skill hashes, exact launch prompts, and result hashes are recorded in [manifest.json](outputs/manifest.json).

## Observed behavior

- **Contract migration:** The coordinator retained ownership of the shared contract and coupled producer/consumer changes, and assigned regression tests to one actual subagent with separate file ownership. The completed artifact preserves v1 imports and emits/accepts v2 entries with archived state. The agent reported seven passing integrated tests. The parent inspected all changed code and ran six additional acceptance checks withheld from the implementer: the starting fixture failed five of six, and the final implementation passed all six. This supports the migration result without requiring separate producer and consumer workers. See the [saved response](outputs/migration-response.md), [implementation patch](outputs/implementation.patch), [final implementation](outputs/implementation), [baseline acceptance](outputs/baseline-acceptance.txt), and [final acceptance](outputs/final-acceptance.txt).

- **Read-only handoffs:** The agent found that the producer writes `documents` while the contract and consumer require `entries`. It reported a failing in-memory round trip, rejected stale `revision-a` evidence for current `revision-b` artifacts, and did not treat the historical producer timeout as proof of shutdown. It recommended a repair without performing it. The parent verified unchanged input and skill hashes. See the [saved response](outputs/handoffs-response.md).

The case catalog includes further scenarios; they were not all rerun. These runs test explicit invocation and the supplied artifacts, not automatic skill selection, token savings, broad model quality, or superiority to single-agent execution. Actual timeout recovery, capacity exhaustion, skill-catalog selection, remote delivery, and live production behavior were not exercised.

## Packaging and installation

- `python3 scripts/validate.py`: passed for all seven skills, including local-reference portability.
- The skill-creator `quick_validate.py`: passed for the source skill and a standalone installed copy.
- Installer listing, selective dry run, symlink installation, and copy installation passed in temporary directories. Copied files matched the source byte for byte, including the license; only the new skill name was installed.
- No installer or validator code changed. No real home directory or user installation was modified. These checks ran on Linux with Node v24.19.0 and Python 3.12.14; they are not macOS runtime validation.

See [command records](outputs/checks.json) and their referenced outputs. Existing users must follow the README migration instructions because the installer preserves old entries and local edits; this change does not migrate installations automatically.
