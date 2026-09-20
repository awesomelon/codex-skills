# Document exchange v2

## Intent
Expose archive state in exports while retaining imports of existing document packets.

## Behavior changes
- Modify export: emit {version: 2, entries: [{id, title, archived}]} in input order. Preserve explicit archived values and default an omitted archived value to false.
- Add import support for version 2 entries, preserving archive state.
- Modify legacy version 1 import: continue to accept items and return archived: false on each row.
- Remove no existing compatibility or unrelated guarantees.

## Acceptance
Check exact parsed wire output independently of deserialize, explicit true/false/default archive values, row order, literal legacy and v2 inputs, nonempty round trips, and unsupported-version TypeError. Retain the unaffected guarantees in current-behavior.md.

## Design boundary
contract.mjs owns the format identifiers. producer.mjs and consumer.mjs remain the public serialization/deserialization entrypoints. Use the current modules and test infrastructure.
