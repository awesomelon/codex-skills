# React quality behavior evaluation

These are evaluation inputs and expectations, distinct from actual execution. Record runs separately in [results.md](results.md).

## Invocation and scope

1. **React implementation:** Request quality improvements to a component or hook. Select relevant correctness/performance criteria and complete edits and validation when implementation is authorized.
2. **Non-invocation:** Request a README typo, CSS color-only edit, Python server function, or React Native style change. Do not add a React web audit or Next.js features.
3. **Review only:** Request only review of a component with several issues. Provide real evidence and remedies while preserving source, configuration, and documentation.
4. **Insufficient input:** The user says 'React is slow' without code or package.json. Separate assumptions and information needed; do not invent files, versions, bottlenecks, or improvement numbers.

## Environment and over-application

5. **React 18 + Vite + TanStack Query:** Review a change in this stack. Do not require migration to Next.js/SWR or immediate use of React.cache, Activity, or useEffectEvent. Use existing query keys, invalidation, and supported APIs.
6. **Already stable code:** Review simple calculations, boolean `&&`, and components with stable props. Do not add memo/useMemo/ternaries to meet a quota or claim a speedup without profiling.
7. **Compiler and imports:** Compiler is active and public barrel imports are optimized. Do not force unnecessary manual memoization or private deep imports; check build behavior and applicability.
8. **Default inside memo:** A memoized component has an omitted callback prop with an internal default, but does not pass that value downstream. Do not claim the parent's every render defeats memo comparison from the default expression alone.

## Correctness and performance boundaries

9. **Editable draft and server refresh:** State is initialized from server data as an independent editing draft. Do not remove it as redundant derived state or let background refetches overwrite input.
10. **Sorting, Effects, and response ordering:** Code sorts props in place, copies the result through an Effect, and can receive search responses out of order. Explain mutation, state drift, and races through actual paths, and propose small fixes.
11. **Submission and transition:** A React 18 form uses mutation pending to prevent duplicate submissions. Do not replace network state with useTransition pending or hide UI updates by moving state to refs.
12. **Dependent requests:** Authorized resources are read after authentication; a write result is needed by the next operation. Do not replace every await with Promise.all. Preserve failure, cancellation, and concurrency constraints.
13. **SSR cache and hydration:** Per-request user values live in module variables and initial client rendering reads localStorage. Inspect request lifetime and initial-render agreement. Do not conceal the issue with a global LRU, warning suppression, or inline scripts alone.
14. **Unavailable verification:** Runtime dependencies are absent and only API adapter types are supplied. Do not claim tests or profiles passed. Do not assert that the adapter lacks cache updates; identify the internal contract requiring verification.

## Reading and validation selection

15. **Small state fix:** A short component's React environment and behavior contract are supplied. Use correctness guidance and relevant code, without making server/source references or full build-configuration inspection prerequisites. Finish available validation without claiming unmeasured performance gains.
16. **Finish after verification:** Required checks and relevant behavior are verified; no significant issue remains. Do not delay completion with optional optimizations or repeated identical checks.

## Connection to general quality evaluation

17. **Before/after evaluation requested:** Compare React behavior, performance, and maintainability before and after. Distinguish correctness, maintainability judgment, and measured performance; reuse evidence. Do not stop because a general-quality skill is missing or infer overall quality improvement solely from tests.
18. **Standalone installation and reference selection:** Only `react-quality-guard` is available for a small SPA component improvement. Finish with relevant state/rendering criteria; do not require another quality skill, a full audit, or server references.

## Judgment

Out-of-scope edits, unsupported APIs, changes to data/state semantics, and fabricated validation results are failures, even if a real bug is also found. Performance findings must distinguish observations from estimates and show how the smallest intervention addresses the actual trigger.

Verify automatic metadata selection separately in desktop Codex. Providing the skill explicitly does not establish automatic invocation quality. Installation/execution on a Mac is also a separate check.

Coverage of reevaluation after the 2026-09-12 body revision is recorded in the [audit](../../docs/skill-audit-2026-09-12.md).
