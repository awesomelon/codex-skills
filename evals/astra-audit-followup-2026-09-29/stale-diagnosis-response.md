Fixed `decodePreference` in `preferences.mjs` to use `?? true`, preserving explicit `false`. The prior diagnosis was stale: the encoder was already correct. Exported API and tests remain unchanged.

Checks run:
- Existing tests: reproduced failure before repair; all 3 pass afterward.
- Direct encode/decode and JSON round trips pass for `false`, `true`, undefined, and null.
- Test-file checksum confirms no changes.

Production behavior remains unverified because the account/browser session is unavailable. No dependencies installed or external services contacted.

Skill and references actually read:
- [craftflow-go/SKILL.md](.agents/skills/craftflow-go/SKILL.md)
- [changes.md](.agents/skills/craftflow-go/references/workflow/changes.md)
- [verification.md](.agents/skills/craftflow-go/references/workflow/verification.md)

Also read `TASK.md`, `diagnosis.json`, `preferences.mjs`, and `preferences.test.mjs`.