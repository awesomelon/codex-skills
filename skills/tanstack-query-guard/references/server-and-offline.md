# Server and offline

## Server rendering

Keep server `QueryClient` instances isolated per request when they hold request/user data. Reuse the browser client across normal renders and navigation. Follow the framework's existing setup; account for initial Suspense rendering discarding a client created in component state before it commits.

Transfer prefetched cache data with the framework's supported `dehydrate` and `HydrationBoundary` integration, preserving keys and data timestamps. `dehydrate` produces a data structure, not HTML-safe text. Use the framework's safe transfer mechanism; do not inject user data into a script with plain `JSON.stringify`. Choose explicitly which data and errors may reach the browser. Successful queries are included by default; transferring pending queries depends on the installed version and streaming setup.

Configure freshness on the consuming browser query when immediate refetch is undesirable. Server-only `staleTime` does not set browser options. Preserve a deliberate browser refresh requirement. Server `gcTime` normally defaults to `Infinity`; do not introduce immediate collection that removes prefetched results before transfer. A numeric minimum from an example is not a timing guarantee.

Server-rendered values do not automatically update when the browser refetches. If both render the same information, define how they stay consistent. Do not add Next.js Server Components or change routers to solve a client-only request.

## Network availability and storage

The default `networkMode: 'online'` pauses work that requires connectivity. `'always'` is suitable for a query function that can run without a network, such as a local data read. `'offlineFirst'` allows an initial attempt, then pauses retries, fitting HTTP/service-worker caches. Choosing a mode does not itself provide persistent storage or make a server API available offline. Show paused work distinctly from active loading where users need that distinction.

Add persistence only for an actual requirement. When using the persistence package, coordinate restoration with query execution, commonly through `PersistQueryClientProvider`. Set `gcTime` to at least the intended persisted `maxAge`; choose `buster` and storage scope according to compatibility and account changes. Filter saved queries through supported `dehydrateOptions`, and do not invent a `hydrateOptions.shouldHydrate` option.

Exclude credentials and data that the storage must not retain. On sign-out/account changes, handle the persisted store as well as in-memory data. Reloading saved mutation state does not restore JavaScript functions: register the required default `mutationFn` by key before resuming paused mutations after restoration. Preserve server-side authorization and duplicate protection on replay.

Official references: [SSR](https://tanstack.com/query/v5/docs/framework/react/guides/ssr), [advanced server rendering](https://tanstack.com/query/v5/docs/framework/react/guides/advanced-ssr), [network mode](https://tanstack.com/query/v5/docs/framework/react/guides/network-mode), [persistence](https://tanstack.com/query/v5/docs/framework/react/plugins/persistQueryClient), [persisted mutations](https://tanstack.com/query/v5/docs/framework/react/guides/mutations#persisting-offline-mutations).
