# Design and extension evaluation — 2026-09-15

Baseline: `0fe26df42a3c97b2595718a51200c161d1c4d72f`. This update applies the user's maintainability review and [OpenAI's skill-authoring article](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra). Descriptions identify the relevant design or implementation work, detailed shared-rule guidance has a dedicated reference, and extension decisions use actual requirements. These are authoring choices, not measured improvements in model speed or general effectiveness.

## Changes

| Skill | Result |
| --- | --- |
| Architecture | Descriptions include design and implementation. Planning uses a required variant or planned addition to compare edit points, affected consumers, and compatibility. |
| Code quality | Shared-rule implementation is selectable. Its dedicated reference distinguishes common decisions from independent rules and connects the requested addition to relevant checks. Extension experiments compare the same added requirement on separate copies. |
| React | Component and hook design considers another consumer, independent interaction state, and differences in eligibility without accumulating unrelated options. |
| TanStack Query | Shared key and request definitions remain consistent as readers, filters, and writes are added. Consumer-specific presentation and refresh choices can remain local. |

Required and optional checks remain distinct. Planning and review preserve files; authorized implementation includes edits and relevant verification. No additional always-loaded instructions or mandatory cross-skill invocation were introduced.

## Method and recorded inputs

Used fresh ephemeral Codex CLI conversations on macOS, requesting `gpt-6-astra` with medium reasoning. No independent model snapshot identifier was verified. Each conversation received only a standalone skill location, synthetic task inputs, and local resource restrictions. Expected designs, solutions, and previous responses were not supplied. Existing authentication and default instruction discovery remained available, so this was not a clean-account selection test.

The [manifest](outputs/manifest.json) records all 11 invocations, requests, before/after hashes, responses, model settings, and environment versions. The [command record](outputs/commands.json) preserves executed commands and exit codes. Temporary case directories are normalized in displayed text; hashes retain their original meaning. Exported test output removes temporary directory details, and linked text copies trim trailing spaces. Unmodified logs remain in the local evaluation directory; the manifest retains their original hashes.

Five final samples are selected below. Earlier runs are retained because they exposed an evaluation-input problem:

- Runs 01–04 skipped relevant reference documents; one response explicitly interpreted the instruction to read only the standalone skill as excluding those documents. Their requested code behavior and file preservation still passed the relevant checks.
- The implementation-reference link was moved into the code-quality work-selection paragraph. Runs 06–07 still skipped references under the same ambiguous evaluation wording.
- The evaluation input then explicitly allowed the entire supplied skill directory, including linked references. Runs 08–11 read the relevant references. The earlier Query run 05 had already done so and was not repeated.

The final samples establish reference use for these requests. They do not isolate the effect of moving the link from the effect of correcting the evaluation input.

## Final samples

| Run | Requested work | Observed result | References read |
| --- | --- | --- | --- |
| 08 | Add expired-status eligibility to the repeated-rule implementation | Added one shared rule file and updated three consumers. Kept pinning independent. All 10 tests passed after editing. | implementation.md, measurement.md |
| 09 | Apply the same addition to the already shared implementation | Changed only archive-policy.mjs. All 10 tests passed after editing. | implementation.md, measurement.md |
| 10 | Design JSON export for download and email | Proposed shared format handling and separate filenames, retaining CSV defaults. Existing CSV assertions passed. All inputs retained their hashes. | preflight.md |
| 11 | Design a second picker with eligibility restrictions | Proposed an additive eligibility input while retaining instance-local search and existing ordering. All inputs retained their hashes. | react-correctness.md |
| 05 | Design status-filtered list and preloading support | Connected tenant/filter keys, requests, list/count refresh, and the existing complete detail update. Kept presentation and refresh intervals local. All inputs retained their hashes. | cache-and-keys.md, mutations.md |

## What the extension comparison establishes

Both code samples began with the same public behavior and received the same [added requirement](fixtures/policy-extension/TASK.md) and [three new tests](fixtures/policy-extension/extension.test.mjs), alongside the seven existing policy tests. The repeated version came from the existing policy fixture. The shared version applied the existing saved implementation patch before adding this task.

Both starting versions passed eight tests and failed two: locked expired documents already produced the required result. The initial preparation expected a different failure count; that expectation was corrected without changing test assertions, and the captured baseline results were reused.

The final agent runs each executed the supplied suite once after editing: **10 passed, 0 failed**. Task, tests, and supplied skills retained their hashes. The parent inspected the command evidence and resulting edits instead of repeating passing tests. Both runs attempted Git inspection in the temporary non-Git input folders, reported its absence, and continued with the supplied snapshots; those unsuccessful commands remain in the record.

| Evidence | Repeated implementation | Shared implementation |
| --- | --- | --- |
| Original check result | [8 pass, 2 fail](outputs/repeated-before.txt) | [8 pass, 2 fail](outputs/shared-before.txt) |
| Resulting edits | [One new file and three consumer edits](outputs/08-implementation.patch) | [One policy edit](outputs/09-implementation.patch) |
| Post-edit checks | [10 pass, 0 fail](outputs/08-checks.txt) | [10 pass, 0 fail](outputs/09-checks.txt) |

The existing shared implementation accommodated this addition without editing its consumers. The repeated implementation also became shared during the task; four changed files therefore include that refactoring work. This is concrete evidence about these two starting implementations and this status addition, not proof that every new feature requires fewer edits. Whole-invocation time is recorded for traceability; editing time, developer productivity, and model speed were not measured.

## Package validation

- Repository `scripts/validate.py` passed for all four skills.
- Skill Creator `quick_validate.py` passed for all four; code quality was checked again after its instruction edit. UI YAML, description lengths, and existing invocation policies were checked.
- Temporary macOS copy and link installations matched all 25 source skill files. The changed code-quality copy was updated after the reference-selection edit.
- Final document references, Markdown formatting, JSON records, and saved patch reproduction were checked. Repository `AGENTS.md` was compared directly with its starting copy and remained unchanged.

Installer and validator code were unchanged, so their full unit suites were not repeated. Real installed skills, user settings, and the unrelated application repository were not edited.

## Reproduce and limits

For either code sample, copy `evals/code-quality-guard/fixtures/policy` to a disposable directory. For the shared sample, first apply `evals/code-quality-guard/outputs/implementation.patch`. Overlay the two files in `fixtures/policy-extension`, then run `node --test policy.test.mjs extension.test.mjs` to reproduce the two expected failures. Apply the corresponding saved patch above and run the same command to reproduce the recorded final behavior. For a fresh agent evaluation, supply that starting copy and the current standalone skill instead of applying the final patch.

For design samples, copy the corresponding fixture and standalone skill into a disposable directory and submit TASK.md with reading allowed throughout both supplied directories. Preserve all files. The picker fixture copies the previous saved React implementation; it avoids mixing the new design question with the earlier sorting defect.

These are explicit-invocation samples. Automatic selection and non-selection after the description changes, other models, repeated-run stability, and broad codebase effectiveness remain unverified. React rendering and Query runtime behavior were not exercised in the design cases. Proposed JSON support was not implemented or tested. The new experiment instructions were reviewed and applied by the parent to this comparison; an independent request to run an entire comparison was not evaluated. No performance improvement is claimed.
