<p align="center">
  <img src="assets/banner-tact.png" width="100%" alt="Tact — Make the right change.">
</p>

# Tact

**Make the right change.**

Tact is one skill for deliberate engineering in Codex and Claude Code: understand the task, choose a simple solution, keep edits focused, and verify the result.

**Version 0.0.5.** Use `$tact` in Codex or `/tact:tact` in Claude Code for implementation, debugging, refactoring, planning, review, and engineering decision records.

## Four principles

| Principle | What it changes |
| --- | --- |
| **Understand before acting.** | Investigate available facts, expose consequential assumptions, and clarify intent when different outcomes remain plausible. |
| **Prefer the simplest sufficient solution.** | Use existing capabilities, preserve useful information, and add complexity only for a concrete need. |
| **Keep changes tied to the request.** | Repair the responsible code and necessary consumers while preserving unrelated work and behavior. |
| **Work toward an observable result.** | Define success, check the relevant final state, and limit completion claims to the evidence. |

Tact keeps its reports easy to use: answer first, choose formatting to fit the content, describe concrete changes and evidence, and keep project terms consistent. Preserve important conditions and enough depth for the request. Short reporting does not mean incomplete work. Requested output formats take precedence.

## Use

Each Codex example is an independent request:

```text
Use $tact to fix this save-and-reload bug and verify the repair.

Use $tact to review this change for correctness and unnecessary complexity.
Do not edit files.

Use $tact to plan this migration. Explain the tradeoffs before implementation.

Use $tact to refactor this parser while preserving its public behavior.

Use $tact to implement this storage change and preserve the decision rationale.

Use $tact to record our agreed API compatibility policy as an ADR.
Do not change the implementation.
```

The requested outcome sets the scope. Planning and review preserve the assessed material. Implementation carries through the authorized change and relevant checks. There is no required assessment stage before coding.

During implementation, Tact keeps affected documentation current and preserves missing context that would prevent a mistaken change or repeated investigation later. It reuses existing documentation and creates an ADR only when the rationale needs an independent record. No new document is needed when the available context is sufficient. Documentation-only requests produce the requested artifact without implementing the decision.

Use the skill name displayed by your host; a plugin prefix may be present. In Claude Code, invoke the same skill with its plugin namespace:

```text
/tact:tact Fix this save-and-reload bug and verify the repair.

/tact:tact Review this change for correctness and unnecessary complexity. Do not edit files.
```

## Install as a Codex plugin

With Git and a Codex CLI that supports plugins, run these commands in order:

```bash
codex plugin marketplace add awesomelon/tact
codex plugin add tact@tact
```

Run the second command after the first succeeds. This installs the **published** repository version. An unpublished local version requires the [local checkout procedure](docs/plugin.md#test-a-local-checkout).

## Install as a Claude Code plugin

With Git and a Claude Code CLI that supports plugins, run these commands in order:

```bash
claude plugin marketplace add awesomelon/tact
claude plugin install tact@tact
```

Run the second command after the first succeeds. This installs the **published** repository version. Restart Claude Code and invoke `/tact:tact`. For an unpublished revision, use the [local checkout procedure](docs/plugin.md#test-a-local-checkout).

Both plugins package the same `skills/` source as the standalone installer. They supply no agent runtime, hooks, MCP server, model settings, or lint dependency.

For installation and updates, see [the installation guide](docs/installation.md). The [macOS standalone installer](docs/installation.md#standalone-installation-on-macos) requires no Python.

## Included skill

| Skill | Purpose |
| --- | --- |
| [tact](skills/tact/SKILL.md) | Implement, debug, refactor, plan, and review code with explicit assumptions, focused changes, concrete code-quality defaults, and claim-specific verification. Maintain affected documentation and preserve otherwise missing context needed for future decisions. Report specific outcomes with consistent project terms and formatting suited to the content. Preserve assessed files during planning and review. |

Use [code evidence](skills/tact/references/code-evidence.md) for TypeScript or JavaScript contracts, assertions, collections, and testing seams; it routes Effect projects to a dedicated reference. [Decision documentation](skills/tact/references/decision-documentation.md) covers record selection, existing conventions, and ADR history. [Verification](skills/tact/references/verification.md) covers regression evidence and completion claims. [Communication](skills/tact/references/communication.md) covers concise reports, requested depth, and exact output formats. These are self-contained internal guides, not a bundled linter or a required sequence of stages.

## Documentation

- [Installation and updates](docs/installation.md)
- [Plugin packaging](docs/plugin.md)
- [Contributing and validation](CONTRIBUTING.md)
- [Evaluation scenarios and evidence](evals/README.md)

## License

[MIT](LICENSE).
