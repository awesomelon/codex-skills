# Codex plugin installation and updates

## Install

Use a Codex CLI with `codex plugin` support and Git available. Add the repository marketplace, then install its plugin:

```bash
codex plugin marketplace add awesomelon/craftflow
codex plugin add craftflow@craftflow
```

Run each command after the preceding one succeeds. The first registers the GitHub marketplace; the second installs the two skills as one plugin. The plugin name and marketplace name are both `craftflow`.

## Verify

```bash
codex plugin marketplace list
codex plugin list --marketplace craftflow --json
```

Confirm the `craftflow` marketplace and an installed, enabled `craftflow` entry. In Codex, use the skill names advertised by the host, which may include a plugin prefix. If a current session does not show the installed skills, check a new conversation.

If `codex plugin` is unrecognized, update Codex through your existing installation method and check `codex plugin --help`. If the marketplace is present but the plugin is missing, inspect its catalog:

```bash
codex plugin list --marketplace craftflow --available --json
```

## Refresh the marketplace

```bash
codex plugin marketplace upgrade craftflow
codex plugin list --marketplace craftflow --json
```

The upgrade command refreshes the Git marketplace. Check the installed plugin version separately; a refreshed catalog alone does not prove that an existing session loaded the new skills. If an older installed copy remains, remove and install the plugin again using the commands below. Preserve any edits to installed files before replacement; maintain reusable changes in the source repository.

## Remove or reinstall

Remove the installed plugin:

```bash
codex plugin remove craftflow@craftflow
```

Install it again from the registered marketplace when needed:

```bash
codex plugin add craftflow@craftflow
```

To stop tracking the marketplace as well, remove it after removing the plugin:

```bash
codex plugin marketplace remove craftflow
```

## Upgrade from earlier skill catalogs

Version 0.4.0 exposes exactly `craftflow-set` and `craftflow-go`. Set combines investigation, design, planning, and review; Go handles implementation through verification. `craftflow-plan` and `craftflow-review` become `craftflow-set`; `craftflow-build` becomes `craftflow-go`. Choose by the requested outcome; technical topics are reference documents rather than separate skill entries. Update saved prompts and project instructions to these names. The [legacy name mapping](standalone-installation.md#migrate-older-installations) covers prior names.

Refresh the marketplace and check the installed version as described above. Reinstall if it still supplies the old catalog, then check the host's advertised skills in a new conversation. Remove superseded standalone entries from discovery separately; the plugin does not clean them up. No compatibility aliases are installed.

## Migrate from individual skills

Before enabling the plugin, locate existing CraftFlow skills in the actual user or project skill directories, such as `~/.agents/skills` or a project's `.agents/skills`. Preserve local edits and move superseded entries outside every skill discovery directory. For symlinks, preserve their source contents too; moving a link alone does not back up its target.

Then install the plugin and confirm that each intended skill is discovered only once. Marketplace installation does not remove old standalone entries. Older names and copy formats are covered in the [legacy standalone guide](standalone-installation.md#migrate-older-installations).

## References

Command syntax follows [OpenAI's developer command reference](https://learn.chatgpt.com/docs/developer-commands#codex-plugin), checked on 2026-09-28. Package layout and catalog details are in the [plugin guide](plugin.md).
