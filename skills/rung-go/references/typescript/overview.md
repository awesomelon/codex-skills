# TypeScript engineering

Make types express actual inputs and outputs. Preserve supported versions, conventions, generated definitions, and runtime error behavior; regenerate generated files instead of editing them manually. A .ts or .tsx extension alone does not require a type-design pass.

| Decision | Reference |
| --- | --- |
| Variants, collections, brands, derived types | [Type modeling](type-modeling.md) |
| Unknown input, schemas, trust boundaries, error behavior | [Input validation](input-validation.md) |
| Predicates, assertions, satisfies, exhaustiveness | [Narrowing](narrowing.md) |
| A concrete modeling or inference example | Relevant section of [patterns](patterns.md) |

Use the existing type check for changed types. Runtime changes or claims require appropriate runtime evidence; type-only edits do not automatically require a runtime suite. Account for strictNullChecks, noUncheckedIndexedAccess, and exactOptionalPropertyTypes; do not enable project-wide options as an incidental fix. A familiar local diagnostic can be resolved without loading every reference.
