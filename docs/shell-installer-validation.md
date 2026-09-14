# Python-free shell installer — 2026-09-13

> English translation of a historical record. [Original at the pre-translation commit](https://github.com/awesomelon/codex-skills/blob/ce11c34e3d1da77140087300218b776594bb65cf/docs/shell-installer-validation.md). Reported runs, hashes, and counts describe the original work, not this translation.

`bash scripts/install.sh` is the installation/update entry point. It supports default link installation, `--mode copy`, `--dest`, repeatable `--skill`, `--list`, `--dry-run`, and `--help`. It does not invoke Python, Node, jq, or package managers, or change user configuration or skill bodies.

## Existing installations

| Existing state | Shell installer behavior |
| --- | --- |
| Link to the same source | Reuse unchanged |
| Unmodified shell-managed copy | Update if source changed |
| Copy with local edits, added/deleted files, or added empty directories | Preserve and report an error |
| Copy created by the Python installer | Preserve without conversion; advise backup, merge, and reinstall |
| Manual installation, external/broken link, or changed installation mode | Preserve and report an error |

The new copy format uses SHA-256 covering file names, content, and empty directories. Management files are checked as strings, never executed or sourced. Symlinks and special files within skills are rejected. The older Python installer remains for old-copy updates and development-validator compatibility; new installation does not require it.

## Validation executed

Environment: Linux, Bash 5.2.21. All fixtures and installation targets were temporary paths.

- `bash -n scripts/install.sh`: syntax passed.
- `python3 scripts/validate.py`: structure/references passed for both skills.
- `python3 -m unittest discover -s tests -v`: 47 passed: the original 24, one new management-file check, and 22 shell CLI tests.
- Shell CLI tests provided only needed file commands in PATH. Installation ran without discoverable Python, Node, Ruby, jq, realpath, or package managers. The Python test runner is separate from installer runtime dependencies.
- Verified repeat execution, deduplicated selections, new skill discovery, non-mutating previews, old link compatibility, copy updates, preservation of user edits, and preflight collision checks across selections.
- Covered spaces and Korean characters in paths, hidden files, empty directories, and newline/shell-special-character filenames within skills. Newlines in checkout or destination directory paths are explicitly rejected.
- Checked destination symlinks and `..`, self-installation blocking, preservation of old copy formats, and management files not executing as code.
- Injected `mv` failures to verify no incomplete skill remains after initial copy failure, restoration after replacement failure, and backup preservation outside discovery paths when restoration also fails.
- Installed both real skills as links and copies in temporary paths and compared content with source. Both skills reported unchanged when rerun in each mode.

## Limits

The script uses Bash 3.2-compatible syntax and macOS/BSD-compatible options, but was not run on macOS hardware or a Bash 3.2 binary. Linux results are not macOS validation.

Installation is not one transaction. Do not run concurrent installers or edit copies during installation. Recovery checks cover injected command failures, not forced termination, power loss, or every filesystem error. Content hashes do not detect permission or extended-attribute changes. GitHub authentication and actual Codex skill discovery on a Mac need separate checks.

User installation needs no Python. Python 3.10+ is used only for repository development checks and updating older Python-managed copies through the old installer.
