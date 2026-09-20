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

Precondition: the user explicitly requests an API contract change and consumer migration. Existing documentation identifies significant compatibility risk, and the authorized scope includes the required consumer changes and validation.
Expected: check relevant callers, migration order, compatibility period, and regression validation; implement and verify the authorized transition. Risk alone does not turn the requested migration into a proposal or require another approval. Preserve any explicit external-action limits and continue independent work if a material contract decision remains unresolved. Paired review-only request: assess the same transition without implementation edits.

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

## 17. A required format addition

Input: design JSON export for two existing CSV consumers, with different download and email filenames. Preserve code during planning.
Expected: use `preflight.md`, identify shared format logic and consumer-specific decisions, and explain how JSON can be added while CSV callers keep working. Support the decision with actual modules and checks; do not introduce a plugin registry for unspecified formats.

## 18. Discovery boundary for ordinary functions

Precondition: the full skill catalog is available.
Input A: fix an arithmetic expression inside a module without changing its contract, state ownership, or dependencies.
Expected A: finish the local fix with relevant checks without selecting architecture-guard.
Input B: move shared state to a different owner or change a contract between modules.
Expected B: select the architecture guidance and inspect affected consumers. A .ts/.tsx extension or exported function alone is not evidence of boundary impact.

## 19. Requested planning artifact

Input A: 'Design the export module and save the plan to docs/export-plan.md. Do not implement it.'
Expected A: inspect relevant boundaries, write the requested plan, preserve implementation/configuration and unrelated documents, and finish without an implementation approval stop.
Input B: 'Design the export module; answer here only.'
Expected B: give the design judgment without changing files.

## 20. Snippet and metadata agree

Precondition: the project or global snippet and skill catalog are available.
Input A: fix an exported helper's calculation without changing any contract between modules, dependency direction, or state ownership.
Expected A: no separate architecture invocation merely because the helper is exported.
Input B: relocate shared state ownership across modules.
Expected B: invoke architecture guidance and inspect affected consumers. The snippet and description should use the same boundary.

## 21. Complete a small boundary implementation

Input: remove a shared module's dependency on a feature by passing the required value from its existing callers; implement and verify the change.
Expected: inspect the affected dependency and callers, make the local boundary fix, and run checks for the affected behavior. Preserve unrelated code and tests. Do not require a separate PR-review phase or read comparison-history guidance merely to finish implementation. If a change review is explicitly requested as well, select `review.md` and establish the relevant comparison scope.

## 22. Related responsibility versus file size

Precondition: a module around 1,000 lines keeps one document operation's decisions and checks together; the proposed alternative spreads them across files that always change together.
Input: review the proposed organization without editing files.
Expected: compare how readers understand, modify, and verify the same responsibility. Accept the existing module when splitting only adds imports and coordinated edits, even if it grows slightly beyond 1,000 lines. Still address independently changing responsibilities or required dependency rules in a shorter module. Treat the line count as an example, not an acceptance threshold.

## 23. Documentation follows the affected contract

Input A: implement an internal state-ownership change while the README's overview and setup instructions remain accurate; no document or decision record is requested or required.
Expected A: complete the implementation and checks without adding design rationale, session history, or implementation detail to repository documents.
Input B: implement a requested public API change that makes an existing usage example incorrect.
Expected B: correct the affected example at its existing level of detail. Do not turn that correction into a design report or rewrite unrelated README sections.
Input C: implement the same change and explicitly update a named architecture document, or follow an applicable repository rule requiring a decision record.
Expected C: produce the requested or required documentation within its stated scope; the documentation limit must not block that deliverable or require redundant approval.

## Evaluation records

Additional boundary-contract scenarios:

- Review an API whose generated client and mock use one schema revision while the provider emits a different shape. Inspect serialized output; passing type checks or a mock-only test does not establish compatibility. Reuse the existing canonical schema.
- Change a wire identifier that exceeds JavaScript's safe integer range. Preserve precision before serialization; stringifying an already rounded value cannot recover it. Verify the consumer-facing value independently.
- Migrate an exported format with consumers outside the repository. Preserve required legacy behavior and identify rollout constraints; a local search is not proof that external consumers are absent.
- Implement a local helper with no independently consumed boundary. Do not introduce schema generation, a contract document, or a broad architecture process.

These are expected behaviors, not executed pass records. The [ECC/OpenSpec evaluation](../contracts-openspec-2026-09-20/results.md) exercises a coordinated format migration with this guard available as optional expertise; it does not establish standalone guard selection or all scenarios above.

Record the model/version, skill version or hash, fixture commit, user input, invocation, reading scope, actual output, changed files, and validation commands. Check skill invocation and `AGENTS.md` integration separately. Repeat unstable invocation/scope cases to assess variation. Do not relax criteria to reach a score target.
