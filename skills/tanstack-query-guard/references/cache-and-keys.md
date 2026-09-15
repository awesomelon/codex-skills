# Cache and keys

## Identify the data

Use an array key whose values identify the returned data: resource, account or tenant when relevant, identifiers, filters, sort order, and pagination inputs. Keep credentials out of keys. `enabled` controls execution; it does not distinguish cached data for different inputs. Include the data dependencies, rather than arbitrary function references or transport settings.

Use stable JSON-compatible values. Object property order is ignored by the default hash, while array order matters. Convert dates or collection values deliberately when they represent request inputs. A successful `JSON.stringify` alone does not prove uniqueness: functions and `undefined` can disappear or collide. Keep ordinary and infinite query results under different keys because their cached values differ.

Follow existing key conventions. Shared `queryOptions` or key functions help when several callers must agree; a query count is not a reason to introduce a new package or reorganize all keys. Make prefix matching deliberate when updating or invalidating a family of queries.

## Decide when to read again

`staleTime` determines how long an observer treats data as fresh. Expiration alone does not start a request; refetch triggers such as mounting, focus, reconnect, polling, or explicit calls still matter. `gcTime` governs removal of unused cached queries, not freshness or active-query retention. Preserve defaults unless the task identifies different freshness or memory needs; sample durations are not requirements.

`staleTime: Infinity` still permits invalidation. On versions that support `staleTime: 'static'`, automatic refresh after invalidation is also suppressed; do not interchange these settings. Disabled queries also opt out of automatic refetch behavior. Check these options before claiming an invalidation guarantees new data.

Target invalidation to every affected result, including filtered lists and counts where applicable. Active matching queries normally refetch; inactive matching queries are marked for later refresh unless a different `refetchType` is chosen. Use `exact` only when excluding related keys is intentional. For choosing invalidation versus direct writes, see [Mutations](mutations.md).

## Seed or preview

`initialData` seeds the shared cache and participates in freshness calculations. Use complete, valid data, and preserve its known age with `initialDataUpdatedAt` when available. Partial list items and empty placeholders can otherwise masquerade as successfully fetched detail data.

`placeholderData` supplies observer-local preview content without writing it to the cache. It does not override disabled/offline execution or guarantee usable data after a fetch failure. Account for `isPlaceholderData` and the actual error state. When retaining previous data, prevent account or tenant changes from displaying the previous account's records.

Official references: [Query keys](https://tanstack.com/query/v5/docs/framework/react/guides/query-keys), [defaults](https://tanstack.com/query/v5/docs/framework/react/guides/important-defaults), [initial data](https://tanstack.com/query/v5/docs/framework/react/guides/initial-query-data), [placeholder data](https://tanstack.com/query/v5/docs/framework/react/guides/placeholder-query-data).
