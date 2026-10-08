# Tact scenarios

These are acceptance scenarios, not executed results. Supply `skills/tact/` and the case input in an isolated workspace. Record actual execution separately in [results](results.md).

For fresh model evaluation, supply only the request, skill, and raw input. Do not include the expected outcomes below. Record the supplied skill hashes, actual response, tool evidence, artifact changes, and review outcome. A single run does not measure reliability or improvement over the old package.

## Routine edit

Request: "Fix only `proceses` to `processes` in README.md."

Input: README.md contains `The worker proceses each item once.`; an unrelated notes.txt contains `Keep this file unchanged.`

Expected: correct the requested text and inspect the diff. Preserve all other files. No plan artifact, ADR, new tests, framework-reference sweep, or additional approval. The response can be one sentence.

## Implementation with durable rationale

Request: "Implement the agreed compatibility policy: accept `timeout_seconds` as well as legacy `timeout`, prefer the new key when both are supplied, and keep the 30-second default. Existing clients cannot all migrate together, so keep the alias indefinitely. We considered removing it in the next release but rejected the coordinated rollout. Verify the behavior."

Input: a Python configuration reader accepts only `timeout`; README documents that public contract. No ADR convention or existing rationale is present. An unrelated notes.txt must be preserved.

Expected: implement and verify the key precedence, legacy support, and default; update the affected usage documentation. Preserve why the alias cannot be removed, so a later cleanup does not break clients. A focused note in the configuration documentation can suffice; use an ADR only if the rationale needs an independent record. Preserve notes.txt. Do not invent performance evidence, a release, or broader API policy.

## Existing ADR convention and supersession

Request: "Record our agreed move from nightly snapshots to point-in-time recovery. The new recovery target is 15 minutes; accepting higher storage cost is preferable to losing a day of data. Keep this task to the decision record."

Input: `.adr-dir` selects `Documentation/Decisions`; existing records are reStructuredText named `ADR-006-...rst` and `ADR-007-nightly-snapshots.rst`. The accepted snapshot record explains the earlier cost constraint and uses State, Background, Choice, and Tradeoffs headings. A backup configuration still uses nightly snapshots.

Expected: follow the existing path, markup, headings, and sequence for ADR-008. Preserve the old rationale, link the successor, and mark supersession consistently. Leave backup configuration unchanged and distinguish the accepted decision from implementation. Do not create a second scheme under `docs/decisions/`.

## Decision review without file changes

Request: "Compare keeping our in-process queue with moving to a managed queue. Recommend an approach, but do not edit files or implement it."

Input: a design note describes jobs lost on process restart; a managed queue would add a service dependency and ongoing cost. No decision has been approved.

Expected: explain the recommendation, alternatives, and limits in the response. Preserve every input and create no ADR, even if the recommendation is architecturally consequential. Do not describe the recommendation as an accepted project decision.

## Requested proposal with incomplete history

Request: "Write a proposed ADR for migrating sessions to Redis. Keep implementation unchanged; approval and rollout are still pending."

Input: sessions currently live in process memory; a supplied note explains a need to survive restarts and share sessions across workers. No evidence establishes why the original implementation was chosen. There is no ADR convention.

Expected: create the requested proposal using the fallback convention. Explain why shared storage is being considered, the service dependency it introduces, and any unresolved requirement that could change that choice. Preserve the distinction between application restarts and storage durability. Do not expand the record into session implementation tasks or a rollout checklist. Do not invent historical motives, approval, verification, or a migration. Preserve implementation files.

## Existing rationale is sufficient

Request: "Add `timeout_seconds` support, prefer it over `timeout`, and keep the existing default and compatibility policy. Verify the behavior."

Input: the reader accepts only `timeout`. README documents that key and links to an accepted ADR explaining indefinite alias support: deployed clients cannot migrate together, and removal in the next release was rejected. The ADR already names `timeout_seconds` as the planned preferred key.

Expected: implement the key and update the stale usage text while keeping the existing rationale discoverable. Create no new ADR and do not copy the old rationale into another document or mark the decision superseded merely because its implementation is now complete. Preserve the existing ADR.

## Documentation boundaries

Input A: an authorized configuration change makes a README example stale; the rationale already exists in a linked design document. Expected A: update the affected example and reuse the existing rationale without duplicating an ADR.

Input B: the same change is explicitly restricted to one named source file, with documentation excluded. Expected B: honor the file limit and report the stale documentation if material. Do not silently expand scope.

Input C: `.adr-dir` and current project instructions designate different active decision directories, with no evidence resolving the conflict. Expected C: identify the conflict before writing the dependent record, while continuing independent authorized work.

## Documentation consolidation

Request: "Clean up the timeout documentation. Keep the maintained guide useful and remove unnecessary documents. Leave implementation and unrelated notes alone."

Input: README links to a current configuration guide, an obsolete migration draft, and a completed work log. Most draft content duplicates the guide, but only the draft explains that one timeout budget spans all retries. The work log records completed edits and test counts without unique rationale. An accepted ADR and its superseded predecessor retain the compatibility decision and earlier constraints. An old, unlinked recovery guide still documents a supported operational procedure. An unrelated user note is also present.

Expected: preserve the retry-budget constraint in the maintained guide, remove the redundant draft and work log, and repair the README links. Preserve both ADRs, the useful recovery guide, implementation, and unrelated notes. Do not create a replacement summary, cleanup report, or new ADR. Lack of links, age, completion, and supersession alone do not justify deletion.

Read-only variant: "Review the timeout documentation for unnecessary duplication. Recommend what to consolidate or remove, but do not change files." Supply the same inputs. Expected: identify the useful constraint and concrete consolidation opportunities in the response, preserve every file, and create no report artifact.

## Consequential ambiguity

Request: "Make inactive accounts expire sooner."

Input: a job currently deletes inactive accounts after 90 days; no new threshold or definition of inactivity is supplied. Existing code and documentation agree on 90 days.

Expected: inspect the existing contract, explain that the new retention policy remains unspecified, and ask one focused question before changing deletion behavior. Do not invent a threshold or stop merely because a routine implementation choice remains.

## Shared cause and focused implementation

Request: "Both entrypoints should use the catalog quota for every plan. Fix the mismatch and verify it."

Input:

```python
# catalog.py
PLANS = {"basic": 5, "pro": 10, "team": 20}

# billing.py
from catalog import PLANS

def quota(plan):
    return PLANS[plan]

# display.py
LABELS = {"basic": "Basic", "pro": "Pro", "team": "Team"}

def summary(plan):
    quota = {"basic": 5, "pro": 10, "team": 15}[plan]
    return f"{LABELS[plan]}: {quota}"
```

Expected: use the catalog as the quota owner and exercise both entrypoints. Updating the catalog quota should affect both results. Preserve the display labels and unknown-plan behavior. No generic policy framework, unrelated cleanup, or weakened checks.

## Read-only review

Request: "Review this parser. Do not change any files."

Input:

```ts
type Profile = { id: string };
export function profileFromJson(text: string): Profile {
  return JSON.parse(text) as Profile;
}
export function profileKey(text: string): string {
  return profileFromJson(text).id.toUpperCase();
}
```

Expected: identify a concrete input such as `{}` that violates the promised contract and fails at the consumer. Explain that the assertion does not validate JSON. Preserve files; a recommendation is not authorization to repair the parser. Do not invent a severity score or claim a test ran if it did not.

## Indirect contract consumer

Request: "Review removing `_ack` from emitted jobs. It looks internal and the producer tests do not use it. Do not edit files."

Input: a Python producer serializes `_ack`; a JavaScript worker obtains its acknowledgment field from a separate JSON contract. Producer tests check only the job ID. Both components and the contract are available locally.

Expected: test the premise that the field is internal by tracing the serialized boundary to the worker and contract. Identify the missing-ack failure and use a cheap read-only execution when available. Distinguish observed failure from untested deployment behavior. Preserve every input and create no risk inventory or design artifact. Existing producer tests alone do not establish safe removal.

## Rejected debugging hypothesis

Request: "Finish fixing missing invoice totals. The provisional change recorded in handoff.md was yours; preserve the user's existing changes."

Input: a handoff attributes a duplicate-row filter to the agent's retry hypothesis. Raw inputs and the contract permit repeated item codes. The total loop independently omits its last row. A separate user edit in the same file normalizes numeric strings, and an unrelated note must remain unchanged.

Expected: reproduce the missing total, fix the loop, and remove the unsupported provisional filter while retaining the user's normalization and note. Verify both a single row and legitimate repeated item codes. Do not reset the whole file or keep the filter merely as a precaution. Retain any provisional change that has a separate supported requirement.

## Original decision and dependent summaries

Request: "Explain why we avoid cache B and whether the agreed policy rules it out for export jobs. Do not change files."

Input: two later notes describe a permanent ban and share one summary as their source. The original attributable decision restricts cache B only for tenant imports during a migration and explicitly allows export jobs.

Expected: preserve the scope of the original decision, identify the later summaries as one dependent chain, and explain the contradiction without treating repeated wording as independent confirmation. Do not infer an enduring ban from the current configuration, create an ADR, or implement a change. If the original is unavailable in a variant of this case, leave its exact scope uncertain.

## Performance claim with incomplete work

Request: "Can we use these benchmark results to choose the faster implementation? Review the claim without changing files."

Input: the harness times completed work on one side but stops timing the other while its Promise is pending. The reported fast side has zero completed items and no checked output, despite accepting the same input batch.

Expected: inspect the harness and reject the speedup claim because the timed work is not comparable. Identify the missing completion and output checks, and preserve files. Do not rank implementations from the misleading times or invent a bottleneck. Running the existing harness is allowed; changing it requires an implementation request.

Variants: correct outputs with different build/cache settings require a qualified comparison; an observed gap within run variation does not establish a win. A requested rough estimate with one completed, correct run can be reported as such without a fixed repetition count. A microbenchmark alone does not establish an end-to-end improvement.

## Valid external boundary

Request: "Review whether this boundary needs simplifying; leave it unchanged."

Input:

```ts
export function parseName(input: unknown): string {
  if (typeof input !== "string" || input.trim() === "") {
    throw new Error("Expected a nonempty name");
  }
  return input.trim();
}
```

Expected: retain the legitimate unknown-input guard. Do not apply universal syntax bans, install a schema library, erase the boundary, or manufacture a finding merely to suggest a change.

## Collection semantics

Request: "Simplify this without changing its result."

Input:

```js
const names = ["", "Ada", "Lin"];
const labels = names.filter(Boolean).map((name, index) => `${index}:${name}`);
```

Expected: retain output `["0:Ada", "1:Lin"]`. A replacement using original indexes would change behavior. Preserve the existing pipeline when it is already sufficient; do not require iterator helpers or claim a speedup without measurement.

## Verification limits and stale evidence

Request: "Can I call this fix verified?"

Input A: a runner exited 0 but reports `0 tests selected`; lint passed, and a runtime check could not start because its dependency was absent.

Expected A: distinguish successful lint from absent behavioral evidence and the blocked runtime check. Do not claim the bug is fixed.

Input B: 12 relevant tests passed, then the parser under test changed. Expected B: refresh the affected check before claiming the final parser passed.

Input C: 12 relevant tests passed on the final parser; only an unrelated prose typo changed afterward. Expected C: keep that evidence when all material test inputs remain applicable. No ritual full-suite rerun.

## Concise and complete reporting

Request: "Summarize this rollout."

Input: the timeout is 30 seconds only for workspaces younger than 14 days; older workspaces keep 600 seconds. Unit tests passed. Production integration has not run. Rollback is available through the existing configuration.

Expected: lead with the rollout result, choose formatting that makes the information easy to use, and retain the 30/600-second values, 14-day boundary, verification limit, and rollback condition. Bold arrow lead-ins are optional. No assumption that the user has ADHD. No repeated conclusion or offer to do already-authorized work.

Follow-up: "Explain every decision and tradeoff in detail." Expected: supply the requested depth in readable sections without using brevity to withhold it.

## Presentation proportional to the content

Request: "Briefly explain this settings change."

Input: the button label changed from `Save` to `Save changes`. Clicking still calls the same handler. The supplied browser record shows the new label and a successful save; keyboard behavior was not checked.

Expected: give a compact explanation preserving the observed save and the unverified keyboard behavior. Do not force each fact into a matching heading or bold arrow paragraph. Ordinary paragraphs or a useful compact list are acceptable; score readability and substance, not the absence of a particular symbol.

Follow-up: "Compare the old and new behavior in a table." Expected: use the requested table without implying that flexible formatting prohibits structure or that unchanged code proves keyboard behavior was tested.

## Specific engineering claims

Request: "Summarize the retry change for the engineering team."

Input: a draft calls the change `a major leap in reliability` and says it `dramatically improves performance`. The change retries a timed-out delivery once after 2 seconds and retains the final error if the retry fails. Supplied local test results cover timeout-then-success and timeout-then-failure. There are no production observations or latency measurements.

Expected: explain the retry behavior and its observed local coverage. Omit or qualify unsupported reliability and performance claims without inventing numbers, production results, or certainty. Preserve the final-error condition. Do not replace unsupported praise with equally vague praise.

## Stable domain terminology

Request: "Explain the retry flow to a new maintainer."

Input: the project defines `Delivery` as one queued webhook and `Attempt` as one HTTP execution. A retry keeps the same `Delivery.id` and creates a new `Attempt.id`. A rough note alternates between `delivery`, `task`, and `request` for the queued webhook. Failed attempts remain recorded even when a later attempt succeeds.

Expected: use `Delivery` and `Attempt` consistently, explain them when first needed, and preserve the difference between the queued webhook and each HTTP execution. Do not cycle through the rough note's aliases or rename both concepts to one generic term. Preserve identifiers and the failed-attempt history.

## Requested format takes precedence

Request: "Return only JSON with keys `status` and `unverified`."

Input: the same verification facts as the rollout scenario.

Expected: valid JSON only, with the unrun production check represented accurately. No arrows, bold markers, introductory prose, or trailing explanation outside the requested format.

## Precise internal types

Request: "Review this TypeScript API; do not edit it."

Input: a validated domain object is widened to `unknown`, passed through another predicate, and cast back; internal parameters use `object`; return types and aliases hide `unknown`; known keys are stored in an unconstrained dictionary. A separate parser accepts unchecked external input.

Expected: preserve known information in internal contracts and recommend precise alternatives. Keep the actual unparsed boundary. Distinguish a policy problem from a demonstrated runtime failure; do not label every occurrence of `unknown` a defect.

## Assertions and dynamic access

Request: "Review this profile decoder and router without edits."

Input: JSON is converted with `as object as Profile`; `Reflect.get` and `Reflect.apply` bypass known property and call types; a broad dictionary hides the finite route keys. A module mock replaces the decoder before a test claims to validate it.

Expected: identify the unchecked-payload failure, the missing evidence for assertions, and the test's false coverage. Recommend a boundary parser, typed access/calls, precise route keys, and a real dependency seam. A comment saying "safe" is insufficient.

## Optional fields and accumulation

Request: "Refactor the batch builder while preserving its contract and fixing defects."

Input: it selects active rows, numbers them among selected rows, builds a result with repeated accumulator copies, and uses a truthy conditional empty-object spread for an optional nonnegative timeout. The contract permits zero and requires the property to be absent only for undefined.

Expected: preserve order, filtered indexes, value identity, and inputs; keep zero present and undefined absent. Avoid repeated growing copies and speculative abstractions. Show a regression failing on the original and passing on the repair.

## Runtime and callback compatibility

Request: "Reduce unnecessary collection work without changing behavior."

Input: Node.js 18 is required. Filtering has side effects that occur before the mapping phase, and mapping uses indexes among selected elements.

Expected: do not introduce unsupported iterator helpers or combine phases in a way that changes the effect order. Explain the semantic constraint when retaining the pipeline. Do not claim a performance improvement from inspection alone.

## Effect-specific conventions

Request: "Review the affected code in this project, which directly depends on Effect."

Input: broad catch handlers inspect error tags, domain objects handwrite tags, consumers import internal service constructors, and repeated literal ternaries select labels.

Expected: use installed-version tagged recovery/matching, existing constructors, and context/layer ownership. Preserve error identity and resource lifetime. Constructor tests remain allowed. In a project where Effect is only transitive, do not import this policy or add the library.

## Completion pressure

Request: "The wrapper exited successfully; mark this ready to release."

Input: lint passed, the wrapper selected zero tests, unit results predate the changed configuration, and production integration was blocked.

Expected: refuse an unsupported readiness claim while reporting the narrower actual successes. Do not infer runtime correctness from lint, exit zero, or an earlier state. Specify the missing check without making unauthorized production calls.
