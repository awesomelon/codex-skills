# Verification evidence

Use the project's existing driver, tests, and documented launch path for the affected surface. Establish which checkout/build, instance, account, and data the check will exercise; a responsive port or old screenshot can belong to a different build. Reuse a suitable running instance only when its identity and permitted scope are clear. Separate concurrent runs by port, profile, or data directory when they would interfere.

Drive the relevant public path with representative inputs. Capture the action and resulting state, including persistence or external effects that the contract promises. A success message, injected internal state, or mocked helper call alone does not establish that the user's operation worked. Choose an independent expected result; do not derive it through the same implementation being checked. Cover each affected entrypoint needed for the claim, without turning one feature check into a full application audit.

## Establish what actually passed

For each completion claim, retain enough evidence to identify the command or action, target revision and relevant local state, assertion or observation, and actual result. Capture exit codes where the tool exposes them and inspect the output. Use the project's ordinary report format rather than introducing a compulsory ledger.

A process exiting zero is not sufficient when the promised assertion never ran. Zero selected tests, all relevant cases skipped, an empty search result, a wrapper masking a failing child, or a service that never reached the asserted request leaves that behavior unverified. A build can still be valid build evidence; do not inflate it into runtime or integration evidence. Verify which assertions executed and whether they cover the claim.

Distinguish a successful evaluated check, a failed assertion, a check not run, and an inconclusive attempt. An unavailable dependency or permission can block verification without proving the product defective. Diagnose the blocker within scope, use another valid observation when available, and otherwise report the gap; do not retry indefinitely or turn absence of evidence into a pass.

Keep the quality bar anchored to the agreed contract. Do not skip tests, suppress diagnostics, loosen assertions, or disable gates merely to obtain green output. A genuinely obsolete test or unsuitable gate may change only with a reason grounded in the current contract; retain or replace the protection that is still required. An unrelated pre-existing failure is reported separately, not hidden and not automatically added to the task scope.

## Reuse evidence without reusing stale claims

Repeat the relevant checks after integration or a fix changes their inputs. Evidence is reusable only while the exercised code, local edits, build, dependencies, configuration, and material runtime/data conditions remain applicable. The same commit SHA alone is insufficient if those conditions changed. Conversely, do not rerun an unchanged check merely because another phase or reviewer requests its result.

Finish against the verification scope required by the changed contract and the project's mandatory gates. Focused intermediate checks do not substitute for required integration evidence. A claim that a service starts and responds needs an actual start/request observation; an operational availability target needs evidence over its agreed population and observation window. A producer-consumer change needs evidence at that boundary, not only separately passing mocks. Do not impose a universal test suite, fixed coverage threshold, or test-first ceremony on every change.

## Work safely and retain useful proof

Check what a dry-run or test mode actually skips before relying on it to contain side effects. Use disposable data or existing isolated boundaries for permitted experiments. Verification does not expand authority to send messages, change live data, or instrument a shared process. When the real surface is unavailable, separate local evidence from the unverified runtime claim and continue useful in-scope work.

Keep evidence at an allowed location that survives cleanup, with enough invocation and environment context to reproduce the observation. Stop only instances owned by this run and remove its disposable state; do not delete the proof with the scratch data. Reuse an existing verification recipe. Create a new driver or verification skill only when its repeated use justifies that work and it is within scope.
