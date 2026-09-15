# Skill audit — 2026-09-15

Baseline: `98e1c4d3cc78b1fdb5baa21ab31a869cb58452fa` on `awesomelon/codex-skills` main.

Reviewed the five skill entrypoints, UI prompts, reference routing, repository guidance, task templates, README, and relevant evaluation records. This is an instruction audit, not a fresh verification of every React, TypeScript, or TanStack API described by the references.

The user-designated [OpenAI article](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) motivates specific selection boundaries, conditional reference loading, and completion criteria that do not introduce unnecessary stops. The findings below are this audit's application of those principles.

## Findings and changes

| Finding | Evidence in the baseline | Change |
| --- | --- | --- |
| TypeScript loads unrelated criteria for small tasks | The 5,659-character entrypoint embeds type modeling, parser validation, and narrowing rules. | Route to three task-specific references; preserve those three sections' decision criteria verbatim apart from heading level. Keep examples optional. |
| TypeScript verification can exceed the change | The entrypoint asks for the existing type check and runtime tests without clearly distinguishing type-only edits. | Use the relevant type check for changed types; require runtime evidence when runtime behavior or a runtime claim is at issue. |
| TypeScript discovery can be interpreted by file extension | The description mentions .ts and .tsx work. | Describe type modeling, diagnostics, and runtime input validation; explicitly exclude selection based on extension alone. |
| Code-quality UI prompt conflicts with implementation use | Its unconditional “without modifying files” conflicts with the implementation workflow advertised by the skill. | Preserve review as the default when no edit is requested, while completing explicitly requested implementation and verification. |
| Architecture discovery can overlap with routine function work | The description lists dependencies, shared state, and public APIs without identifying module-boundary impact. | Specify module boundaries, dependency direction, shared-state ownership, and contracts between modules; clarify local edits in the body. |
| README suggests excessive development checks | Its add-skill section presents shell syntax, structure checks, and the full repository suite as one block, while AGENTS.md scopes the full suite to installer/validator changes. | Separate structure, installer/validator, and behavioral checks by change type. |

React and TanStack Query already have useful task-specific routers. Keep their current guidance, technical references, upstream attribution, and license. Keep the general code-quality evidence/scoring separation, architecture preflight/review distinction, macOS installation behavior, and AGENTS.md conventions. No new skill, automatic companion invocation, mandatory delegation, or model-specific instruction fork is needed.

## Reading size

Character counts include whitespace and newlines; they are not token counts or measured latency.

| Material | Before | After |
| --- | ---: | ---: |
| TypeScript entrypoint | 5,659 | 2,345 |
| TypeScript selection description | 5 | 90 |
| Architecture selection description | 5 | 112 |

The TypeScript entrypoint is about 59% smaller. The three new references total 4,316 characters, so reading every reference does not save context. The intended benefit is avoiding unrelated reading for a focused task. No token, speed, or model-quality improvement has been measured.

Removed the TypeScript-specific reminder about general logging hygiene; it added no type-modeling decision. Preserve the existing no-new-logger expectation in the compatibility scenario. Compiler-option cautions, generated-type handling, checked assertions, parser errors, independent optional fields, and runtime limitations remain.

## Validation actually performed

The execution environment failed to initialize. Files were read at the pinned baseline and prepared through the GitHub connector. In-memory JavaScript checks covered:

- All five entrypoints: matching single-line name/description fields and the repository's description length limit.
- All 25 skill Markdown files and 43 relative links: existing targets within each installable skill folder.
- All five UI metadata files: quoted interface values, short-description length, and explicit skill invocation names.
- Three moved TypeScript sections: original decision text preserved.
- Changed text: final newlines, trailing whitespace, and merge-conflict markers.

These checks passed. They are a structural subset, not execution of the repository validator or a general YAML parser.

## Behavioral cases and remaining verification

Updated the architecture, TypeScript, and code-quality scenario catalogs for local edits, type-only/parser reference selection, and paired UI review/implementation behavior. These are expected outcomes, not newly executed model results.

Not run for this revision:

- `python3 scripts/validate.py`.
- Standalone installation of the restructured TypeScript skill.
- Fresh model executions of the added/updated scenarios, including automatic selection.
- Runtime/compiler example checks or macOS execution.

The existing TypeScript examples and historical execution records are unchanged; their results do not validate this revision's routing or UI behavior. Installer and validator code are unchanged, so their full regression suite is not newly required by AGENTS.md. Keep the PR as a draft with these gaps visible; do not claim that the required repository or behavioral validation passed.
