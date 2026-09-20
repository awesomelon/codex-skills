# Saved implementation response

Implemented v2 exports and imports with archive state, while retaining v1 imports with `archived: false`.

`node --test exchange.test.mjs` passes all 8 tests, covering exact wire output, archive defaults, ordering, both input versions, round trips, Unicode, immutability, and unsupported-version errors. Before implementation, the expanded suite exposed 5 failures.

Updated current-behavior.md and work.md with verified behavior and actual evidence. Confirmed notes.txt remained byte-for-byte unchanged.

The original response linked the two files in the temporary workspace; those links are omitted here. Their exact final contents are retained in [implementation.patch](implementation.patch). Agent-reported red/green results are distinct from the parent's withheld checks.
