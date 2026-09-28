# Expertise boundaries

Choose expertise for the decision that remains unresolved. The available catalog is authoritative; the names below describe common capabilities, not required installations or an invocation order. Resolve a matching skill through its advertised resource, including any plugin prefix. Do not assume sibling folders exist in a standalone installation.

| Decision | Relevant expertise | Boundary with adjacent work |
| --- | --- | --- |
| Module ownership, dependency direction, or a producer/consumer contract | Architecture | Establish the affected contract and its consumers; let implementation expertise handle internal details. |
| Shared business policy or the cost of the next change | Code quality | Identify rules that change together; preserve similar-looking rules with independent reasons to change. |
| React composition, hooks, or interaction state | React quality | Own component behavior and state lifetime; use cache expertise when remote-state behavior is the unresolved issue. |
| Query keys, invalidation, mutations, or server-state lifecycle | TanStack Query | Own cache/request semantics; coordinate with the affected UI and API contract instead of reviewing every component. |
| Type relationships, narrowing, or runtime input validation | TypeScript quality | Own type guarantees and the runtime trust boundary; a TypeScript filename alone does not require a separate pass. |
| Carrying out a behavior-preserving structural change | Refactoring | Establish preserved behavior and reversible steps; broader redesign or bug fixing needs the task's authorization. |

For example, a React screen consuming a changed API may need an agreed wire contract, runtime validation, and a cache transition. One implementation owner can apply several skills. Assign separate work only where its outcome can be checked independently; the coordinator accepts the assembled API-to-cache-to-UI behavior.

When recommendations overlap, state the shared decision once and retain its evidence. A local simplification that removes required compatibility is not an acceptable refactor; a passing type check does not demonstrate runtime input validity. Resolve the actual tradeoff against the user's contract and source behavior. Escalate a missing product decision only when it changes the result and cannot be settled from the available evidence.

A small edit or a standalone domain review can finish with its relevant expertise alone. Packaging several skills together does not make the coordinator a required gateway.
