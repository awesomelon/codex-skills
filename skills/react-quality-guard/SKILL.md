---
name: react-quality-guard
description: Design, implement, and review React web components, hooks, state, and performance. Exclude wording-only, styling-only, and React Native work.
---

# React Quality Guard

Reduce state errors and unnecessary React work while preserving user behavior and data contracts. Use Vercel React Best Practices and Composition Patterns as judgment references.

Planning, review, and explanation preserve the assessed material; write only explicitly requested deliverables, such as a plan or report. Implementation and improvement requests include necessary edits and verification. Start with the specified code and directly connected state/request paths; perform full audits at the requested scope.

## Relevant context and references

Reuse environment information already provided. Check versions and types when React API support affects the decision; inspect Compiler/build configuration when memoization or bundles are at issue. Do not make a survey of all dependency and configuration files a prerequisite for every change. Do not assume Next.js or the latest APIs, or replace the existing data library wholesale.

| Decision area | Reference |
| --- | --- |
| Component and hook design, state, Effects, form behavior | [react-correctness.md](references/react-correctness.md) |
| Component variants, children, render props, compound components, shared providers | [composition.md](references/composition.md) |
| Requests, client caches, bundles, rendering cost | [performance.md](references/performance.md) |
| Actual SSR/RSC, server functions, hydration | [server-react.md](references/server-react.md) |
| Source verification, comparison with upstream, updating the baseline | [sources.md](references/sources.md) |

Select only relevant references. The source document is not required reading for ordinary code review.

## Intervention and completion

Keep a component's state, handlers, and rendering close when they must be read and modified together. Components and hooks may remain in the same file; extraction does not require a new file. Prioritize readability and maintainability over LOC, and accept a cohesive file around 1,000 lines without treating that number as a target or limit. Split for independently changing behavior, actual reuse, or clearer verification, accounting for extra props, imports, and navigation.

Prioritize correctness, data isolation, and compatibility. For performance, start with serial requests, initial transfer, and expensive rendering/subscriptions on real user paths. Do not add component splits or memoization to meet a count. If boundary review is also requested, reuse its findings without making another skill a mandatory step.

Verify behavior/state changes using existing checks or interactions that match the reproduction conditions. Beyond required validation, additional checks need a concrete uncertainty to resolve. Do not weaken Hooks or type-checking rules. A simple state fix does not require a benchmark; a claim of improved performance does require measurements under comparable conditions.

For reviews, order findings by importance and connect each file/symbol, trigger, impact, and remedy. For implementation, report the change, verification, and unresolved in-scope issues. Distinguish correctness, maintainability, and measured performance; separate observations from estimates and executed checks from unrun ones. For a requested before/after comparison, reuse the same scope, criteria, and evidence. Finish once the requested work is sufficiently verified; optional optimization is not a reason to expand it.
