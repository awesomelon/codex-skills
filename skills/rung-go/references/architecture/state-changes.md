# Retried and concurrent state changes

Use this guidance when an operation can repeat, stop after a partial write, or overlap another writer. Start from the intended effects and existing ownership; ordinary read-only or local edits need no recovery audit. Assessment can identify a failure window and propose a check without changing code or running it.

## Repetition and partial completion

Identify what makes two attempts the same logical operation and which durable state records its outcome. Trace a consequential interruption between effects and completion recording. Reaching the same final record is not enough if a retry also duplicates a notification, charge, or other external effect.

Reuse the existing transaction, operation key, conditional write, or recovery mechanism when it covers the actual failure window. A completion flag written after an effect leaves a replay gap; writing it first can lose the effect. When the effect and record cannot commit together, establish how an uncertain outcome is queried, deduplicated, resumed, or compensated before retrying. Do not promise exactly-once execution from a local flag or assume every operation can safely repeat.

For authorized implementation, check a repeated request and an interruption at the relevant persistence or effect boundary using disposable state. Observe the required effects as well as the final state. Select failure points that could invalidate the repair rather than attempting every instruction boundary. Preserve unrelated or still-owned state during recovery; uncertainty about ownership is not permission to remove it.

## Shared writers

Determine whether writers publish independent facts or maintain one invariant together. Independent progress records may belong in separate owned files or keys with aggregation on read. Separate fields in one read-modify-write document still share a write target. Splitting state is useful only if consumers do not require an atomic view of the combined values.

When a shared invariant is real, retain its owner and use the supported transaction, conditional update, serialization, or locking mechanism across all relevant writers. A process-local queue cannot coordinate other processes. Judge a lock by the invariant and failure behavior it protects, not by its presence alone.

Choose an overlapping execution that could lose a write or violate the invariant, and check both writers' effects. Where practical, control the interleaving rather than depending on timing. A serial passing run does not establish concurrency correctness; a separated-state design still needs verification at the consumer that combines it.
