## Findings

1. **[P1] Detail cache keys omit the tenant.**
   [records.tsx:10](../fixtures/review/records.tsx#L10) and [records.tsx:21](../fixtures/review/records.tsx#L21) identify records only by ID. Since tenants can share IDs, their detail queries collide, and saving one tenant’s record overwrites the shared entry. The 60-second freshness window can also allow another tenant’s cached record to display without a new request.
   **Remedy:** Use a shared key function returning `['records', tenantId, 'detail', recordId]` for both reads and writes. The `detail` segment keeps detail entries distinct from the infinite-page cache.

2. **[P2] Loading more can interrupt a background refresh.**
   [records.tsx:34](../fixtures/review/records.tsx#L34) checks only `isFetchingNextPage`, which is false during a background refresh. Calling `fetchNextPage()` then can cancel that refresh under the default behavior and use the existing, potentially outdated server cursor, risking inconsistent pages.
   **Remedy:** Gate loading with:
   ```tsx
   if (result.hasNextPage && !result.isFetching) {
     void result.fetchNextPage()
   }
   ```

The full save response supports the direct `setQueryData` update; the stated consumers do not require additional list/count invalidation. The infinite query’s initial parameter and `null` terminal cursor are valid for v5.

Review used the supplied skill and relevant references. No files changed; no runtime checks executed.
