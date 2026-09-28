# When SSR, RSC, or Next.js applies

Apply this reference only to actual server-rendering or server-function paths. It is not a reason to introduce this architecture into a Vite SPA. Upstream and official documentation are in [sources.md](sources.md).

## Data and server boundaries

- Client-callable server mutations must verify authentication and resource authorization on their actual execution paths. Hiding a button in a page or layout is not a substitute.
- Keep request/user data within its render/request lifetime. Do not use mutable server-module variables or browser-oriented singletons as shared state across requests. Distinguish immutable static configuration and intentionally designed shared caches.
- Use `React.cache()` for its intended RSC request-scoped deduplication. It is neither a general client-hook cache nor a cache across requests. For persistent caching, first establish authorization/tenant scope of keys, expiration, invalidation, and process/deployment behavior. Do not add an LRU dependency by default.
- Send only the public data needed in RSC-to-client props. Compare reduced duplicate-object transfer against total transfer size and added client computation. Do not transmit unnecessary source data merely to keep object references stable.

## Loading and rendering

- Consider structures that start independent data dependencies in parallel. Use Suspense with supported data sources and meaningful loading boundaries. Wrapping an ordinary Effect fetch does not make it Suspense-aware.
- Check data, time, IDs, and environment access so server HTML matches the initial client render. Consider both server availability and hydration when initializing from `localStorage`.
- Do not use `suppressHydrationWarning` or pre-render DOM mutation scripts as generic fixes. Keep unavoidable exceptions narrow. When a script is necessary, verify actual constraints including server markup, safe value handling, and CSP.
- Use `next/dynamic`, `after()`, Activity, and React DOM resource hints only when the installed version, router, runtime, and semantics support them. Prefer existing framework capabilities.
- Before moving work after the response, check whether it is part of a completion guarantee, such as essential persistence, authorization, or audit records. Do not downgrade guaranteed work to best-effort side effects as a simple performance optimization.

Check server rules only as far as the changed execution path requires. Do not turn a client review into a server redesign or an unrelated backend-wide audit.
