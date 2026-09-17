# TypeScript Quality Guard evaluation cases

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

16. **Renamed discovery and standalone package:** Discover and install `typescript-quality-guard` alone. Directory, frontmatter, display name, and default `$typescript-quality-guard` invocation must agree; all references must resolve inside that package. The repository must not expose a second skill under the old name.
17. **UI mode and saved design:** With the UI prompt, request only a union review: preserve files. Request a type-design plan in a specified Markdown file: write only that deliverable. Request a union fix: complete affected type checks without requiring unrelated parser work.
18. **Existing installation migration:** Using disposable destinations, cover an old symlink (including a broken link after pull) and an old managed copy with a local edit. Follow the README to preserve source/copy edits outside discovery paths and install the new name with the original mode/destination. The old name must no longer be discovered, and new standalone links must resolve. Do not treat a moved symlink as a backup of its source or expect automatic rename cleanup.

19. **Type review in discovery:** With the catalog available and no explicit skill invocation, ask to review a discriminated union without changing files. TypeScript type review should be discoverable; do not select parser guidance unless unchecked input is involved. Pair with case 15 to distinguish type review from a TSX wording change.
20. **Parameter guidance stays conditional:** Fix configuration inference without changing the API; do not load parameter-design guidance. When designing a function with easily swapped same-typed arguments, select type-modeling guidance and preserve existing public APIs unless a change is requested.

21. **Types read with their implementation:** Fix a parser type error in a cohesive file around 1,000 lines containing its schema, inferred types, and parsing code. Keep definitions together when understanding and modifying the parser requires reading them together. Avoid separate files merely for types or helpers and avoid dense utility types chosen only to save lines. Split only for demonstrated independent change or reuse, preserve generated definitions and public APIs, and verify the requested fix.

For model evaluation, provide a realistic task and the standalone skill without these expected answers. Use an isolated temporary directory and compare review-only inputs before and after. Compilation and runtime checks establish example behavior only; they do not establish automatic selection or model execution quality.
