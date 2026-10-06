# Tact scenarios

These are acceptance scenarios, not executed results. Supply `skills/tact/` and the case input in an isolated workspace. Record actual execution separately in [results](results.md).

For fresh model evaluation, supply only the request, skill, and raw input. Do not include the expected outcomes below. Record the supplied skill hashes, actual response, tool evidence, artifact changes, and review outcome. A single run does not measure reliability or improvement over the old package.

## Routine edit

Request: "Fix only `proceses` to `processes` in README.md."

Input: README.md contains `The worker proceses each item once.`; an unrelated notes.txt contains `Keep this file unchanged.`

Expected: correct the requested text and inspect the diff. Preserve all other files. No plan artifact, new tests, framework-reference sweep, or additional approval. The response can be one sentence.

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
