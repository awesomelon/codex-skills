# Propose migrating sessions to Redis

Status: Proposed  
Recorded: 2026-10-07

Propose storing sessions in Redis so workers can share session state and application process restarts do not discard it. This proposal awaits approval; the current implementation is unchanged and rollout remains pending.

The [session requirements](../../context.md) call for shared sessions that survive process restarts. The [current implementation](../../sessions.py) stores sessions in a process-local dictionary, which cannot satisfy those requirements across independent workers or restarts. No record of the original store's rationale is available; this ADR does not infer one.

Redis would move session state outside application processes and provide a common store for workers. This recommendation assumes that “process restarts” means application process restarts. If sessions must also survive Redis restarts or failures, the required durability and acceptable data loss must be agreed before accepting the proposal.

The migration would add a network and operational dependency to session access. Approval should settle session lifetime and expiration requirements, and the expected behavior when Redis is unavailable; neither is specified in the supplied requirements. These decisions determine whether the proposed store meets the session contract. Rollout remains pending and requires a separate plan for existing in-process sessions.
