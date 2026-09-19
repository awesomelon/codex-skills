# Offline and persistence

The default `networkMode: 'online'` pauses work that requires connectivity. `'always'` is suitable for a query function that can run without a network, such as a local data read. `'offlineFirst'` allows an initial attempt, then pauses retries, fitting HTTP/service-worker caches. Choosing a mode does not itself provide persistent storage or make a server API available offline. Show paused work distinctly from active loading where users need that distinction.

Add persistence only for an actual requirement. When using the persistence package, coordinate restoration with query execution, commonly through `PersistQueryClientProvider`. Set `gcTime` to at least the intended persisted `maxAge`; choose `buster` and storage scope according to compatibility and account changes. Filter saved queries through supported `dehydrateOptions`, and do not invent a `hydrateOptions.shouldHydrate` option.

Exclude credentials and data that the storage must not retain. On sign-out/account changes, handle the persisted store as well as in-memory data. Reloading saved mutation state does not restore JavaScript functions: register the required default `mutationFn` by key before resuming paused mutations after restoration. Preserve server-side authorization and duplicate protection on replay.

Official references: [network mode](https://tanstack.com/query/v5/docs/framework/react/guides/network-mode), [persistence](https://tanstack.com/query/v5/docs/framework/react/plugins/persistQueryClient), [persisted mutations](https://tanstack.com/query/v5/docs/framework/react/guides/mutations#persisting-offline-mutations).
