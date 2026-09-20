# Changes

Choose the branch matching the requested behavior. These are decision guides, not mandatory steps to copy into a checklist.

## Bug fix

Reproduce the reported failure before choosing a fix. Match the trigger, data, timing, and affected surface closely enough to test the suspected mechanism. A deterministic local reproduction is valuable; forcing an unrelated failure is not evidence for this bug. If the live target is unavailable, distinguish a local reproduction from confirmation on that target.

Trace the failure to the responsible state transition or contract. Choose a test or observation that separates the surviving hypothesis from its strongest alternative. Use temporary instrumentation only when permitted and needed, and remove your diagnostic additions before delivery unless they are useful project diagnostics.

When a cheap regression test exercises the actual failure, demonstrate that it fails for the intended reason on the starting code, then passes with the fix. Keep return values, errors, and meaningful effects in the assertion; do not assert merely that a helper was renamed or invoked. Do not stage broken commits just to preserve a red-first history.

Apply the supported fix and rerun the original reproduction on the available affected surface, plus required checks and relevant neighboring cases. Compile success alone does not prove that the reported bug disappeared. If the target cannot be exercised, finish useful in-scope work and identify exactly which result remains unverified.

## Feature or migration

Reuse the request and authoritative product artifacts to establish intended behavior. Code establishes current behavior, not an unstated business policy. Resolve only uncertainty that could change the result; a clear request needs no discovery interview or extra approval. Keep unresolved decisions separate from facts and continue independent work.

Express material acceptance conditions as a starting situation, action, observable result, and relevant forbidden effect or compatibility constraint. Identify how each will be checked; several conditions may share one test, and some need runtime or manual observation. Keep these in the existing task or plan unless a durable artifact is useful and in scope. Do not create a specification for an obvious local edit.

Inspect existing implementations and dependencies before introducing another helper or package. Search further when a concrete gap remains, without requiring an external survey for every change. Define the state or contract needed to express the behavior and inspect actual consumers before changing a shared shape. Choose the simplest coherent design for the concrete requirement; crossing a function boundary alone is not a reason for a design competition.

For an independently consumed boundary, identify the authoritative contract and revision, its owner, affected producers/consumers, and acceptance evidence before splitting implementation. Use an existing schema or generation path where available; generated types and mocks must agree with that same contract. Check actual serialized output against consumer expectations. A type cast, matching prose, or both sides accepting the same accidental shape is insufficient evidence.

Work in units that leave a checkable result. For a migration, identify both editable and external consumers, compatibility requirements, and rollout order. Remove obsolete paths when the affected consumers have migrated and the requested contract permits it. A local search is not proof that a public API has no external users.

Verify the behavior through its real entrypoint when practical, including the failure or transition most likely to invalidate the design. Use [runtime verification](verification.md) when correctness depends on a running UI, CLI, or service. Keep build-only evidence labeled accordingly.

## Behavior-preserving refactoring

Identify the observable contract and establish a relevant baseline before changing structure. Preserve values, errors, public entrypoints, and effect order/count where they matter. Make small transformations that can be checked before dependent changes accumulate. A newly discovered bug is separate work unless its correction was also requested.

Judge the result by ease of understanding and changing the code, not fewer lines or files. Existing refactoring or domain guidance can supply deeper criteria when available; this workflow does not require it.

## Prototype or competing approaches

Name the uncertain decision and what observation would resolve it. Build the smallest permitted sketch that exposes that difference. Choose isolated alternatives only when comparison is worth the cost; an architecture discussion does not automatically require multiple implementations.

Keep prototypes separate from the production path until a choice is made. Reuse the selected approach deliberately and verify the integrated result; passing isolated prototypes does not establish compatibility after combining them. Report what the experiment establishes and what a production implementation would still require.
