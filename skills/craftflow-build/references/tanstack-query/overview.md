# TanStack Query engineering

These references target v5. Check installed versions and callback types when support matters; retain v4 APIs unless migration is requested. Reuse existing keys, options, requests, and QueryClient setup. Keep definitions together when they share a reason to change. Do not introduce Query, a router, or persistence for ordinary data fetching alone.

| Decision | Reference |
| --- | --- |
| Keys, freshness, retention, initial/placeholder data | [Cache and keys](cache-and-keys.md) |
| Failures, cancellation, parallel reads, subscriptions | [Requests and rendering](requests-and-rendering.md) |
| Saving, invalidation, optimistic UI, overlapping writes | [Mutations](mutations.md) |
| Pagination, infinite lists, loaders, prefetching | [Pagination and prefetch](pagination-and-prefetch.md) |
| Request-scoped clients and hydration | [Server rendering](server-rendering.md) |
| Network modes and persisted state | [Offline and persistence](offline-and-persistence.md) |
| Attribution | [Sources](sources.md) |

Start with the affected query, its consumers, and related cache writes. Load only relevant details and verify the changed request/cache behavior; inspection is distinct from runtime evidence or measured performance.
