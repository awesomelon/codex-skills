# Applying specification-driven change concepts

Rung uses OpenSpec change-management concepts with existing engineering records. You can use issues, product requirements, plans, and task conversations.

Rung does not require OpenSpec installation, its CLI, generated skills, a workflow schema, or a specific directory structure.

| Concept | Application in Rung |
| --- | --- |
| Proposal | Clarify the reason, intended result, scope, and compatibility limits when needed. |
| Behavioral specification | Describe observable requirements and scenarios. Keep implementation choices separate. |
| Change delta | Identify added, changed, and removed behavior. Preserve accepted behavior outside the change. |
| Design | Record important boundary decisions, tradeoffs, and dependencies. Match the detail to the change. |
| Tasks | Connect each checkable result to requirements, owners, dependencies, and evidence in the existing task record. |
| Verification | Check requirement coverage, correctness, and design quality separately. Completed task checkboxes do not prove success. |
| Reconciliation | Update affected requirements and tasks when evidence changes the plan. Add verified behavior to existing specifications when requested. |

These concepts connect information. They do not require seven stages or seven documents. Use the [spec-driven change reference](../skills/rung-get-set/references/workflow/spec-driven-changes.md) when needed.

Choose Get Set for assessment. Choose Go for implementation and integration. Reference documents do not change the requested scope.

For example, a document export may need an archive state. This changes the serialized format and adds a default value. Legacy import must still work.

An existing issue can describe these changes and their acceptance scenarios. Tasks connect producer and consumer changes to separate format and legacy-import checks. If the specification changes during implementation, update the affected tasks and evidence. An earlier completed checklist does not prove that the revised requirements are met.

```text
Use $rung-go to implement this document-format change.
Reuse the existing issue and specification.
Separate changed behavior from behavior that must stay the same.
Verify the required compatibility before you complete the task.

Use $rung-get-set to review whether this change meets its requirements.
Compare the current implementation and evidence with the existing plan.
Do not edit files.
```

For a clear small edit, make the change and run a relevant check. Complex work can need a saved plan or specification. Use the project's format and the requested deliverable. A new document system is not required.

The earlier source review inspected OpenSpec's [spec-driven schema](https://github.com/Fission-AI/OpenSpec/blob/bae58cf61479986431bb798acbe5a688a591c18c/schemas/spec-driven/schema.yaml), [verification guidance](https://github.com/Fission-AI/OpenSpec/blob/bae58cf61479986431bb798acbe5a688a591c18c/src/core/templates/workflows/verify-change.ts), and [specification reconciliation guidance](https://github.com/Fission-AI/OpenSpec/blob/bae58cf61479986431bb798acbe5a688a591c18c/src/core/templates/workflows/sync-specs.ts). Rung adapts these concepts independently. It does not provide a compatible OpenSpec adapter. See [evaluation results](../evals/spec-driven-concepts-2026-09-20/results.md) for executed behavior and limits.
