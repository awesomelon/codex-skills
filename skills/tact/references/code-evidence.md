# Code evidence

Apply these defaults to TypeScript and JavaScript code within the requested scope. In implementation, use the supported alternative; in review, identify the lost information, unnecessary work, or policy violation without editing files. An existing project contract takes precedence. Explain a necessary exception and keep it at the smallest boundary; do not use an exception to evade a failing check.

## Preserve precise contracts

- Keep inferred keys, discriminants, and concrete values. Do not widen a known value to `unknown`, `any`, `object`, an anonymous object, or an open dictionary and then narrow or assert it back. Use inference, a precise type, or `satisfies` where appropriate. Do not send already-validated values through an `unknown` predicate without a new source of uncertainty.
- Internal function inputs and outputs should express the domain contract. Avoid the broad `object` parameter type, `unknown` returns including `Promise<unknown>`, and aliases that merely hide `unknown`. Named object parameters with meaningful fields are fine; this is about loss of type information, not positional versus named arguments.
- Avoid dictionaries whose values are unconstrained `any`, `unknown`, `object`, or `{}`. Use a domain value type, finite keys, or a defined recursive JSON type when the protocol really permits arbitrary JSON. Generic constraints and fresh typed accumulators are different from erasing a known value.
- Use domain names for locally owned symbols instead of `Shape` decorations that say little about their role. Preserve names owned by an external API, such as a schema's `.shape` property.

## Parse at the boundary

Keep unchecked data at the external-input boundary and return a validated domain value or an explicit failure. Use the project's schema/parser when present. In a schema-free project, a focused predicate or parser can contain the necessary `typeof` and property checks; do not spread repeated type inspection through trusted application code. An environment-existence probe such as `typeof window === "undefined"` serves a different purpose.

`unknown` is justified for actual unparsed input, an error cause, or a relevant generic constraint. That exception does not permit broad internal contracts or opaque return types. Do not add a schema dependency for a trivial boundary, remove necessary validation, or pretend a generated declaration checks an external payload.

Use typed property access and direct function calls instead of `Reflect.get` or `Reflect.apply`. If a foreign dynamic API requires reflection, isolate it in a narrow adapter, establish the required runtime facts, and expose a precise contract to callers.

## Require evidence for assertions

Do not fabricate compatibility with chained assertions, including `as unknown as T` or intermediate `object` casts. Correct the type relationship or validate the input. Literal preservation through `as const` is distinct from asserting an unchecked value into a domain type.

For each necessary non-const assertion, put a nearby explanation of the specific invariant and where it was established, using the project's comment convention. A generic "safe" comment is not evidence. If the invariant cannot be explained, repair the contract rather than adding a cast or silencing the diagnostic.

## Construct values without hidden costs

- Avoid repeated copies of a growing accumulator, including spread, `concat`, `slice`, and `Object.assign({}, accumulator, ...)` inside reductions. Use a fresh locally owned accumulator or a suitable collection constructor; preserve order, duplicate-key behavior, and caller-owned state.
- Prefer a suitable single collection pass over adjacent eager `filter`/`map` passes in new code. Lazy iterator pipelines are an option only when the target runtime supports them. Before rewriting existing code, account for callback order, indexes, sparse arrays, `thisArg`, and truthiness. If a single pass changes required behavior, preserve the semantics and explain the constraint. Fewer allocations alone do not prove a measured speedup.
- Avoid conditional empty-object spreads that obscure optional-field construction. Use explicit branches or typed construction. Preserve the difference between an absent property and a property whose value is `undefined`; do not mechanically substitute one for the other.

## Keep dependencies and layout understandable

Test through real dependency seams rather than replacing entire modules with Jest/Vitest module mocks. Use a small injected dependency, an existing adapter, or an isolated integration fixture when appropriate. Do not build a dependency-injection framework just for a test. Keep unavoidable legacy mocking localized and state what integration remains untested.

Separate top-level declarations and meaningful multiline/control-flow blocks with readable spacing. Keep compact related bindings, import groups, documentation attachment, and overload groups intact. Use the established formatter and avoid unrelated whitespace churn.

For code in a project that directly uses Effect, read [Effect conventions](effect-code.md) for its construction, matching, and service boundaries. Do not introduce Effect into another project or infer its use solely from a transitive dependency.

These are authoring and review defaults. Respect the project's executable rules, but do not install a new linter or change repository policy merely because this reference was loaded. When enforcement changes are requested, use existing tooling and preserve local configuration; instruction text by itself is not automated enforcement.
