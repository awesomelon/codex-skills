# User latency and unnecessary work

Apply the upstream Vercel criteria for requests, bundles, clients, rendering, and JavaScript in the project's context. Attribution and exceptions are in [sources.md](sources.md).

## Requests and client caches

- Check dependencies between awaited operations first. Parallelize independent reads only; preserve authentication/authorization gates, prerequisite results, mutation ordering, and concurrency limits. Do not add a parallelization package for a simple dependency graph.
- Avoid starting expensive requests when a cheap synchronous condition already establishes that the work is unnecessary. Handle rejections from promises already started, including early-return and failure paths.
- Remember that the first rejection in `Promise.all()` does not cancel other requests. Distinguish screens that support partial success from operations requiring complete success.
- For duplicate requests, first inspect the keys, deduplication, refetching, and invalidation settings of existing TanStack Query, SWR, or router data features. Replacing the library with SWR or adding another cache layer is not the default solution.
- Include user, tenant, filter, and pagination dimensions that affect data in query keys and cache lifetimes. Check related data updates after mutations and isolation of prior data after logout or tenant switching.
- The absence of cache-update code in a component does not prove that no update path exists. If API adapters or shared mutation implementations are omitted, flag their contracts for verification. Separate paths directly established by supplied code from those requiring assumptions about internals.

## Initial transfer and bundles

- Use actual entry points and import graphs to check whether heavy editors, charts, or viewers are needed on the first screen. Use supported `React.lazy`, `import()`, or framework features for lazy loading, preserving loading, error, and retry UX.
- Use statically analyzable import paths. For barrel imports, check build output, externalization, tree shaking, and framework optimizations. Do not infer cost from path shape or bypass public APIs through internal `/dist/` paths. Verify subpath exports and types too.
- Check whether lazy loading delays required content or adds request stages. Limit hover/focus prefetching to likely features and balance it against bandwidth and memory.
- Delaying third-party scripts must preserve initial error collection and required execution order. `async` does not guarantee order. If CSS, images, or fonts are the bottleneck, JavaScript changes alone do not establish a fix.

## Rendering and subscription costs

- Start with broad subscriptions, unnecessary Effects, and expensive work repeated with the parent. Subscribe to the minimum state needed by the UI; consider reading event-only values at event time.
- Use `memo`, `useMemo`, and `useCallback` selectively for expensive calculations or boundaries that require referential stability. Do not wrap cheap expressions or every handler. Identify whether props, context, or state cause updates, and whether Compiler is actually enabled and applies to this code.
- Follow paths where new objects/functions reach downstream props or Effect dependencies on each render. A newly created default argument inside a memoized component does not prove that the component's props comparison always fails.
- Update input values immediately and use transitions or deferred values for expensive result rendering when appropriate. They do not automatically debounce/cancel network requests or move synchronous computation to a Worker.
- Network request state and transition pending state differ. In particular, React 18 `useTransition` alone cannot replace asynchronous mutation loading state. Even where async work is supported, preserve response ordering, errors, and duplicate-submission handling separately.
- For long lists, distinguish DOM count, layout/paint, and React computation before choosing virtualization or `content-visibility`. The latter does not remove DOM nodes or components. Verify scrolling, search, focus, accessibility, and target browser support.
- Avoid repeated interleaving of DOM writes and layout reads. When sharing global listeners is useful, check subscription counts and cleanup. Do not force passive listeners on wheel/touch handlers that need `preventDefault()`.

## JavaScript optimization and measurement

For paths with repeated searches, consider reducing computation through Map/Set or a single pass. Account for construction, memory, and key-update costs; do not replace readable small-list code with loops indiscriminately. Add module caches only with established keys, capacity, expiration, invalidation, and SSR isolation.

Distinguish development startup, production bundle size, request latency, render time, and DOM cost. Compare under the same input, build, and device conditions and record those conditions. Do not convert Strict Mode development render counts or upstream improvement multiples into measured user-facing improvements.
