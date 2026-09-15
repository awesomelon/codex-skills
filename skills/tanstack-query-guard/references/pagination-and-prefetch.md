# Pagination and prefetch

## Pages and infinite lists

For page-by-page queries, put the page/cursor and filters in the query key. In v5, `placeholderData: keepPreviousData` can retain the previous result while a new page loads; account for `isPlaceholderData` before enabling navigation that depends on the new result. Keep tenant/account changes from retaining another account's preview.

For `useInfiniteQuery`, provide `initialPageParam`, read `pageParam` in the query function, and derive `getNextPageParam` from the API's cursor or paging semantics. Return `undefined` or `null` at the end. Keep both `pages` and `pageParams` aligned when manually updating an infinite result. Do not share the same key with an ordinary query.

Repeated loading triggers can conflict with background refetches as well as the next-page request. In the usual case, gate `fetchNextPage` with `hasNextPage && !isFetching`; checking only `isFetchingNextPage` misses background refresh. If overlapping requests are intentional, verify the installed `cancelRefetch` behavior and which result the UI should retain.

Use `maxPages` only when retained pages or refetch cost warrant eviction. Derive subsequent cursors from the API or the actual `lastPageParam`, not the number of retained pages. When users must revisit evicted pages, supply the required previous-page calculation and preserve expected scrolling behavior. A fixed page cap is not universally required.

## Choose a loading API by its promise

| API | Cached data and errors |
| --- | --- |
| `prefetchQuery` | Warms the cache; returns no data and does not reject on a query failure. |
| `fetchQuery` | Returns data fresh enough for its `staleTime`, fetching when necessary; rejects on failure. |
| `ensureQueryData` | Returns existing data even when due for refresh; fetches and rejects on failure only when data is missing. |

With `revalidateIfStale: true`, `ensureQueryData` can return cached data immediately and start a background refresh. It does not wait for fresh data. Choose `fetchQuery` when navigation or a decision requires the refreshed result, rather than treating every loader as cache-first.

Reuse matching keys and options between preloaders and consumers. A `staleTime` passed only to prefetch does not set the consumer's freshness policy. Keep immediate background refresh if the product requires it; otherwise configure the consuming query accordingly. Prefetch likely next reads when latency warrants it, respecting authorization and network cost. Use the project's existing router and include keyboard focus when adding intent-based prefetching.

Official references: [Infinite queries](https://tanstack.com/query/v5/docs/framework/react/guides/infinite-queries), [paginated queries](https://tanstack.com/query/v5/docs/framework/react/guides/paginated-queries), [prefetching](https://tanstack.com/query/v5/docs/framework/react/guides/prefetching), [QueryClient implementation](https://github.com/TanStack/query/blob/main/packages/query-core/src/queryClient.ts).
