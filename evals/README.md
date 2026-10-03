# Evaluation evidence and translations

Scenario catalogs define expected behavior. Result documents and saved responses describe particular runs; neither proves that every scenario passes.

For a before/after comparison, hold the task input, starting fixture revision, model configuration, tool access, and permissions constant. Give fresh workers only the task, raw artifacts, and the selected skill resources; withhold expected findings and coordinator acceptance checks. Record the skill and reference content hashes, changed artifacts, commands/results, and actual output. Use independent behavioral assertions rather than checking for headings or preferred wording. Repeat cases when observed variation affects the conclusion; a single pair is a smoke comparison, not a reliability benchmark.

For incremental maintenance, review changes to referenced resources, metadata, fixtures, and checks along with SKILL.md. Use Git/content changes rather than file modification time. Keep a reason for retaining, improving, merging, or removing a skill, and leave task success, automatic discovery, elapsed time, token usage, and cost as separate measures. Do not infer unmeasured usage or savings from shorter prompts.

Use [comparative evaluations](comparison.md) to record matched runs, actual model settings, usage, and success criteria. Missing measurements remain unknown; structural validation and a model process exiting successfully are not task-success evidence.

Repository instructions, Markdown documentation, UI metadata, and task descriptions are now in English. Historical reports and saved Markdown responses are labeled translations with links to their original versions. Translation is not a new model run, and historical character counts, tool versions, commands, and pass totals still describe the original run.

The current skill names use the Rung prefix. Recorded runs retain CraftFlow names and hashes from their original revision; the rename is not a new behavioral evaluation.

## Current skill catalogs

The [1.0 contract suite](release-1.0/README.md) provides 13 cases and a bounded evaluation runner. Its [qualification record](runs/2026-10-03-qualification/results.md) separates contract behavior, installed tasks, distribution, and author adjudication. The earlier [native pilot](runs/2026-10-03-native-pilot/results.md) records 24 comparison attempts with correct artifacts in both arms and no demonstrated comparative gain. The [startup failures](runs/2026-10-03-pilot/results.md) are retained.

| Skill | Scenarios |
| --- | --- |
| `rung-get-set` | [Investigation, planning, and review](set-go-2026-09-29/cases.md#get-set) |
| `rung-go` | [Implementation and verification](set-go-2026-09-29/cases.md#go) |

[Set/Go results](set-go-2026-09-29/results.md) record actual execution separately. The [previous three-skill results](three-skills-2026-09-28/results.md) describe their historical revision.

[2026-10-03 long-running work](long-running-2026-10-03/results.md) provides matched-case fixtures for changed instructions, stale asynchronous results, and a routine edit. The local CLI failed before model execution, including a bounded configuration retry. Eight author-created fixture/checker controls behaved as expected; they are not model runs or evidence of comparative improvement.

[2026-10-02 state-change cases](state-changes-2026-10-02/results.md) record a read-only shared-state assessment, an interrupted-operation repair, verification-tool maintenance that exposes a product regression, and a routine edit. These are unpaired explicit-invocation smoke cases; parent checks cover edit boundaries and replay behavior, not comparative improvement or live concurrency correctness.

[2026-10-01 quality-goal cases](quality-goals-2026-10-01/results.md) record four baseline smoke cases and one follow-up after clarifying operational availability evidence. Existing instructions already handled missing latency conditions, policy-based security acceptance, and mismatched quality claims in these samples. The results explain why broader instruction additions were not retained; they do not establish a comparative quality gain.

[2026-09-30 ambiguity cases](ambiguity-2026-09-30/results.md) record explicit-invocation checks for vague performance and onboarding requests, a focused delivery plan using the changed execution-strategy reference, and a routine edit. These are unpaired smoke cases, not proof of improvement over the previous instructions.

[2026-09-30 platform signal cases](platform-signals-2026-09-30/results.md) record explicit-invocation checks for differing user workarounds, abandonment without a workaround, migration cohorts with different barriers, and a routine edit. These are unpaired smoke cases; the results separate reference selection, decisions, and file preservation from claims of comparative improvement.

[2026-09-29 audit follow-up](astra-audit-followup-2026-09-29/results.md) records fresh local CLI cases for valid/stale diagnosis reuse and a read-only review using Go's technical references, including observed resource selection and its limits.

Historical scenario catalogs and raw evidence retain the names used at their recorded revision: [orchestration](engineering-orchestrator/cases.md), [architecture](architecture-guard/cases.md), [quality](code-quality-guard/cases.md), [React](react-quality-guard/cases.md), [refactoring](refactoring-guard/cases.md), [Query](tanstack-query-guard/cases.md), and [TypeScript](typescript-quality-guard/cases.md). They are not the current install catalog.

## Focused instruction maintenance

[2026-09-28 consolidation](instruction-consolidation-2026-09-28/results.md) records two fresh standalone smoke cases, resource hashes, and text-size changes. It does not establish automatic discovery or comparative performance.

## Reproduce a historical run

Use the [complete pre-translation tree](https://github.com/awesomelon/codex-skills/tree/ce11c34e3d1da77140087300218b776594bb65cf) for original Korean skill bodies, task wording, and saved responses. For example, create an independent checkout without changing the current working tree:

```bash
git worktree add --detach ../codex-skills-original-evidence ce11c34e3d1da77140087300218b776594bb65cf
```

A historical manifest's hashes refer to the original input/skill bytes identified by that run, not the current English translations. Follow the run's source commit and manifest when replaying an evaluation. Do not rewrite recorded hashes to match translated files or count old results as validation of the English instructions.

## Raw evidence retained unchanged

| Material | Reason to preserve the original bytes |
| --- | --- |
| JSON manifests and command records | Exact requests, commands, versions, and input/output hashes |
| TAP/text logs and implementation patches | Original execution evidence and reproducible diffs |
| Historical skill snapshot in `quality-initial-SKILL.txt` | Captures the actual instructions used before a correction |
| Fixture/generated code with Korean labels and Unicode-path tests | Product strings and Unicode test inputs are behavior/evidence, not instruction prose |

These raw artifacts may contain Korean. Their surrounding explanations and translated reports are in English. For new runs, record the actual instruction/input hashes and results separately. English instructions do not force English replies: existing task requests for Korean responses remain expressed in English.
