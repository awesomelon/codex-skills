# Code evidence

Use this guidance when TypeScript or JavaScript changes depend on type information, input validation, or collection behavior. Existing project contracts and runtime support determine the choice.

## Keep type information useful

Preserve inferred keys and discriminants through internal code. A broad annotation followed by a cast often discards information the compiler already had. Prefer an accurate contract or, where appropriate, `satisfies` over widening a known value and asserting it back.

At an external boundary, `unknown` is appropriate until the input is checked. Use existing schemas or a focused guard that validates the properties the consumer requires. Neither a generated type nor `as T` checks an external payload. Avoid adding a validation dependency for a simple boundary that the project already handles adequately.

If an assertion is necessary, identify the invariant that makes it sound and where that invariant is established. A double assertion or a comment claiming safety cannot create that evidence. Correct the contract or validation when the evidence is missing.

## Preserve behavior when simplifying collections

A reduction that repeatedly copies a growing accumulator can do unnecessary work. A fresh local accumulator may be simpler, but first establish its ownership; do not mutate caller-owned state.

Choose collection operations for their actual semantics and the supported runtime. Replacing `filter().map()` mechanically can change callback order, indexes, sparse-array behavior, or truthiness handling. Iterator helpers need runtime support; declarations alone do not provide it. Measure representative completed work before claiming a performance improvement.

## Make checks support the claim

Tests should observe the promised behavior, including a relevant boundary when the contract crosses one. A mocked implementation returning the expected answer does not verify the real integration. Use the project's existing seams for focused tests and distinguish their scope from integration evidence.

Choose lint policy for the project's contracts. `unknown`, `typeof`, reflection, module mocks, and array pipelines each have legitimate uses; their presence alone is not a defect. Adopt or change enforcement only when the requested work calls for it.
