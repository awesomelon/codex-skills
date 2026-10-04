# Tact 0.0.1 validation

Date: 2026-10-04. These results describe the current package and repository checks.

Environment: macOS arm64, Python 3.13.9 (`/opt/anaconda3/bin/python3`), PyYAML 6.0.3, system Bash 3.2.57, Node.js 24.21.0.

| Command | Result |
| --- | --- |
| `python3 scripts/validate.py` | Passed: skill metadata, UI fields, portable contents, and internal references. |
| `/bin/bash -n scripts/install.sh` | Passed. |
| `python3 -m unittest discover -s tests -v` | 62 passed, no skips. Covers installation safety and metadata validation. |
| `node --test evals/semantic-controls.mjs` | Four passed, no skips. Exercises code-example semantics. |
| Temporary standalone and Codex plugin installation | Passed for `tact` and `tact@tact` 0.0.1 with Codex CLI 0.158.0. Installed skill files, `logo`, and `composerIcon` match the source. |
| `git diff --check` and `git diff --cached --check` | Passed. |

The Python commands above used the listed Python 3.13.9 executable. The macOS system Python does not meet the development requirement.

These checks do not execute or grade a model. The [behavioral scenarios](cases.md) have not been run as independent model evaluations. Automatic skill selection and comparative behavioral quality remain unverified.
