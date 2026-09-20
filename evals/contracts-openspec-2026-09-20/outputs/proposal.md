# Proposal: document-v2

## Purpose and planning status

Implement the selected `document-v2` exchange contract: export version 2 documents with archive state while continuing to import legacy version 1 documents. Preserve the public `serialize(rows)` → JSON string and `deserialize(text)` → rows API, document order, and existing export/import capabilities.

This is a planning deliverable only. No implementation, test execution, tracking edits, installation, synchronization, archive operation, or external service access is part of this work.

## Sources and current evidence

Project root: `/tmp/codex-contracts-openspec-evaluation/candidate-proposal/project`.

The supplied `status.json` and `apply.json` captures select change `document-v2` and schema `team-exchange`. Their relative change and context paths resolve against this project root to `planning/changes/document-v2`, with `requirements.md` as the behavior requirements and `work.md` as the durable task source. These are the actual captured paths; a conventional `openspec/` layout is not assumed.

The CLI is unavailable. These captures were inspected as supplied, not refreshed. `status.json` reports `isComplete: true` and both artifacts done; `apply.json` reports `all_done` and 3/3 tasks complete. Its suggestion to archive does not authorize archiving and does not establish behavioral completion.

Static inspection contradicts recorded completion:

| Artifact | Observed behavior or evidence | Required work |
| --- | --- | --- |
| `contract.mjs` | `CURRENT_VERSION = 1`, `COLLECTION_FIELD = 'items'` | Define current v2 representation and retain explicit legacy identifiers. |
| `producer.mjs` | Uses those constants and emits only `id` and `title` | Emit v2 `entries` with `archived`, including its default. |
| `consumer.mjs` | Accepts only `CURRENT_VERSION`, reads only `COLLECTION_FIELD`, returns only `id` and `title` | Dispatch by version, support both representations, and return archive state. |
| `exchange.test.mjs` | Empty round trip and rejection of version 99 only | Assert the wire format independently, legacy import, defaults, order, and nonempty integration. |
| `planning/changes/document-v2/work.md` | All three items checked | Reconcile tracking with implementation evidence during future authorized implementation. Leave it unchanged in this proposal. |

Updating the two shared constants alone would move the consumer to v2-only behavior and remove required legacy import. The existing empty round trip could pass while both modules use the wrong wire format. No runtime pass or failure is claimed here.

## Scope and contract decisions

Use the existing three-module boundary: `contract.mjs` owns shared wire identifiers; `producer.mjs` owns serialization; `consumer.mjs` owns version dispatch and deserialization. Both entry points depend on the contract, not on each other. There is no shared mutable state in the inspected code and no need for additional service layers, a new schema generator, or new modules.

The proposed shared contract keeps `CURRENT_VERSION` and `COLLECTION_FIELD` for current output (`2` and `'entries'`) and adds explicit legacy version/collection identifiers (`1` and `'items'`). The consumer chooses a collection based on the packet's version rather than assuming all accepted packets use the current collection field. Keep these identifiers in the existing contract instead of duplicating version policy across modules. Independently authored test fixtures should use literal wire expectations so a mistaken shared constant cannot make tests agree with a mistaken implementation.

| Direction | Version and collection | Row representation |
| --- | --- | --- |
| Export | Numeric `version: 2`, collection `entries` | `id`, `title`, `archived`; preserve supplied boolean archive values and default a missing archive value to `false`. |
| Import v2 | Numeric `version: 2`, collection `entries` | Preserve `id`, `title`, and the archive state. |
| Import legacy | Numeric `version: 1`, collection `items` | Preserve `id` and `title`; normalize legacy rows without archive state to `archived: false`. |
| Import unsupported | Any version outside the supported v1/v2 versions | Throw `TypeError`. |

Preserve row order in both directions and preserve identifier/title values without coercion. Keep JSON-string input/output and the existing exported function names. Do not require JSON object-key order; array order and the actual parsed wire fields are the observable contract.

Only version 2 export is required. Do not add a version-selection API or remove version 1 import. Preserve the unrelated note in `notes.txt`; export column-order work is outside this change. Also outside scope are broad malformed-input validation, migration of stored documents, dependencies, deployment, synchronization, and archival.

The requirements define missing archive defaults for export and legacy input. They do not specify handling of null/nonboolean archive values, missing archive state in a malformed v2 packet, or unexpected fields in malformed legacy packets. Do not silently coerce those cases or expand this proposal into a validation redesign. Resolve them before implementation only if actual caller data makes them necessary; the specified valid representations can proceed independently.

## Observable acceptance criteria

1. `serialize(rows)` returns a JSON string. Parsing a representative nonempty result produces exactly a packet with numeric `version: 2` and `entries`, with each entry containing `id`, `title`, and `archived`; no legacy `items` collection is emitted.
2. Export preserves explicit `archived: true` and `archived: false`. An input row without `archived` exports `archived: false`.
3. Export and both import versions preserve a deliberately unsorted sequence of identifiers and the corresponding title values.
4. `deserialize(text)` accepts an independently written v2 JSON fixture and returns rows preserving both true and false archive values.
5. `deserialize(text)` accepts an independently written legacy v1 `items` fixture with no archive fields and returns the same ordered identifiers/titles with `archived: false` on every row. This must remain true after the current export constants change to v2.
6. Unsupported versions throw `TypeError`. Retain the version 99 check and cover another unsupported version adjacent to the supported range.
7. Empty export is observably `{ "version": 2, "entries": [] }` after JSON parsing; independent empty v1 and v2 imports both return `[]`.
8. A nonempty serialize/deserialize integration preserves ordered rows and normalizes missing archive state to false. This supplements the independent producer and consumer checks rather than replacing them.

Representative export expectation, defined independently of the implementation:

```json
{
  "version": 2,
  "entries": [
    { "id": "b", "title": "Second", "archived": true },
    { "id": "a", "title": "First", "archived": false },
    { "id": "c", "title": "Third", "archived": false }
  ]
}
```

Use input rows in that order, with the archive field absent on `a` and explicitly false on `c`. Use separate literal input fixtures for v1 and v2 imports; do not obtain all consumer test input from the serializer.

## Implementation and verification handoff

`planning/changes/document-v2/work.md` remains the sole task tracker. The table below maps the captured task IDs to necessary work and evidence; it does not create a second completion ledger. One implementation owner should coordinate this small, tightly coupled change and be the sole writer of the shared contract and tracking artifact.

| Existing task | Implementation work when authorized | Acceptance evidence |
| --- | --- | --- |
| 1.1 — Update producer and contract | Establish current and legacy wire identifiers in `contract.mjs`; update `serialize` in `producer.mjs` to emit v2 `entries`, include archive state, and apply the missing-value default without reordering rows. | Independent parsed-wire assertions for nonempty and empty output; string return type; true/false/default behavior and order. Criteria 1–3 and 7. |
| 1.2 — Update consumer | In `consumer.mjs`, explicitly accept v1 and v2, select the version-specific collection, normalize legacy archive state, retain v2 archive state, and reject unsupported versions with `TypeError`. | Literal v1/v2 fixtures covering multiple ordered rows and empty collections, plus unsupported-version assertions. Criteria 3–7. |
| 1.3 — Verify compatibility | Extend `exchange.test.mjs` using its existing `node:test` and strict assertions. Keep useful existing checks and add the independent boundary checks above plus a nonempty integration case. | Run `node --test exchange.test.mjs` from the project root and record the actual outcome and any unavailable checks. Criteria 1–8. |

Dependency order: settle the shared version contract first; complete both consumer compatibility and producer changes before claiming integration. If these components are released independently, deploy the consumer accepting v1/v2 before enabling v2 export. The supplied project does not establish deployment topology or whether other consumers exist, so this is a conditional rollout requirement, not a verified deployment plan.

Before future implementation, reconcile the checked work items with the observed missing behavior in the existing tracker, within that future authorized scope. Mark or retain completion only after the required implementation and verification evidence support it. Once the test command passes, inspect its coverage against these criteria; an all-done capture or an empty round trip alone is insufficient. Do not sync or archive as part of this planning request.

## Material limitations

This proposal is based on the supplied captures, requirements, tracker, and four JavaScript files. No CLI state was refreshed, no application tests were run, and no external consumer or deployment compatibility was verified. No repository revision metadata was supplied in the inspected project. The observed source/tracker discrepancy remains unresolved because all existing artifacts are preserved. The only requested addition is this proposal.
