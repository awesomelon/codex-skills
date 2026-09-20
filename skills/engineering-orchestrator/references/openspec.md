# OpenSpec integration

Use this reference when the user selects an OpenSpec change or the task's repository policy requires OpenSpec. An `openspec/` directory alone does not route every edit through a specification workflow. This integration is optional; ordinary tasks and the other references do not require the CLI or generated skills.

## Select scope and the execution owner

Preserve the requested endpoint. Explicit proposal or exploration requests remain planning work; the official `openspec-propose` skill deliberately stops after its artifacts. Do not route an ordinary implementation request into that planning-only endpoint. For implementation of an established change, continue authorized work without introducing another approval ceremony.

Resolve available OpenSpec skills from the actual catalog. Codex installations use generated `.agents/skills/openspec-*/SKILL.md` resources; names may be qualified by the host. Leave those resources under their existing management rather than copying or rewriting them. For a direct OpenSpec task, its official skill can lead. For coordinated delivery, retain one coordinator, use CLI instructions as the artifact workflow, and assign bounded implementation or review outcomes. Do not start a second competing apply loop.

Confirm the project root and selected change from the request and current context. With the project's supported CLI, use `openspec context --json`, `openspec status --change "<name>" --json`, and `openspec instructions apply --change "<name>" --json` as appropriate to the task. A known single active change can be selected; ambiguous changes need resolution. Preserve an explicitly selected store on applicable commands. Respect returned `planningHome`, `changeRoot`, and `actionContext`; a returned path identifies an artifact, not permission to edit outside the task's scope.

Follow the installed version's help and generated guidance if commands or fields differ. If the CLI is missing or scope cannot be resolved, report the specific limitation, inspect available artifacts, and continue independent permitted work. Do not claim refreshed CLI state, guess a different change/root, or silently install, initialize, or reconfigure OpenSpec.

## Read the active contract

Use the returned schema, artifact dependencies, and `contextFiles` map (artifact IDs to arrays of concrete paths). Read the listed context files needed by the selected action. Do not assume a fixed proposal/design/specs/tasks layout or reconstruct paths from the working directory. Check the current contents when resuming; a checkpoint does not freeze manually edited requirements.

Consider project `context` and `operationGuidance` alongside the requested scope and workflow constraints. They do not override CLI state, expand permissions, or establish completion. Report material conflicts instead of silently weakening requirements.

Keep the schema's tracking artifact as the durable task source. A session plan may summarize dependencies, owners, and evidence, but should not become a second independently maintained backlog. Map each material requirement to its implementation and suitable evidence in the existing artifacts or handoff. Reuse any canonical API/event schema; an OpenSpec behavior specification does not replace the wire contract.

## Implement and establish completion

Honor a CLI `blocked` state: resolve the reported missing artifacts or tracking problem within scope before implementation. Do not fabricate files or checkboxes just to advance state. Continue unaffected work where possible.

Treat `ready` as workflow readiness and `all_done` as recorded task progress. In the reviewed CLI, `all_done` is computed from checked tasks, not passing application tests. Inspect the actual implementation and current evidence before reporting behavioral completion. If checked tasks contradict the code, reconcile them within authorized edit scope; in read-only work, report the discrepancy without changing them.

Use [changes](changes.md) and [runtime verification](verification.md) for the affected behavior. Mark tasks complete only after their specified outcome is implemented and the task's required verification is satisfied; report unavailable checks separately. The official verify skill can assess completeness, correctness, and design coherence, but a verification report or schema validation alone does not prove runtime behavior. Keep quality judgments and executed checks distinct.

Assign one writer to shared specifications and tracking artifacts. Communicate changed requirements or contracts before dependent work proceeds. When implementation reveals a scope decision, resolve it without silently dropping scenarios, narrowing the requirement, or overriding an explicit planning-only request.

## Sync and archive within the requested endpoint

Syncing modifies the main specifications; archiving moves the change. Perform them when included in the requested endpoint or applicable established workflow, after reconciling implementation evidence. Preserve unrelated requirements and existing scenarios when applying deltas. Finish and verify sync before archiving; do not race shared writes. Neither operation establishes that code was merged or deployed.

When the endpoint is implementation or review only, report that result and any remaining lifecycle work without doing it automatically. Use [sources](sources.md) for the reviewed CLI/template revision and adaptation limits.
