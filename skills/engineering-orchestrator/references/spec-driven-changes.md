# Spec-driven changes

Use this guidance when a behavior change spans dependent work, evolves during implementation, or needs a durable handoff. Apply it through the existing issue, plan, specification, or conversation. Scale the record to the uncertainty and coordination needed; a clear local edit needs no separate specification, document set, or process setup.

## Describe the intended change

Distinguish accepted behavior, observed implementation, and the proposed change. Existing code can diverge from the accepted behavior; neither a stale document nor a convenient implementation silently resolves that discrepancy. Use the request and authoritative product decisions to establish intent, scope, and what must remain compatible.

Express the change as added, modified, or removed behavior while preserving unaffected requirements. Make removals explicit; omitting a legacy scenario from a new plan does not authorize dropping it. Use observable scenarios and acceptance conditions as described in [changes](changes.md), with a machine-readable boundary contract where one already governs representation.

Keep the rationale for a change, required behavior, and implementation design distinguishable. Record design choices only where boundaries, tradeoffs, or dependencies need explanation. These are kinds of information, not required files or a fixed sequence of phases. Resolve only decisions that block the affected work, and continue independent authorized outcomes.

## Connect requirements to execution

Use one authoritative task record. Link each material outcome to its requirement or scenario, responsible owner, dependencies, and suitable verification evidence. Existing section names or issue references can supply that connection; no new ID scheme or duplicate backlog is required.

Prefer tasks that produce a checkable behavior across the necessary components. Settle a shared contract or other real prerequisite before dependent edits. The coordinator owns shared decisions and integration; specialist skills supply expertise within those tasks. Use [coordination](coordination.md) for delegation and shared-writer boundaries when needed.

## Reconcile as the work changes

When a requirement or implementation finding changes the plan, inspect the affected requirements, consumers, tasks, and evidence together. Update only the impacted scope, tell affected owners, and reuse evidence that remains valid. Do not restart every phase or maintain an unchanged plan merely because it was written first.

Do not weaken a requirement or delete a scenario to make an implementation appear complete. Resolve a material intent conflict with its authority; reconcile a stale progress note against current code and evidence. Planning and review preserve implementation files and existing records unless the user requested a specific written deliverable.

## Complete with evidence

Separate recorded task progress, implemented requirements, executed verification, and quality judgments. Checkboxes and a complete plan do not establish working behavior. For each material outcome, connect the changed implementation to relevant evidence and disclose unavailable checks or remaining gaps. Use [runtime verification](verification.md) when the claim requires running behavior.

When maintaining an existing specification is within scope, fold the implemented and verified behavior into it while preserving unaffected requirements. Keep proposed or unverified behavior distinguishable from accepted behavior; retain useful decision history through the project's existing convention. Do not create a specification store, archive hierarchy, or new document merely to close a task. Complete the user's requested endpoint without an extra planning approval gate; a planning-only endpoint remains planning-only.

The [source record](sources.md) identifies the OpenSpec concepts informing this guidance. They operate through ordinary task artifacts without requiring OpenSpec software or generated skills.
