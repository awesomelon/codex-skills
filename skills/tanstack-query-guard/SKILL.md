---
name: tanstack-query-guard
description: Implement, review, and debug TanStack Query queries, mutations, and caching in React applications. Exclude generic React work and TanStack Router-only tasks.
---

# TanStack Query Guard

Keep cached server data correct across reads, writes, navigation, and failures. Adapt the relevant criteria from Deckard Gerritsen's TanStack Query skill to the requested work.

Review and explanation requests preserve files. Implementation requests include the needed edits and relevant verification. Start with the affected query, its consumers, and related cache writes; reuse existing query keys, options, request functions, and `QueryClient` setup.

The references target TanStack Query v5. Check the installed version and types when API support or callback arguments affect the change. Preserve v4 APIs in v4 projects unless migration is requested. Do not infer a need for TanStack Query from ordinary React data fetching, or introduce a router, persistence, or different data library just to follow an example.

## Choose the relevant detail

| Task | Read |
| --- | --- |
| Query identity, retention, refetches, initial or placeholder data | [Cache and keys](references/cache-and-keys.md) |
| Request failures, cancellation, parallel reads, subscriptions | [Requests and rendering](references/requests-and-rendering.md) |
| Saving data, cache updates, optimistic UI, concurrent writes | [Mutations](references/mutations.md) |
| Pagination, infinite lists, route loading, prefetching | [Pagination and prefetch](references/pagination-and-prefetch.md) |
| Server rendering, persisted caches, offline requests | [Server and offline](references/server-and-offline.md) |
| Attribution, upstream comparison, updating this skill | [Sources](references/sources.md) |

Read only what the current decision needs. A small query fix does not require server/offline guidance or another review skill. Use existing checks that exercise the changed cache or request behavior; distinguish code inspection from executed runtime checks and measured performance.
