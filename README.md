<p align="center">
  <img src="assets/logo.png" width="180" alt="CraftFlow: an open code book supporting connected modules">
</p>

# CraftFlow

Engineering orchestration for Codex: choose worthwhile problems, plan dependent work, and deliver verified changes with focused technical skills.

Use the seven skills independently or as the **CraftFlow** plugin. The orchestrator coordinates work; the specialists provide expertise. Small tasks stay small, and delegation is optional.

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

## Use

Ask for the outcome and the scope you want:

```text
Use $craftflow-orchestrator to plan this migration without editing code.

Use $craftflow-orchestrator to implement the approved change and verify integration.

Use $craftflow-react to review the current changes without editing files.
```

In a plugin host, use the skill names advertised by that host; they may include a plugin prefix. Reviews and plans preserve the assessed code. Implementation requests include relevant verification.

## Included skills

| Skill | Use it for |
| --- | --- |
| [craftflow-orchestrator](skills/craftflow-orchestrator/SKILL.md) | Priorities, planning, dependent work, and resuming interrupted tasks. |
| [craftflow-architecture](skills/craftflow-architecture/SKILL.md) | Module boundaries, dependencies, ownership, and contracts. |
| [craftflow-code-quality](skills/craftflow-code-quality/SKILL.md) | Diagnosing maintainability, comparing designs, and choosing shared-rule ownership. |
| [craftflow-refactoring](skills/craftflow-refactoring/SKILL.md) | Planning and executing chosen structural changes while preserving behavior. |
| [craftflow-react](skills/craftflow-react/SKILL.md) | Components, composition, hooks, state, and performance. |
| [craftflow-tanstack-query](skills/craftflow-tanstack-query/SKILL.md) | Query v5 caching, mutations, pagination, SSR, and persistence. |
| [craftflow-typescript](skills/craftflow-typescript/SKILL.md) | Type modeling, narrowing, diagnostics, and runtime validation. |

## Documentation

- [Guides and design history](docs/README.md)
- [Contributing and validation](CONTRIBUTING.md)
- [Evaluation evidence](evals/README.md)

Built around [OpenAI's skill-authoring guidance](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra): concise entrypoints, details loaded when needed, and work sized to the task. Staff-level judgment is the design goal; evaluation records describe what was actually tested.
