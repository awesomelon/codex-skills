# Spec-driven changes

Use this guidance when a behavior change spans dependent work, evolves during implementation, or needs a durable handoff. Apply it through the existing issue, plan, specification, or conversation. Scale the record to the uncertainty and coordination needed; a clear local edit needs no separate specification, document set, or process setup.

## Describe the intended change

Distinguish accepted behavior, observed implementation, and the proposed change. Existing code can diverge from the accepted behavior; neither a stale document nor a convenient implementation silently resolves that discrepancy. Use the request and authoritative product decisions to establish intent, scope, and what must remain compatible.

Express the change as added, modified, or removed behavior while preserving unaffected requirements. Make removals explicit; omitting a legacy scenario from a new plan does not authorize dropping it. Use observable scenarios and acceptance conditions as described in changes guidance in `craftflow-go` (`references/workflow/changes.md`, when available), with a machine-readable boundary contract where one already governs representation.

Keep the rationale for a change, required behavior, and implementation design distinguishable. Record design choices only where boundaries, tradeoffs, or dependencies need explanation. These are kinds of information, not required files or a fixed sequence of phases. Resolve only decisions that block the affected work, and continue independent authorized outcomes.

## Resolve the decisions that matter

Separate what can be established by inspecting the project from what requires a user's choice. Investigate facts, existing contracts, conventions, and verification commands rather than asking the user to retrieve them. Choose reversible implementation details within the agreed contract. A conventional tuning value can be an explicit adjustable default; an access rule, retention period, or conflict-resolution policy is not made harmless by calling it a default.

For a consequential choice not settled by the request or an authoritative decision, state the concrete ambiguity, consequence, and recommended option, then ask only for the missing decision. Technical choices can also belong to the user when they change scope, cost, compatibility, security, or accepted risk. Do not re-ask an explicit decision just because it arrived in another document. Conversely, a detailed imported plan does not authorize its assumptions or expand a planning-only request into implementation.

For the affected behavior, examine the relationships and state transitions that could make the request mean different things, including interactions with existing actors and contracts. This is a targeted search for omissions, not a mandatory whole-project model or fixed interview. Keep unresolved choices visible in the working record instead of converting them into settled requirements.

Before costly dependent implementation, a consequential or uncertain design can merit an independent intent check. Give an available reviewer the relevant authoritative excerpts, unresolved choices, and affected contract, not only the author's summary. Ask whether a decision lacks support or the handoff loses a requirement; a reviewer must not invent the answer. Resolve material findings with the decision owner and recheck only affected parts. Use an existing sufficient review rather than another panel. If independence is unavailable, perform a local check and label its limits. This does not create an extra approval stage: existing implementation authorization remains sufficient for settled work.

## Connect requirements to execution

Use one authoritative task record. Link each material outcome to its requirement or scenario, responsible owner, dependencies, and suitable verification evidence. Existing section names or issue references can supply that connection; no new ID scheme or duplicate backlog is required. Check both directions: each required outcome has work and evidence, and each task serves the authorized outcome or a necessary stated prerequisite. Unrequested improvements do not become in-scope merely by entering the plan.

Prefer tasks that produce checkable behavior across the necessary components. Use coordination guidance in `craftflow-go` (`references/workflow/coordination.md`, when available) for assigning dependent work and shared-writer boundaries; keep requirement ownership in the task record.

If an existing plan supplies a machine-readable dependency graph, validate its task references and cycles before scheduling. Keep it consistent with the actual task record. Do not introduce a graph format for its own sake or obey a stale dependency after evidence disproves it; reconcile a technical replan within the agreed intent and escalate changes to that intent.

## Reconcile as the work changes

When a requirement or implementation finding changes the plan, inspect the affected requirements, consumers, tasks, and evidence together. Update only the impacted scope, tell affected owners, and reuse evidence that remains valid. Do not restart every phase or maintain an unchanged plan merely because it was written first.

Do not weaken a requirement or delete a scenario to make an implementation appear complete. Resolve a material intent conflict with its authority; reconcile a stale progress note against current code and evidence. Planning and review preserve implementation files and existing records unless the user requested a specific written deliverable.

## Complete with evidence

For each material requirement, link its implementation and actual evidence using verification evidence guidance in `craftflow-go` (`references/workflow/verification.md`, when available) when needed. Mark missing or inconclusive evidence explicitly; task checkboxes are progress records, not proof of completion.

When maintaining an existing specification is within scope, fold the implemented and verified behavior into it while preserving unaffected requirements. Keep proposed or unverified behavior distinguishable from accepted behavior; retain useful decision history through the project's existing convention. Do not create a specification store, archive hierarchy, or new document merely to close a task. Complete the user's requested endpoint without an extra planning approval gate; a planning-only endpoint remains planning-only.

The source record guidance in `craftflow-go` (`references/workflow/sources.md`, when available) identifies the OpenSpec concepts informing this guidance; plugin adaptation provenance guidance in `craftflow-go` (`references/workflow/sources.md#plugin-adaptation-provenance`, when available) identifies the later intent and evidence refinements. These concepts operate through ordinary task artifacts without requiring upstream software or generated skills.
