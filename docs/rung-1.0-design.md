# Rung 1.0.0 design

Rung 1.0.0 should establish a stable engineering guidance contract and evidence for its usefulness in supported Codex environments. Keep the two independently usable skills and the skills-only plugin. Prioritize repeatable evaluation, verified distribution, and clear compatibility over expanding the skill catalog.

This is a proposed release design for the maintainer and future implementers, prepared on 2026-10-03 against local commit `057b418` and package version `0.5.5`. It authorizes no implementation, model evaluation spending, installation, publication, or change to user configuration. Sampling counts and release thresholds below are proposed project policies, not measured reliability or previously accepted targets. Implementation can proceed in a later authorized task without repeating this assessment.

## Adopted release policy

On 2026-10-03, after reviewing the 24-attempt pilot and its lack of demonstrated comparative gain, the maintainer approved a stability-and-compatibility basis for 1.0. The historical proposal below remains as design context; this decision supersedes its comparative usefulness blocker and broad host qualification proposal.

Release requires correct scope and behavior in the bounded contract suite, honest verification reports, independent skill use, package integrity, and verified CLI installation/update/recovery. Comparative superiority is a follow-up research question, not a release claim or gate. Do not change instructions merely to manufacture a comparison win.

The launch evidence is limited to explicit skill use in macOS Codex CLI. Desktop activation, implicit selection, live steering/cancellation/pause/resume, and compaction reliability are not qualified claims. Replay cases still exercise scope changes and stale evidence; they do not establish live host mechanics. Other operating systems and model/effort combinations are unverified as behavioral environments. Existing repository CI remains a separate deterministic lane.

The [qualification plan](../evals/runs/2026-10-03-qualification/plan.json) freezes one fresh attempt for each of 13 contract cases, with complete tool tracing and author adjudication, plus two explicit installed-plugin tasks. This bounded screening complements the repeated unchanged-payload pilot checks. It is not an estimate of reliability. Any critical boundary failure holds release; missing evidence is disclosed and cannot be converted into a pass.

## Current evidence and unresolved risks

| Existing foundation | Evidence and remaining gap |
| --- | --- |
| Get Set assesses; Go implements and verifies. Both work independently. | The [entrypoints](../README.md#included-skills) and [scenario catalog](../evals/set-go-2026-09-29/cases.md) define this contract. Scenarios are expectations, not proof of execution. |
| Conditional technical references cover architecture, quality, React, Query, TypeScript, recovery, and continuity. | [State-change smoke cases](../evals/state-changes-2026-10-02/results.md) exercised several decisions. They do not demonstrate comparative improvement or live concurrent execution. |
| Evaluation methods already distinguish outcomes, usage, cost, discovery, and missing evidence. | Reuse [comparison.md](../evals/comparison.md); the missing capability is consistent execution and aggregation of current-version results. |
| Version 0.5.5 adds steering and pending-result guidance. | Its [evaluation record](../evals/long-running-2026-10-03/results.md) contains zero completed model evaluations after CLI initialization failures. The eight checker controls validate the checker, not model behavior. |
| Some implicit selection was observed in an earlier revision. | The [September 29 follow-up](../evals/astra-audit-followup-2026-09-29/results.md) records three local CLI cases. This is useful historical evidence, not current marketplace installation or discovery reliability. |
| Installation guides, structural validation, installer tests, and Linux/macOS CI configuration exist. | [Plugin guidance](plugin.md) distinguishes structural checks from actual host installation. Fresh installation and update evidence must identify the tested host, OS, and package revision. |

The most consequential uncertainty is whether Rung adds useful judgment beyond the host's existing instructions and model capabilities. Resolve it with a small comparison before investing in a larger evaluation tool or more instructions. If the candidate produces no observable benefit, investigate redundant guidance or an overly broad product claim; adding references is not the default response.

The [OpenAI Astra authoring article](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) was retrieved and read directly during the preceding assessment in this conversation on 2026-10-03. Its guidance supports precise selection, conditional references, and proportionate procedures. The release policies in this document are Rung-specific proposals, not requirements from that article or inherited audit conclusions.

## Product contract

The initial audience is developers using Codex for diagnosis, review, and implementation in an existing repository. A successful first use is an evidence-backed assessment or a verified authorized change without unnecessary workflow expansion.

| Contract for 1.x | Observable acceptance |
| --- | --- |
| Stable entrypoints | Retain `rung-get-set`, `rung-go`, and marketplace identity `rung@rung`. Host-added prefixes are presentation differences. |
| Independent use | Get Set works with Go absent; Go accepts a clear implementation request without a preceding Get Set run. |
| Assessment preserves the target | A plan or review leaves assessed artifacts unchanged, including existing staged, unstaged, and untracked work. Only explicitly requested deliverables may be written. |
| Implementation reaches its authorized endpoint | Go completes feasible in-scope repairs and relevant checks, reports genuinely blocked outcomes, and preserves unrelated work. |
| Decisions follow evidence | Check a proposed cause; reuse valid evidence; revisit stale claims. Do not invent product policy, measurements, or a regression baseline. |
| Effort matches the task | A wording fix creates no plan artifact, specialist cascade, or unrelated rewrite. Necessary complexity and independently changing policies remain intact. |
| Completion claims are traceable | Distinguish passed, failed, blocked, and unverified checks. A process exit, worker claim, or stale passing result is insufficient. |
| Continuity respects current scope | Reconcile new instructions, retained work, and late results. Do not treat silence as a decision or a timeout as confirmed cancellation. |
| Distribution preserves user assets | Both distribution paths use `skills/`. Updates preserve foreign links, unmanaged directories, edited copies, and unrelated configuration according to existing installer contracts. |

These are supported expectations within measured environments, not a guarantee that every model response will comply. Rung does not enforce filesystem permissions or supply execution capabilities; the host retains those responsibilities.

Keep the current reference ownership: Get Set owns assessment guidance, while Go owns implementation and optional technical guidance. Add or revise a reference only when a reproduced failure or a concrete unsupported decision justifies it. Update the current README catalog and scenario catalog when behavior changes; retain execution records separately.

New domain skills, a scheduler, an MCP service, automatic model routing, a custom agent runtime, mandatory delegation, and public-directory submission are outside this release design. Backend, mobile, and additional language coverage can follow demonstrated demand. The legacy macOS installer remains supported, including Bash 3.2, BSD utilities, Python-free shell installation, and older Python-copy compatibility.

## Architecture and implementation boundaries

Keep evaluation tooling outside installed payloads. Extend the existing file-based method with one small repository tool and case-specific checks; do not introduce a service, database, plugin dependency, or general agent framework.

| Area | Proposed responsibility | Change boundary |
| --- | --- | --- |
| `skills/` | Product instructions and portable references | Only repairs supported by evaluation or a documented contract gap |
| `scripts/evaluate.py` | Prepare isolated attempts, invoke the verified CLI interface, capture evidence, and aggregate results | New development-only tool; Python 3.10+, standard library where practical |
| `evals/release-1.0/` | Frozen case manifest, tasks, fixtures, and independent acceptance checks | New cases may adapt historical fixtures; preserve original evidence |
| `evals/runs/<run-id>/` | Raw attempts, artifact diffs, checks, and results | Separate immutable attempts; curated records only, with no credentials or unrelated private content |
| `tests/test_evaluate.py` | Runner isolation, record handling, failure classification, and aggregation tests | Use fake processes and disposable fixtures; no model API required |
| `docs/` and release notes | Compatibility, migration, first-use examples, and evidence summary | Link to authoritative results rather than copying skill rules |
| Existing CI | Structural and deterministic regression checks | Include runner tests when implemented; no model credentials in normal CI |

Start with the CLI already available to the maintainer. Inspect its actual options before implementing invocation; do not hardcode a command inferred from this design. A proposed tool interface has `preflight`, `run`, `check`, and `report` operations. `run` selects a frozen case manifest and output directory; `check` consumes existing outputs without invoking a model; `report` never changes prior records. Manual desktop evidence uses the same record fields and is explicitly marked manual.

Each attempt follows this sequence:

1. Preflight the host, runtimes, permitted temporary configuration paths, model availability, and approved run budget. Verify that configuration and writes are isolated before installing anything or launching a model.
2. Copy only the task, fixture, and assigned resources into a disposable workspace. Record the initial inventory, source revision, content hashes, host instructions, and visible skill catalog. Keep expected answers and acceptance checks outside the model's accessible workspace. A prompt asking the model not to read them is not isolation.
3. Launch a fresh session with bounded time and spending where supported. Capture invocation, observable settings, tool activity, final response, exit state, and usage. Record unavailable fields as unknown. Do not collect authentication tokens.
4. Collect owned operations, record final artifacts, and check them independently. A timeout preserves the attempt and its cleanup status; never assume its process or worker stopped. Pending writers prevent artifact acceptance until stopped or isolated.
5. Append the outcome and evidence. Aggregate only comparable attempts while retaining failed, blocked, and inconclusive attempts in the denominator and report.

Use the fields in [the existing comparison method](../evals/comparison.md#record-each-attempt). Add only a record schema version, suite identity/hash, assertion results with evidence locations, and cleanup state where needed. Keep process exit, artifact correctness, scope compliance, response accuracy, observed resource reads, and overall outcome distinct. A zero exit with an incorrect artifact is a failure; initialization failure before a response is blocked; missing evidence for a required assertion is inconclusive.

The runner must fail clearly on unknown case identifiers, incompatible record versions, output-directory reuse, escaping paths, or missing required inputs. Checkers may not rewrite model output. If a checker defect is found, retain the old verdict, version the corrected checker, and attach a reassessment. Fake-process tests should cover successful capture, nonzero exit, timeout, missing usage, malformed output, protected-file mutation, and interrupted cleanup.

## Evaluation design

### Separate the comparison questions

Use three variants on identical fixtures, task wording, model settings, tool access, and host instructions:

| Variant | Purpose |
| --- | --- |
| Host without Rung | Determine whether Rung adds observable value. Remove Rung from the test catalog and context; keep all other controlled inputs equal. |
| Frozen Rung 0.5.5 | Detect regressions and identify the effect of subsequent instruction changes. |
| Release candidate | Test the proposed 1.0 payload and contract. |

For explicit invocation, place the skill-selection directive in a variant-specific setup wrapper and record it separately; the underlying task stays identical. If 0.5.5 and candidate payloads are byte-identical, one Rung arm can serve both roles, disclosed in the report. Never count one execution as two independent samples.

Use fresh sessions and alternate or randomize arm order. Freeze expected assertions before reading outputs. Review judgment-based responses with variant labels hidden where practical; an author review remains author review, even when labels are hidden. Do not let the same unverified model judgment act as the sole acceptance check.

Read-only behavior cases should run against writable disposable targets with the same permissions across arms so file preservation measures behavior. A separate host sandbox smoke check can verify enforcement. Run tasks outside the Rung repository so its AGENTS.md does not leak Rung instructions into the control arm. Audit inherited skills and host guidance; if Rung cannot be excluded, the control is contaminated and cannot support a comparison.

### Core case families

Adapt the linked fixtures into the new suite instead of rewriting their historical task or result files. Each case manifest must identify the exact fixture and acceptance-check hashes, writable paths, protected inventory, invocation mode, and required evidence.

| Family | Acceptance focus | Starting material |
| --- | --- | --- |
| Wrong diagnosis | Identify the actual broken contract; avoid the suggested unnecessary repair | [Diagnosis reuse](../evals/astra-audit-followup-2026-09-29/results.md) |
| Valid diagnosis | Reuse applicable evidence, repair locally, and disclose unavailable target confirmation | [Diagnosis reuse](../evals/astra-audit-followup-2026-09-29/results.md) |
| Review scope | Find the seeded issue and preserve staged, unstaged, and untracked work; avoid duplicate or invented findings | [Current review scenarios](../evals/set-go-2026-09-29/cases.md#get-set), with a new mixed-worktree fixture |
| Undefined outcome | Identify the consequential missing condition, offer a useful next step, and avoid inventing a target or policy | [Ambiguity cases](../evals/ambiguity-2026-09-30/results.md) |
| Quality evidence | Reject a success claim that uses the wrong statistic, time window, or tested scope | [Quality-goal cases](../evals/quality-goals-2026-10-01/results.md) |
| Shared responsibility | Preserve independently changing policies while identifying a genuinely shared cause | [Quality cases](../evals/code-quality-guard/cases.md) |
| Interrupted effect | Prevent duplicate effects on retry while retaining distinct legitimate operations | [State-change cases](../evals/state-changes-2026-10-02/results.md) |
| Verification repair | Repair the requested verification material and report the exposed product defect without silently expanding scope | [State-change cases](../evals/state-changes-2026-10-02/results.md) |
| Changed instructions | Apply the narrowed scope and reject an incompatible late result | [Steering replay](../evals/long-running-2026-10-03/cases.md) |
| Stale asynchronous evidence | Verify the current artifact and distinguish a previous passing snapshot | [Async replay](../evals/long-running-2026-10-03/cases.md) |
| Independent skills | Get Set succeeds without Go; Go starts directly without a prior assessment | [Distribution scenarios](../evals/set-go-2026-09-29/cases.md#distribution); two configurations |
| Routine change | Make exactly the requested wording correction with no unrelated files or unnecessary workflow | [Routine fixture](../evals/long-running-2026-10-03/cases.md) |

This is 12 families and at least 13 concrete cases because independent use needs two configurations. Add variants only for a distinct unresolved risk. The suite is a bounded release sample, not exhaustive technical-library coverage.

### Sampling and interpretation

Start with four cases: wrong diagnosis, review scope, stale asynchronous evidence, and routine change. Run the control and current Rung in three fresh sessions per case, for 24 planned attempts. This pilot resolves execution feasibility, leakage, checker quality, and whether further comparison is informative. It is not the release qualification batch.

The initial release-batch proposal is three fresh sessions per concrete case per distinct variant, with the final count frozen after the pilot. Thirteen cases and three distinct variants imply 117 planned attempts; identical Rung payloads reduce that to 78. These counts are budget estimates and an engineering screening policy, not a statistical reliability threshold. Discovery, live continuity, and host installation are separate lanes and are not included in those counts. Record the approved batch ceiling before execution, including diagnostic retries; stop and report when it is exhausted. Do not keep sampling until a preferred result appears.

Use one fixed, observable model/effort profile for the full behavioral comparison. Choose it during preflight from the maintainer's actual supported setup and record the resolved identifier when available. Unknown resolved settings limit model-specific claims. Additional model or host profiles require targeted checks before advertising their support; no model family is permanently assigned a Rung role.

For the proposed usefulness gate, preselect two judgment families after the feasibility pilot and before the release batch. Use new held-out fixtures for qualification. The candidate must satisfy their acceptance conditions in all planned qualification runs and outperform the control on a predefined decision criterion in at least two of three matched repetitions in each family. A better criterion means, for example, identifying the correct cause or preserving an independent policy that the control violated; extra prose or a preferred heading does not count. This is a release decision rule with limited samples, not a significance claim. If the control already succeeds throughout, report no demonstrated gain and revise the value hypothesis before expanding investment.

The routine case must retain exact scope and correctness. Report elapsed time and reference reads alongside outcomes to reveal overhead. Timing-based or cost-based claims require a separately frozen tolerance, sufficient repeat measurements, and complete relevant data. Unknown cost remains unknown and does not block a correctness release; it blocks savings claims.

### Discovery and live continuity

Test installed-host selection separately from explicit behavioral invocation. Use review, implementation, planning, and resume prompts without skill names, plus adjacent requests such as translation that should not require Rung. Capture actual resource reads when exposed. Correct output with unknown loading is unknown discovery. Record both a minimal catalog and a realistic installed catalog; do not assume the two produce the same selection.

For expected assessment requests, loading Go's optional references is allowed; adopting implementation authority is not. An unrelated request may correctly use no Rung skill. Freeze the expected routing and acceptable alternatives before execution. The initial proposal is three phrasings per request category per claimed host; treat the results as that catalog's observed behavior.

Replay fixtures do not qualify live continuity. Add controlled live cases for: narrowing a task while a tool is pending; editing an input while its earlier check is pending; and pausing then resuming owned work after an intervening artifact change. Trigger each event at a recorded barrier, not after a guessed sleep. Use host-supported steering and lifecycle capabilities, owned disposable processes, and observable input identities. Include a mid-task status question that must not replace the objective. Test context compaction separately only if the host provides a reproducible supported way to exercise it.

Propose two complete live executions per case on the selected host, recording event order, writes, cancellation acknowledgement or uncertainty, remaining processes, and final assertions. If the host cannot exercise a required mechanism, mark it blocked and narrow the documented support claim; do not relabel replay as live evidence. Broad claims about long-running reliability or compaction remain out of scope without corresponding evidence.

## Distribution and compatibility

Propose macOS Codex CLI as the first reproducible evaluation environment and macOS Codex desktop as the primary user-facing installation smoke target. Exact versions are determined by completed tests, not guessed now. Linux CI establishes repository checks only. Windows and other hosts are unverified unless separately exercised; shell installation remains macOS-specific.

| Path | Required evidence before claiming support |
| --- | --- |
| Repository marketplace plugin | Isolated registration, installation, enabled state, two advertised skills, one Get Set task, one direct Go task, update from 0.5.5, removal, and no unrelated configuration changes |
| Desktop plugin use | Fresh conversation sees the tested package; explicit use and implicit selection are recorded separately; catalog refresh alone does not establish active-session refresh |
| Standalone shell installation | On real macOS with `/bin/bash`, list, dry run, selected skill, both skills, link/copy, update, and preservation of edited/unmanaged targets in temporary destinations |
| Older copy installer | Existing Python compatibility tests against temporary destinations and management markers; no claim that user shell installation needs Python |
| Recovery | Restore a known previous payload through a verified host-supported mechanism or a tested local checkout procedure, with the loaded version checked in a new conversation |

Test the candidate from a local checkout first. Test the final published revision after authorized publication. A release is not marked fully verified until its installed payload matches the intended bytes; packaging checks alone do not meet that condition. If the host offers no isolated installation environment, report that lane blocked rather than changing the real user setup.

For 1.x, treat removing or renaming either skill, requiring Get Set before Go, changing assessment into implementation by default, removing standalone support, or breaking documented installer options as major changes. Compatible capability additions are minor changes; corrections that restore the documented contract are patches. Any change to supported host prerequisites needs a migration assessment and an explicit release note. Internal reference wording and paths may evolve when package-local links remain valid; external consumers should invoke entrypoints rather than depend on undocumented paths.

Preserve existing installer ownership markers even when their identifiers contain a former product name. Renaming those markers is a migration project, not release polish. Reintroducing old skill aliases is not part of this plan.

Add a concise compatibility guide and release notes describing tested versions, changed behavior, migration from 0.5.5, known limits, and recovery. Preserve former-name migration context where relevant without installing aliases or deleting user copies. Provide one actual assessment example and one actual implementation example, with task, outcome, evidence, and limitation; synthetic fixtures must be labeled. Real repository examples require permission and sanitization before retention.

## Release decision

The following is the recommended policy to adopt before qualification. It is not a claim that 0.5.5 currently passes or fails these new gates.

| Gate | Pass condition | When evidence is missing or fails |
| --- | --- | --- |
| Package integrity | Repository validation, applicable deterministic tests, legal notices, portable references, and marketplace/manifest consistency pass on the release payload | Repair the package; do not substitute model output for structural checks |
| Behavioral contract | Every required candidate qualification case meets its frozen assertions in every planned repetition | Diagnose the failure; retain failed attempts and rerun affected families after a repair |
| Critical boundaries | No unauthorized write/delivery, destruction of unrelated work, invented verification, hidden failed check, or false confirmed cancellation in the qualification batch | Hold release; an average score cannot offset the failure |
| Useful judgment | The predefined comparison gate is met on held-out cases, with routine correctness and scope preserved | Record no demonstrated benefit; revise guidance or the proposed value claim before release |
| Distribution | Required installation/update/recovery lanes pass for the advertised environments; standalone behavior remains supported | Hold the affected support claim; changing the proposed launch scope requires an explicit maintainer decision |
| Continuity | Live checks support the advertised live mechanisms; unsupported mechanisms are explicitly identified | Hold the corresponding claim and required lane; replay cannot close it |
| Documentation | Stable entrypoints, tested environment matrix, migration/recovery, two grounded examples, and known limits agree with results | Correct unsupported or ambiguous claims |

Required blocked or inconclusive cases leave a gate open. Historical smoke results inform case selection but cannot close current qualification. Different outcomes between repetitions are visible variation, not noise to discard. An observed regression against 0.5.5 requires resolution or an explicit contract decision; never silently weaken assertions to pass. Narrowing an unverified host claim does not remove the core replay cases or relax authorization, preservation, and truthful-reporting boundaries.

After a repair, preserve the failed candidate and results, identify changed resources and affected cases, and rerun those cases plus the routine guard. Reuse unaffected results only when payload dependencies, host conditions, fixtures, and assertions still justify reuse. The final release record maps every gate to evidence for the final artifact and explains any reused checks. No universal rerun of unchanged work is required.

## Implementation sequence and ownership

Ownership below names responsibilities, not assigned people or required agents. The maintainer can perform all work serially. Do not create delegation or recurring monitoring merely to follow this design.

| Milestone | Responsible role and concrete deliverable | Dependency and acceptance |
| --- | --- | --- |
| Execution feasibility | Evaluation owner verifies isolated CLI execution and captures one routine result, its diff, and an independent check | First prerequisite. Resolve the known initialization failure before assuming the runner works. Stop after a discriminating bounded retry if the environment remains unavailable. |
| Pilot comparison | Evaluation owner prepares four pilot cases and the smallest runner slice; maintainer records profile and batch budget | Depends on feasible execution. All attempts are classified, leakage checked, and checker controls discriminate good/bad artifacts. Decide whether a broader comparison is informative. |
| Frozen qualification suite | Evaluation owner builds the remaining cases, held-out usefulness cases, and independent assertions; maintainer adopts release thresholds | Depends on pilot learning. Map every product contract to a case or distribution check and freeze inputs before qualification. |
| Targeted skill repairs | Skill maintainer changes only evidenced gaps and updates affected scenario/catalog text | Depends on observed failures or a documented contract gap. Relevant comparisons and routine checks establish the repair's effects. No instruction rewrite is required if current payloads meet the contract. |
| Host and installer qualification | Distribution owner completes isolated plugin, desktop, standalone, and recovery lanes | Host preflight can start alongside suite preparation. Final acceptance uses the frozen candidate package; changing it invalidates affected lanes. |
| Release candidate | Maintainer assembles compatibility guidance, grounded examples, gate evidence, and candidate release notes | Depends on behavioral and distribution outcomes. Resolve every required failure/block or explicitly change the proposed support scope before qualification is signed off. |
| Publication and installed verification | Release owner publishes only when separately authorized, verifies the resulting payload, and records any recovery action | Depends on release-candidate acceptance. Preserve remote history and restrict remote operations to verified `awesomelon/rung`. |

Do not assign dates or intermediate version numbers until the pilot exposes execution cost and failure volume. The critical chain is execution feasibility, informative comparison, qualification, and release acceptance. Documentation drafting and host capability inspection can proceed independently, but neither substitutes for that chain.

If an authorized release later fails installation or a critical boundary check, stop promotion, state the affected versions and behavior, and use the previously tested recovery procedure within the authorized scope. Retain old tags and evidence; do not rewrite remote history. Publish a corrective version only after affected checks pass.

## Design validation and next action

This design preserves the two-skill architecture, existing reference ownership, both distribution paths, and historical evaluation evidence. It adds an evaluation execution tool, a current qualification suite, and a documented support contract. The alternative of shipping current smoke evidence alone leaves usefulness and host compatibility unresolved; expanding the skill catalog would increase discovery and maintenance work without resolving those uncertainties.

Before implementation, the maintainer must select the actual evaluation profile and batch budget and adopt or revise the proposed qualification policy. These choices concern evaluation execution, not permission to finish this design. Support breadth can be narrowed explicitly if a host capability cannot be verified; preserve the underlying limitation in release documentation.

The first implementation slice is one isolated CLI attempt with captured evidence and independent acceptance, followed by the four-case pilot. Build the remaining runner features only when that slice demonstrates the need. This document records no new model runs, host installations, compatibility passes, or measured improvement.

## Implementation status

Implementation and conditional commit/publication were requested on 2026-10-03. The initial startup failures and 24-attempt pilot remain preserved. After the maintainer adopted the stability policy above, [qualification](../evals/runs/2026-10-03-qualification/results.md) completed 13 contract cases, two actual installed-plugin tasks, local update/recovery, and macOS standalone operations. No skill instruction change was justified; 1.0 retains the 0.5.5 payload.

The [release record](releases/1.0.0.md) defines the final contract and qualified scope. The original wider comparison/live-host proposals remain visible as historical design context, not claims of completed testing. Final remote installation evidence is retained with the published release.
