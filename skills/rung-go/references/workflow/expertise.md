# Expertise boundaries

Choose references for the decision that remains unresolved. Technical topics are not separate installed skills. Use the [build reference library](../../SKILL.md#load-only-the-expertise-needed) to locate domain guidance. Optional Get Set resources are resolved through the current catalog, never assumed sibling folders. Reading a reference does not change the task's scope.

| Decision | Relevant expertise | Boundary with adjacent work |
| --- | --- | --- |
| Module ownership, dependency direction, or a producer/consumer contract | Architecture | Establish the affected contract and its consumers; let implementation expertise handle internal details. |
| Shared business policy or the cost of the next change | Code quality | Diagnose what should improve and which rules change together; reuse the diagnosis during implementation. |
| React composition, hooks, or interaction state | React quality | Own component behavior and state lifetime; use cache expertise when remote-state behavior is the unresolved issue. |
| Query keys, invalidation, mutations, or server-state lifecycle | TanStack Query | Own cache/request semantics; coordinate with the affected UI and API contract instead of reviewing every component. |
| Type relationships, narrowing, or runtime input validation | TypeScript quality | Own type guarantees and the runtime trust boundary; a TypeScript filename alone does not require a separate pass. |
| Carrying out a behavior-preserving structural change | Refactoring | Execute or assess a chosen structural change without repeating the quality audit; preserve behavior and keep bug fixes within authorization. |

For example, a React screen consuming a changed API may need an agreed wire contract, runtime validation, and a cache transition. One implementation owner can consult several reference areas. Assign separate work only where its outcome can be checked independently; the coordinator accepts the assembled API-to-cache-to-UI behavior.

When recommendations overlap, state the shared decision once and retain its evidence. A local simplification that removes required compatibility is not an acceptable refactor; a passing type check does not demonstrate runtime input validity. Resolve the actual tradeoff against the user's contract and source behavior. Escalate a missing product decision only when it changes the result and cannot be settled from the available evidence.

A small edit or a standalone domain review can finish with its relevant expertise alone. Get Set assesses and Go executes; either can be used directly.
