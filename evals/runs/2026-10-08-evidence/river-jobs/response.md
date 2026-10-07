**Do not remove `_ack` from emitted jobs under the current contract.**

- **[P1] Removal breaks worker acknowledgement.** [producer.py](/private/tmp/workspace-36n2vr7j/river-jobs/producer.py:4) emits `_ack`, which [contract.json](/private/tmp/workspace-36n2vr7j/river-jobs/contract.json:1) declares as the acknowledgement field. The worker reads it dynamically and throws `Missing acknowledgment token` when absent ([worker.mjs](/private/tmp/workspace-36n2vr7j/river-jobs/worker.mjs:5)).
- The producer check only asserts `id` ([checks.py](/private/tmp/workspace-36n2vr7j/river-jobs/checks.py:4)), so it cannot establish that removal is safe.

Verified in memory: the current emitted job acknowledges successfully; removing `_ack` preserves the producer assertion but makes the worker throw. Removal would require a coordinated replacement for token delivery and coverage across the producer–worker boundary.

No files were edited.