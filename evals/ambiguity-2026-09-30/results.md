# Ambiguity handling — 2026-09-30

## Change and basis

Get Set's reference table now explicitly routes unclear outcomes and problem framing to the existing problem-selection guidance. Execution strategy connects a failed assumption to affected people, harm after shipping, and practical recovery, using those consequences to set the evidence needed before dependent investment. The existing scope boundaries and direct execution path for clear Go requests remain intact. No fixed interview, mandatory discovery phase, or new skill was added.

The source was the user-supplied article *What Actually Makes You Senior*; no author or publication URL was supplied. Its ambiguity-reduction argument was compared with existing instructions before these narrow changes. The designated [Astra authoring article](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) was fetched directly during the preceding review in this conversation on September 30, 2026, Asia/Seoul. The recommendations follow its contextual reference loading and avoidance of overprescribed workflows; they are not inferred solely from earlier repository audits.

The English README and current [scenario catalog](../set-go-2026-09-29/cases.md) describe the supported behavior. Plugin version is 0.5.1; marketplace identity and source path remain consistent without a marketplace edit.

## Method

Four fresh subagents received explicit skill invocations, temporary copies of the supplied skills, and only their task and raw artifacts. No conversation history, expected findings, coordinator analysis, or sibling answers were supplied. Models and reasoning settings were inherited without overrides; no independent model/version measurement was captured. The environment was macOS; this evaluates responses and local file behavior, not macOS installer support.

The first two tasks ask for assessment of vague goals. Their wrappers name Get Set but no reference, allowing observation of reference selection. The routine task invokes Go. The onboarding reviewer did not load execution-strategy.md, so a fourth fresh planning case explicitly requested that reference to exercise the changed paragraph. This fourth case does not test reference routing.

The [manifest](manifest.json) records the base commit, exact wrapper prompts, input and supplied-resource hashes, response hashes, post-run inventories, and actual resource reads reported by each evaluator. [Raw responses](responses/) retain the agents' wording and temporary paths. The rollout fixture reuses [onboarding evidence](fixtures/onboarding/evidence.md), copied to its temporary directory as `evidence.md`; its separate [task](fixtures/rollout/TASK.md) is preserved. Source and skill directories were checked after execution. The only permitted task mutation was the routine spelling correction. Response records were written outside each assessed directory.

## Observed results

| Case | Observed decision | Parent acceptance |
| --- | --- | --- |
| [Vague performance goal](responses/performance.md) | Selected problem-selection, investigation, and measurement. Narrowed the affected workflow to fresh-session large-trace opening; calculated parse time at about 81.5% in the supplied captures; treated a shared cache as unproven and proposed discriminating profiling. Did not claim production percentiles or a measured improvement. | Calculations match the supplied sequential spans. Forwarded complaints were not counted independently. Task inventory unchanged. |
| [Vague onboarding complaint](responses/onboarding.md) | Selected problem-selection and review-scope. Separated expiry from approval handoff, identified the unresolved meaning of an invitation, and connected immediate access to downloads that revocation cannot recall. Recommended a bounded check without inventing access policy. | The distinction and recovery limit match the supplied notes. Asked for the consequential policy decision while identifying independent investigation. Task inventory unchanged. |
| [Focused delivery plan](responses/rollout.md) | Read execution-strategy. Deferred automatic activation pending an access contract, identified the first document response as the irreversible disclosure boundary, and distinguished synthetic workflow checks from authority to expose real documents. Allowed policy-preserving preparation and proposed outcome evidence. | Concrete harm, recovery limits, and investment gates are supported by the fixture. No production action, outreach, implementation, or invented commitment. Task inventory unchanged. |
| [Routine edit](responses/routine.md) | Read only Go's entrypoint and corrected the requested word without discovery questions or a plan artifact. | Parent asserted the entire resulting README equals the original with only `proceses` replaced by `processes`; TASK.md unchanged and no extra task files. [Result](routine-result.md). |

[Acceptance records](acceptance.json) separate parent file assertions from qualitative assessment. All four cases met the scoped acceptance criteria. No instruction revision was justified by these responses.

## Structural verification

- Both skills passed `scripts/validate.py`; the changed skill passed Skill Creator's `quick_validate.py`.
- Final checks used Python 3.11 and the pinned PyYAML 6.0.3 in a temporary virtual environment. The system Python initially lacked PyYAML. No user Python installation, installed skill, or Codex configuration was changed.
- Changed documentation links, root plugin/marketplace consistency, and `git diff --check` passed. [Recorded commands and output](structural-checks.json).
- Installer and validator implementations were unchanged, so their regression suites were not rerun. No Plugin Creator validator was found in the installed plugin cache. No installation, marketplace registration, or remote release was performed.

## Limits

These are four unpaired, explicit-invocation smoke cases. They do not establish a before/after quality gain, reliability, automatic skill discovery, plugin-host behavior, latency, or cost savings. The first three do not exercise the changed execution-strategy paragraph; the fourth exercises it through a forced reference read. The evidence is synthetic and supplies relevant observations and policy gaps. Success here does not establish performance with missing, inaccessible, or contradictory real-world evidence. The assessment cases ran no application code, production workflow, or new benchmark. Unchanged files establish the final inventory, not an audit of every intermediate filesystem operation.
