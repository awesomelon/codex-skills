# Codex plugin installation and updates

## Install

You need Git and a Codex CLI with `codex plugin` support.

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

## References

Command syntax follows [OpenAI's developer command reference](https://learn.chatgpt.com/docs/developer-commands#codex-plugin). The source check occurred on 2026-09-28. See the [plugin guide](plugin.md) for package structure and catalog details.
