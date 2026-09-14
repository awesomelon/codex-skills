# Sources and adaptation

Checked: 2026-09-12.

## Upstream baseline

- User-provided [Vercel React Best Practices AGENTS.md](https://github.com/vercel-labs/agent-skills/blob/main/skills/react-best-practices/AGENTS.md).
- Authoring baseline: [AGENTS.md at the pinned commit](https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/react-best-practices/AGENTS.md), commit `063bee94c3f4df8453406c830b0a7df0f2860278`, file blob `4e340a50684a8e7811d5bfa4df48bd9989d0fd87`.
- Attribution: Vercel Engineering. The original [SKILL.md](https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/react-best-practices/SKILL.md) declares an MIT license.

This skill is not an official Vercel distribution. It does not bundle the complete upstream document or examples. It adapts the decision criteria and adds correctness and verification conditions; the original Korean adaptation is now available in English. Upstream changes are not applied automatically.

## Upstream areas and local references

| Upstream area | Local coverage |
| --- | --- |
| 1. Eliminating Waterfalls | Request dependencies in [performance.md](performance.md) |
| 2. Bundle Size Optimization | Initial transfer and public import paths in [performance.md](performance.md) |
| 3. Server-Side Performance | Runtime, caching, and server boundaries in [server-react.md](server-react.md) |
| 4. Client-Side Data Fetching | Existing data layers and subscriptions in [performance.md](performance.md) |
| 5. Re-render Optimization | State/Effects in [react-correctness.md](react-correctness.md) and rendering costs in performance.md |
| 6. Rendering Performance | UI costs in performance.md and hydration in server-react.md |
| 7. JavaScript Performance | Computational cost and cache lifetimes in [performance.md](performance.md) |
| 8. Advanced Patterns | Effect Events and app lifetimes in [react-correctness.md](react-correctness.md) |

## Criteria not generalized verbatim

- `SWR`, `better-all`, and LRU are upstream implementation choices. Do not force new dependencies when the existing data layer and standard promises meet the requirements.
- A barrel file is not inherently a defect. Upstream section 2.1 distinguishes framework import optimization and subpath type support.
- Apply section 5.5's default-argument stability advice to downstream passing and dependencies. Do not confuse comparison of omitted props at a memo boundary with default-value creation after the component begins executing.
- Follow section 8.1 and React documentation by excluding Effect Events from dependencies. Do not interpret section 8.3's 'stable reference' wording as a general callback-stability guarantee.
- Consider transition-based network loading, new React APIs, and hydration suppression only when version, semantics, and the actual problem match. Upstream numbers are not measurements from this project.

## Official documentation used for additions

- [React: You Might Not Need an Effect](https://react.dev/learn/you-might-not-need-an-effect) — derived values, events, and external synchronization.
- [React: Preserving and Resetting State](https://react.dev/learn/preserving-and-resetting-state) — component identity, keys, and state preservation.
- [React: memo](https://react.dev/reference/react/memo) — props comparison and Compiler applicability.
- [React: useEffectEvent](https://react.dev/reference/react/useEffectEvent) — call sites, reactive values, and dependency restrictions.
- [React 18: useTransition](https://18.react.dev/reference/react/useTransition) and [current documentation](https://react.dev/reference/react/useTransition) — async support differences and the meaning of input/request state.
- [React: cache](https://react.dev/reference/react/cache) — RSC request scope.
- [TanStack Query: Query Keys](https://tanstack.com/query/latest/docs/framework/react/guides/query-keys) — data identity and dependencies.
- [Next.js: Data Security](https://nextjs.org/docs/app/guides/data-security) — server functions and data boundaries.

Current documentation may differ from installed versions. Prefer documentation and types for the target version when applying an API. Reading this reference is not a reason to upgrade unrelated dependencies.

Maintain the skill's structure using the user-specified [OpenAI article on rethinking skills and prompts](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra): concise discovery metadata, relevant references, and outcome-oriented decision criteria.
