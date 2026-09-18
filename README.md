# codex-skills

A personal collection of Codex skills to install and update on multiple Macs. The supported user environment is macOS.

GitHub repository: [awesomelon/codex-skills](https://github.com/awesomelon/codex-skills).

## Included skills

| Skill | Purpose |
| --- | --- |
| [architecture-guard](skills/architecture-guard/SKILL.md) | Design and review module boundaries, dependency direction, shared-state ownership, and contracts between modules. Local edits without boundary impact need no architecture review. |
| [react-quality-guard](skills/react-quality-guard/SKILL.md) | Design and improve React components, composition, hooks, state, and performance. Choose variants and shared providers while preserving independent interaction state. |
| [code-quality-guard](skills/code-quality-guard/SKILL.md) | Design and implement shared business rules using practical SOLID, design pattern, and YAGNI criteria; review, improve, and compare maintainability using evidence of actual change costs. |
| [refactoring-guard](skills/refactoring-guard/SKILL.md) | Plan, perform, and review behavior-preserving refactoring using Martin Fowler's small, verified transformations. |
| [tanstack-query-guard](skills/tanstack-query-guard/SKILL.md) | Design, implement, and review Query behavior using task-specific v5 guidance. Keep shared query definitions consistent when readers, filters, or writes are added. |
| [typescript-quality-guard](skills/typescript-quality-guard/SKILL.md) | Design and review TypeScript types, fix diagnostics, and implement or review input validation. |

Across the collection, readability and maintainability take precedence over LOC, smaller files, or the smallest diff. Keep responsibilities together when understanding and changing them requires reading the same code. A cohesive file around 1,000 lines can be appropriate; this is neither a target nor a limit. Split when independent change, reuse, or verification becomes clearer after accounting for extra navigation and coordinated edits. Each skill carries the relevant criteria for standalone use.

`architecture-guard` focuses on module boundaries, `react-quality-guard` on React execution and user behavior, `code-quality-guard` on maintainability across languages and frameworks, and `tanstack-query-guard` on TanStack Query-specific cache and request behavior. Each skill works when installed alone. Reuse existing evidence when a task needs several perspectives; there is no need to invoke every skill each time. Small current-state quality reviews can use the skill body alone. Select [change-review guidance](skills/code-quality-guard/references/review.md) for PRs, full audits, maintainability improvements, or future-change analysis; select comparison, scoring, and source-metric references only for those requested decisions.

For TypeScript, use `Use $typescript-quality-guard to implement and verify this parser` or `Use $typescript-quality-guard to review these types without editing files`. The skill supports automatic selection for type modeling, type diagnostics, and input validation; a .ts or .tsx extension alone is not a trigger. Its entrypoint routes to type modeling, input validation, or narrowing guidance as needed. It works independently and does not require a framework-specific review. Install it with `bash scripts/install.sh --skill typescript-quality-guard`. See [evaluation cases](evals/typescript-quality-guard/cases.md) and [historical example checks](evals/typescript-quality-guard/results.md), recorded before this rename.

For TanStack Query, use `Use $tanstack-query-guard to review this mutation without editing files` or `Use $tanstack-query-guard to fix and verify this query's cache behavior`. Install it separately with `bash scripts/install.sh --skill tanstack-query-guard`. The [source record](skills/tanstack-query-guard/references/sources.md) identifies the pinned upstream, MIT notice, and corrections; [evaluation cases](evals/tanstack-query-guard/cases.md) and [results](evals/tanstack-query-guard/results.md) distinguish intended behavior from executed checks.

If you installed the former `tanstack-query` name, preserve any local edits and replace that entry with `tanstack-query-guard` to avoid duplicate discovery. The installer does not automatically remove renamed skills.

For review only, ask `Use $react-quality-guard to review the current changes without editing files.` For implementation, ask `Use $react-quality-guard to improve and verify the React code.`

For refactoring, use `Use $refactoring-guard to simplify this calculation without changing its behavior, and verify the result.` For a plan, use `Use $refactoring-guard to propose small refactoring steps without editing the code.` This independently installable skill focuses on how to carry out and verify structural changes; `code-quality-guard` covers broader maintainability assessment and shared-rule design. Use only the guidance needed for the request. Install it with `bash scripts/install.sh --skill refactoring-guard`. See [Fowler sources and interpretation](skills/refactoring-guard/references/sources.md), [evaluation cases](evals/refactoring-guard/cases.md), and [actual validation](evals/refactoring-guard/results.md).

For component variants, use [composition guidance](skills/react-quality-guard/references/composition.md) to choose children, render props, compound components, or shared providers. It preserves ordinary boolean state, simple props, and supported React versions. Try `Use $react-quality-guard to design reply and edit composers from shared elements while preserving independent drafts.`

Example requests for general code quality:

```text
Use $code-quality-guard to review the current changes, separating correctness from maintainability. Provide evidence and the smallest improvements without modifying files.

Use $code-quality-guard to improve and verify this module's maintainability. Use the starting state as a baseline to assess behavior preservation and the difference in change cost.

Use $code-quality-guard to add this eligibility rule to the list, detail menu, and bulk action. Keep the independent pinning rule unchanged and verify the affected behavior.
```

UI selection alone does not request implementation changes. Review and planning preserve the assessed code; explicitly requested plans and review reports can still be written. Implementation requests continue through relevant verification.

Shared-rule implementation uses [implementation guidance](skills/code-quality-guard/references/implementation.md). A routine local edit needs no separate quality review. For a concrete required addition, assess its edit points and compatibility; additional abstractions need evidence from the actual requirements. The [design and extension evaluation](evals/design-extension-2026-09-15/results.md) records the tested cases and their limits.

Report passing tests, diagnostic signals such as complexity/duplication, and maintainability judgments separately. Leave unavailable measurements unmeasured; do not optimize for a single score or lower LOC. See [comparison and measurement](skills/code-quality-guard/references/measurement.md), [scoring](skills/code-quality-guard/references/scoring.md), [Earendil source metrics](skills/code-quality-guard/references/earendil-metrics.md), [quality evaluation cases](evals/code-quality-guard/cases.md), and [execution records](evals/code-quality-guard/results.md). The installer discovers new folders automatically; after updating, select this skill with `bash scripts/install.sh --skill code-quality-guard`.

Upstream sources, pinned commits, and exceptions are in [React sources](skills/react-quality-guard/references/sources.md). Behavioral evaluation scope is in [React evaluation results](evals/react-quality-guard/results.md). The [composition validation record](evals/react-quality-guard/composition-results-2026-09-17.md) separates structural checks and author assessment from unrun behavioral evaluations.

The [2026-09-12 audit](docs/skill-audit-2026-09-12.md) records duplicate-instruction cleanup, conditional reference/check selection, and behavioral results. The [2026-09-14 full audit](docs/skill-audit-2026-09-14.md) includes the new quality skill and a fix for repeated checks observed in evaluation. The [follow-up audit](docs/skill-audit-2026-09-14-followup.md) refines reference selection, task-template duplication, and guidance. Each record distinguishes verified and unrun work. See [evaluation evidence](evals/README.md) for the relationship between English translations and original runs.

The [2026-09-15 audit](docs/skill-audit-2026-09-15.md) covers all five skill entrypoints, TypeScript reference routing, architecture selection, and the code-quality UI prompt. Its structural checks are separate from unrun repository and model evaluations.

The [2026-09-15 follow-up audit](docs/skill-audit-2026-09-15-followup.md) covers requested-document boundaries, UI work modes, and the TypeScript rename, including installation migration and validation limits.

The [2026-09-16 follow-up audit](docs/skill-audit-2026-09-16.md) records the five-entrypoint inspection, code-quality reference routing, selective-install examples, and the limits of source retrieval and validation.

The [Astra refinement](docs/astra-refinement-2026-09-16.md) records the fresh article check, focused discovery and workflow updates, upstream ideas considered, and independent evaluation limits.

The [upstream comparison audit](docs/skill-audit-2026-09-16-upstream.md) records selective Ponytail/ECC/pstack adoption, unchanged discovery metadata, and the calibrated simplification fixture. The existing [improvement prompt](prompts/improve-skills.md) also covers explicitly requested parallel audits.

The [English translation record](docs/english-translation.md) documents the language change, preserved behavior, and its validation limits.

### TypeScript skill rename

`typescript-best-practices` is now `typescript-quality-guard` (display name: **TypeScript Quality Guard**), matching the collection's `*-guard` convention. Update explicit `$typescript-best-practices` invocations, selected `--skill` arguments, and any personal/project guidance to the new name.

The installer discovers the new directory but does not migrate or remove old installations. After updating the clone:

1. Locate the old `typescript-best-practices` entry in the destination you actually used (default: `~/.agents/skills`; also check project installations if applicable). Preserve local edits from a copy or the source checkout before replacing it.
2. Move the old entry to a backup **outside every skill discovery directory**. For link installations, preserve the edited source files too: a moved symlink is not a backup of its target, and the old link may already be broken after the rename.
3. Install with `bash scripts/install.sh --skill typescript-quality-guard`, retaining your previous `--dest` and `--mode copy` options when applicable. Start a new Codex session and verify that only the new name is discovered.

No compatibility skill is installed under the old name; keeping both would add duplicate discovery metadata. Historical validation records retain the name used in their original run.

## Install on a new Mac

**Installation does not require Python.** It uses macOS `/bin/bash` and built-in commands such as `shasum`. Downloading the repository requires Git. The public HTTPS clone below needs neither GitHub CLI nor authentication. For a restricted repository, you can use `gh repo clone awesomelon/codex-skills` with an authorized, authenticated GitHub CLI account.

The default destination for all skills is `~/.agents/skills`. User configuration and `AGENTS.md` are not modified automatically.

With Git available, clone the repository and inspect the available skills. Run each command only after the preceding one succeeds:

```bash
git clone https://github.com/awesomelon/codex-skills.git
cd codex-skills
bash scripts/install.sh --list
```

Choose only skills you expect to use repeatedly. For example, to install the code-quality skill alone:

```bash
bash scripts/install.sh --skill code-quality-guard --dry-run
bash scripts/install.sh --skill code-quality-guard
```

Replace the example name or repeat `--skill <name>` for your chosen subset. To deliberately install the whole collection, run `bash scripts/install.sh` without `--skill`. The installer's default is unchanged. Selecting fewer skills reduces discovery metadata; it is not a measured performance claim.

`install.sh` is the installation/update entry point. It does not invoke Python, Node, jq, or package installation.

The default mode creates symbolic links. Clone into a durable location rather than a temporary directory such as Downloads. Moving or deleting the source folder after installation breaks those links.

### Inspect or select an installation

```bash
bash scripts/install.sh --list
bash scripts/install.sh --skill architecture-guard --dry-run
bash scripts/install.sh --skill architecture-guard
```

In Codex CLI/IDE, inspect `/skills` or invoke `$architecture-guard`. If it is missing, check in a new session. Successful file installation is separate from verifying model execution or review accuracy.

To copy skills into a team project, specify that project's path. Avoid duplicate installation of the same skill at both user and project scope.

```bash
bash scripts/install.sh --skill code-quality-guard --mode copy --dest /path/to/other-project/.agents/skills
```

Installing this collection into itself is blocked. Before changing installation modes, back up and remove or reconcile the existing installation separately.

## Update

Run from the cloned `codex-skills` folder. If pull fails, do not proceed to installation.

```bash
git pull --ff-only
bash scripts/install.sh --skill code-quality-guard
```

The update command above matches the single-skill installation example. Retain your actual `--skill` selections, `--dest`, and `--mode` options. To maintain the entire collection, omit `--skill`. Selections are not saved separately; a bare installer command also installs skills you did not previously select.

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

Installation and invocation policy are separate. These examples apply when module boundaries, dependency direction, shared-state ownership, or contracts between modules change, or when structural review is requested. They do not require a separate review at the start and end of every coding task.

Use `snippets/architecture-guard.project.md` for project guidance or `snippets/architecture-guard.global.md` for personal global guidance. **Merge only the needed block into existing instruction files; do not overwrite them.** The installer does not do this for you.

Project guidance belongs in that project's `AGENTS.md`. Personal global guidance commonly lives in `~/.codex/AGENTS.md`; when using `CODEX_HOME` or `AGENTS.override.md`, first identify the file actually loaded. Check which instructions are read in a new Codex session after applying changes.

`AGENTS.md` guides the agent; it is not an enforcement mechanism. Put mandatory dependency/boundary rules in the target project's lint, tests, or CI. This collection does not install a resident monitor, automatic Git synchronization, or background reviews.

## Add skills incrementally

Create `skills/<skill-name>/SKILL.md`, adding `references/`, `scripts/`, or `agents/openai.yaml` only when useful. Update the README catalog and `evals/<skill-name>/cases.md`. The installer discovers folders automatically.

Python 3.10+ is required only for repository development and validation. The checks below are not part of user installation. The shell installer uses Bash 3.2-compatible syntax and BSD-compatible options; the test runner exercises the CLI directly.

Use [prompts/add-skill.md](prompts/add-skill.md), filling in one concrete skill purpose. There is no need to create many skills up front or abstract a common framework.

For an existing skill or collection audit, use [prompts/improve-skills.md](prompts/improve-skills.md). It anchors changes in the designated Astra article and concrete findings, and separates structural checks from independent behavioral evaluation. Keep effective instructions instead of rewriting every skill on each audit.

For skill changes, check structure and local references:

```bash
python3 scripts/validate.py
```

For installer or validator changes, also check shell syntax, run the repository suite, and exercise affected CLI operations in temporary paths:

```bash
bash -n scripts/install.sh
python3 -m unittest discover -s tests -v
```

The optional [simplification fixture calibration](tests/test_quality_simplification_fixture.py) uses an existing Node.js 18+ runtime and skips when Node is absent. It does not affect Python-free installation or establish model behavior. Run it separately with `python3 -m unittest discover -s tests -p "test_quality_simplification_fixture.py" -v`.

For significant instruction changes, run the relevant behavioral cases and record actual results. Existing sufficient checks need not be repeated solely to produce another report.

`validate.py` is a small check for this repository's single-line `name`/`description` convention and local references. It is neither a general YAML parser nor an official Codex validator. Evaluate invocation, non-invocation, and execution quality separately using `evals/` scenarios.

## References

Installation paths, discovery, link support, and invocation were checked against the OpenAI documentation below. This installer is a custom implementation, not an official installer. GitHub creation/authentication commands follow GitHub CLI documentation.

- [Build skills](https://learn.chatgpt.com/docs/build-skills)
- [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [gh repo create](https://cli.github.com/manual/gh_repo_create)
- [gh auth login](https://cli.github.com/manual/gh_auth_login)

The user-designated skill-authoring reference is [Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra).

See [shell installer validation](docs/shell-installer-validation.md) for the shell migration's scope and limits, and [earlier validation](docs/validation.md) for previous work.
