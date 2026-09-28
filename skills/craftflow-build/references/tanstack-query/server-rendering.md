# Server rendering

Keep server `QueryClient` instances isolated per request when they hold request/user data. Reuse the browser client across normal renders and navigation. Follow the framework's existing setup; account for initial Suspense rendering discarding a client created in component state before it commits.

Transfer prefetched cache data with the framework's supported `dehydrate` and `HydrationBoundary` integration, preserving keys and data timestamps. `dehydrate` produces a data structure, not HTML-safe text. Use the framework's safe transfer mechanism; do not inject user data into a script with plain `JSON.stringify`. Choose explicitly which data and errors may reach the browser. Successful queries are included by default; transferring pending queries depends on the installed version and streaming setup.

Configure freshness on the consuming browser query when immediate refetch is undesirable. Server-only `staleTime` does not set browser options. Preserve a deliberate browser refresh requirement. Server `gcTime` normally defaults to `Infinity`; do not introduce immediate collection that removes prefetched results before transfer. A numeric minimum from an example is not a timing guarantee.

Server-rendered values do not automatically update when the browser refetches. If both render the same information, define how they stay consistent. Do not add Next.js Server Components or change routers to solve a client-only request.

Official references: [SSR](https://tanstack.com/query/v5/docs/framework/react/guides/ssr), [advanced server rendering](https://tanstack.com/query/v5/docs/framework/react/guides/advanced-ssr).
