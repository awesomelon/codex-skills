<p align="center">
  <img src="assets/logo.png" width="180" alt="CraftFlow: an open code book supporting connected modules">
</p>

# CraftFlow

**Make the right change.**

Judgment-driven engineering for Codex: understand the problem, choose a proportionate change, and verify the result.

## Why CraftFlow

Working code is one part of a successful change. The change also needs to address the actual problem, respect existing contracts, and leave the next change understandable. CraftFlow brings those decisions into planning, implementation, and review, with focused technical expertise where it helps.

Use it when a proposed solution needs scrutiny, a change crosses responsibilities, or several plausible implementations have different maintenance costs. A clear local request can go straight to execution.

## Three principles

| Principle | What it means in practice |
| --- | --- |
| **Understand the problem.** | Separate the symptom from its cause and connect the proposed change to the intended outcome. Reuse settled decisions; bring consequential unresolved user choices back with evidence and a recommendation. |
| **Change what the problem requires.** | Repair a local cause locally and a shared cause at its owner. Judge scope by current requirements, affected consumers, and future change cost. Preserve useful complexity and independently changing policies. |
| **Verify the result.** | Connect completion claims to checks that actually ran. Distinguish working behavior, maintainability judgment, measured performance, and remaining uncertainty. |

These are decision criteria applied at the relevant depth, not required phases. Planning may end with a recommendation; implementation includes relevant verification; review preserves the assessed code. A small edit needs no new specification, review panel, or learning document.

## Use

Ask for the outcome and scope you want:

```text
Use $craftflow-orchestrator to assess whether this migration solves the reported
problem and propose a plan. Do not edit code.

Use $craftflow-orchestrator to implement the approved change and verify integration.

Use $craftflow-react to review this form's state and request behavior without edits.
```

For example, a request to split a large module calls for examining what changes together and what changes independently. File length alone does not establish the right boundary. The useful result explains the chosen boundary, its effect on change cost, and the behavior that must remain intact.

The orchestrator owns scope, dependencies, and completion. Specialists support the technical decisions within that work and can also be used independently. Delegation is an execution choice when independent work warrants it. Preserve project learning when verified, non-obvious reasoning will improve a future decision and writing it is in scope.

In a plugin host, use the skill names advertised by that host; they may include a plugin prefix.

## Install on a new Mac

Requires Git and macOS Bash; no Python or package installation. Keep the clone in a permanent location because the installer creates symlinks by default.

```bash
git clone https://github.com/awesomelon/craftflow.git
cd craftflow
bash scripts/install.sh --list
bash scripts/install.sh --skill craftflow-orchestrator --dry-run
bash scripts/install.sh --skill craftflow-orchestrator
```

Run each command after the previous one succeeds. Skills install into `~/.agents/skills`; configuration and `AGENTS.md` are left untouched. Repeat `--skill <name>` to select more skills, or omit it to install all seven.

[Update, copy mode, and migration](docs/installation.md) · [Plugin installation](docs/plugin.md)

Choose one installation route per skill to avoid duplicate discovery.

## Included skills

| Skill | Decision it supports |
| --- | --- |
| [craftflow-orchestrator](skills/craftflow-orchestrator/SKILL.md) | What deserves attention, how dependent work fits together, and when the outcome is complete. |
| [craftflow-architecture](skills/craftflow-architecture/SKILL.md) | Where responsibilities belong and which boundaries and contracts must hold. |
| [craftflow-code-quality](skills/craftflow-code-quality/SKILL.md) | What makes the next change costly and which rules should have one owner. |
| [craftflow-refactoring](skills/craftflow-refactoring/SKILL.md) | How to carry out a structural improvement while preserving observable behavior. |
| [craftflow-react](skills/craftflow-react/SKILL.md) | How components, hooks, state, and rendering preserve the intended interaction. |
| [craftflow-tanstack-query](skills/craftflow-tanstack-query/SKILL.md) | How Query v5 reads and writes keep server data correct across consumers. |
| [craftflow-typescript](skills/craftflow-typescript/SKILL.md) | Which guarantees belong in types and which require runtime validation. |

## Documentation

- [Guides and design history](docs/README.md)
- [Contributing and validation](CONTRIBUTING.md)
- [Evaluation evidence](evals/README.md)

Built around [OpenAI's skill-authoring guidance](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra): concise entrypoints, details loaded when needed, and work sized to the task. Staff-level judgment is the design goal; evaluation records describe what was actually tested.
