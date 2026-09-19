# Runtime verification

Use the project's existing driver, tests, and documented launch path for the affected surface. Establish which checkout/build, instance, account, and data the check will exercise; a responsive port or old screenshot can belong to a different build. Reuse a suitable running instance only when its identity and permitted scope are clear. Separate concurrent runs by port, profile, or data directory when they would interfere.

Drive the relevant public path with representative inputs. Capture the action and resulting state, including persistence or external effects that the contract promises. A success message, injected internal state, or mocked helper call alone does not establish that the user's operation worked. Choose an independent expected result; do not derive it through the same implementation being checked. Cover each affected entrypoint needed for the claim, without turning one feature check into a full application audit.

Check what a dry-run or test mode actually skips before relying on it to contain side effects. Use disposable data or existing isolated boundaries for permitted experiments. Verification does not expand authority to send messages, change live data, or instrument a shared process. When the real surface is unavailable, separate local evidence from the unverified runtime claim and continue useful in-scope work.

Keep evidence at an allowed location that survives cleanup, with enough invocation and environment context to reproduce the observation. Stop only instances owned by this run and remove its disposable state; do not delete the proof with the scratch data. Reuse an existing verification recipe. Create a new driver or verification skill only when its repeated use justifies that work and it is within scope.
