> English translation of a historical record. [Original at the pre-translation commit](https://github.com/awesomelon/codex-skills/blob/ce11c34e3d1da77140087300218b776594bb65cf/evals/code-quality-guard/outputs/improve.md). Reported runs, hashes, and counts describe the original work, not this translation.

Maintainability improvements are complete. Changes were limited to four files in the specified `project`.

- Added `canArchive` in `archive-policy.mjs`, consolidating **three independent archive-policy definitions into one** for list, detail, and bulk operations.
- Preserved the four public functions in the three existing modules and all UI action names.
- Kept `canPin` independent and documented the intentional separation in a comment.
- Left `TASK.md` and existing tests unchanged.

Correctness was checked with Node.js `v24.19.0`. `node --test policy.test.mjs` passed **7/7 before and after**. It covered six status/lock combinations, action ordering, bulk ID order and empty input, and immutability using frozen inputs. A separate check confirmed unchanged export names and function types in existing modules.

Maintainability is **improved**: a future archive-condition change has one central edit point and does not affect pinning. The tradeoff is one additional step to follow the shared module.

The baseline was file content saved at task start. No Git history was available for historical comparison. AST complexity and clone rate are unmeasured because analyzers were absent. Validation covers valid inputs guaranteed by `TASK.md`.
