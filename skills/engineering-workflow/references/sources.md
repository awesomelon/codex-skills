# Sources and adaptation

Checked: 2026-09-19. Engineering Workflow is an independent adaptation of the source below. It is not a complete mirror or an official package from the upstream author or platform providers.

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

- Replace platform-specific frontmatter, sticky mode, slash commands, `Task` parameters, named model slugs, and custom agent requirements with ordinary skill metadata and available runtime capabilities. Automatic selection remains enabled by default.
- Replace the 23-playbook root and principle-loading cascade with a short router and selectively loaded references. Existing specialist guards remain optional; no instruction requires reading every skill or principle.
- Remove automatic PR creation, blanket external-action permission, unrelated follow-up PRs, destructive worktree recovery, and simulator/cache cleanup. Task requests determine the endpoint.
- Replace mandatory worker panels, fixed cloud lane counts, and agreement-as-confidence with scoped delegation and artifact verification. No Bun runtime, orchestration database, watcher, webhook, or provider setup is bundled.
- Correct ambiguous read-only diagnosis/prototype routing, stale continuation claims, and CI classification by file location. Retain needed validation and external API compatibility rather than treating deletion as success.
- Omit prose rewriting, comment stripping, bot UI generation, transcript mining, skill self-modification, and the Benny automation pack. Those are separate capabilities, not prerequisites for engineering execution.

## Authoring sources

The following official pages were fetched during this adaptation:

- [Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra): concise discovery, conditional detail, and outcome-based completion informed the package structure.
- [Build skills](https://learn.chatgpt.com/docs/build-skills): `SKILL.md`, progressive disclosure, and optional UI metadata.
- [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents): use available delegation capabilities and configured defaults; capabilities and tool names can vary by runtime.

This source review is separate from behavioral validation. Installation and metadata checks do not establish automatic selection, better task outcomes, lower token usage, or superiority to upstream.
