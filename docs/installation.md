# Codex plugin installation and updates

## Install

You need Git and a Codex CLI with `codex plugin` support.

GitHub installation requires a published Tact revision. For an unpublished revision, use the [local installation procedure](plugin.md#test-a-local-checkout).

Add the repository marketplace. Then install the plugin.

```bash
codex plugin marketplace add awesomelon/tact
codex plugin add tact@tact
```

Run each command only after the previous command succeeds. The first command registers the GitHub marketplace. The second command installs the `tact` skill as one plugin. The plugin name and marketplace name are both `tact`.

## Verify

Run these commands:

```bash
codex plugin marketplace list
codex plugin list --marketplace tact --json
```

Confirm that the marketplace list includes `tact`. Confirm that the plugin list shows `tact` as installed and enabled.

Use the skill names shown by Codex. They can include a plugin prefix. If the current conversation does not show the installed skills, start a new conversation.

If Codex does not recognize `codex plugin`, update Codex through your usual installation method. Then check `codex plugin --help`.

If the marketplace exists but the plugin is missing, inspect the catalog:

```bash
codex plugin list --marketplace tact --available --json
```

## Refresh the marketplace

Run these commands:

```bash
codex plugin marketplace upgrade tact
codex plugin list --marketplace tact --json
```

The upgrade command refreshes the Git marketplace. Check the installed plugin version separately. A catalog refresh does not prove that an existing conversation uses the new skills.

If the installed copy is old, remove it and install the plugin again. Use the commands below. First preserve any edits to installed files. Keep reusable changes in the source repository.

## Remove or reinstall

Remove the installed plugin:

```bash
codex plugin remove tact@tact
```

When needed, install it again from the registered marketplace:

```bash
codex plugin add tact@tact
```

To remove the marketplace, first remove the plugin. Then run:

```bash
codex plugin marketplace remove tact
```

## Standalone installation on macOS

Clone or use a local Tact checkout. The Bash installer uses the system tools included with macOS and does not require Python. Run from the repository root:

```bash
bash scripts/install.sh --list
bash scripts/install.sh --skill tact --dry-run
bash scripts/install.sh --skill tact
```

The default installs a symlink under `~/.agents/skills`; keep the checkout at a stable path. To install an independent managed copy instead:

```bash
bash scripts/install.sh --skill tact --mode copy --dest /absolute/path/to/skills
```

The installer preserves unmanaged folders, foreign links, and locally edited managed copies. Use `--help` for options. The Python installer, `python3 scripts/install.py`, is also available for managed copies; use `--help` for its options.

For development tests, always supply a temporary `--dest` instead of installing into your real home.
