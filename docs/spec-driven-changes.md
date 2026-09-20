# Applying specification-driven change concepts

Engineering Orchestrator applies OpenSpec's useful change-management concepts through ordinary engineering artifacts. It requires no OpenSpec installation, CLI, generated skills, workflow schema, or directory layout. Existing issues, product requirements, plans, and task conversations remain sufficient.

| Concept | Application in codex-skills |
| --- | --- |
| Proposal | Explain the reason, intended outcome, scope, and compatibility constraints when they need clarification. |
| Behavioral specification | Describe externally observable requirements and scenarios; keep implementation choices separate. |
| Change delta | Identify what is added, modified, or removed while preserving unaffected accepted behavior. |
| Design | Record meaningful boundary decisions, tradeoffs, and dependencies at the scale of the change. |
| Tasks | Connect checkable outcomes to requirements, owners, dependencies, and evidence in the existing task record. |
| Verification | Assess requirement coverage, actual correctness, and design quality separately; do not infer success from checked tasks. |
| Reconciliation | Update affected requirements/tasks when evidence changes the plan; incorporate verified behavior into existing specifications when in scope. |

These are information relationships, not mandatory stages or seven documents. The conditional [spec-driven change reference](../skills/engineering-orchestrator/references/spec-driven-changes.md) supplies the decision guidance. The orchestrator continues to own execution and integration, and guards remain independently usable.

For example, adding archive state to a document export changes its wire representation, adds defaulting behavior, and preserves legacy import. An existing issue can state those changes and their acceptance scenarios. Tasks then connect producer and consumer work to independent wire-format and legacy-import checks. If the specification changes during implementation, revise only affected tasks and evidence; do not treat a prior completed checklist as proof.

```text
Use $engineering-orchestrator to implement this document-format change. Reuse the existing issue and specification, distinguish changed and preserved behavior, and verify the required compatibility before completing the task.

Use $engineering-orchestrator to review whether this change meets its requirements. Compare the current implementation and evidence with the existing plan; do not edit files.
```

A clear small edit can remain a direct change with a relevant check. Complex work may justify a durable plan or specification, but its location and format follow the project and requested deliverable. Introducing a new document system is not a prerequisite.

Source concepts were inspected in OpenSpec's [spec-driven schema](https://github.com/Fission-AI/OpenSpec/blob/bae58cf61479986431bb798acbe5a688a591c18c/schemas/spec-driven/schema.yaml), [verification guidance](https://github.com/Fission-AI/OpenSpec/blob/bae58cf61479986431bb798acbe5a688a591c18c/src/core/templates/workflows/verify-change.ts), and [specification reconciliation guidance](https://github.com/Fission-AI/OpenSpec/blob/bae58cf61479986431bb798acbe5a688a591c18c/src/core/templates/workflows/sync-specs.ts). This is an independent conceptual adaptation, not a compatible OpenSpec adapter. See [current evaluation results](../evals/spec-driven-concepts-2026-09-20/results.md) for executed behavior and limits.
