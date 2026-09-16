---
name: typescript-quality-guard
description: Design and review TypeScript types, fix type diagnostics, and implement or review input validation.
---

# TypeScript Quality Guard

Make types express the values callers can actually provide and the results code can actually return. Preserve repository conventions, supported TypeScript versions, generated API definitions, and existing error behavior. Planning, review, and explanation preserve the assessed material; write only explicitly requested deliverables, such as a plan or report. Implementation requests include relevant fixes and verification.

Use this skill for type modeling, diagnostics, or input validation, not merely because a file ends in .ts or .tsx. Regenerate generated definitions rather than editing them manually. This skill works independently of other skills.

## Choose the relevant guidance

| Decision | Reference |
| --- | --- |
| State variants, collections, brands, derived types, domain constraints | [Type modeling](references/type-modeling.md) |
| Unknown input, schemas, trust boundaries, parser error behavior | [Input validation](references/input-validation.md) |
| Predicates, assertions, satisfies, exhaustive handling | [Narrowing and construction](references/narrowing.md) |
| A concrete example needed to resolve a modeling or inference question | Relevant section of [patterns.md](references/patterns.md) |

Read only the guidance needed for the current decision. A configuration inference fix need not load parser or domain-modeling guidance.

## Complete the requested work

Use the existing type check for changed types. Add or run runtime checks when runtime behavior changes or a runtime claim needs verification; a type-only edit does not by itself require a runtime suite. Account for strictNullChecks, noUncheckedIndexedAccess, and exactOptionalPropertyTypes when interpreting diagnostics; do not enable project-wide compiler options as an incidental edit.

Resolve in-scope issues through relevant verification, then report checks actually run and remaining uncertainty. Do not stop after diagnosis when implementation is requested, or add unrelated cleanup once the requested behavior is sufficiently verified.
