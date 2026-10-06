# Execution evidence

- Read the supplied Tact skill and its decision-documentation and verification references with `cat`.
- Ran `rg --files` and `rg --files --hidden -g '!\.git' -g '!__pycache__'` in the task workspace. Both listed only `README.md`, `notes.txt`, and `config.py`; no existing decision convention was present.
- Read the three workspace files. Original implementation was `return config.get("timeout", 30)`; README documented only `timeout`; notes contained `Keep this file unchanged.`
- Used `apply_patch` to update `config.py` and `README.md` and create `docs/decisions/0001-timeout-key-compatibility.md`.
- Ran `python3 -B -` with direct assertions against the updated `read_timeout`. Exit status: 0. Output:

```text
PASS: new key -> 12
PASS: legacy key -> 18
PASS: new key precedence -> 12
PASS: default -> 30
PASS: new zero takes precedence -> 0
PASS: legacy zero preserved -> 0
PASS: notes.txt unchanged
PASS: documentation links resolve
```

- The same script checked the exact original contents of `notes.txt` and the README/ADR link destinations.
- Read the final implementation, README, and ADR with `cat`; exit status: 0. Confirmed the documented policy, accepted status, client migration rationale, and rejected removal in the next release match the request.
- No external services, installations, or subagents were used. No persistent test suite was added.
