# ADR-0001: Migrate sessions to Redis

Status: Proposed
Recorded: 2026-10-07

## Context

[Session requirements](../../context.md) state that sessions should survive application process restarts and be shared across workers. Approval and rollout of a Redis migration are pending.

The current [implementation](../../sessions.py) stores sessions in the process-local `SESSIONS` dictionary. `get_session(session_id)` returns the stored value, or `None` when the key is absent. The dictionary does not provide shared storage across workers or retain its contents after its process exits. No record is available explaining why the original in-process store was chosen; this proposal does not infer that rationale.

## Proposed decision

Use Redis as the shared session store, with application workers reading and writing sessions in the same Redis deployment. Keeping session data outside the application processes would allow sessions to remain available across application restarts, provided Redis retains the data and remains reachable.

This is a recommendation awaiting approval. It does not authorize implementation or rollout. The current implementation remains unchanged.

## Alternative considered

Retaining the current in-process dictionary avoids adding a separate service and network access, but does not satisfy the stated restart and worker-sharing requirements. This comparison explains the proposed change; it is not a claim about the original decision or a completed rejection by the approval process. No other alternatives have been evaluated in the supplied evidence.

## Expected consequences and unresolved decisions

Redis would provide a common session store for all workers and separate session lifetime from application process lifetime. It would also introduce a service to operate and a network dependency on session access. Redis unavailability must be distinguishable from an absent session; silently falling back to per-process storage would lose the required shared behavior.

Before implementation, agree on session serialization, key naming, expiration and renewal behavior, access controls, and how callers handle unavailable storage. Preserve the observed missing-session behavior unless a contract change is separately approved. The supplied code contains no session creation, update, deletion, or expiration paths, so their contracts remain to be established.

Survival of Redis restarts, failover, or data loss is a separate durability question. Persistence, retention, eviction, recovery requirements, and the acceptable operational cost need agreement; selecting Redis alone does not establish those guarantees.

## Approval and rollout gates

Approval is pending. Once the proposal and unresolved contracts are agreed, implementation can be planned separately. The rollout plan must decide how to handle existing in-process sessions, mixed worker versions, rollback, and any resulting reauthentication.

Before rollout, verify that a session created through one worker can be read through another and remains available after application processes restart. Verify the agreed missing-session, expiration, and Redis outage behavior as well. These are proposed acceptance checks; no migration, rollout, or Redis integration validation has been performed for this ADR.
