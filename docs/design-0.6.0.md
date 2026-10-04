# Rung 0.6.0 design

Status: proposed implementation design, 2026-10-04. This document does not record implementation or evaluation success.

Implementation follow-up: [candidate results](../evals/v0.6.0/results.md) record the local implementation, checks, and blocked model evaluation. The behavioral release gate remains unmet; this design is not a release approval.

## Outcome

Make engineering claims more trustworthy in two situations: a performance number may measure the wrong work, and a recurring mistake may need executable prevention rather than another written reminder. Demonstrate the resulting behavior with reproducible model evaluations and host installation checks.

Keep the two independently usable endpoints, `rung-get-set` and `rung-go`, and the skills-only distribution. Evaluate the existing instructions first. Add instruction detail only for a demonstrated gap or a clearly identified decision boundary, and distinguish that design rationale from measured improvement.

## Baseline and evidence

- Current Rung main: `0925ce0ac0bc3ddbd56f722d9e86befb20486098`; its tree matches v0.5.5 (`057b418b89047af8d1aef10ce03ebef4e37f28f8`). The intervening 1.0 release commit was reverted. This proposal does not restore its stability contract.
- [The v0.5.5 evaluation](../evals/long-running-2026-10-03/results.md) completed zero model runs because CLI initialization failed. Its eight checker controls validate the checker, not model behavior. Treat this as an execution blocker to resolve, not a demonstrated skill failure.
- [Performance guidance](../skills/rung-go/references/workflow/performance.md) already covers representative workloads, repeated measurements, end-to-end tradeoffs, and accepted/rejected experiments.
- [Learning guidance](../skills/rung-go/references/workflow/learning.md) already prioritizes verified, non-obvious reasoning and avoids redundant documentation. The proposed extension concerns selecting and proving executable prevention.
- Rung's previously pinned pstack source is `032be146865d973682535de75f2287da438550bf`. The inspected current upstream is [cursor/plugins at e43c7ee](https://github.com/cursor/plugins/tree/e43c7ee26e0038c6c1fa8380dd34ce86ff94cb2a/pstack). `benchmark-checklist`, `principle-explain-the-number`, and `correct` were added between those revisions.
- [OpenAI's Astra skill-authoring article](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) was fetched and read on 2026-10-04. Its short descriptions, conditional references, and outcome-based completion inform this design. It does not prescribe this release or evaluation design.

## 1. Validate the meaning of performance measurements

### Trigger and ownership

Apply when an assessment or authorized optimization depends on measured latency, throughput, resource use, or a claimed speedup. A routine edit, theoretical explanation, or clearly labeled rough estimate does not require a full benchmark procedure.

Go's existing `references/workflow/performance.md` owns execution detail. Get Set's `references/quality/measurement.md` receives a short assessment rule and points to Go's optional reference through catalog resolution. Preserve standalone Get Set use: its assessment rule must remain usable without Go installed, and a missing optional reference must not block the review.

### Decisions to add

1. Define the claim and inspect the measurement boundary: statistic, unit, workload, successful operation count, error count, and what completion means.
2. Check that the work actually completes inside the timed region. Account for unawaited work, unconsumed lazy results, unintended cache hits, early rejection, and discarded results when relevant. A cache hit is valid evidence when it represents the claimed workload; it is not evidence for an uncached claim.
3. Establish comparable conditions for the actual question. Record build mode, versions, settings, cache state, and competing machine load. For adoption decisions, compare realistic configurations for each option. For an explicitly scoped shipped-configuration comparison, report that narrower result without generalizing to the implementations.
4. Explain material differences using observed profiles or counters when needed. Check whether the generator, CPU, lock, disk, or network limits the result. Separate profiling runs from reported timing when instrumentation materially affects timing.
5. Check plausibility against the contribution of the changed path and relevant capacity bounds. A suspicious result calls for a discriminating check; it is not automatically proof of a bug.
6. Repeat and interleave measurements when noise or drift can change the decision. Report samples and variability. Use the workload and observed variation to choose repetitions; do not import a universal five-run rule.
7. Report the supported result separately from its explanation: observed faster/slower, no measurable difference, or inconclusive. A repeatable observed difference can be reported while its cause remains uncertain. Do not claim a causal mechanism or general winner without the corresponding evidence.

Example: a benchmark reports 80% lower latency because most requests are now rejected. The correct outcome is to reject the speedup claim, preserve the error evidence, and repair the harness or product only within the requested scope.

### Delivery shape

Extend the existing performance reference with a compact measurement-validity section. Add a short pointer from verification only if baseline cases demonstrate a routing gap. Do not copy the same checklist into both entrypoints or introduce a third performance skill.

## 2. Prevent recurring mistakes through executable constraints

### Trigger and ownership

Apply when the authorized task concerns a recurring defect, repeated maintenance error, or a rule whose violation can be detected mechanically. Use relevant supplied history or project records; do not mine unrelated conversations. A single routine correction does not trigger a repository-wide hardening sweep.

Extend Go's existing `references/workflow/learning.md`. Widen its entry in Go's reference table to cover prevention of recurring errors if evaluation shows the current wording misses that use. Get Set can recommend the same options through its existing architecture and review criteria while preserving assessed files.

### Decision order

Consider the least costly effective prevention in this order, allowing project constraints to change the choice:

1. Remove the invalid path or duplicate source of truth through ownership or API design.
2. Encode the invariant in existing types or schemas when the language and domain permit it.
3. Use an existing lint or CI mechanism when the violation has a reliable static signal; diagnostics should name the supported alternative.
4. Add a behavior test for the observable invariant when static enforcement is insufficient.
5. Preserve a short explanation for judgment calls or non-obvious tradeoffs that executable constraints cannot express.

This is a preference order, not a mandate to redesign architecture for every bug. Do not delete necessary compatibility, merge independently changing policies, or create speculative infrastructure to eliminate a minor local error.

### Proof of prevention

- Identify the mistake, affected contract, and evidence that the selected mechanism addresses its cause.
- Show that the check rejects a faithful reproduction of the mistake. Use a permitted disposable copy rather than altering history or introducing a broken production commit.
- Show that the correction and a legitimate neighboring case are accepted, including independent consumer policies or supported compatibility where relevant.
- Reuse the project's local/CI command where appropriate. A check existing only in prose is not executable protection.
- Keep unresolved judgment in existing documentation when useful and authorized. Do not automatically rewrite AGENTS.md, install hooks, or introduce an exception-approval system.

Example: repeated drift between two registries representing one rule may justify deriving both from one owner. Similar-looking rules with different consumer contracts must remain independently changeable.

## 3. Reproducible evaluation support

### Minimal repository tooling

Build on [comparison.md](../evals/comparison.md), the existing fixtures, and independent checkers. Add a repository-development runner, not a runtime dependency of the installed plugin:

| Proposed path | Responsibility |
| --- | --- |
| `scripts/run_evals.py` | Prepare isolated cases, invoke the supported CLI adapter, retain attempts, run independent checkers, and produce a summary. |
| `evals/v0.6.0/cases.json` | Case IDs, fixture paths, task prompts, supplied skill endpoint, editable/protected paths, and checker references. Never expose the case catalog or checker to candidates. |
| `evals/v0.6.0/fixtures/` | New measurement and prevention cases. Reuse existing long-running fixture sources rather than duplicating them. |
| `evals/v0.6.0/check_outputs.py` | Behavior and scope assertions for new cases, independent of candidate implementation details. |
| `evals/v0.6.0/results.md` | Actual attempts, retained/rejected instruction changes, comparison limits, and release decision. |
| `tests/test_run_evals.py` | Runner failure accounting, isolation setup, timeout handling, and result parsing with a local fake CLI. |

Use the current Python development setup and standard library where sufficient. Support one verified Codex CLI integration initially. Add another adapter only for a concrete need; do not build a generalized evaluation service.

### Execution contract

1. Preflight the actual CLI/version, supported isolation flags, writable task/log locations, and a minimal model invocation before scheduling a batch. Keep authentication in the supported host path. Do not print secrets, change real user configuration, or solve initialization failures by silently expanding privileges.
2. Freeze baseline and candidate content hashes. Create independent disposable workspaces and isolated sessions. Candidate-visible directory names must not reveal the variant or scoring criteria. Preserve ordinary project test names; blinding must not make the task artificial.
3. Keep the rubric, independent checker, other candidates' artifacts, and result logs outside candidate-readable inputs using supported runtime isolation. A separate directory alone does not prove inaccessibility. Record isolation limitations rather than claiming a blinded run that the host cannot enforce.
4. Hold model, effort, task, host instructions, tools, permissions, and fixtures constant. Record requested and observed settings separately. Alternate baseline/candidate execution order to expose drift; keep shared-resource contention out of timing comparisons.
5. Invoke the CLI using argument arrays, capture output and exit status, and apply a bounded timeout. Preserve every executed attempt. Stop the batch on a repeated environment prerequisite failure; unstarted cases remain listed as not run.
6. Evaluate a snapshot of candidate outputs. Run checks outside the candidate session, compare protected files/inventory, and retain evidence tied to the checked bytes. Verify checker controls before relying on the checker.
7. Check report claims separately from artifact correctness. For qualitative judgments, use a fixed rubric and reviewer blinded to variant identity where available. Record human or model review provenance; do not grade required phrases or headings.

Reuse the fields in `evals/comparison.md`: case/variant/repetition, source and input hashes, invocation mode, runtime configuration, actual resource reads, process exit, elapsed time, usage/cost, acceptance evidence, and limitations. Unexposed measurements stay `null`.

Keep `execution_status` separate from `outcome`. For example, a CLI initialization error is `blocked`, a fully evaluated wrong artifact is `failed`, and missing evidence after an interrupted run is `inconclusive`. A started timed-out attempt remains recorded; later unstarted cases are `not_run`. Process exit zero is never the acceptance criterion.

### Case matrix

| Case | Required observation |
| --- | --- |
| Fast failures | Reject a latency win caused by increased errors; retain the agreed correctness condition. |
| Work outside timing | Identify incomplete asynchronous/lazy work and avoid claiming completed-work throughput. |
| Configuration and noise | Withhold a general winner when setup or observed variation explains the gap; recommend a discriminating measurement. |
| Valid measurement control | Accept a well-supported scoped improvement without demanding an unrelated benchmark campaign. |
| Shared-rule recurrence | Implement authorized prevention at the actual owner and demonstrate rejection of the old mistake. |
| Independent-policy control | Preserve intentional consumer differences despite similar syntax; avoid false-positive enforcement. |
| Review-only recurrence | Recommend prevention with evidence while preserving all assessed files. |
| Routine edit | Make only the requested correction, without a new rule, benchmark, or lesson record. |
| Scope-change replay | Reuse the existing steering fixture; reconcile the current request and late result. |
| Stale-evidence replay | Reuse the existing async-result fixture; do not accept results for obsolete inputs. |

Start with one paired run per case to validate the setup and expose gaps. Then use a predeclared repeated batch for changed decisions and controls; three paired runs per selected case are an initial engineering screen, not a reliability estimate. Declare the batch and budget before viewing its results. Retain failures, and investigate ambiguity instead of selecting only favorable runs. If both versions already succeed, report no demonstrated benefit and consider reducing the added instruction.

Keep explicit invocation separate from host discovery. Replayed histories do not establish live steering, cancellation, or process control. Live asynchronous integration is outside this release's required claim unless separately implemented and tested.

## 4. Installation and selection acceptance

Use a host-supported temporary configuration and disposable installation destinations. Do not modify an existing user installation. Record OS, CLI/host version, source revision, installed metadata, skill file hashes, and exposed skill names.

Exercise these paths on each host/OS combination the release claims to support:

- Install the candidate from a local marketplace and invoke each endpoint in a new session.
- Install v0.5.5, update the marketplace to the candidate, and inspect the installed version and bytes. If the host requires reinstall, verify and document that exact path. A refreshed catalog is not a verified upgrade.
- Test a standalone Get Set installation and a standalone Go installation with the other endpoint unavailable. Optional cross-package references must not become hard dependencies.
- In separate fresh sessions, present review, implementation, and routine requests without skill names. Record actual skill/reference selection as well as task outcome. Do not force a skill load to turn a failed discovery case green.
- Recheck a clean removal/reinstall path when needed for the documented recovery procedure.

Linux/macOS structural CI is not proof that both hosts were installed and exercised. State the tested support matrix and keep unavailable combinations unverified. Do not claim reliable automatic selection from a single successful session.

## 5. File changes and integration order

| Stage | Changes | Exit condition |
| --- | --- | --- |
| A. Establish baseline | Runner, cases, checker controls, recorded v0.5.5 attempts | Real model execution works; cases and protected boundaries discriminate valid/invalid controls. |
| B. Measurement guidance | Go performance reference; short Get Set assessment guidance | Changed decisions have behavioral evidence; valid measurements and routine work remain proportionate. |
| C. Recurrence prevention | Go learning reference and its routing text where needed | Prior mistake is rejected, legitimate behavior is retained, and read-only review stays read-only. |
| D. Integrated acceptance | Both changes together, matched evaluations, host checks | No observed unresolved contract violations in the required batch; targeted benefit and remaining limits are documented. |
| E. Release preparation | README catalogs, current scenario catalog, source provenance, release notes, root manifest version | Evidence matches final installed skill bytes; required checks pass and release claims stay within coverage. |

Keep historical evaluation reports intact. Add the new results to `evals/README.md`; update the current scenario catalog at `evals/set-go-2026-09-29/cases.md` without presenting scenarios as completed runs. Extend workflow source history with the pinned pstack paths and selective adaptation decisions, preserving existing MIT notices. Maintain English instructions and documentation; keep the existing Korean README translation aligned.

The marketplace file contains no version field to bump. Keep its identity/path consistent; change `.codex-plugin/plugin.json` to `0.6.0` during release preparation after the accepted scope is settled. Do not introduce a 1.x compatibility guarantee.

## 6. Release decision and validation

Required for this proposed 0.6.0 scope:

- At least one retained user-facing improvement has a demonstrated baseline gap and successful repeated candidate evidence under the recorded conditions. A design argument alone is labeled as such and cannot support a measured quality claim.
- Every required candidate case has been evaluated; read-only boundaries, protected inputs, correctness constraints, and routine-edit scope have no unresolved observed violation. Report counts and limits rather than asserting universal reliability.
- Installation, upgrade/reinstall, and independent endpoint use succeed for the declared support matrix. Discovery results are reported separately; do not advertise automatic routing beyond the observed evidence.
- `python3 scripts/validate.py`, relevant runner regression tests, link/metadata consistency checks, and the existing CI gates pass. Keep model evaluations opt-in; ordinary CI requires no model credentials and does not run paid batches implicitly.
- New checker controls reject broken artifacts and accept correct ones. Final artifact hashes match the evidence used for acceptance, or affected checks are refreshed.

If baseline behavior is already sufficient, remove redundant candidate instructions. If model execution remains blocked, keep the work as an unvalidated candidate and report the exact blocker. Do not label checker controls as model evidence or publish the proposed quality claim. If a regression remains, reduce scope or repair and reevaluate affected cases before promoting the candidate.

Commit, push, PR creation, release publication, and changes to user installations are later execution actions. This design request creates only this reviewable design document.
