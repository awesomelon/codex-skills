The application uses React 19 and @tanstack/react-query 5.90.2 with the framework's supported, safely escaped hydration transfer. There is no offline or persistence feature. The endpoint always derives the account from the server request. Different users may access the same server process concurrently. The product intentionally treats this account data as fresh for 60 seconds after the server fetch, including the first browser mount. Browser navigation retains one QueryClient. The account object may contain private user details.

```tsx
// server.tsx
import { QueryClient, dehydrate, HydrationBoundary } from '@tanstack/react-query';
const serverClient = new QueryClient();

export async function AccountPage({ request }) {
  await serverClient.prefetchQuery({
    queryKey: ['account'],
    queryFn: () => loadAccountFromRequest(request),
    staleTime: 60_000,
  });
  return <HydrationBoundary state={dehydrate(serverClient)}><Account /></HydrationBoundary>;
}

// browser.tsx; QueryClientProvider wiring is already correct
const browserClient = new QueryClient();

export function Account() {
  const { data } = useQuery({
    queryKey: ['account'],
    queryFn: () => fetch('/api/account').then(assertSuccessfulJson),
  });
  return <span>{data?.displayName}</span>;
}
```
