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
19. **Another picker consumer:** Design selection rules for two picker instances that share search/display behavior but differ in eligibility and maintain independent search input. Use the component/hook design criteria, retain the existing picker API or explain an additive change, and identify checks for both old and new consumers. Avoid a universal form framework or flags for unrelated cases.

## UI work mode and requested artifacts

20. **UI selection without implementation:** Use the UI default prompt with a component snapshot and no edit request. Provide the assessment without changing the component or creating an unsolicited report file.
21. **UI selection with implementation:** Use the same prompt and ask to fix the component's state bug. Complete the requested edit and affected checks; do not stop at the assessment.
22. **Saved review or design:** Ask for component findings or a design plan in a specified Markdown file without implementation changes. Write that deliverable and preserve the assessed source/configuration. Merely requesting a plan without a file destination does not require creating a file.

## Component composition

23. **Conflicting composer modes:** Design a reusable composer whose header, recipient controls, and submit action each branch on `isReply`, `isEditing`, and `isForwarding`. Callers require different sets of controls. Propose explicit variants or caller composition that removes invalid combinations, preserves existing callers or explains migration, and retains independent drafts. Do not prescribe a new component for every boolean.
24. **Simple props remain useful:** Review `<SaveButton disabled={isSaving} isLoading={isSaving} />` and `<Badge variant="warning" />`, with straightforward implementations and no conflicting modes. Do not demand compound components, a provider, or removal of boolean props solely because composition guidance is available.
25. **Static content and data callbacks:** Review a panel with `renderHeader={() => <Title />}` and a virtual list with `renderItem={({ item, index }) => <Row item={item} index={index} />}`. Consider children or a node prop for the panel; retain the list's data callback. Do not require Context to replace either callback, or break existing callers without addressing migration.
26. **External preview and two editors:** Design two editors in the same dialog, each with its own draft, preview, reset, and submit controls. A preview sits outside its editor's visual container. Identify a common parent for each editor's consumers; use props or a suitably scoped provider. Avoid one shared draft, Effect-based copies, or a ref replacing rendered state. Check editing/resetting one editor leaves the other unchanged.
27. **Same UI with different state management:** Design reusable editor parts for a local draft and an existing remotely synchronized draft. Keep their differing update/submit behavior in the parent or provider while exposing the data/actions each part needs. Do not replace the existing cache library or require generic setters and state/actions/meta fields without a use for them.
28. **React 18 and React 19 compatibility:** Review a shared input library supporting React 18 and 19 that uses `forwardRef`, `Context.Provider`, and `useContext`. Preserve compatibility and do not require React 19 APIs. For a separate React 19-only input, consider ref props without treating valid `useContext` calls as defects.
29. **Required provider and frequent input:** Review `createContext<EditorValue | null>(null)` consumed without a null check. Its value combines a changing draft and actions, and an action-only consumer performs expensive work on each edit. Address missing-provider behavior; explain why grouping fields does not isolate subscriptions. Consider targeted context separation or existing selective subscriptions without promising an unmeasured speedup or adding memoization everywhere.
30. **Web form behavior during composition:** Implement an approved split of a form into input, cancel, and submit parts. Preserve labels, controlled input and IME behavior, Enter submission, non-submitting cancel, focus, pending state, and instance isolation as applicable. Choose web DOM examples and supported APIs, not Native-style events or a framework migration. Distinguish actual interaction checks from static review.

31. **Related form code in one file:** Improve a form around 1,000 lines whose state, validation, handlers, and JSX must be read together for the requested behavior change. Consider local components or hooks in the same file when they clarify the code; do not move each part into a new file to meet a line count. Explain any extraction through independent change, real reuse, or clearer verification. Preserve component identity, focus, form submission, and independent drafts; nearby code does not imply one shared state instance.

32. **Content composition without a state redesign:** Review an additive `header` node prop for a stateless panel. All callers and the supported React version are supplied. Assess API compatibility and content placement using composition guidance without making state, performance, server, or source references prerequisites. Report supported findings; do not invent a reason to add a provider or broaden the review.
33. **Reuse an established consumer boundary:** Add a second picker using its existing API and an independent draft; no component composition or shared-state boundary changes are needed. Verify isolation and the affected selection behavior without requiring a separate composition redesign. Report the implemented change and actual checks rather than a mandatory review report.

## Judgment

Out-of-scope edits, unsupported APIs, changes to data/state semantics, and fabricated validation results are failures, even if a real bug is also found. Performance findings must distinguish observations from estimates and show how the smallest intervention addresses the actual trigger.

Verify automatic metadata selection separately in desktop Codex. Providing the skill explicitly does not establish automatic invocation quality. Installation/execution on a Mac is also a separate check.

Coverage of reevaluation after the 2026-09-12 body revision is recorded in the [audit](../../docs/skill-audit-2026-09-12.md).
