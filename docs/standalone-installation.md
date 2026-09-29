# Legacy standalone installation

Use the [Codex plugin](installation.md) for new installations. Use this guide for existing macOS installations or selected standalone skills.

## Prepare a standalone clone

The shell installer uses macOS Bash 3.2 and built-in utilities. It does not require Python. For link mode, keep the clone in a permanent location.

```bash
git clone https://github.com/awesomelon/rung.git
cd rung
bash scripts/install.sh --list
```

## Select skills and destination

The default destination is `~/.agents/skills`. Use `--skill` for each skill you want to install. Without `--skill`, the installer selects all skills.

First use `--dry-run` to inspect the plan. Then run the installation command.

```bash
bash scripts/install.sh --skill rung-get-set --skill rung-go --dry-run
bash scripts/install.sh --skill rung-get-set --skill rung-go
```

The default **link mode** connects installed skills to the clone. Moving or deleting the clone breaks those links.

To install independent managed copies in a project, use copy mode:

```bash
bash scripts/install.sh --skill rung-get-set --mode copy --dest /path/to/project/.agents/skills
```

The installer blocks installation into this repository. Keep only one discoverable installation of each skill. Check user directories, project directories, and plugin installations for duplicates.

In Codex CLI or IDE, inspect `/skills` or invoke the selected `$skill-name`. If the skill is missing, check a new session.

## Update

Review source changes before you update. From the clone, pull the changes. Continue only if the pull succeeds.

Run the installer with the same skill selections, mode, and destination as before. For example:

```bash
git pull --ff-only
bash scripts/install.sh --skill rung-go
```

The installer does not save your selections. A command without `--skill` also installs skills you did not select before.

Existing links use source changes immediately after the pull. Run the installer to add links for newly selected skills. Managed copies change only when the installer runs.

## Conflicts and recovery

- The installer preserves foreign links, unmanaged directories, and locally edited copies. It reports them as conflicts. Back them up outside skill discovery directories. Merge required edits before you retry.
- Copy checks detect content changes, added files, removed files, and directory changes. They do not detect permission-only changes. Edit the source skill where possible. Do not edit management metadata.
- Installation is not one transaction. Earlier successful installs remain after an I/O failure. If copy replacement fails, the installer tries to restore the previous copy. If restoration also fails, it reports the backup path.
- The installer does not remove deleted or renamed skills. Do not run installers concurrently. Back up an existing installation and merge required edits before you change modes.

## Product rename

CraftFlow is now Rung. The repository address is now `awesomelon/rung`. Update the remote URL in an existing clone:

```bash
git remote set-url origin https://github.com/awesomelon/rung.git
```

You can keep the local clone directory name.

Before you pull the skill renames, preserve locally edited copies and symlink source contents outside skill discovery directories. A source-folder rename can break old skill symlinks. The installer does not remove those links.

Use the name mapping below. Keep your existing destination and installation mode.

## Migrate older installations

| Previous names | Choose by the requested outcome |
| --- | --- |
| `craftflow-get-set` | `rung-get-set` for investigation, design, planning, and review. |
| `craftflow-go` | `rung-go` for implementation through verification. |
| `craftflow-orchestrator`, `engineering-orchestrator`, `pstack`, `engineering-workflow` | `rung-get-set` for investigation, planning, or assessment; `rung-go` for execution/resumption. |
| `craftflow-architecture`, `architecture-guard` | `rung-get-set` for design or architecture review; `rung-go` for boundary changes. |
| `craftflow-code-quality`, `code-quality-guard` | `rung-go` for improvements; `rung-get-set` for quality assessment. |
| `craftflow-react`, `react-quality-guard` | `rung-go` or `rung-get-set`; React guidance is a reference library. |
| `craftflow-refactoring`, `refactoring-guard` | `rung-go` for transformations; `rung-get-set` for proposals or assessment. |
| `craftflow-tanstack-query`, `tanstack-query-guard`, `tanstack-query` | `rung-go` or `rung-get-set`; Query guidance is a reference library. |
| `craftflow-typescript`, `typescript-quality-guard`, `typescript-best-practices` | `rung-go` or `rung-get-set`; TypeScript guidance is a reference library. |
| `craftflow-set`, `craftflow-plan`, `craftflow-review` | `rung-get-set` for investigation, design, planning, and review. |
| `craftflow-build` | `rung-go` for implementation through verification. |
| `multi-agent-guard` | Removed; no replacement entry to install. |

Update skill names in explicit requests and installer selections. Find each old entry in the actual installation destination. Preserve local edits. Move the entry outside all skill discovery directories before you install its replacement.

For symlinks, also preserve the source contents. Moving a symlink does not back up its target. The installer does not create aliases for previous names. Check the skill names in a new session.

For the older Python installer:

- Existing link installations can use the shell installer from the same clone. Use the same skill selections.
- The shell installer does not convert or overwrite Python-managed copies. Back up those copies. Merge local edits into the source. Then install shell-managed copies with the previous destination and selections. The Python installer can still update its old format.

Shell copies use `.codex-skills-install.v2`. Python copies use `.codex-skills-install.json`. Both retain the `awesomelon/codex-skills` ownership identifier for compatibility. These internal names are not plugin or skill names.

Do not change copy formats by editing metadata files. See the [plugin guide](plugin.md) for plugin migration.

## Optional architecture guidance

For repeated work on module boundaries, use the [project snippet](../snippets/rung.project.md) or [global snippet](../snippets/rung.global.md). Merge relevant project guidance into the project's `AGENTS.md`. Merge global guidance into the personal instructions that your host actually loads. Preserve existing instructions.

If you use `CODEX_HOME` or `AGENTS.override.md`, identify the active instruction file first.

The snippets cover boundaries, dependencies, state ownership, contracts, and requested structural reviews. They do not require a separate review for every edit. Enforce required architecture rules with the target project's lint checks, tests, or CI.
