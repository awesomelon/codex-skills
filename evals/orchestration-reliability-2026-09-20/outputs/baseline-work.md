# Work

- [x] Export v2 and shared contract
- [x] Import v1/v2
- [x] Verify integrated compatibility

## Completed

- The partner confirmed the revised v2 wire field `isArchived`. This replaces
  the earlier unshipped `archived` spelling, which has no compatibility alias.
  The previous importer handoff is resolved.
- `contract.mjs` declares version `2`, collection field `entries`, and archived
  wire field `isArchived`, shared by exporter and v2 importer.
- `producer.mjs` exports `{version: 2, entries: [{id, title, isArchived}]}` from
  in-memory `{id, title, archived}` rows. Omitted or undefined `archived`
  defaults to `false`; explicit flags are retained. Entry fields remain ordered
  as `id`, `title`, `isArchived`.
- `consumer.mjs` now imports legacy v1 `items` with `archived: false` and v2
  `entries` with `isArchived` mapped to `archived`. Omitted v2 flags default to
  `false`. Unsupported versions raise `TypeError`.
- Row order, Unicode, and caller-owned data are preserved; imports produce
  fresh rows. `requirements.md` now records the confirmed contract.
- Updated `producer.test.mjs` and `exchange.test.mjs` for the revised exporter,
  legacy imports, and integrated migration. Unrelated `notes.txt` is unchanged.

## Verification performed

- `node --test` on Node v24.19.0: all 10 tests passed (4 producer/contract
  tests and 6 exchange tests).
- Producer checks cover the v2 envelope, empty exports, archived defaults and
  explicit flags, row and field order, Unicode, and frozen caller-owned data.
- Exchange checks cover empty and populated v2 round trips, v1 imports, v2
  flag mapping and defaults, v1-to-v2 re-export, row order, Unicode, caller
  nonmutation, and independent imported rows. Unsupported numeric versions,
  string versions, null, and missing versions are checked for `TypeError`.
- A separate Node assertion verified `notes.txt` against its original exact
  contents and confirmed the runtime version.

## Result

The integrated migration is complete and locally verified against the revised
contract. The previously observed v1 rejection and lost v2 archived flags are
resolved. No migration work remains within this module.
