# Installation and updates

For a first installation, follow the [macOS quick start](../README.md#install-on-a-new-mac). The shell installer uses macOS Bash 3.2 and built-in utilities. It requires no Python, Node, jq, or package installation.

## Select skills and destination

The default destination is `~/.agents/skills`. Repeat `--skill` to choose a subset; omitting it installs the entire collection. Preview with `--dry-run`.

```bash
bash scripts/install.sh --skill craftflow-architecture --skill craftflow-react --dry-run
bash scripts/install.sh --skill craftflow-architecture --skill craftflow-react
```

Default **link mode** keeps skills connected to the clone. Moving or deleting that clone breaks the links. For independent managed copies in a team project:

```bash
bash scripts/install.sh --skill craftflow-code-quality --mode copy --dest /path/to/project/.agents/skills
```

Installing into this collection itself is blocked. Avoid duplicate installations at user/project scope or through both a plugin and the individual installer. In Codex CLI/IDE, inspect `/skills` or invoke a selected `$skill-name`; check a new session if it is missing.

## Update

From the clone, pull first. Continue only if the pull succeeds, then rerun the installer with your original selections, mode, and destination:

```bash
git pull --ff-only
bash scripts/install.sh --skill craftflow-orchestrator
```

Selections are not saved: a bare `bash scripts/install.sh` also installs skills you did not previously select. Review source changes before updating. Existing links reflect pulled changes immediately; rerunning adds links for newly selected skills. Managed copies update when the installer runs.

## Conflicts and recovery

- Foreign links, unmanaged directories, and locally changed managed copies are preserved and reported as conflicts. Back up outside all skill discovery directories, reconcile changes, then retry.
- Copy checks cover file content, additions, and deletions, including directories; permission-only changes are not detected. Prefer editing the source skill and committing there. Do not edit management metadata.
- The collection is not one transaction. Earlier successful installs remain after an I/O failure. A failed copy replacement attempts restoration and reports the backup path if restoration also fails.
- Removed or renamed skills are not deleted automatically. Do not run installers concurrently. Back up and reconcile an existing installation before changing modes.

## Repository rename

After the GitHub repository is renamed to `craftflow`, update the remote in your existing clone:

```bash
git remote set-url origin https://github.com/awesomelon/craftflow.git
```

The local clone directory can keep its old name. Before pulling the skill renames, preserve locally edited copies and symlink source contents outside skill discovery directories. Old skill symlinks can break when their source folders are renamed; the installer does not remove them. Follow the name mapping below, retaining your existing destination and mode.

## Migrate older installations

| Previous name | Current name |
| --- | --- |
| `engineering-orchestrator` | `craftflow-orchestrator` |
| `architecture-guard` | `craftflow-architecture` |
| `code-quality-guard` | `craftflow-code-quality` |
| `react-quality-guard` | `craftflow-react` |
| `refactoring-guard` | `craftflow-refactoring` |
| `tanstack-query-guard` | `craftflow-tanstack-query` |
| `typescript-quality-guard` | `craftflow-typescript` |
| `pstack` / `engineering-workflow` | `craftflow-orchestrator` |
| `typescript-best-practices` | `craftflow-typescript` |
| `tanstack-query` | `craftflow-tanstack-query` |
| `multi-agent-guard` | Removed; no replacement entry to install. |

Update explicit invocations and installer selections. Locate the old entry in your actual destination, preserve local edits, and move it outside every skill discovery directory before installing the current name. For symlinks, preserve the source contents too: moving a link does not back up its target. No compatibility aliases are installed. Verify only the intended names appear in a new session.

For the older Python installer:

- Existing link installations can use the shell installer from the same clone with the same selections.
- Python-managed copies are not converted or overwritten automatically. Back them up, merge local edits into the source, then install shell-managed copies with the previous destination and selections. The Python installer remains available for updates to its old format.

Shell copies keep `.codex-skills-install.v2`; Python copies keep `.codex-skills-install.json`. The installer retains the `awesomelon/codex-skills` ownership identifier for compatibility; these internal names are not plugin or skill names. Do not convert formats by editing those files. Plugin migration is covered in the [plugin guide](plugin.md).

## Optional architecture guidance

For recurring boundary work, merge the relevant [project snippet](../snippets/craftflow-architecture.project.md) into your project's `AGENTS.md`, or the [global snippet](../snippets/craftflow-architecture.global.md) into the personal instructions actually loaded by your host. Do not overwrite existing instructions. With `CODEX_HOME` or `AGENTS.override.md`, identify the active file first.

The snippets apply to boundaries, dependencies, state ownership, contracts, and requested structural reviews. They do not require an extra review for every edit. Enforce mandatory architecture rules through the target project's lint, tests, or CI.
