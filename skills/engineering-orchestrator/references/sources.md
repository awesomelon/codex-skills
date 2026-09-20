# Sources and adaptation

Checked: 2026-09-20. Engineering Orchestrator (formerly Engineering Workflow and pstack) is an independent adaptation of the sources below. It is not a complete mirror or an official package from the upstream authors or platform providers.

## Pinned upstream

Lauren Tan's [pstack in cursor/plugins](https://github.com/cursor/plugins/tree/032be146865d973682535de75f2287da438550bf/pstack), commit `032be146865d973682535de75f2287da438550bf`. The original MIT notice is preserved unchanged in [LICENSE](../LICENSE), including in standalone installations.

The main entrypoint, selected supporting skills, and engineering playbooks were inspected. This adaptation does not claim a line-by-line audit of every upstream file or automation.

| Upstream material under pstack/skills | Local decision |
| --- | --- |
| `poteto-mode/SKILL.md`, investigation and trace-forensics playbooks, `how`, `why` | Select task-specific evidence; separate current behavior from recorded intent and hypotheses. |
| Bug-fix, feature, refactoring, prototype, visual-parity playbooks | Preserve reproduction and observable contracts; allow focused work without mandatory delegation or competing designs. |
| Perf-issue and hillclimb playbooks | Keep representative before/after measurement and accepted/rejected experiments. |
| `interrogate`, babysit, shipping, opening-a-pr | Validate findings and the reviewed revision; distinguish status, repair, monitoring, and delivery authority. |
| `swarm`, `arena`, orchestrate and autonomous-run | Use bounded delegation and verified integration when useful, without a separate fleet runtime. |
| Session-pickup and pause-safely | Reconcile current state with prior evidence; preserve useful work without automatic WIP commits. |

## Deliberate changes

### Additional port review

[michael-denyer/pstack-claude](https://github.com/michael-denyer/pstack-claude/tree/af7aa63b5e196cb3d04fbe18dc2a970918fc883a), commit `af7aa63b5e196cb3d04fbe18dc2a970918fc883a`, was inspected separately on 2026-09-19. Selected source paths under `plugins/pstack/skills/`:

- `create-verification-skill/SKILL.md`: adapt public-path checks, instance identity, side-effect observation, and evidence-preserving cleanup into [runtime verification](verification.md). Reuse existing drivers; do not generate a verification skill on every task.
- `poteto-mode/playbooks/shipping.md` and `poteto-mode/references/merge-safety.md`: add service-enforced head conditions, distinguish future merge requests, and confirm the destination after an authorized merge in [delivery](review-and-delivery.md). No watcher or forge-specific script is bundled.
- `poteto-mode/references/codex-tools.md`, `playbooks/orchestrate.md`, `playbooks/session-pickup.md`, and `references/resume-storage.md`: retain capability-based tools, existing scoped handoffs, and checkpoint reconciliation. Do not import fixed model panels, automatic hooks, global settings, or a new checkpoint store.

The port carries the same Lauren Tan MIT notice already preserved in [LICENSE](../LICENSE). These are independently worded, selective adaptations, not a full port, a runtime compatibility certification, or measured speed/token improvements. The Astra authoring article below was freshly fetched for this review; conditional detail stays outside the discovery description.

### Existing adaptations

- Replace platform-specific frontmatter, sticky mode, slash commands, `Task` parameters, named model slugs, and custom agent requirements with ordinary skill metadata and available runtime capabilities. Automatic selection remains enabled by default.
- Replace the 23-playbook root and principle-loading cascade with a short router and selectively loaded references. Existing specialist guards remain optional; no instruction requires reading every skill or principle.
- Remove automatic PR creation, blanket external-action permission, unrelated follow-up PRs, destructive worktree recovery, and simulator/cache cleanup. Task requests determine the endpoint.
- Replace mandatory worker panels, fixed cloud lane counts, and agreement-as-confidence with scoped delegation and artifact verification. No Bun runtime, orchestration database, watcher, webhook, or provider setup is bundled.
- Correct ambiguous read-only diagnosis/prototype routing, stale continuation claims, and CI classification by file location. Retain needed validation and external API compatibility rather than treating deletion as success.
- Omit prose rewriting, comment stripping, bot UI generation, transcript mining, skill self-modification, and the Benny automation pack. Those are separate capabilities, not prerequisites for engineering execution.

## Ponytail

Checked 2026-09-20: [Ponytail](https://github.com/DietrichGebert/ponytail/blob/e3ba2aa6f1e6f0bc4d69eb09c9f0d0a93af56156/skills/ponytail/SKILL.md) and its sibling `ponytail-review/SKILL.md`. The [MIT notice](../THIRD_PARTY_NOTICES.md) is retained for standalone installs. [Changes](changes.md) adapts bounded reuse selection and shared-cause repair. Sticky modes, blanket activation, line-count targets, and reduced user scope are not adopted.

## Authoring sources

### Staff engineering judgment

Freshly read on 2026-09-20: [How I Find Problems to Solve as a Staff Engineer](https://lalitm.com/post/find-problems-staff-engineer/) by Lalit Maganti. Its problem-discovery perspective informs [problem selection](problem-selection.md). [Execution strategy](execution-strategy.md) extends the collection's own delivery guidance to connect prioritization, uncertain design decisions, adoption, and outcome evidence. These are original decision aids, not a copy of the article or a guarantee of staff-level performance. Its organizational context is not assumed to apply everywhere.

The designated Astra article was freshly read for this revision too. The existing coordinator gains two conditional references and a specific discovery trigger; no new overlapping skill, fixed thinking ritual, or required agent panel is added.

### ECC and OpenSpec concepts

Reviewed on 2026-09-20: [ECC](https://github.com/affaan-m/ECC/tree/934195f955cf0da847d59fcd6f68856bce112d8b), commit `934195f955cf0da847d59fcd6f68856bce112d8b`, and [OpenSpec](https://github.com/Fission-AI/OpenSpec/tree/bae58cf61479986431bb798acbe5a688a591c18c), commit `bae58cf61479986431bb798acbe5a688a591c18c` (CLI 1.13.1). Their MIT notices are preserved in [third-party notices](../THIRD_PARTY_NOTICES.md). Upstream code, installers, and generated skills are not bundled.

- ECC `skills/intent-driven-development/SKILL.md` and `skills/contract-first/SKILL.md` inform acceptance conditions and producer/consumer evidence in [changes](changes.md). Reuse existing product artifacts and schemas; omit mandatory discovery interviews, new documents, or new schema tools for small work.
- ECC `skills/search-first/SKILL.md` and `skills/iterative-retrieval/SKILL.md` inform bounded reuse searches and missing-context handoffs. Omit fixed search cycles, score thresholds, and mandatory researcher agents.
- ECC `skills/agent-eval/SKILL.md` and `skills/skill-stocktake/SKILL.md` inform repository evaluation and maintenance practices, outside the installed task workflow. No external evaluation CLI, background learning, or session-observation hooks are dependencies.
- OpenSpec's `schemas/spec-driven/schema.yaml` and `src/core/templates/workflows/{propose,verify-change,sync-specs}.ts` inform [spec-driven changes](spec-driven-changes.md): distinguish intent, required behavior, and design; describe added/modified/removed behavior; connect tasks to evidence; and reconcile accepted specifications with verified outcomes. Reuse ordinary issues, plans, and documents. No CLI, generated skill, workflow schema, file layout, or archive process is required.

OpenSpec Plus at `311dd818f2de99d38c1f0a144fc4946895d6aed4` and Superpowers OpenSpec Team Skills at `1426ddcb85f203c7de8a13b5d1ba4cfd188fb265` were also inspected. Their additional execution coordinators, recurring review panels, and overlapping plan stores are not imported. No blanket claim of upstream incompatibility or comparative performance is made.

An initial CLI adapter was recorded in commit `08b4044c7b466a0fdc1e6cf2abeeb845fd5c1116`. The user clarified that the intended scope is conceptual adoption; the adapter and setup guide were removed. Historical evaluation inputs and results retain the original scope and are not evidence for the replacement guidance.

The designated Astra article was fetched during this revision. Keep discovery descriptions unchanged, put conditional change-management detail behind a task-specific link, and extend existing decision guidance instead of adding another orchestration skill. These are local design choices; the article does not prescribe this adaptation.

For the orchestration revision, the designated Astra article was fetched again on 2026-09-19. The entrypoint now centers on task dependencies, skill selection, ownership, and verified integration; execution playbooks remain conditional support. Agent dispatch and recovery details stay in one coordination reference. These are local design choices informed by the article, not claims that it prescribes a particular multi-agent architecture. No new upstream pstack audit was performed for this revision.

The following official pages were fetched during this adaptation:

- [Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra): concise discovery, conditional detail, and outcome-based completion informed the package structure.
- [Build skills](https://learn.chatgpt.com/docs/build-skills): `SKILL.md`, progressive disclosure, and optional UI metadata.
- [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents): use available delegation capabilities and configured defaults; capabilities and tool names can vary by runtime.

This source review is separate from behavioral validation. Installation and metadata checks do not establish automatic selection, better task outcomes, lower token usage, or superiority to upstream.
