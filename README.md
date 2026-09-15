# codex-skills

A personal collection of Codex skills to install and update on multiple Macs. The supported user environment is macOS.

GitHub repository: [awesomelon/codex-skills](https://github.com/awesomelon/codex-skills).

## Included skills

| Skill | Purpose |
| --- | --- |
| [architecture-guard](skills/architecture-guard/SKILL.md) | Design, implement, and review module responsibilities, dependencies, shared state, and public APIs. Assess concrete required additions and compatibility. |
| [react-quality-guard](skills/react-quality-guard/SKILL.md) | Design and improve React components, hooks, state, and performance. Separate shared behavior from consumer-specific interaction state. |
| [code-quality-guard](skills/code-quality-guard/SKILL.md) | Design and implement shared business rules; review maintainability and compare implementations using evidence of actual change costs. |
| [tanstack-query-guard](skills/tanstack-query-guard/SKILL.md) | Implement and review Query behavior using task-specific v5 guidance. Keep shared query definitions consistent when readers, filters, or writes are added. |
| [typescript-best-practices](skills/typescript-best-practices/SKILL.md) | Design, implement, and review TypeScript types, checked input, assertions, and configuration inference. |

`architecture-guard` focuses on module boundaries, `react-quality-guard` on React execution and user behavior, `code-quality-guard` on maintainability across languages and frameworks, and `tanstack-query-guard` on TanStack Query-specific cache and request behavior. Each skill works when installed alone. Reuse existing evidence when a task needs several perspectives; there is no need to invoke every skill each time. Small quality reviews can use the skill body alone. Select references for before/after or A/B comparison, scoring, and special metrics according to the request.

For TypeScript, use `Use $typescript-best-practices to implement and verify this parser` or `Use $typescript-best-practices to review these types without editing files`. The skill supports automatic selection for relevant TypeScript work and excludes wording-only and styling-only edits. It works independently and does not require a framework-specific review. Install it with `bash scripts/install.sh --skill typescript-best-practices`. See [evaluation cases](evals/typescript-best-practices/cases.md) and [execution results](evals/typescript-best-practices/results.md).

For TanStack Query, use `Use $tanstack-query-guard to review this mutation without editing files` or `Use $tanstack-query-guard to fix and verify this query's cache behavior`. Install it separately with `bash scripts/install.sh --skill tanstack-query-guard`. The [source record](skills/tanstack-query-guard/references/sources.md) identifies the pinned upstream, MIT notice, and corrections; [evaluation cases](evals/tanstack-query-guard/cases.md) and [results](evals/tanstack-query-guard/results.md) distinguish intended behavior from executed checks.

If you installed the former `tanstack-query` name, preserve any local edits and replace that entry with `tanstack-query-guard` to avoid duplicate discovery. The installer does not automatically remove renamed skills.

For review only, ask `Use $react-quality-guard to review the current changes without editing files.` For implementation, ask `Use $react-quality-guard to improve and verify the React code.`

Example requests for general code quality:

```text
Use $code-quality-guard to review the current changes, separating correctness from maintainability. Provide evidence and the smallest improvements without modifying files.

Use $code-quality-guard to improve and verify this module's maintainability. Use the starting state as a baseline to assess behavior preservation and the difference in change cost.

Use $code-quality-guard to add this eligibility rule to the list, detail menu, and bulk action. Keep the independent pinning rule unchanged and verify the affected behavior.
```

Shared-rule implementation uses [implementation guidance](skills/code-quality-guard/references/implementation.md). A routine local edit needs no separate quality review. For a concrete required addition, assess its edit points and compatibility; additional abstractions need evidence from the actual requirements. The [design and extension evaluation](evals/design-extension-2026-09-15/results.md) records the tested cases and their limits.

Report passing tests, diagnostic signals such as complexity/duplication, and maintainability judgments separately. Leave unavailable measurements unmeasured; do not optimize for a single score or lower LOC. See [comparison and measurement](skills/code-quality-guard/references/measurement.md), [scoring](skills/code-quality-guard/references/scoring.md), [Earendil source metrics](skills/code-quality-guard/references/earendil-metrics.md), [quality evaluation cases](evals/code-quality-guard/cases.md), and [execution records](evals/code-quality-guard/results.md). The installer discovers new folders automatically; after updating, select this skill with `bash scripts/install.sh --skill code-quality-guard`.

Upstream sources, pinned commits, and exceptions are in [React sources](skills/react-quality-guard/references/sources.md). Behavioral evaluation scope is in [React evaluation results](evals/react-quality-guard/results.md).

The [2026-09-12 audit](docs/skill-audit-2026-09-12.md) records duplicate-instruction cleanup, conditional reference/check selection, and behavioral results. The [2026-09-14 full audit](docs/skill-audit-2026-09-14.md) includes the new quality skill and a fix for repeated checks observed in evaluation. The [follow-up audit](docs/skill-audit-2026-09-14-followup.md) refines reference selection, task-template duplication, and guidance. Each record distinguishes verified and unrun work. See [evaluation evidence](evals/README.md) for the relationship between English translations and original runs.

The [English translation record](docs/english-translation.md) documents the language change, preserved behavior, and its validation limits.

## Install on a new Mac

**Installation does not require Python.** It uses macOS `/bin/bash` and built-in commands such as `shasum`. Downloading the repository requires Git. The public HTTPS clone below needs neither GitHub CLI nor authentication. For a restricted repository, you can use `gh repo clone awesomelon/codex-skills` with an authorized, authenticated GitHub CLI account.

The default destination for all skills is `~/.agents/skills`. User configuration and `AGENTS.md` are not modified automatically.

With Git available, run each command only after the preceding one succeeds:

```bash
git clone https://github.com/awesomelon/codex-skills.git
cd codex-skills
bash scripts/install.sh
```

`install.sh` is the installation/update entry point. It does not invoke Python, Node, jq, or package installation.

The default mode creates symbolic links. Clone into a durable location rather than a temporary directory such as Downloads. Moving or deleting the source folder after installation breaks those links.

### Inspect or select an installation

```bash
bash scripts/install.sh --list
bash scripts/install.sh --dry-run
bash scripts/install.sh --skill architecture-guard
```

In Codex CLI/IDE, inspect `/skills` or invoke `$architecture-guard`. If it is missing, check in a new session. Successful file installation is separate from verifying model execution or review accuracy.

To copy skills into a team project, specify that project's path. Avoid duplicate installation of the same skill at both user and project scope.

```bash
bash scripts/install.sh --mode copy --dest /path/to/other-project/.agents/skills
```

Installing this collection into itself is blocked. Before changing installation modes, back up and remove or reconcile the existing installation separately.

## Update

Run from the cloned `codex-skills` folder. If pull fails, do not proceed to installation.

```bash
git pull --ff-only
bash scripts/install.sh
```

To maintain only selected skills, use the same `--skill` options each time. The default includes all repository skills; selections are not saved separately.

For links, changes to existing skills take effect in the source immediately after pull; rerunning the installer links newly added skills. For copies, rerunning updates managed copies and adds new skills. Review script and skill changes before installation.

Safety behavior:

- Repeated installation does not create duplicates. New skills are discovered from `skills/`, so adding a skill does not require installer changes.
- Manual installations, links to other repositories, and name collisions are preserved and reported as errors. Back up existing folders **outside** skill discovery paths, merge needed changes, and rerun.
- Managed copies are checked by hash for local additions, edits, and deletions of files/directories; updates stop if changes exist. Prefer editing the source in `skills/<name>/` and committing there. Do not edit a copy's management metadata.
- Selected paths are checked for conflicts before changes, but the entire collection is not one transaction. Skills installed before an I/O failure remain installed and can be revisited by rerunning. A failed copy replacement attempts restoration; if that also fails, the backup path is reported.
- Skills removed upstream and other installations are not automatically deleted. Do not run multiple installers concurrently. File permission changes alone are not covered by content hashes.

### Migrate from the Python installer

- For an existing **link installation**, run `bash scripts/install.sh` from the same clone. Existing links are reused.
- Copies made by **`install.py --mode copy`** are not automatically converted or overwritten. Back them up outside skill discovery paths, merge any local changes into the source repository, then run `bash scripts/install.sh --mode copy --dest <previous-installation-path>`. Keep using the Python installer if you need to update the old format immediately.

Shell-managed copies use `.codex-skills-install.v2`; older Python copies use `.codex-skills-install.json`. Do not switch formats by editing management files.

## Apply architecture review to relevant work

Installation and invocation policy are separate. These examples apply when module responsibilities, dependency direction, shared state, or public API design changes, or when structural review is requested. They do not require a separate review at the start and end of every coding task.

Use `snippets/architecture-guard.project.md` for project guidance or `snippets/architecture-guard.global.md` for personal global guidance. **Merge only the needed block into existing instruction files; do not overwrite them.** The installer does not do this for you.

Project guidance belongs in that project's `AGENTS.md`. Personal global guidance commonly lives in `~/.codex/AGENTS.md`; when using `CODEX_HOME` or `AGENTS.override.md`, first identify the file actually loaded. Check which instructions are read in a new Codex session after applying changes.

`AGENTS.md` guides the agent; it is not an enforcement mechanism. Put mandatory dependency/boundary rules in the target project's lint, tests, or CI. This collection does not install a resident monitor, automatic Git synchronization, or background reviews.

## Add skills incrementally

Create `skills/<skill-name>/SKILL.md`, adding `references/`, `scripts/`, or `agents/openai.yaml` only when useful. Update the README catalog and `evals/<skill-name>/cases.md`. The installer discovers folders automatically.

Python 3.10+ is required only for repository development and validation. The checks below are not part of user installation. The shell installer uses Bash 3.2-compatible syntax and BSD-compatible options; the test runner exercises the CLI directly.

Use [prompts/add-skill.md](prompts/add-skill.md), filling in one concrete skill purpose. There is no need to create many skills up front or abstract a common framework.

```bash
bash -n scripts/install.sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

`validate.py` is a small check for this repository's single-line `name`/`description` convention and local references. It is neither a general YAML parser nor an official Codex validator. Evaluate invocation, non-invocation, and execution quality separately using `evals/` scenarios.

## References

Installation paths, discovery, link support, and invocation were checked against the OpenAI documentation below. This installer is a custom implementation, not an official installer. GitHub creation/authentication commands follow GitHub CLI documentation.

- [Build skills](https://learn.chatgpt.com/docs/build-skills)
- [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [gh repo create](https://cli.github.com/manual/gh_repo_create)
- [gh auth login](https://cli.github.com/manual/gh_auth_login)

The user-designated skill-authoring reference is [Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra).

See [shell installer validation](docs/shell-installer-validation.md) for the shell migration's scope and limits, and [earlier validation](docs/validation.md) for previous work.
