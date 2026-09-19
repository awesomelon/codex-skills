# Raw delegated result

Fixed and verified the race while preserving the documented API and state shapes.

- Changed search.mjs: each call advances a request counter before the empty-query check; only the current request publishes success or error.
- Expanded search.test.mjs: out-of-order results/errors, newer loading state, clearing pending searches, repeated identical queries, and active errors.

Reproduction: started `cat`, then `dog`; resolved `dog` before `cat`. Before the fix, the new regression failed because an extra `ready(cat)` state followed `ready(dog)`.

Verification commands actually run:
- `node --version` → `v24.16.0`
- `node --test search.test.mjs` → baseline **2/2 passed**
- Same command after adding the regression → **2 passed, 1 failed**, specifically the stale-result assertion
- Same command after implementation and neighboring cases → **10/10 passed**

Inspection used `cat`, `rg --files`, an ancestor `AGENTS.md` check, and `nl -ba`. `git status --short && git rev-parse HEAD …` failed immediately because this fixture is not a Git repository; no starting revision was available.

Limits: verification is deterministic controller testing in Node, not browser or production testing. Only the two files above were edited; the skill was unchanged. No commits, installs, external services, publishing, or further delegation.

This record retains the returned prose, with temporary absolute file links replaced by filenames for portability. It is not a full tool transcript.
