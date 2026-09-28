# Choose the smallest useful type

Keep domain types, schemas, and their consuming code together when they change for the same responsibility. Split for independently changing or reused responsibilities, not merely to collect types or helpers or reduce file length.

- Represent mutually exclusive states with a discriminated union using an existing literal field, such as `status` or `type`. Optional properties are appropriate for independent optional data; replace them only when they admit contradictory states.
- Keep arrays and primitives when they meet the actual requirements. Use a non-empty tuple only when at least one element is required; otherwise return an optional value or handle emptiness. Prefer readonly inputs when the function does not mutate them.
- Use tuples for fixed relationships, such as pairs. A number remains capable of being negative, infinite, or NaN. A start plus a numeric duration does not by itself guarantee a valid time range.
- Brand a primitive when confusing two domain values would cause a concrete error. Reuse the repository's branding convention. Validate through a small constructor; do not brand every primitive or change public API types solely to satisfy this preference.
- Reuse generated types and existing schemas. Use indexed access, `Pick`, `Omit`, `Parameters`, `ReturnType`, `Awaited`, or `typeof` when the new type intentionally follows an existing definition. Declare a separate type when it represents a separately maintained concept; avoid complex utility chains that obscure a small type.
- Use object parameters when same-typed positional arguments are easy to swap or options need names; keep simple functions and established APIs. Do not change allocation behavior for performance without relevant evidence.

Read the relevant example in [patterns.md](patterns.md) only when a concrete state, collection, or branded-value question remains.
