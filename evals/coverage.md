# Instruction coverage

The four user-supplied references and the designated authoring article were retrieved and read on 2026-10-04 for Tact 0.0.2. On 2026-10-06, the current [no-ai-slop skill](https://github.com/petergyang/no-ai-slop/blob/main/skills/no-ai-slop/SKILL.md), its [evaluation guide](https://github.com/petergyang/no-ai-slop/blob/main/skills/no-ai-slop/eval.md), and the [authoring article](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) were read directly for the 0.0.3 communication revision. This map covers the current source. It is an instruction audit, not a model-success score. The skill contains original integrated wording and internal links only.

| Area | Concrete coverage | Owner |
| --- | --- | --- |
| Intent | Visible material assumptions, competing interpretations, investigation before questions, recommendation and pushback, settled choices retained. | [Entrypoint](../skills/tact/SKILL.md) |
| Simplicity | No speculative features, extension points, single-use frameworks, impossible defensive cases, or success-shaped fallbacks; simplify an elaborate first attempt when a direct solution meets the same contract. | Entrypoint |
| Scope | Match surrounding style, preserve unrelated edits/comments, repair shared causes, remove only newly orphaned code, maintain read-only endpoints. | Entrypoint |
| Decision context | Preserve missing context for a concrete future question, reuse sufficient existing rationale, omit speculative checklists, follow existing ADR conventions, preserve superseded rationale, and distinguish proposals, accepted choices, and implementation evidence. | [Decision documentation](../skills/tact/references/decision-documentation.md) |
| Type information | Avoid known-value widening, broad object inputs, unknown outputs/aliases, unsafe dictionary values, and widen-then-assert flows. Preserve literal keys and use precise contracts. | [Code evidence](../skills/tact/references/code-evidence.md) |
| Boundaries | Parse external input, confine necessary runtime type inspection, retain environment-existence checks, isolate dynamic foreign adapters. | Code evidence |
| Assertions | No fabricated chained casts; each necessary non-const assertion has a specific adjacent invariant explanation. A comment cannot replace validation. | Code evidence |
| Construction | Avoid eager duplicate passes and growing accumulator copies; preserve callback semantics, runtime support, ownership, and omitted-versus-undefined fields. | Code evidence |
| Dependencies | Prefer real seams over module replacement; do not create an unnecessary injection framework. | Code evidence |
| Readability | Domain-oriented names, readable declaration/control-flow spacing, preserved external member names, formatter and scope respected. | Code evidence |
| Effect | Tagged recovery, tagged matching, constructors, service ownership, and repeated-branch matching; conditional on direct project use. | [Effect conventions](../skills/tact/references/effect-code.md) |
| Evidence | Explicit claim-to-check mapping, actual output and exit status, test selection, original-failure/fixed-success regression evidence, artifact inspection and requirement coverage. | [Verification](../skills/tact/references/verification.md) |
| Final state | Changed-input invalidation, limited reuse of applicable observations, worker-artifact inspection, no diagnostic suppression, distinct failed/blocked/unrun outcomes. | Verification |
| Reporting | Answer first, formatting chosen for the content, specific changes and evidence instead of inflated claims, consistent project terms, complete scoped values and risks, requested depth, no filler or repeated conclusions. | [Communication](../skills/tact/references/communication.md) |
| Interaction | Focused questions, blocking decision visible, progress orientation, executable work retained, requested artifact formats preserved. | Communication |

## Explicit adaptations

These are default engineering decisions rather than an imported AST ruleset. External-input parsers may accept `unknown`; callbacks and unsupported runtimes may justify retaining an existing pipeline; a foreign dynamic API may require a narrow reflection adapter. Such exceptions need a concrete constraint. They do not license unconstrained internal types or a blanket dismissal of the defaults.

Names and spacing are maintenance policies, not proof of runtime bugs. Existing project contracts and read-only requests still govern scope. Effect guidance is conditional and does not authorize installing a library. Tact does not bundle or install lint enforcement.

Completion evidence must cover the relevant final state. Repeating every unchanged check in every message is not required; an earlier success cannot establish a subsequently changed result. Communication style does not override JSON-only output or requested depth, and makes no assumptions about a user's health.

The communication revision selectively adapts flexible presentation, subject-specific wording, and stable terminology for engineering reports. Emphasis remains available when useful; distinct domain concepts stay distinct. It adds no global vocabulary blacklist, personal-voice editing workflow, or mandatory prose checklist. Specific wording must preserve uncertainty and cannot supply missing evidence.

Use [scenarios](cases.md) for expected behavior and [results](results.md) for actual execution and its limits.

On 2026-10-07, the user-supplied `documentation-and-adrs` skill and the authoring article were read directly for the decision-documentation revision. The integration retains context, tradeoffs, repository conventions, and decision history. Record selection depends on a concrete future question and missing context, not the size or architectural importance of a change. It replaces the supplied checklist and fixed template with selective recording, preserves read-only requests, and adds no second skill or ADR tooling. This is source verification and instruction coverage; behavioral execution is recorded separately.
