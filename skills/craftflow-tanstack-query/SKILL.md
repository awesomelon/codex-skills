---
name: craftflow-tanstack-query
description: Design, implement, review, and debug TanStack Query queries, mutations, and caching in React applications. Exclude generic React work and TanStack Router-only tasks.
---

# CraftFlow TanStack Query

Keep cached server data correct and shared query definitions easy to extend across readers and writers. Adapt the relevant criteria from Deckard Gerritsen's TanStack Query skill to the requested work.

For planning, review, or explanation, preserve the assessed material and write only requested deliverables. Implementation requests include the needed edits and relevant verification. Start with the affected query, its consumers, and related cache writes; reuse existing query keys, options, request functions, and `QueryClient` setup.

Keep query keys, requests, options, and cache writes together when they share a reason to change. Split for independent responsibilities or required execution environments, not file length.

The references target TanStack Query v5. Check the installed version and types when API support or callback arguments affect the change. Preserve v4 APIs in v4 projects unless migration is requested. Do not infer a need for TanStack Query from ordinary React data fetching, or introduce a router, persistence, or different data library just to follow an example.

## Choose the relevant detail

| Task | Read |
| --- | --- |
| Shared query definitions, identity, retention, refetches, initial or placeholder data | [Cache and keys](references/cache-and-keys.md) |
| Request failures, cancellation, parallel reads, subscriptions | [Requests and rendering](references/requests-and-rendering.md) |
| Saving data, cache updates, optimistic UI, concurrent writes | [Mutations](references/mutations.md) |
| Pagination, infinite lists, route loading, prefetching | [Pagination and prefetch](references/pagination-and-prefetch.md) |
| Request-scoped clients, server prefetching, hydration | [Server rendering](references/server-rendering.md) |
| Network modes, persisted caches, restoring mutations | [Offline and persistence](references/offline-and-persistence.md) |
| Attribution, upstream comparison, updating this skill | [Sources](references/sources.md) |

Read only what the current decision needs. A small query fix does not require server/offline guidance or another review skill. Use existing checks that exercise the changed cache or request behavior; distinguish code inspection from executed runtime checks and measured performance.
