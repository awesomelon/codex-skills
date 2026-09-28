The migration is incomplete: the supplied producer and consumer cannot interoperate.

- **Blocking contract mismatch:** `producer.mjs` emits `{version: 2, documents: rows}`, while `contract.mjs` specifies `entries` and `consumer.mjs` reads that field. Passing producer output to the consumer throws when it calls `.map` on `undefined`. The smallest remedy is to make the producer emit the contract’s collection field, preferably using the shared constants.
- **Completion evidence is insufficient:** The checkpoint labels the plan “done,” but producer checks and integration results cover `revision-a`, while the recorded current revision is `revision-b`. The consumer’s reported checks at `revision-b` do not establish integration success.
- **Worker status remains historical:** The checkpoint records a producer timeout without confirmed shutdown. It establishes neither an active worker nor confirmed shutdown in this session. Any relevant worker status needs live confirmation in the originating environment.

The next useful action is to correct the producer’s field, then verify producer contract compliance and a producer-to-consumer round trip against the exact resulting files. Record that revision and fresh results before declaring completion.

Checks actually run: a non-writing inline Node check against the supplied modules. Producer contract compliance **failed**; producer-consumer round trip **failed**; consumer handling of a v2 `entries` payload **passed**. The command exited 1. The historical `node integration.test.mjs` command was not rerun; that test file was not supplied.

Resources read: `resources-review/SKILL.md` and `resources-review/references/quality/review.md`. Project files read: `TASK.md`, `checkpoint.json`, `contract.mjs`, `producer.mjs`, and `consumer.mjs`. No files changed, workers started, or external actions performed.
