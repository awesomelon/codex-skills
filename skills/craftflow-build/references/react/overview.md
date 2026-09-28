# React engineering

Preserve repository conventions and supported React APIs. Check versions/types when API support matters and Compiler/build configuration when memoization or bundles are at issue. Do not assume Next.js or introduce a new data library for a local change. Keep a component's state, handlers, and rendering together when they change together; split for actual independent behavior, reuse, or verification rather than file length.

| Decision | Reference |
| --- | --- |
| State, Effects, hooks, forms, component identity | [Correctness](react-correctness.md) |
| Variants, children, render props, compound components, providers | [Composition](composition.md) |
| Requests, caches, bundles, rendering and subscriptions | [Performance](performance.md) |
| Actual SSR/RSC, server functions, hydration | [Server React](server-react.md) |
| Attribution or upstream comparison | [Sources](sources.md) |

Prioritize correctness, isolation, and compatibility. Do not weaken Hooks/type rules or add memoization to meet a count. Verify changed interactions under the reproduction conditions; performance claims need comparable measurements. Preserve Korean IME, focus, labels, and keyboard behavior where affected. Styling-only, wording-only, and React Native work do not require these references.
