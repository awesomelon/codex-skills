# Narrow and construct before asserting

- Prefer the narrowing that matches the value: a discriminant for variants, `typeof` for primitives, `instanceof` for actual class instances, and `in` for property presence. Presence alone does not prove the property's value type; optional properties may occur in both results of an `in` check.
- Type predicates must verify their complete claim. A predicate only tests an existing union member's discriminant when the input is already that validated union. Prefer direct narrowing or constructing a validated result when a predicate adds no value.
- Avoid unchecked `as`, double assertions, `any`, and non-null assertions used to silence errors. Localize a necessary assertion to code that establishes its claim, such as a validated branded constructor or a documented limitation in third-party declarations. An assertion performs no runtime check. `as const` and import aliases serve different purposes and are not banned.
- Use `satisfies` to check a configuration expression's assignability while keeping useful inference. It is not runtime validation, does not preserve every literal, and does not make an object immutable. Use an annotation when callers should see the declared type, and `as const` when literal/readonly inference is intended and compatible.
- Check all variants with `never` when a switch is intended to be exhaustive. Follow the repository's helper or throw convention; do not return the supposedly impossible object as a successful result. Validate unknown variants before treating input as a closed union.

Read the relevant example in [patterns.md](patterns.md) only when a concrete inference or exhaustive-handling question remains.
