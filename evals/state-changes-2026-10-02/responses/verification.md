Updated only [docs/verify.md](/private/tmp/rung-state-checks/verification/docs/verify.md) and [verify.mjs](/private/tmp/rung-state-checks/verification/verify.mjs): corrected `add` to `create`, aligned the nested creation response, and retained removal persistence checks.

Checks:

- `node --check verify.mjs`: passed, exit 0.
- `node verify.mjs`: failed, exit 1, at line 22. Creation, saved listing, and removal acknowledgement passed; the final list still contained `{"id":"1","title":"hello"}`.
- Hashes confirmed `app.mjs`, `CONTRACT.md`, and `TASK.md` unchanged.

The remaining product defect is that `remove` returns `{"removed":true}` without deleting saved notes. Product repair is outside this task’s read-only scope.

Skill resources read:

- `/private/tmp/rung-state-checks/verification/resources/rung-go/SKILL.md`
- `/private/tmp/rung-state-checks/verification/resources/rung-go/references/workflow/verification.md`
