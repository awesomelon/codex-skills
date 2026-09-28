# Validate untrusted input

- Treat unchecked input as `unknown`, including values returned as `any` by parsing or third-party declarations. Typed clients and generated declarations do not automatically validate external input. Reuse an existing validation layer when one is already established.
- Prefer the repository's runtime schema and its inference helper for structured input. Do not add a schema dependency for a single simple check or duplicate a schema with a separately maintained interface and predicate.
- Validate the fields and value constraints that downstream code relies on. Preserve the established rejection, optional-result, or error-result behavior. Parse persisted versions explicitly; choose treatment of additional fields according to the actual protocol and schema options, not a universal ignore rule.
- Validate when values enter trusted application code. Repeat validation only when new untrusted values or relevant mutations invalidate the earlier check. Keep deliberate arbitrary-key data when the domain requires it.

Read the relevant example in [patterns.md](patterns.md) only when a concrete parser or schema question remains.
