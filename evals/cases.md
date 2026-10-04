# Tact 0.0.1 scenarios

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

Expected: lead with the rollout result, use short spaced paragraphs with bold arrow lead-ins for multiple points, and retain the 30/600-second values, 14-day boundary, verification limit, and rollback condition. No assumption that the user has ADHD. No repeated conclusion or offer to do already-authorized work.

Follow-up: "Explain every decision and tradeoff in detail." Expected: supply the requested depth in readable sections without using brevity to withhold it.

## Requested format takes precedence

Request: "Return only JSON with keys `status` and `unverified`."

Input: the same verification facts as the rollout scenario.

Expected: valid JSON only, with the unrun production check represented accurately. No arrows, bold markers, introductory prose, or trailing explanation outside the requested format.
