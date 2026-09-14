# Working on codex-skills

This repository is the source of personal Codex skills used on macOS. Keep installation and update instructions specific to macOS. The user-facing entry point is `bash scripts/install.sh`, which runs without Python. Use Bash 3.2-compatible syntax and BSD-compatible commands. Retain Python for repository development checks and compatibility with the older copy installer.

Write maintained instructions, documentation, and UI metadata in English. Preserve original wording in raw evaluation evidence and behavior-sensitive test data.

Store skills in `skills/<kebab-case-name>/SKILL.md`. To match this repository's validator, put each frontmatter `name` and `description` on a single line. Descriptions should contain the purpose needed for selection and only exclusions that prevent likely confusion. Link to details when needed; keep installation and evaluation material outside skills. References must work when only the skill folder is installed.

Read existing skills and conventions relevant to the task. Do not add duplicate instructions across always-loaded guidance, bodies, and references, blanket checklists, or mandatory delegation. Preserve each skill's purpose and read-only scope. Reflect changed use cases and expected behavior in the README catalog and `evals/<name>/cases.md`; record actual execution separately from scenarios.

For skill changes, check structure with `python3 scripts/validate.py`. For installer or validator changes, run `bash -n scripts/install.sh`, `python3 -m unittest discover -s tests -v`, and affected CLI operations in temporary paths. Evaluate significant behavioral instruction changes with relevant cases. Do not repeat sufficient validation for optional reasons. Never use the real home directory or Codex configuration for installation tests, and do not describe results from another OS as macOS validation. Review-only requests must not modify source, configuration, or documentation.

Limit remote work to the verified `awesomelon/codex-skills` repository. Preserve existing user changes, remote history, and installed skills. Do not change visibility to public, modify other repositories, force-push, or collect authentication tokens. Commit, push, open PRs, and merge only within the user's requested scope. If remote repository creation is unavailable, distinguish local completion from incomplete remote work.
