# Tact plugin

**Tact — Make the right change.** The plugins give Codex and Claude Code the same [engineering guidance](../README.md#four-principles) in this repository.

Use the [installation guide](installation.md) to install, update, or remove the plugin.

## Package and marketplace

The repository contains a marketplace and plugin manifest for each host. Both package the same skills-only plugin from the repository root.

| File | Purpose |
| --- | --- |
| [`.agents/plugins/marketplace.json`](../.agents/plugins/marketplace.json) | Lists the Codex `tact` marketplace and its `tact` plugin. |
| [`.codex-plugin/plugin.json`](../.codex-plugin/plugin.json) | Defines the Codex plugin name, version, display fields, and `./skills/` source. |
| [`.claude-plugin/marketplace.json`](../.claude-plugin/marketplace.json) | Lists the Claude Code `tact` marketplace and its `tact` plugin. |
| [`.claude-plugin/plugin.json`](../.claude-plugin/plugin.json) | Defines the Claude Code plugin name, version, metadata, and `./skills/` source. |
| [`skills/`](../skills/) | Provides the single `tact` skill included in both plugins. |

The Codex catalog sets `source.path` to `"./"`; the Claude Code catalog sets `source` to `"./"`. Both paths are relative to the marketplace repository root and select the root plugin. No second skill copy is necessary. Keep skills outside `.claude-plugin/`; that directory holds Claude Code's manifests only.

Claude Code exposes the skill as `/tact:tact`. The skill's `agents/openai.yaml` provides Codex UI metadata; Claude Code reads `skills/tact/SKILL.md` directly.

The skills use the host's tools. The package includes no MCP server, hooks, scheduler, or agent runtime.

## Test a local checkout

Use an isolated configuration for the host under test. A local marketplace named `tact` can otherwise replace an existing Git marketplace with that name.

### Codex

Register the checkout as the marketplace source. Then install the plugin.

```bash
codex plugin marketplace add /absolute/path/to/tact
codex plugin add tact@tact
```

Use the actual checkout path. Its directory name does not have to be `tact`.

`codex plugin marketplace upgrade` refreshes Git marketplaces; it does not upgrade a local-path marketplace. After changing a local source, use the remove/reinstall procedure in the isolated test configuration and verify the installed version and file contents separately. Local-path tests do not establish the Git marketplace upgrade behavior.

### Claude Code

From the repository root, use a temporary configuration directory in a subshell:

```bash
(
  export CLAUDE_CONFIG_DIR="$(mktemp -d)"
  claude plugin validate .claude-plugin/plugin.json --strict &&
  claude plugin validate .claude-plugin/marketplace.json --strict &&
  claude plugin marketplace add "$PWD" &&
  claude plugin install tact@tact &&
  claude plugin list
)
```

Validate both files explicitly because the root contains a marketplace and a plugin manifest. The temporary configuration keeps test installation out of your normal Claude Code settings.

To test skill invocation with your usual Claude Code authentication without registering a marketplace, start a session from the checkout:

```bash
claude --plugin-dir "$PWD"
```

Invoke `/tact:tact` with a concrete task. This loads the local plugin for that session. It does not establish that installation or updates from GitHub work.

### Host behavior

In a new conversation, test implementation, planning, review, a small README edit, and task resumption. To test automatic skill selection, do not specify a skill name.

Record the host version, OS, source commit, installation method, and skill names shown by the host. Record the resources loaded, changes made, and task result. A correct answer alone does not show which skill the host loaded.

## Maintain and validate

Keep both hosts' marketplace and plugin names consistent with `tact@tact`. Keep source paths inside the marketplace root and both manifests pointing at `./skills/`. Retain Codex's policy, category, and interface fields in its own files; do not copy host-specific fields into Claude Code's manifests.

Update both plugin versions together when the package changes, and keep the README version aligned. Use the [repository checks](../CONTRIBUTING.md) to validate skill metadata and references.

For Claude Code, run `claude plugin validate` on each `.claude-plugin/` JSON file and test installation in an isolated configuration. See the official [manifest reference](https://code.claude.com/docs/en/plugins-reference) and [marketplace guide](https://code.claude.com/docs/en/plugin-marketplaces). For Codex, run Plugin Creator's `validate_plugin.py` if available. Also test installation in the affected host.

Report structural checks separately from CLI and host tests. Repository validation does not prove successful installation or skill discovery. Repository marketplace distribution does not submit the plugin to OpenAI's or Anthropic's public directory.
