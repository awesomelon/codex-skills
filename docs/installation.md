# Plugin installation and updates

Choose [Codex](#codex) or [Claude Code](#claude-code). Both plugins use the same `skills/` source. The [macOS standalone installer](#standalone-installation-on-macos) remains available for Codex.

## Codex

### Install

You need Git and a Codex CLI with `codex plugin` support.

GitHub installation requires a published Tact revision. For an unpublished revision, use the [local installation procedure](plugin.md#test-a-local-checkout).

Add the repository marketplace. Then install the plugin.

```bash
codex plugin marketplace add awesomelon/tact
codex plugin add tact@tact
```

Run each command only after the previous command succeeds. The first command registers the GitHub marketplace. The second command installs the `tact` skill as one plugin. The plugin name and marketplace name are both `tact`.

### Verify

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

### Refresh the marketplace

Run these commands:

```bash
codex plugin marketplace upgrade tact
codex plugin list --marketplace tact --json
```

The upgrade command refreshes the Git marketplace. Check the installed plugin version separately. A catalog refresh does not prove that an existing conversation uses the new skills.

If the installed copy is old, remove it and install the plugin again. Use the commands below. First preserve any edits to installed files. Keep reusable changes in the source repository.

### Remove or reinstall

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

## Claude Code

### Install in Claude Code

You need Git and a Claude Code CLI with `claude plugin` support. If the command is unavailable, update Claude Code through your usual installation method and check `claude plugin --help`.

Add the published repository marketplace, then install the plugin:

```bash
claude plugin marketplace add awesomelon/tact
claude plugin install tact@tact
```

Run each command only after the previous command succeeds. The marketplace and plugin names are both `tact`. Installation defaults to user scope. For an unpublished revision, use the [local checkout procedure](plugin.md#test-a-local-checkout).

### Verify in Claude Code

```bash
claude plugin marketplace list
claude plugin list
```

Confirm that the `tact` marketplace is registered and `tact@tact` is installed and enabled. Restart Claude Code to load the installed skill, then invoke:

```text
/tact:tact Review this change for correctness and unnecessary complexity. Do not edit files.
```

`/tact:tact` combines the plugin name and skill name. `$tact` is the Codex invocation syntax. Listing an installed plugin alone does not establish that a conversation loaded its skill.

### Update in Claude Code

Refresh the marketplace and then update the installed plugin:

```bash
claude plugin marketplace update tact
claude plugin update tact@tact
claude plugin list
```

Check the installed version and restart Claude Code. A marketplace refresh alone does not update the installed plugin. Preserve any edits to installed files before updating; keep reusable changes in the source repository.

### Remove or reinstall in Claude Code

```bash
claude plugin uninstall tact@tact
```

To reinstall from the registered marketplace:

```bash
claude plugin install tact@tact
```

To remove the marketplace as well:

```bash
claude plugin marketplace remove tact
```

These commands use the default user scope. If you installed with `--scope project` or `--scope local`, use that same scope when updating or uninstalling.

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
