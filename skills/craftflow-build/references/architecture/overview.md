# Architecture during implementation

Judge actual change cost and failure risk rather than folder shape. Keep responsibilities that change for the same reason close, and preserve policies that change independently. Inspect dependency paths through public entrypoints, events, callbacks, shared state, and network calls as well as imports. Respect explicit repository boundaries; do not apply DTOs, services, DDD, or FSD uniformly.

Inspect actual consumers when changing APIs, types, caches, or events. Preserve authorization, tenant isolation, concurrency, and transaction invariants. Use [boundary contracts](contracts.md) for independently consumed interfaces and rollout compatibility. A local function edit with no changed boundary needs no separate architecture pass.

Prefer maintainability and readable changes over low LOC or a minimal diff. Extract a module only when the benefit outweighs navigation and coordinated edits. Correct existing documentation made inaccurate by the change; create new records only when useful and in scope. For design uncertainty, plan's architecture preflight is optional supporting guidance.
