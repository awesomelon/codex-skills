# Command and check record

- Read the supplied `skill/tact/SKILL.md` plus its `references/decision-documentation.md` and `references/verification.md` with `cat`.
- Ran `pwd && rg --files -g '!node_modules' -g '!vendor'` in the assigned workspace. The files were `README.md`, `config.py`, and `docs/decisions/0001-timeout-compatibility.md`.
- Read those three workspace files with `cat`. The existing accepted ADR already specified new-key precedence, indefinite legacy support, and a 30-second default; no new decision record was needed.
- Ran an inline `python3` baseline check against the original implementation. New-key-only input returned 30 instead of 12; both-key input returned legacy value 7 instead of new value 12. Both mismatches were confirmed. Exit status: 0.
- Used `apply_patch` to change the single lookup in `config.py` and update the existing README contract. The ADR was not edited.
- Ran `PYTHONDONTWRITEBYTECODE=1 python3` with eight inline assertions against the changed `read_timeout`:
  - `{}` returned `30`.
  - `{'timeout': 8}` returned `8`.
  - `{'timeout_seconds': 12}` returned `12`.
  - `{'timeout_seconds': 12, 'timeout': 8}` returned `12`.
  - `{'timeout_seconds': 0, 'timeout': 8}` returned `0`.
  - `{'timeout_seconds': None, 'timeout': 8}` returned `None`.
  - `{'timeout': 0}` returned `0`.
  - `{'timeout': None}` returned `None`.
- The same command printed `8 behavior checks passed`, verified the existing ADR text remained unchanged and the README link resolved, printed the final implementation and README, and removed the Python cache generated during baseline verification. Exit status: 0.
- Final workspace inventory remained the original three files. No test suite, new ADR, external service, installation, or subagent was used.
