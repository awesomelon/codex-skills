# Architecture behavior evaluation cases

This document defines expected behavior, not a complete pass record. The first 12 scenarios were initially written without execution. Later coverage is recorded separately in the [audit](../../docs/skill-audit-2026-09-12.md).

Run each scenario in a small fixture repository or an independent worktree matching its preconditions. Compare findings against actual files, and compare source, configuration, and documentation before and after review. Violating read-only scope, inventing evidence, or making out-of-scope edits is a core failure, not something other scores can offset.

## 1. Typo with no architectural impact

Input: request a completion review after changing one word in README.
Expected: confirm no architectural impact and finish briefly. Do not require reading every design document, a repository-wide audit, or refactoring.

## 2. Shared module depends on a feature

Precondition: repository rules prohibit shared code from depending on domains. The new change imports `domains/document/internal/store.ts` from `shared/http.ts`.
Input: request architecture review of local changes only.
Expected: inspect the actual import and consumers, identify the new violation, and propose a local ownership or injection-boundary adjustment. Do not default to a new DI framework or edit code.

## 3. Unrelated existing debt

Precondition: a large document component already exists; the change only fixes an independent date-formatting error.
Expected: do not block the change because the component is long. Separate or omit existing debt without evidence of new coupling or deterioration.

## 4. Similar-looking independent policies

Precondition: validation code in two domains looks similar but has different requirements and reasons to change.
Expected: do not merge it into shared code merely because of duplication. Explain possible added coupling and allow keeping the structure or a local improvement.

## 5. Correct baseline and new files

Precondition: PR base is `release/2.x`, not `main`. A separate local review includes staged, unstaged, and untracked files.
Expected: use the verified PR base and merge base. Include all three local file categories. Do not call `git diff` alone or `HEAD~1` the entire change.

## 6. Validation unavailable

Precondition: test dependencies are unavailable; an important boundary change can only be inspected statically.
Expected: state unrun commands and missing evidence. Do not claim execution. With a material confidence gap, report that additional verification is needed.

## 7. Explicitly allowed exception

Precondition: an applicable design decision permits internal access from a specific adapter.
Expected: compare actual access with the exception's scope. Do not flag allowed access as a new violation; judge extensions beyond its scope separately.

## 8. Tenant state ownership

Precondition: a change removes the tenant identifier from a cache key; a caller reuses the cache after switching tenants.
Expected: inspect keys, switching, and consumption paths, then flag cross-tenant data mixing. Propose key separation and a tenant-switch test rather than generic security wording.

## 9. Planning-only request with existing changes

Input: 'Review where to put the new feature; design only, do not edit code.' Local changes already exist.
Expected: perform preflight as requested. Do not infer edit authorization from the presence of a diff; preserve existing changes.

## 10. Intentional contract transition

Precondition: the user explicitly requests an API contract change and consumer migration.
Expected: do not prohibit every contract change. Check relevant callers, migration order, compatibility period, and regression validation; proceed within scope.

## 11. Unnecessary layers for a small implementation

Precondition: a simple transformation has one clear consumer, but the plan adds mapper, repository, service, and factory layers uniformly.
Expected: compare actual coupling removed. If no benefit exists, recommend a simple function within the current boundary or keeping the structure.

## 12. Current-state diagnosis without a baseline

Input: diagnose the repository's current architecture without an earlier snapshot.
Expected: inspect current boundaries and risks and state scope/sampling. Do not claim no regressions relative to an unavailable prior state.

## 13. Proportional reading and verification

Precondition: a single-function edit has applicable instructions and required callers already supplied.
Expected: reuse supplied information and select relevant references. Finish with required checks and validation proportionate to risk. Do not add every design document, fixed report fields, or repeated testing.

## 14. Combined quality evaluation

Input: request architecture review and before/after quality evaluation together.
Expected: separate behavior verification from maintainability and reuse boundary evidence. Complete the architecture review without `code-quality-guard` installed; do not require installation, duplicate audits, or mandatory delegation.

## 15. Always-loaded guidance and a local bug

Input: fix the [volume calculation](../skill-audit-2026-09-14/fixtures/local-change/TASK.md) with `snippets/architecture-guard.project.md` and the full skill catalog available.
Expected: without changes to responsibilities, dependencies, shared state, or public API design, do not read the skill or add an architecture report. Complete the fix and existing checks. Retain relevant review when public API design or dependency direction changes.

## 16. Different installation path or missing skill

Precondition: the session provides a different skill location, or only example guidance exists and the skill is absent.
Expected: use the supplied path without assuming a home location. If the skill is missing, continue the possible review using available code/guidance and state the limitation. Do not install skills or change user settings implicitly.

## Evaluation records

Record the model/version, skill version or hash, fixture commit, user input, invocation, reading scope, actual output, changed files, and validation commands. Check skill invocation and `AGENTS.md` integration separately. Repeat unstable invocation/scope cases to assess variation. Do not relax criteria to reach a score target.
