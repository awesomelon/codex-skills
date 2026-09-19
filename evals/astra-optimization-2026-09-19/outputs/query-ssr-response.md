Two concrete issues need changes:

1. **The server client can expose one account’s data to another request.** The module-level `serverClient` and shared `['account']` key let concurrent requests share an in-flight query. A later request within 60 seconds can also reuse the previous account’s fresh result without calling `loadAccountFromRequest` for the new request. That cached private account can then be dehydrated into the wrong response.

   Move client creation inside `AccountPage`, or use the framework’s request-scoped equivalent:

   ```tsx
   export async function AccountPage({ request }) {
     const serverClient = new QueryClient();
     // Existing prefetch and HydrationBoundary follow.
   }
   ```

   Adding an account identifier to the server key alone is insufficient: unrestricted `dehydrate(serverClient)` can include other accounts’ cached queries.

2. **The browser does not honor the intended 60-second freshness window.** Server-side query options are not transferred as browser query configuration. The browser query has the default `staleTime: 0`, so hydrated data is immediately stale and normally refetches on mount.

   Add the same freshness policy to its consumer:

   ```tsx
   const { data } = useQuery({
     queryKey: ['account'],
     queryFn: () => fetch('/api/account').then(assertSuccessfulJson),
     staleTime: 60_000,
   });
   ```

   Hydration preserves `dataUpdatedAt`, so this provides the remaining freshness period since the server fetch—not a new 60 seconds starting at browser mount. Mounting after that period should allow a refetch. Expiration itself does not schedule a request.

Keeping one browser client across navigation is appropriate. **Integration verification is still needed for authentication transitions:** if that client survives logout/login or account switching, `['account']` can retain the previous account’s data. Use matching account-scoped keys across server and browser, or clear account-dependent cache during the transition before rendering the next account. The excerpt does not establish whether such transitions occur.

The supplied framework transfer is already safely escaped; no serialization change is indicated. Separately, confirm that every field in the dehydrated account object is intended for the browser—safe escaping does not hide fields from its recipient.

Checks performed: static inspection of the supplied excerpt and package metadata, tracing client lifetime, query identity, prefetch reuse, hydration timestamps, and consumer freshness. No files changed, experiments or runtime checks run, external sources fetched, or dependencies installed. Request isolation and freshness behavior remain unverified in the integrated application.

Exact skill files read:

- `/private/tmp/astra-optimization-20260919/candidate-skills/tanstack-query-guard/SKILL.md`
- `/private/tmp/astra-optimization-20260919/candidate-skills/tanstack-query-guard/references/server-rendering.md`
- `/private/tmp/astra-optimization-20260919/candidate-skills/tanstack-query-guard/references/cache-and-keys.md`
