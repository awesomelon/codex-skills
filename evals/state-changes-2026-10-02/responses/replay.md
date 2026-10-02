Fixed replay handling in [job.mjs](/private/tmp/rung-state-checks/replay/job.mjs:8) using the provider’s durable `credit:${requestId}` operation key. The API and `provider.mjs` are unchanged.

Changed files:

- `job.mjs`
- `job.test.mjs`

Verification: `node --test job.test.mjs` passed all 3 tests, exit 0. The new restart regression first failed on the original code with receipt ID 2 instead of 1. After repair, it confirms one credit effect, the original receipt, and persisted job completion. Separate request IDs still produce two credits for identical account and amount.

Limits: verified sequential execution and interruption after provider persistence; concurrency remains outside scope.

Supplied skill/reference files read:

- `/private/tmp/rung-state-checks/replay/resources/rung-go/SKILL.md`
- `/private/tmp/rung-state-checks/replay/resources/rung-go/references/architecture/state-changes.md`
- `/private/tmp/rung-state-checks/replay/resources/rung-go/references/workflow/changes.md`
- `/private/tmp/rung-state-checks/replay/resources/rung-go/references/workflow/verification.md`
