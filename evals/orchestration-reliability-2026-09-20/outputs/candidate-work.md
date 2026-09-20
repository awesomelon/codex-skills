# Work

- [x] Export v2 and shared contract
- [x] Import v1/v2
- [x] Verify integrated compatibility

## Completed integrated migration

- The partner confirmed the revised v2 wire entry field `isArchived`. In-memory rows continue to use `archived`. The earlier unshipped v2 spelling is superseded and has no compatibility fallback.
- `contract.mjs` documents the revised wire shape and legacy v1 shape; export version remains 2 with collection field `entries`.
- `producer.mjs` emits `{version: 2, entries: [{id, title, isArchived}]}`, mapping in-memory `archived` and defaulting omitted or undefined values to `false`. It retains input row order, Unicode, and field order without changing caller-owned rows or extra data.
- `consumer.mjs` now accepts v1 `items` with `archived: false`, and v2 `entries` with `isArchived` mapped to `archived` (omitted flags default to `false`). Unsupported versions still raise `TypeError`.
- `requirements.md` reflects the confirmed contract. `producer.test.mjs` and `exchange.test.mjs` cover direct wire fixtures and integrated behavior.
- The unrelated `notes.txt` is unchanged: its before/after SHA-256 is `9f337a38f9d9a28f3eb5bcd1ad8955a700f9b8cb53a87c5c4e601355587fe859`.
- This directory is not a Git repository, so no revision or Git diff is available.

## Actual verification

- Before the revised implementation, `node --test` ran 10 tests: 4 passed and 6 failed, exposing the old v2 spelling, rejected v1 imports, and missing imported archive values.
- After updating export and import together, `node --test`: all 10 tests passed.
- Verification includes the exact empty v2 wire shape; explicit true/false flags and defaults; independent v1 and v2 import fixtures; unsupported versions (including string, missing, and null versions); empty and nonempty round trips; v1 import followed by exact v2 re-export; row order; Unicode; frozen caller-owned rows; and independence of imported results across calls.
- `sha256sum notes.txt` confirms the unrelated note was preserved.

## Handoff history and remaining work

The first requested handoff completed only the exporter and shared contract, leaving `consumer.mjs` untouched. At that point 6 tests passed, but a direct probe showed rejected v1 imports and dropped archive flags. That was deliberately an incomplete integration.

Partner confirmation and authorization to finish superseded the importer hold and revised the wire flag to `isArchived`. Both observed integration gaps are now resolved and covered by passing tests. No requested implementation work remains. Verification is local to this module; no external partner service or deployment was exercised.
