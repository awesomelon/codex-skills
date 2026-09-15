# TypeScript Best Practices validation

Executed on macOS on 2026-09-15. These checks cover the new skill's files and examples, not model behavior in a later conversation.

## Changes from the supplied draft

- Used the repository's single-line name and description metadata and Codex's automatic-selection setting in `agents/openai.yaml`. Limited selection to relevant TypeScript work.
- Removed mandatory companion-skill requirements and fixed-order narrowing advice. Kept the skill independently installable.
- Replaced absolute assertion bans with checked, localized uses and accurate treatment of `as const` and `satisfies`.
- Corrected non-empty array indexing and numeric duration guarantees. Added runtime rejection and compile-time exhaustiveness examples.
- Kept schema reuse, generated definitions, error behavior, argument design, logging, and tests proportional to the task.

## Executed example checks

A temporary harness extracted all six TypeScript blocks from `references/patterns.md`, compiled them independently as modules, and tested their exports. Only test exports and the resolution of the already-installed Zod module were added; example logic was unchanged.

Environment: TypeScript 6.0.3, Zod 4.5.4, Node.js 26.8.2. Compiler settings: `strict`, `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes`, ES2022, Node16 modules and module resolution; library declaration checks remained enabled.

- All six examples compiled.
- Eight expected type errors were confirmed: incomplete ready state, empty input, arbitrary indexed read, unchecked duration, invalid member role, missing schema output field, widened numeric property, and writing a readonly property.
- Adding an unhandled union variant failed compilation at the `never` assignment with TS2322.
- All 39 runtime assertions passed: union results and unexpected variants, empty/non-empty arrays, missing indexed values, valid and invalid durations, both parsers' acceptance and rejection behavior, additional-field treatment, and configuration values.

## Package checks

- The bundled skill-creator `quick_validate.py` passed.
- `python3 scripts/validate.py` passed for all five repository skills.
- `bash scripts/install.sh --list` discovered the new skill.
- Copy installation into a temporary destination succeeded; installed skill contents matched the source.
- UI YAML parsed successfully with automatic selection enabled.
- `git diff --check` passed; direct comparison confirmed `AGENTS.md` was unchanged.

## Scope limits

Automatic discovery in the Codex UI, actual implicit/explicit model invocation, and independent model execution of the twelve scenarios were not tested. Compiler examples were executed with the versions above; compatibility with TypeScript 4.9 and Zod 3 was not executed. This documentation addition required no application build, browser test, installer implementation change, or validator implementation change.
