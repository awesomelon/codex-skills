# Mutations

## Complete the cache update

Inspect existing mutation callbacks, request helpers, and shared cache handling before reporting missing updates. The absence of a local invalidation call is not enough evidence when the implementation is elsewhere.

Use the server response with immutable `setQueryData` updates when it contains the complete result needed by the affected cache entry. Invalidate results whose membership, order, count, or server-computed values remain unknown. A correct direct cache update does not also require an automatic refetch. Target the affected account and records, including other displayed results when their data changes.

Return or await the invalidation promise when mutation completion must include refreshing the UI. Keep essential cache updates in the mutation's configured callbacks or shared handling: callbacks passed to individual `mutate` calls depend on the observer still being mounted and may execute only for the latest consecutive call.

Use `mutateAsync` when the caller needs a promise and handle its rejection. In v5, mutation `isPending` indicates unfinished work; preserve duplicate-submission prevention and error feedback. `useMutationState` can track selected matching mutations across components; use an appropriate `mutationKey` when those components need to identify a particular group.

## Choose optimistic behavior deliberately

Optimistic UI is optional. Prefer showing pending variables in the affected UI when shared cache changes are unnecessary. Validate failure and retry behavior; do not make an unconfirmed write appear permanent.

For optimistic cache writes, cancel conflicting reads, capture the affected previous values, and update immutably. Return the information required to undo the specific write if it fails. Account for a cache miss: writing `undefined` with `setQueryData` is a no-op, not a way to delete a newly created optimistic entry.

Use installed callback types. In v5, the value returned by `onMutate` is the third argument to `onError` and `onSuccess`, but the fourth argument to `onSettled` after data, error, and variables. Newer versions also provide a separate context argument; do not confuse it with the saved previous values.

Restoring a whole-list snapshot can erase a later successful or still-pending write. Where writes can overlap, choose behavior that preserves other work: limit concurrency where the product permits it, undo only the affected change, or keep pending items in the UI. A same-scope queue for network mutations does not by itself prove that optimistic callbacks cannot overlap. Similarly, refetching after every completion can replace another pending optimistic result; decide when the affected group can safely refresh.

Mutation retries are off by default. Enabling retries or offline replay needs a write that can safely repeat, with server-side duplicate protection where required. A pending button alone does not guarantee exactly-once execution.

Official references: [Mutations and callback signatures](https://tanstack.com/query/v5/docs/framework/react/guides/mutations), [response updates](https://tanstack.com/query/v5/docs/framework/react/guides/updates-from-mutation-responses), [optimistic updates](https://tanstack.com/query/v5/docs/framework/react/guides/optimistic-updates), [invalidations from mutations](https://tanstack.com/query/v5/docs/framework/react/guides/invalidations-from-mutations).
