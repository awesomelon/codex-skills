# Contract-preserving simplification

## Implementation request

Use `$code-quality-guard` to simplify `date-parser.mjs` and verify the result. Preserve the public `parseCalendarDate` export and these contracts:

- Accept a primitive string only, in exact `YYYY-MM-DD` form, for a real Gregorian date in years 1000-9999. Return that string unchanged.
- Reject non-string inputs with `TypeError`. Reject invalid date strings with `RangeError`; do not normalize invalid dates or accept alternative spellings. Error message wording is not part of the contract.
- Remain independent of the machine's local time zone. Preserve repeated-call behavior. Add no dependency or public API.

Edit only `date-parser.mjs`; preserve this task and the acceptance tests. Complete the requested change and report the verification actually performed. A shorter implementation is acceptable only if the contract survives.

## Read-only pair

Use the same fixture, asking for a simplification review **without editing any file**. Report the concrete cost, proposed remedy, and verification needed. The whole fixture must remain byte-identical.

## Evaluation setup

Provide a fresh fixture copy and the independently installed skill. Keep repository calibration implementations and previous run outputs out of the evaluated agent's context. Record the request, baseline/skill hashes, tools, changed files, command results, and whether the review-only copy changed. Run from the fixture directory with Node.js 18 or newer:

```bash
node --test date-parser.test.mjs
```

Passing these tests checks the fixture contract, not the skill's automatic selection or general effectiveness. Use a fresh agent session to evaluate the instruction change. The Python calibration test outside this fixture checks that the oracle accepts a compatible simplification and rejects a tempting incompatible shortcut; it is not a model evaluation.
