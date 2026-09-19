---
name: architecture-guard
description: Design or review module boundaries, dependency direction, shared-state ownership, and contracts between modules.
---

# Architecture Guard

Assess responsibilities and dependencies so the next change can be understood, modified, and verified locally. Judge actual change cost and failure risk rather than folder shape or pattern compliance.

## Select the work

Use [preflight.md](references/preflight.md) for design and planning, and [review.md](references/review.md) for PR/change reviews and current-architecture diagnosis. Read only the reference needed for the current decision. Implementation or improvement requests include necessary design decisions, edits, and verification of affected boundaries and contracts. Planning, review, and explanation preserve the assessed material; write only explicitly requested deliverables, such as a plan or report.

Start with the specified change and its directly connected callers, consumers, and state owners. Distinguish explicit boundary rules from conventions inferred from code. Expand investigation to boundaries affected by the change; for a requested full audit, identify the major boundaries and samples covered. A local function edit without changed boundaries or contracts needs no separate architecture review. If explicitly invoked for a wording-only or formatting-only change, confirm whether it has architectural impact and finish briefly.

## Design judgment

- **Responsibilities:** Keep code that must be read together and changes for the same reason close together, so a policy update can be understood and verified without unnecessary movement between files. Find repeated policy definitions that require coordinated edits; preserve similar-looking policies that change independently.
- **Dependency paths:** Check public entry points and agreed dependency direction. Include coupling through events, global state, callbacks, and network calls, not just imports.
- **Contracts:** Check actual consumers of changed APIs, types, caches, and events. Preserve relevant invariants when touching authorization, tenant isolation, concurrency, or transaction boundaries. For a requested contract transition, review consumers and migration order together.
- **Intervention cost:** Prefer readable, maintainable code over lower LOC or a smaller diff. A file around 1,000 lines can be appropriate when its responsibilities belong together; that number is neither a target nor a limit. Extract a module when independent change or verification becomes clearer, accounting for extra imports and coordinated edits. Preserve required dependency rules; do not apply DTOs, services, DDD, or FSD uniformly.

## Validation and completion

Start with existing checks that address risks in the changed boundaries and contracts. Run explicitly required validation; add checks when they resolve remaining uncertainty. Do not weaken checking rules to obtain a pass. A small automated check may help with recurring, significant boundary violations. Update only relevant documentation when a design decision changes.

Connect files, symbols, and actual dependency paths to impact and the smallest remedy. Separate behavior verification from maintainability judgment. If before/after quality comparison is also requested, use the same scope and criteria and reuse established evidence. State comparison scope, checks run and their limits, and significant unresolved issues. Resolve and verify problems within the requested edit scope. Leave contract transitions or migrations as proposals when they are outside that scope. Finish when only optional improvements remain.
