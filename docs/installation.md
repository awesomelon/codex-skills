# Codex plugin installation and updates

## Install

You need Git and a Codex CLI with `codex plugin` support.

Rung was previously named CraftFlow. Version 0.5.0 changes the package and skill names. The repository address is now `awesomelon/rung`.

GitHub installation requires a published Rung revision. For an unpublished revision, use the [local installation procedure](plugin.md#test-a-local-checkout).

Add the repository marketplace. Then install the plugin.

```bash
codex plugin marketplace add awesomelon/rung
codex plugin add rung@rung
```

Run each command only after the previous command succeeds. The first command registers the GitHub marketplace. The second command installs the two skills as one plugin. The plugin name and marketplace name are both `rung`.

## Verify

Run these commands:

```bash
codex plugin marketplace list
codex plugin list --marketplace rung --json
```

Confirm that the marketplace list includes `rung`. Confirm that the plugin list shows `rung` as installed and enabled.

Use the skill names shown by Codex. They can include a plugin prefix. If the current conversation does not show the installed skills, start a new conversation.

If Codex does not recognize `codex plugin`, update Codex through your usual installation method. Then check `codex plugin --help`.

If the marketplace exists but the plugin is missing, inspect the catalog:

```bash
codex plugin list --marketplace rung --available --json
```

## Refresh the marketplace

Run these commands:

```bash
codex plugin marketplace upgrade rung
codex plugin list --marketplace rung --json
```

The upgrade command refreshes the Git marketplace. Check the installed plugin version separately. A catalog refresh does not prove that an existing conversation uses the new skills.

If the installed copy is old, remove it and install the plugin again. Use the commands below. First preserve any edits to installed files. Keep reusable changes in the source repository.

## Remove or reinstall

Remove the installed plugin:

```bash
codex plugin remove rung@rung
```

When needed, install it again from the registered marketplace:

```bash
codex plugin add rung@rung
```

To remove the marketplace, first remove the plugin. Then run:

```bash
codex plugin marketplace remove rung
```

## Migrate from the CraftFlow plugin

First preserve any edits to installed files. Remove the old plugin. Then remove the old marketplace.

```bash
codex plugin remove craftflow@craftflow
codex plugin marketplace remove craftflow
```

Add the current source and install `rung@rung`. Use the GitHub source only after publication of the renamed catalog. Before publication, use an isolated local checkout.

Check the new plugin name and installed skills. A refresh of the old marketplace alone does not prove that migration succeeded.

## Upgrade from earlier skill catalogs

The current catalog contains two skills:

| Current name | Purpose | Previous names |
| --- | --- | --- |
| `rung-get-set` | Investigation, design, planning, and review | `craftflow-get-set`, `craftflow-set`, `craftflow-plan`, `craftflow-review` |
| `rung-go` | Implementation and verification | `craftflow-go`, `craftflow-build` |

Choose the skill that matches the requested result. Technical topics are reference documents, not separate skills. Update saved prompts and project instructions with the current names. See the [legacy name mapping](standalone-installation.md#migrate-older-installations) for older catalogs.

Refresh the marketplace and check the installed version. If the plugin still contains the old catalog, install it again. Check the skill names in a new conversation.

Remove old standalone entries from skill discovery separately. The plugin does not remove them. It does not install aliases for previous names.

## Migrate from individual skills

Find existing Rung or CraftFlow skills in the user and project skill directories. Examples include `~/.agents/skills` and a project's `.agents/skills`.

Preserve local edits. Move old entries outside all skill discovery directories before you enable the plugin. For symlinks, also preserve the source contents. Moving a symlink does not back up its target.

Install the plugin. Confirm that the host finds each intended skill only once. Marketplace installation does not remove old standalone entries.

The [legacy standalone guide](standalone-installation.md#migrate-older-installations) covers older names and copy formats.

## References

Command syntax follows [OpenAI's developer command reference](https://learn.chatgpt.com/docs/developer-commands#codex-plugin). The source check occurred on 2026-09-28. See the [plugin guide](plugin.md) for package structure and catalog details.
