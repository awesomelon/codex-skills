<p align="center">
  <img src="assets/logo.png" width="180" alt="Codex Skills: an open code book supporting connected modules">
</p>

# codex-skills

Engineering orchestration for Codex: choose worthwhile problems, plan dependent work, and deliver verified changes with focused technical skills.

Use the seven skills independently or as the **Engineering Orchestration** plugin. The orchestrator coordinates work; the guards provide expertise. Small tasks stay small, and delegation is optional.

## Install on a new Mac

Requires Git and macOS Bash; no Python or package installation. Keep the clone in a permanent location because the installer creates symlinks by default.

```bash
git clone https://github.com/awesomelon/codex-skills.git
cd codex-skills
bash scripts/install.sh --list
bash scripts/install.sh --skill engineering-orchestrator --dry-run
bash scripts/install.sh --skill engineering-orchestrator
```

Run each command after the previous one succeeds. Skills install into `~/.agents/skills`; configuration and `AGENTS.md` are left untouched. Repeat `--skill <name>` to select more skills, or omit it to install all seven.

[Update, copy mode, and migration](docs/installation.md) · [Plugin installation](docs/plugin.md)

Choose one installation route per skill to avoid duplicate discovery.

## Use

Ask for the outcome and the scope you want:

```text
Use $engineering-orchestrator to plan this migration without editing code.

Use $engineering-orchestrator to implement the approved change and verify integration.

Use $react-quality-guard to review the current changes without editing files.
```

In a plugin host, use the skill names advertised by that host; they may include a plugin prefix. Reviews and plans preserve the assessed code. Implementation requests include relevant verification.

## Included skills

| Skill | Use it for |
| --- | --- |
| [engineering-orchestrator](skills/engineering-orchestrator/SKILL.md) | Priorities, planning, dependent work, and resuming interrupted tasks. |
| [architecture-guard](skills/architecture-guard/SKILL.md) | Module boundaries, dependencies, ownership, and contracts. |
| [code-quality-guard](skills/code-quality-guard/SKILL.md) | Shared rules, maintainability, and evidence-based quality reviews. |
| [refactoring-guard](skills/refactoring-guard/SKILL.md) | Structural improvements that preserve behavior. |
| [react-quality-guard](skills/react-quality-guard/SKILL.md) | Components, composition, hooks, state, and performance. |
| [tanstack-query-guard](skills/tanstack-query-guard/SKILL.md) | Query v5 caching, mutations, pagination, SSR, and persistence. |
| [typescript-quality-guard](skills/typescript-quality-guard/SKILL.md) | Type modeling, narrowing, diagnostics, and runtime validation. |

## Documentation

- [Guides and design history](docs/README.md)
- [Contributing and validation](CONTRIBUTING.md)
- [Evaluation evidence](evals/README.md)

Built around [OpenAI's skill-authoring guidance](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra): concise entrypoints, details loaded when needed, and work sized to the task. Staff-level judgment is the design goal; evaluation records describe what was actually tested.
