# Work

- [x] Export v2 and shared contract: version 2, entries, archived defaults to false.
- [x] Import v1/v2: legacy items and v2 entries normalize to id/title/archived rows.
- [x] Verify integrated compatibility: `node --test exchange.test.mjs` — 8 passed, 0 failed.

The previously timed-out exporter worker was stopped through its project-local
control. Its acknowledgement confirms it stopped before writing, and no late-write
marker exists. Ownership transferred only after that acknowledgement. The
coordinator separately confirmed the managed worker session exited with code 0.

Verification covers the exact serialized v2 contract, both import formats,
populated and empty round trips, legacy-to-v2 conversion, row order, Unicode,
archived values/defaults, caller-data preservation, and unsupported versions.
The expanded suite exposed five expected failures before implementation.

No remaining work or active writers. Unrelated notes and processes were preserved.
