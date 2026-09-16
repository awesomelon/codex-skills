# Selective upstream audit and contract-preserving simplification

## Scope and execution status

Initial audit: `8d59c883a8e5b1ada712c76f9feb051c16cef2fa` (after PRs #9 and #10). Publication base: `08cd4eadbdb132973245410eb74908bdeba0c26f` after PR #11 arrived during this audit. Its changed-file list was compared and overlapping authoring files were read and reconciled. Its other changes are preserved. At the initial baseline, reviewed all five skill entrypoints, the complete code-quality package, repository authoring guidance, and selected upstream files. This was not a line-by-line audit of every reference in the other four skills.

The user requested multiple agents. No subagent runtime or coding-agent CLI was available, and tool discovery did not find an execution capability. The parent performed the audit and edits directly. The existing [improvement prompt](../prompts/improve-skills.md), extended for explicitly requested parallel audits, enables a future explicitly requested parallel audit where real subagents exist; it is not evidence that this audit used multiple agents. No fresh model or automatic-selection evaluation was executed.

## Primary authoring reference

The designated [OpenAI article](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) was retrieved during the initial investigation. Its guidance informed narrow discovery, on-demand detail, task-appropriate checks, authority boundaries, and meaningful completion criteria. A later retrieval attempt returned a cache miss; the initial reading, not that failed retry, is the basis for this comparison.

The initially inspected five entrypoints already largely met those goals; incoming PR #11 refinements are preserved. All five `SKILL.md` files and their discovery descriptions remain unchanged. Useful read-only and implementation boundaries remain intact. No new skill, mandatory skill chain, runtime dependency, installer change, or permanent delegation policy was introduced.

## Upstream decisions

These are the exact inspected file identities, not repository commit SHAs. Ideas were selectively synthesized into original wording; upstream packages, code, hooks, and prompts were not copied wholesale.

| Source and inspected blob | Adopted or retained | Deliberately not adopted |
| --- | --- | --- |
| [Ponytail review](https://github.com/DietrichGebert/ponytail/blob/main/skills/ponytail-review/SKILL.md), blob `e137a855bd87119a4517895a1000a59b0999e1b8` | Look for unused flexibility and suitable existing/native replacements. Explain what disappears and what preserves its contract. | Net line deletion as the objective; treating one implementation as proof of waste; reducing input validation without equivalent behavior. |
| [ECC verification loop](https://github.com/affaan-m/ECC/blob/main/skills/verification-loop/SKILL.md), blob `8713f2b78a927f330428475c72b5192d1839cfea` | Keep executed verification distinguishable from judgment. Existing skill guidance already covers this, so no duplicate verification skill was added. | Universal build/type/lint/security phases, arbitrary coverage targets, and periodic or per-function full rechecking. |
| [pstack structural lessons](https://github.com/backnotprop/pstack/blob/main/skills/principle-encode-lessons-in-structure/SKILL.md), blob `df9cd5ff2fb3c18267349cc6aecd8121848ef834` | Make a concrete regression mechanically detectable with a calibrated acceptance fixture rather than adding repeated blanket warnings. | Automatic memory/configuration changes, mandatory principle loading, or generalizing every isolated correction into a new rule. |

## Changes and rationale

`code-quality-guard/references/implementation.md` now checks existing policy owners and compatible platform/library capabilities before adding another implementation. `references/review.md` adds contract-preserving simplification decisions: native semantics, runtime support, errors, and useful adapter seams. It requires a discriminating verification case for a replacement, not an arbitrary extra full suite. These details remain behind the existing task-specific routes.

The new date-parser fixture contains intentionally removable indirection while preserving strict date spelling, calendar validity, error classes, primitive-string input, UTC behavior, and exports. Its 34 acceptance tests are shared by an original implementation, an independently written compatible simplification, and a deliberately incompatible native shortcut. The Python calibration uses only temporary copies and an existing Node runtime; it is not a model run. Calibration implementations must stay outside future evaluated-agent context.

Cases 22-25 cover authorized simplification, a read-only pair, the incompatible shortcut, and a justified one-implementation adapter. They are expectations, not completed behavioral evaluations. The original 21 cases and historical execution records are preserved.

`AGENTS.md` already gained the mandatory source rule in incoming PR #11 and is unchanged by this patch. A proposed duplicate audit prompt was discarded; the existing `prompts/improve-skills.md` gains one paragraph for explicitly requested parallel audit scopes and truthful execution reporting. Its isolated behavioral-evaluator guidance is preserved. The README catalog and development guidance reflect the remaining changes.

## Executed verification

A direct clone failed DNS resolution. A partial checkout was reconstructed through connector reads. The 13 reconstructed baseline files were verified against Git blob hashes, including the complete seven-file code-quality package and the unchanged development validator and its installer dependency. No placeholder references or mocked discovery were used.

- The unchanged `python3 scripts/validate.py` passed for **code-quality-guard in the partial checkout**, not all five packages.
- A standalone temporary copy of that package passed the same validator with byte-identical copied files. UI metadata and all eight skill-local Markdown links passed.
- `python3 -m unittest discover -s tests -p "test_quality_simplification_fixture.py" -v` passed all three calibration tests. Original and compatible implementations each passed 34 acceptance tests under both UTC and America/Los_Angeles. The incompatible native shortcut was rejected, including invalid-date normalization and non-string coercion cases.
- Original scenario text, unchanged package files, and development scripts passed hash/text preservation checks. Added local documentation links and the staged partial-tree whitespace check passed.

These results establish structural portability and that this fixture distinguishes these implementations. They do not establish improved model quality, invocation accuracy, token use, latency, or general extensibility. Machine-readable scope and artifact hashes are in [structural results](../evals/skill-audit-2026-09-16-upstream/structural-results.json).

## Remaining verification and PR status

Fresh-agent cases 22 and 23 should be paired with the existing shared-rule implementation case 15 and justified-adapter case 25 before treating the instruction change as behaviorally verified. Record actual skill and fixture hashes, unchanged review inputs, implementation changes, and executed checks. Run the repository validator on a full checkout. Automatic selection, the official skill validator, the complete existing test suite, the shell installer, and macOS/Bash 3.2 were not tested here.

The change is proposed as a draft PR. No merge or modification of installed skills is included. Relative to the reconciled publication base, all five skill entrypoints, AGENTS.md, the other four skill packages, shell and Python installers, validator, and historical execution evidence are unchanged.
