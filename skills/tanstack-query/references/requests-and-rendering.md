# Requests and rendering

## Failures and cancellation

A query function must return data or reject. Native `fetch` resolves for HTTP errors, so check the response status before accepting its body. Follow the existing request client's error representation rather than assuming every error exposes `status`. Do not turn a failed request into successful empty data to suppress an error state.

Forward the query function's `signal` through supported request functions when cancellation is required. An unused request can finish and populate the cache if the signal is not consumed; changing `enabled` to `false` alone does not cancel an ongoing request. Explicit `cancelQueries` cancels the query, and aborts the transport when it uses the signal. Account for other observers of the same key. The v5 Suspense hooks have cancellation limitations; do not promise identical behavior to `useQuery`.

Distinguish initial absence of data, background refresh, terminal errors, and paused requests. A background error need not replace previously successful data. Choose inline error UI or `throwOnError`/Suspense handling according to the existing screen; use `QueryErrorResetBoundary` or `useQueryErrorResetBoundary` when the retry UI needs to reset query errors.

Query retry defaults differ between browser and server execution. Respect application-specific transient/permanent error distinctions and rate limits. Do not increase retries to conceal authentication or validation failures. Mutation retry has different defaults and requires replay-safe writes; see [Mutations](mutations.md).

## Concurrent reads

Independent fixed queries can run together. Use `useQueries` for a variable set, and preserve genuine dependencies such as an identifier obtained from a previous result. Do not call query hooks inside a changing loop. In Suspense code, use supported parallel-query APIs such as `useSuspenseQueries` where ordinary sequential suspension would delay the other reads.

## Subscription cost

`select` changes an observer's result without replacing the cached original. Keep it pure; sorting cached arrays in place also changes other consumers. It runs again when the cached data or the selector function reference changes. Stabilize an expensive selector when that matters, keeping all changing inputs in its dependencies; a trivial selector does not require extra memoization.

Keep default `structuralSharing` and accessed-property tracking unless the data format or a measured cost justifies a change. Object rest destructuring reads all result properties and broadens updates. A manual `notifyOnChangeProps` list must include every property the UI needs, including error/pending information; a shorter list can silently suppress required UI updates. Do not depend on the entire query result object having stable identity.

Official references: [Query functions](https://tanstack.com/query/v5/docs/framework/react/guides/query-functions), [cancellation](https://tanstack.com/query/v5/docs/framework/react/guides/query-cancellation), [parallel queries](https://tanstack.com/query/v5/docs/framework/react/guides/parallel-queries), [render optimizations](https://tanstack.com/query/v5/docs/framework/react/guides/render-optimizations).
