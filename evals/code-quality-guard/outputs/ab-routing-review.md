# A/B comparison — independent final response

> English translation of a historical record. [Original at the pre-translation commit](https://github.com/awesomelon/codex-skills/blob/ce11c34e3d1da77140087300218b776594bb65cf/evals/code-quality-guard/outputs/ab-routing-review.md). Reported runs, hashes, and counts describe the original work, not this translation.

Run date: 2026-09-14. The response below originally normalized temporary absolute file links to `A/` and `B/`. A is the existing `fixtures/policy`; B applies the existing `outputs/implementation.patch` to the same input. Preparation, hashes, request, and limits are in the [manifest](ab-routing-manifest.json).

**B is better for maintainability. Both implementations passed the supplied correctness checks.**

- **Code evidence:** A independently defines archive eligibility in `A/list.mjs` lines 2–3, `A/detail.mjs` lines 3–4, and `A/bulk.mjs` lines 3–4. Excluding `cancelled`, for example, requires changing all three decisions; omission could cause inconsistencies between screens and bulk operations.
- B calls `canArchive` from `B/archive-policy.mjs` in `B/list.mjs`, `B/detail.mjs`, and `B/bulk.mjs`. It adds one navigation step but leaves a single archive-condition edit point. This is **code-tracing judgment**, not a performed change experiment.
- Both keep `canPin` independent, as required by `CONTRACT.md`; matching current conditions do not justify combining it with archiving. B retains UI-facing function names and existing exports. The smallest remedy is to adopt B's structure and verify policy changes through existing public functions.

**Correctness:** Identical `A/policy.test.mjs` and `B/policy.test.mjs` cover three statuses × two lock values, detail action order, bulk ID order and empty input, and frozen-input immutability. Actual UI callers were not supplied, so integration was not verified.

| Location/command | Result |
| --- | --- |
| A and B separately: `node --version && node --test policy.test.mjs` | Same Node v24.19.0; each passed 7, failed 0, exit 0 |
| Comparison folder: `cmp A/policy.test.mjs B/policy.test.mjs && diff -ru A B` | Identical test files; product differences and B's new policy file confirmed. Exit 1 means diff found differences |
| `cat`, `nl -ba`, `rg --files`, `find … -name AGENTS.md` | Read contracts, skill, product code, and tests. No applicable AGENTS.md in the comparison folder or checked ancestors |

Used the requested `SKILL.md` and A/B reference `references/measurement.md`. Complexity and clone rate are unmeasured without analyzers, and no scores were assigned. No file modifications, network access, package installation, or GitHub operations were performed.
