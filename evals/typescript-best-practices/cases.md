# TypeScript Best Practices evaluation cases

These are intended behaviors, not model execution results. Record actual checks in [results.md](results.md).

1. **Selection:** Implement a TypeScript parser, fix a type error, or review a union in TSX. Apply only relevant guidance. A CSS or wording-only edit should not start a type audit.
2. **Review only:** Review a provided parser without edits. Identify any unsupported predicate claim and report it without changing files or installing dependencies.
3. **Contradictory states:** Loading, success, and failure have independent optional data. Introduce a union if invalid combinations are possible, while retaining independent optional metadata.
4. **Empty collections:** An ordinary sum already handles an empty array. Keep its array input. A function requiring a first element should accept a non-empty input or return an optional result according to requirements.
5. **Arbitrary index:** A random read from a non-empty tuple fails with indexed access checking enabled. Do not claim the tuple guarantees every indexed read, add `!`, or weaken compiler options.
6. **Numeric constraints:** Review a time range with a numeric duration. Explain that negative values, NaN, infinity, invalid dates, and overflow need distinct treatment. Introduce a checked duration only if required.
7. **Input and predicates:** Parse unknown JSON with an existing schema. Without a schema dependency, validate and construct a simple result. A check for `id` alone must not claim a complete member with a valid role.
8. **Assertions and inference:** Keep justified `as const`, import aliases, and a checked brand assertion. Explain that `satisfies` does not preserve every literal or perform runtime checks.
9. **Generated types:** A generated server definition already exists. Reuse it where appropriate and regenerate instead of editing generated files. Keep a separately maintained application concept separate when required.
10. **Compatibility and scope:** Preserve an older compiler, current error behavior, library options, public function signatures, and task scope. Do not require another skill, a new logger, universal object parameters, or project-wide compiler changes.
11. **Exhaustiveness:** Add a new union variant. The missing case should fail compilation; unexpected runtime data must not be returned as a valid result from the default arm.
12. **Standalone installation:** Install only this skill into a temporary destination. All local references should resolve; no companion skill should be required.

13. **Type-only reference selection:** Fix a configuration inference diagnostic without changing runtime behavior. Read narrowing guidance; use a relevant example only if needed. Do not load parser/modeling guidance or run a runtime suite merely because this is TypeScript. Run the relevant existing type check.
14. **Parser reference selection:** Implement an input parser in a project with an existing schema. Read input-validation guidance, and narrowing guidance only if the implementation needs it. Preserve established errors and complete relevant runtime verification. Do not survey unrelated React or architecture guidance.
15. **File extension is not a trigger:** Correct a CSS class string inside a TSX component without changing types, state, or behavior. Do not select this skill merely because the file is TSX.

For model evaluation, provide a realistic task and the standalone skill without these expected answers. Use an isolated temporary directory and compare review-only inputs before and after. Compilation and runtime checks establish example behavior only; they do not establish automatic selection or model execution quality.
