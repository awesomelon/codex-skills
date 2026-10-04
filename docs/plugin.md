# Tact plugin

**Tact — Make the right change.** The plugin gives Codex the [engineering guidance](../README.md#four-principles) in this repository.

Use the [installation guide](installation.md) to install, update, or remove the plugin.

## Package and marketplace

The repository contains one marketplace and one plugin. The plugin contains skills only.

| File | Purpose |
| --- | --- |
| [`.agents/plugins/marketplace.json`](../.agents/plugins/marketplace.json) | Lists the `tact` marketplace and its `tact` plugin. |
| [`.codex-plugin/plugin.json`](../.codex-plugin/plugin.json) | Defines the plugin name, version, display fields, and `./skills/` source. |
| [`skills/`](../skills/) | Provides the single `tact` skill included in the plugin. |

The catalog sets `source.path` to `"./"`. This path is relative to the marketplace repository root. It selects the existing root plugin. No second plugin directory or skill copy is necessary.

The skills use the host's tools. The package includes no MCP server, hooks, scheduler, or agent runtime.

## Test a local checkout

Register the checkout as the marketplace source. Then install the plugin.

```bash
codex plugin marketplace add /absolute/path/to/tact
codex plugin add tact@tact
```

Use the actual checkout path. Its directory name does not have to be `tact`.

Use an isolated Codex test configuration. This prevents the local source from replacing an existing Git marketplace with the same name.

`codex plugin marketplace upgrade` refreshes Git marketplaces; it does not upgrade a local-path marketplace. After changing a local source, use the remove/reinstall procedure in the isolated test configuration and verify the installed version and file contents separately. Local-path tests do not establish the Git marketplace upgrade behavior.

In a new conversation, test implementation, planning, review, a small README edit, and task resumption. To test automatic skill selection, do not specify a skill name.

Record the host version, OS, source commit, installation method, and skill names shown by the host. Record the resources loaded, changes made, and task result. A correct answer alone does not show which skill the host loaded.

## Maintain and validate

Keep the marketplace and plugin names consistent with `tact@tact`. Keep the source path inside the marketplace root. Retain the required policy and category fields.

Update the plugin version when the package changes. Use the [repository checks](../CONTRIBUTING.md) to validate skill metadata and references.

If Plugin Creator is available, run its `validate_plugin.py`. Also test installation in the target host.

Report structural checks separately from CLI and host tests. Repository validation does not prove successful installation or skill discovery. Marketplace distribution does not submit the plugin to OpenAI's public directory.
