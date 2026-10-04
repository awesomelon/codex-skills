<p align="center">
  <img src="assets/banner-tact.png" width="100%" alt="Tact — Make the right change.">
</p>

# Tact

**Make the right change.**

Tact is one Codex skill for deliberate engineering: understand the task, choose a simple solution, keep edits focused, and verify the result.

**Version 0.0.1.** Use `$tact` for implementation, debugging, refactoring, planning, and review.

## Four principles

| Principle | What it changes |
| --- | --- |
| **Understand before acting.** | Investigate available facts, expose consequential assumptions, and clarify intent when different outcomes remain plausible. |
| **Prefer the simplest sufficient solution.** | Use existing capabilities, preserve useful information, and add complexity only for a concrete need. |
| **Keep changes tied to the request.** | Repair the responsible code and necessary consumers while preserving unrelated work and behavior. |
| **Work toward an observable result.** | Define success, check the relevant final state, and limit completion claims to the evidence. |

Tact keeps its reports easy to use: answer first, short paragraphs with bold arrow lead-ins when useful, important conditions intact, and enough depth for the request. Short reporting does not mean incomplete work. Requested output formats take precedence.

## Use

Each example is an independent request:

```text
Use $tact to fix this save-and-reload bug and verify the repair.

Use $tact to review this change for correctness and unnecessary complexity.
Do not edit files.

Use $tact to plan this migration. Explain the tradeoffs before implementation.

Use $tact to refactor this parser while preserving its public behavior.
```

The requested outcome sets the scope. Planning and review preserve the assessed material. Implementation carries through the authorized change and relevant checks. There is no required assessment stage before coding.

Use the skill name displayed by your host; a plugin prefix may be present.

## Install as a Codex plugin

With Git and a Codex CLI that supports plugins, run these commands in order:

```bash
codex plugin marketplace add awesomelon/tact
codex plugin add tact@tact
```

Run the second command after the first succeeds. This installs the **published** repository version. An unpublished local version requires the [local checkout procedure](docs/plugin.md#test-a-local-checkout).

The plugin packages the same `skills/` source as the standalone installer. It supplies no agent runtime, hooks, MCP server, model settings, or lint dependency.

For installation and updates, see [the installation guide](docs/installation.md). The [macOS standalone installer](docs/installation.md#standalone-installation-on-macos) requires no Python.

## Included skill

| Skill | Purpose |
| --- | --- |
| [tact](skills/tact/SKILL.md) | Implement, debug, refactor, plan, and review code with explicit assumptions, focused scope, and evidence for the result. Preserve assessed files during planning and review. |

The skill links to [code evidence](skills/tact/references/code-evidence.md) for TypeScript or JavaScript decisions and [communication](skills/tact/references/communication.md) for reports and detailed explanations. Both are self-contained internal guides.

## Documentation

- [Installation and updates](docs/installation.md)
- [Plugin packaging](docs/plugin.md)
- [Contributing and validation](CONTRIBUTING.md)
- [Evaluation scenarios and evidence](evals/README.md)

## License

[MIT](LICENSE).
