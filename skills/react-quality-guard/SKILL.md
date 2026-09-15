---
name: react-quality-guard
description: Design, implement, and review React web components, hooks, state, and performance. Exclude wording-only, styling-only, and React Native work.
---

# React Quality Guard

Reduce state errors and unnecessary React work while preserving user behavior and data contracts. Use Vercel React Best Practices as a judgment reference.

Review-only or planning-only requests must not modify source, configuration, or documentation. Implementation and improvement requests include necessary edits and verification. Start with the specified code and directly connected state/request paths; perform full audits at the requested scope.

## Relevant context and references

Reuse environment information already provided. Check versions and types when React API support affects the decision; inspect Compiler/build configuration when memoization or bundles are at issue. Do not make a survey of all dependency and configuration files a prerequisite for every change. Do not assume Next.js or the latest APIs, or replace the existing data library wholesale.

| Decision area | Reference |
| --- | --- |
| Component and hook design, state, Effects, form behavior | [react-correctness.md](references/react-correctness.md) |
| Requests, client caches, bundles, rendering cost | [performance.md](references/performance.md) |
| Actual SSR/RSC, server functions, hydration | [server-react.md](references/server-react.md) |
| Source verification, comparison with upstream, updating the baseline | [sources.md](references/sources.md) |

Select only relevant references. The source document is not required reading for ordinary code review.

## Intervention and completion

Prioritize correctness, data isolation, and compatibility. For performance, start with serial requests, initial transfer, and expensive rendering/subscriptions on real user paths. Do not add component splits or memoization to meet a count. If boundary review is also requested, reuse its findings without making another skill a mandatory step.

Verify behavior/state changes using existing checks or interactions that match the reproduction conditions. Beyond required validation, additional checks need a concrete uncertainty to resolve. Do not weaken Hooks or type-checking rules. A simple state fix does not require a benchmark; a claim of improved performance does require measurements under comparable conditions.

Report findings by importance, connecting file/symbol, trigger, impact, and remedy. Distinguish correctness, maintainability, and measured performance. If before/after quality comparison is also requested, use the same scope and criteria and reuse evidence. Separate observations from estimates and executed checks from unrun ones. State unresolved in-scope issues; do not keep expanding sufficiently verified work solely for optional optimization.
