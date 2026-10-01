# Quality goals — 2026-10-01

## Decision and scope

The user requested improvements following a review of [a video about verifiable quality goals](https://www.youtube.com/watch?v=OTttvhEHncQ). Its full Korean auto-generated transcript was read in the preceding review on 2026-10-01. The [OpenAI authoring article](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) was fetched directly in that review. This is fresh source verification in this conversation, not an interpretation inherited from an earlier audit. Neither source's full text is redistributed here.

The proposed additions covered defining quality acceptance conditions, matching evidence to claims, and testing those decisions. Baseline evaluation showed that the existing skills already handled these decisions in the supplied cases. Therefore no new quality skill, mandatory form, ISO checklist, numerical defaults, or repeated requirements workflow was added. The Get Set entrypoint and requirements reference, and Go's performance reference, remain unchanged.

One existing sentence in Go's [verification guidance](../../skills/rung-go/references/workflow/verification.md) used "availability" for a start/request observation. It now distinguishes a service starting and responding from an operational availability target, which needs evidence over its agreed population and observation window. This is a wording clarification; the baseline did not demonstrate a behavioral failure. The README catalog and current [scenario catalog](../set-go-2026-09-29/cases.md) now expose the relevant use cases and expected behavior.

## Executed cases

Four fresh subagents evaluated copies of the baseline skill packages in a temporary workspace. Each received an explicit skill invocation, its raw task, permitted resource paths, and an instruction to record actual reads and checks. They did not receive the preceding conversation, expected findings, sibling responses, or acceptance checks. A fifth fresh subagent evaluated the same evidence task with only the revised verification resource changed. All used inherited model/reasoning settings; the resolved model configuration was not independently captured. Exact prompts, input/resource hashes, and response hashes are in the [manifest](manifest.json).

| Case | Observed result | Acceptance |
| --- | --- | --- |
| [Incomplete performance target](responses/baseline-performance.md) | Identified missing percentile, workload, timing boundary, and measurement window. Preserved read-your-writes. Declined to justify a shared cache or four replicas from the laptop mean. | Met the scoped criteria; no target was invented and no implementation began. |
| [Broad security request](responses/baseline-security.md) | Converted existing team/admin access policy and incidents into allow/deny and regression cases. Preserved legitimate access and excluded retention/certification expansion. | Met the scoped criteria without a numerical security score or new policy interview. |
| [Quality evidence, baseline](responses/baseline-evidence.md) | A: mean does not establish p95. B: 0.8% errors fail the 0.1% guardrail despite passing latency. C: startup does not establish monthly request availability. D: the controlled audit check passes only within its tested scope; overall security remains unverified. | All four dispositions matched the supplied contracts. |
| [Routine edit](responses/baseline-routine.md) | Corrected one typo, read only Go's entrypoint, and produced no quality-goal interview or specification. | Exact expected file bytes; only README.md changed. [Result](routine-result.md). |
| [Quality evidence, revised](responses/revised-evidence.md) | Preserved all four baseline dispositions after the availability wording clarification. Read verification and performance references. | Met the same criteria; no comparative improvement demonstrated. |

The [acceptance record](acceptance.json) separates manual semantic judgments from automated file-integrity assertions. Parent checks confirmed preservation of all assessment fixtures and baseline skill resources, the exact routine substitution, and that only verification.md differed in the revised skill copy. Paths actually read are self-reported in the saved responses and indexed in the manifest. Baseline performance used measurement and problem-selection references; baseline security used problem-selection and architecture preflight. Neither needed an expanded requirements reference to meet these cases.

## Verification and limits

[Structural checks](structural-checks.json) record repository validation, the changed skill's Skill Creator validation, current local documentation links, and whitespace checks. Checks use an isolated temporary Python environment; no installed skills or user configuration were modified. Installer and validator code did not change, so their regression suites and installation operations were not rerun.

These are synthetic, explicit-invocation smoke cases. The evidence case supplies accepted contracts; it does not test discovering them in a real project. The security case supplies a policy and incidents, not application source. The performance case has no runnable benchmark. The follow-up is one baseline/revised comparison, not a reliability benchmark. There is no evidence of automatic discovery, plugin-host behavior, live security or availability, model-specific reliability, token/cost savings, or comparative quality improvement. The ISO-example expectation in the scenario catalog remains unexecuted: no fixture supplied an ISO-derived default. Prompt-level resource restrictions and final inventories do not prove every intermediate filesystem operation was confined.

## Release packaging follow-up

The subsequent release request sets the root plugin version to 0.5.3. Marketplace identity, policy, category, and root source path remain aligned. [Release checks](release-checks.json) record a successful local-path marketplace registration and plugin installation using Codex CLI 0.158.0 on macOS in a temporary Codex configuration. The plugin was listed as installed and enabled at 0.5.3, and every installed skill file matched the source. Existing user configuration and installed plugins were preserved. Plugin Creator's validator was not available in the installed skill/plugin catalog. This check establishes local CLI installation, not Git marketplace retrieval, automatic skill selection, or an existing installation's upgrade behavior. Remote CI and publication are reported in the GitHub release.
