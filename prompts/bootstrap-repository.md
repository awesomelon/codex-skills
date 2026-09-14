# One-shot prompt for initial publication

First extract the package and open the `codex-skills` folder containing `README.md`, `skills/`, and `scripts/` in desktop Codex. Submit the complete block below. This is a request template, not an execution record.

```text
Use the files in this folder to create the private awesomelon/codex-skills repository in my GitHub account and upload the initial version. Perform the work that is possible, rather than only explaining it.

The goal is to add future Codex skills one at a time under skills/<name>/ and reuse them on a new Mac with one installation command after clone. The user environment is macOS. Recommend bash scripts/install.sh, which does not require Python, for user installation. Preserve the existing architecture-guard body and references.

1. Read this folder's AGENTS.md, README.md, skills/, scripts/, and tests/ and use the supplied structure. Do not rebuild it with a new implementation or package-management system.
2. Check the Git repository boundary, working tree, and remotes. If this folder is inside an unrelated parent repository, do not commit or publish that repository. Preserve existing user changes and authentication files.
3. Check Git and GitHub CLI. Distinguish Python 3.10+ for repository development validation from user installation dependencies. Use gh auth status and gh api user --jq .login to verify that the active github.com account is awesomelon. Do not display tokens/authentication files or ask for them in chat. If authentication is unavailable, explain the need for browser sign-in and complete independent work such as validation.
4. Use gh repo view to check whether awesomelon/codex-skills exists and its visibility. Do not equate every lookup failure with absence; distinguish authentication, access, and network errors. If it exists, inspect and preserve files and history without recreating it, changing it to public, or force-pushing. Isolate conflicting changes in a working branch and PR in the existing repository.
5. Run bash -n scripts/install.sh, python3 scripts/validate.py, and python3 -m unittest discover -s tests -v. Exercise link/copy installation and repeated execution with bash scripts/install.sh in temporary paths; do not change my actual global configuration or installed skills.
6. For a new local repository, initialize main and explicitly stage only files intended for publication. Review the diff and check for secrets, then commit with feat: add architecture-guard and portable skill installer. Do not invent Git author identity if none is configured.
7. For a new remote, create and upload with gh repo create awesomelon/codex-skills --private --source=. --remote=origin --push. For an empty existing remote, confirm its observed state and push normally; for an existing history, use a safe branch/PR workflow. Do not write to another repository or account.
8. After upload, query remote files, the commit SHA, and private visibility again. Distinguish local creation, remote upload, and execution validation. Do not describe authentication/permission-blocked steps as successful.

Report the actual repository or PR URL, added skills, verification and limits, and macOS installation/update commands in Korean. Leave actual model execution of the skill unverified unless checked separately. Do not automatically modify my global AGENTS.md or config.toml.
```
