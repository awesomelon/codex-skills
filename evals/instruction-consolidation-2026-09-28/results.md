# Instruction consolidation: focused evidence

Baseline: `cb47695e83612b1bdba3f68cbfca234da6a663b2`. Authoring input: the user-supplied Markdown copy of **Rethinking skills and prompts for GPT-6 Astra**; the upstream page was not freshly fetched in this revision.

## Changes and structural checks

- Keep the orchestrator entrypoint focused on coordination; detailed handoff and evidence rules remain in conditional references.
- Clarify quality diagnosis versus behavior-preserving execution without making either skill depend on another installation.
- Remove numeric file-length examples and shorten standalone scope reminders.
- Move plugin-adaptation provenance from learning into sources, preserving pinned links and license files.
- `python3 scripts/validate.py`: all seven skills passed.
- `git diff --check`: passed.
- Entrypoint text, counted with Python `str.split()`: 3,464 to 2,993 words; orchestrator 857 to 547. These are text counts, not measured token, latency, or cost savings.

## Behavioral runs

Two fresh subagents used isolated copies of one skill and its raw fixture, without the parent audit, expected-behavior catalog, or other agents' conclusions. No model override was requested; agents inherited the session defaults. Model identity and sampling settings were not independently captured. Exact task text and input/resource hashes are in [manifest.json](manifest.json).

| Case | Observed result | Parent verification |
| --- | --- | --- |
| Standalone orchestrator, historical handoffs | Reported migration incomplete: producer emits `documents`, consumer expects `entries`; older checks do not establish current integration. Distinguished an old timeout from a live worker. | Inspected answer against source/checkpoint; all supplied project and skill file hashes unchanged; no new files. Runtime behavior was not executed or claimed. |
| Standalone refactoring, receipt construction | Consolidated shipment selection and receipt construction; reported baseline and final tests passing. | Inspected [result.patch](result.patch); only `checkout.mjs` changed. Existing test assertions and skill hashes unchanged. Parent ran `node --test`: 8 tests passed, 0 failed/skipped. Coverage includes both delivery modes, empty orders, error identity, effect sequencing, and awaiting reservation. |

The raw final responses are preserved in [responses.json](responses.json). Baseline test execution is worker-reported; the parent independently observed the final run. The second run of final tests checked the worker's handoff, not a new model sample.

## Limits

These are two focused smoke cases, not a before/after behavioral comparison or a reliability benchmark. Quality/refactoring automatic selection, plugin-host discovery, concurrent live-writer recovery, native macOS installation, and learning behavior were not exercised. Historical fixtures retain their original bytes; task invocations were renamed only in the disposable copies. Installer, validator, domain technical references, and license files were not changed.
