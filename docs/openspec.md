# Optional OpenSpec integration

Use OpenSpec when a project benefits from persistent change proposals, behavioral specifications, and tracked implementation work. Keep normal edits on the existing direct or specialist path unless the request or repository policy requires a specification workflow. The seven skills and macOS shell installer remain usable without OpenSpec or Node.js.

## Ownership

| Component | Responsibility |
| --- | --- |
| Official OpenSpec CLI and generated skills | Resolve the selected change, schema, artifact instructions, task state, synchronization, and archive operations. |
| Engineering Orchestrator | Coordinate dependencies, expertise, task ownership, implementation, and current integration evidence. |
| Existing API/event schema | Define the canonical wire representation for producers and consumers. |
| Specialist guards and project checks | Assess domain quality and verify observable behavior. |

Choose one execution coordinator per change. For a direct OpenSpec operation, use the official generated skill. For dependent work across components, invoke the orchestrator and name the selected change. Its [conditional adapter](../skills/engineering-orchestrator/references/openspec.md) reads CLI instructions without starting another apply coordinator. Use the schema's tracking artifact as the durable task source.

## Pilot setup

The reviewed baseline is **OpenSpec 1.13.1**, whose CLI requires **Node.js 20.19.0 or later**. This is a pilot compatibility baseline, not a requirement to downgrade an existing installation. Check the project's installed version and help first. Later versions and custom schemas need their own compatibility check.

For a project where installing and initializing OpenSpec is desired, these are upstream setup commands with a pinned pilot version. Run each only after the preceding one succeeds, in the intended application project rather than this skills repository:

```bash
npm install -g @fission-ai/openspec@1.13.1
openspec --version
openspec init --tools codex --profile core
```

Installation changes the selected npm prefix, and init creates project artifacts and generated skills. These are setup instructions, not actions performed by the skill installer or automatically by the adapter. For an already initialized project, reconcile existing generated files and use the project's documented `openspec update` flow when an update is intended; do not initialize it again or overwrite local customizations blindly.

Codex uses `.agents/skills/openspec-*/SKILL.md`. The core profile contains propose, explore, apply, update, sync, and archive; verify is an optional expanded workflow. Do not change a user's global workflow profile just to add this integration. Resolve actual invocation names from the host catalog, including plugin prefixes where present.

## Requests and endpoints

```text
Use $engineering-orchestrator to implement the selected OpenSpec change add-document-pagination and verify the integrated API and UI behavior. Preserve the specified compatibility. Stop after local implementation and verification.

Use $engineering-orchestrator to review whether the selected OpenSpec change is actually complete. Do not modify any files.
```

For a proposal-only request, invoke the official `$openspec-propose` skill when installed. It stops at planning artifacts. For direct implementation, the official generated skill is `$openspec-apply-change`; `$openspec-verify-change` is available only if that workflow was generated. Skill invocations are prompts to Codex, not shell commands.

CLI `all_done` reflects checked tasks. It does not establish passing tests, real runtime behavior, a merged PR, or a deployed release. Use current requirement-to-implementation evidence before reporting completion. Sync and archive follow the requested endpoint; an implementation-only request does not automatically authorize them.

## Compatibility scope and sources

Start with a single repository and selected change. External stores and cross-repository worksets are outside this pilot's executed coverage. The adapter preserves CLI-resolved paths and scope constraints rather than hardcoding the default directory layout. If the CLI is missing, continue useful permitted artifact inspection and report that live state was not refreshed; do not claim OpenSpec installation or integration was verified.

Sources inspected at OpenSpec commit `bae58cf61479986431bb798acbe5a688a591c18c`:

- [CLI setup and profiles](https://github.com/Fission-AI/OpenSpec/blob/bae58cf61479986431bb798acbe5a688a591c18c/docs/cli.md).
- [Codex support and invocations](https://github.com/Fission-AI/OpenSpec/blob/bae58cf61479986431bb798acbe5a688a591c18c/docs/supported-tools.md).
- [Node.js requirement](https://github.com/Fission-AI/OpenSpec/blob/bae58cf61479986431bb798acbe5a688a591c18c/package.json).
- [Apply state calculation](https://github.com/Fission-AI/OpenSpec/blob/bae58cf61479986431bb798acbe5a688a591c18c/src/commands/workflow/instructions.ts).

The [evaluation record](../evals/contracts-openspec-2026-09-20/results.md) distinguishes offline behavioral cases from live CLI or native Codex discovery validation.
