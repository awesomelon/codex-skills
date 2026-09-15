---
name: typescript-best-practices
description: Design, implement, review, and debug TypeScript types and runtime input validation in .ts and .tsx code. Exclude wording-only and styling-only edits, and generated files that should be regenerated.
---

# TypeScript Best Practices

Make types express the values callers can actually provide and the results code can actually return. Preserve repository conventions, supported TypeScript versions, generated API definitions, and existing error behavior. Review-only requests produce findings without edits; implementation requests include relevant fixes and verification. This skill works independently of other skills.

## Choose the smallest useful type

- Represent mutually exclusive states with a discriminated union using an existing literal field, such as `status` or `type`. Optional properties are appropriate for independent optional data; replace them only when they admit contradictory states.
- Keep arrays and primitives when they meet the actual requirements. Use a non-empty tuple only when at least one element is required; otherwise return an optional value or handle emptiness. Prefer readonly inputs when the function does not mutate them.
- Use tuples for fixed relationships, such as pairs. A number remains capable of being negative, infinite, or NaN. A start plus a numeric duration does not by itself guarantee a valid time range.
- Brand a primitive when confusing two domain values would cause a concrete error. Reuse the repository's branding convention. Validate through a small constructor; do not brand every primitive or change public API types solely to satisfy this preference.
- Reuse generated types and existing schemas. Use indexed access, `Pick`, `Omit`, `Parameters`, `ReturnType`, `Awaited`, or `typeof` when the new type intentionally follows an existing definition. Declare a separate type when it represents a separately maintained concept; avoid complex utility chains that obscure a small type.

## Validate untrusted input

- Treat unchecked input as `unknown`, including values returned as `any` by parsing or third-party declarations. Typed clients and generated declarations do not automatically validate external input. Reuse an existing validation layer when one is already established.
- Prefer the repository's runtime schema and its inference helper for structured input. Do not add a schema dependency for a single simple check or duplicate a schema with a separately maintained interface and predicate.
- Validate the fields and value constraints that downstream code relies on. Preserve the established rejection, optional-result, or error-result behavior. Parse persisted versions explicitly; choose treatment of additional fields according to the actual protocol and schema options, not a universal ignore rule.
- Validate when values enter trusted application code. Repeat validation only when new untrusted values or relevant mutations invalidate the earlier check. Keep deliberate arbitrary-key data when the domain requires it.

## Narrow and construct before asserting

- Prefer the narrowing that matches the value: a discriminant for variants, `typeof` for primitives, `instanceof` for actual class instances, and `in` for property presence. Presence alone does not prove the property's value type; optional properties may occur in both results of an `in` check.
- Type predicates must verify their complete claim. A predicate only tests an existing union member's discriminant when the input is already that validated union. Prefer direct narrowing or constructing a validated result when a predicate adds no value.
- Avoid unchecked `as`, double assertions, `any`, and non-null assertions used to silence errors. Localize a necessary assertion to code that establishes its claim, such as a validated branded constructor or a documented limitation in third-party declarations. An assertion performs no runtime check. `as const` and import aliases serve different purposes and are not banned.
- Use `satisfies` to check a configuration expression's assignability while keeping useful inference. It is not runtime validation, does not preserve every literal, and does not make an object immutable. Use an annotation when callers should see the declared type, and `as const` when literal/readonly inference is intended and compatible.
- Check all variants with `never` when a switch is intended to be exhaustive. Follow the repository's helper or throw convention; do not return the supposedly impossible object as a successful result. Validate unknown variants before treating input as a closed union.

## Keep changes proportionate

Use object parameters when same-typed positional arguments are easy to swap or options need names. Keep simple single-argument functions and established APIs. Change allocation behavior for performance only with relevant evidence.

Use the repository's logger for actionable diagnostics; avoid adding ad hoc production logs, sensitive payloads, or a new telemetry system for a type fix. Choose tests that exercise the changed behavior; use real local implementations when practical and deterministic substitutes for external or unavailable services.

Read the relevant section of [patterns.md](references/patterns.md) when an example will resolve a modeling or inference question. Verify with the project's existing type check and relevant runtime tests. Account for `strictNullChecks`, `noUncheckedIndexedAccess`, and `exactOptionalPropertyTypes` when interpreting diagnostics; do not enable project-wide compiler options as an incidental edit. Report checks actually run and remaining uncertainty separately.
