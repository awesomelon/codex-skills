# CraftFlow plugin

**CraftFlow — Make the right change.** The plugin packages the [judgment-driven engineering approach](../README.md#three-principles) for Codex. Use the [installation guide](installation.md) to install from GitHub, update, or migrate from individual skills.

## Package and marketplace

The repository contains one marketplace and one skills-only plugin:

| File | Purpose |
| --- | --- |
| [`.agents/plugins/marketplace.json`](../.agents/plugins/marketplace.json) | Advertises the `craftflow` marketplace and its `craftflow` plugin. |
| [`.codex-plugin/plugin.json`](../.codex-plugin/plugin.json) | Defines the plugin identity, version, presentation, and `./skills/` source. |
| [`skills/`](../skills/) | Single source for all seven skills, also usable independently. |

The catalog uses `source.path: "./"`, relative to the marketplace's repository root. This resolves to the existing root plugin; no second plugin directory or copied skill tree is required. The plugin provides guidance using the host's tools and bundles no MCP server, hooks, scheduler, or agent runtime.

## Test a local checkout

Contributors can register a checkout as the marketplace source:

```bash
codex plugin marketplace add /absolute/path/to/craftflow
codex plugin add craftflow@craftflow
```

Use an isolated Codex test configuration so the local source does not replace an existing Git-backed marketplace with the same name. For a selected standalone subset, use the [legacy installer](standalone-installation.md).

In a fresh conversation, check implementation, planning, review-only work, a small README edit, and resuming a task. To assess automatic selection, omit explicit skill names. Record the host version, OS, source commit, installation route, advertised names, observed resource loads, changes, and outcome. A correct answer alone does not establish which skill was loaded.

## Maintain and validate

Keep marketplace and plugin names aligned with the documented `craftflow@craftflow` identifier. Keep the source path within the marketplace root and retain required catalog policy/category fields. Update the plugin version for a package revision and validate skill metadata and references using [repository checks](../CONTRIBUTING.md).

When the host's Plugin Creator is available, use its `validate_plugin.py` and test installation in that host. Record structural checks and actual CLI/native-host execution separately; repository validation does not prove installation or discovery. Marketplace distribution does not submit the plugin to OpenAI's public directory.

## Basis

Checked on 2026-09-28 against [OpenAI's plugin packaging and marketplace metadata](https://developers.openai.com/plugins/build/plugins#marketplace-metadata) and [developer commands](https://learn.chatgpt.com/docs/developer-commands#codex-plugin). These document the existing compatibility manifest, repository catalog, and CLI commands. This environment had no Codex CLI, so the GitHub install flow was not executed here.
