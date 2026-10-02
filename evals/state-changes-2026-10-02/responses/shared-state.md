Both proposed fixes should be rejected.

1. **Stock reservations:** Separate files initialized to `1` create two independently reservable units, violating the shared limit in [design.md](/private/tmp/rung-state-checks/shared-state/design.md:7). The current [reserve function](/private/tmp/rung-state-checks/shared-state/workers.mjs:7) also permits both processes to read `1` and return success.

   Retain one authoritative stock record. Serialize the entire **read → check → decrement → persist** operation across processes, using a suitable cross-process lock or a single shared owner. Reload stock after acquiring that serialization boundary. Atomic file replacement alone cannot prevent conflicting decisions.

   To establish correctness, run two actual processes against disposable shared-disk state, controlling contention: starting stock `1` must produce exactly one success, one rejection, and final stock `0`. Check successful reservation count as well as final state. Verify interruption recovery preserves valid stock and restores safe access.

2. **Worker progress:** A mutex inside each process cannot coordinate the other process. Moreover, [saveProgress](/private/tmp/rung-state-checks/shared-state/workers.mjs:3) rewrites the entire startup snapshot, so even sequential saves can erase another worker’s newer progress.

   Give each worker its own owned progress file and aggregate them when the dashboard reads. This fits the explicit allowance for differing freshness in [design.md](/private/tmp/rung-state-checks/shared-state/design.md:3). Publish each record atomically so readers see valid JSON. Keeping one document would instead require cross-process serialization plus a fresh read and merge for every save.

   To establish correctness, exercise both workers repeatedly with controlled overlapping publication and verify the dashboard retains both latest published values while accepting mixed freshness. Check reads during publication and worker interruption.

**Executed:** Loaded the unchanged `workers.mjs` with in-memory filesystem mocks. Three assertions reproduced lost progress after sequential saves, two successful reservations against one shared unit, and two successes using the proposed separate stock files. No project files were written.

**Remaining evidence:** These checks establish the failure mechanisms; they do not validate a repair or real filesystem/process coordination. Dashboard and locking implementations were not supplied.

Skill/reference files actually read:

- [rung-get-set/SKILL.md](/private/tmp/rung-state-checks/shared-state/resources/rung-get-set/SKILL.md)
- [review-scope.md](/private/tmp/rung-state-checks/shared-state/resources/rung-get-set/references/quality/review-scope.md)
- [preflight.md](/private/tmp/rung-state-checks/shared-state/resources/rung-get-set/references/architecture/preflight.md)
- [rung-go/SKILL.md](/private/tmp/rung-state-checks/shared-state/resources/rung-go/SKILL.md)
- [state-changes.md](/private/tmp/rung-state-checks/shared-state/resources/rung-go/references/architecture/state-changes.md)
