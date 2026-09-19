# Correctness of state, Effects, and components

Follow actual update and consumption paths for relevant issues. See [sources.md](sources.md) for attribution and upstream mapping.

## What state represents

- Prefer deriving values from current props/state during rendering. Distinguish independently edited drafts, server snapshots, and explicit initial values from redundant derived state. Background refetches must not overwrite unsaved user input.
- Do not mutate state, props, or shared caches in place. Sort a copied array or use `toSorted()` where supported. Even with a new array, consider shared element objects.
- Consider functional setters for updates that accumulate from the previous value. Keep updaters and initializers pure; do not put API calls, logging, or other state writes inside them.
- Consider lazy initialization for expensive initial calculations, but do not freeze a value into an initial snapshot when it should follow later prop changes. Account for initializer reinvocation in Strict Mode.
- Values displayed in the UI or used to enable buttons must trigger rendering when updated. Use refs for render-independent values such as timers and DOM handles.

## Effects and asynchronous lifetimes

- Use Effects for synchronization with external systems and event handlers for work caused by a specific click or submission. Consider simplifying Effects that only store derived values or cause chained state updates.
- Include reactive values actually read by an Effect in its dependencies. Moving object creation or depending on the primitive values used can be appropriate; deleting dependencies or disabling lint to reduce execution count is not.
- Release created subscriptions, timers, and connections in cleanup. Do not automatically treat development re-execution as a bug or hide it with a global `didInit` flag. App initialization and component/user/tenant lifetimes differ.
- For reads in Effects, inspect paths where older responses overwrite newer state. Prefer existing data-library keys and cancellation. For direct requests, block obsolete results through cleanup, generation identifiers, or similar mechanisms. Do not assume cancellation rolls back a server mutation.
- Ensure success, error, and loading state belong to the same request or screen target. Duplicate-submission prevention and optimistic updates must preserve contracts during failure, reordered responses, and rollback.
- Use `useEffectEvent` only when the installed React and Hooks lint versions support it and the logic is non-reactive work within an Effect. It is not a replacement for ordinary event props or stable memo callbacks. Do not put its returned function in Effect dependencies or use it to hide required reactive dependencies.

## Identity and interaction

- A nested definition rendered as an actual `<Child />` component can change type on every parent render, resetting state or focus. Distinguish ordinary render helpers and pass required values through props.
- Keys must identify the same logical item after reordering or insertion. Do not flag indices in fixed lists without context; preserve intentional resets caused by changing keys.
- Replace conditions such as `count && <Row />` with an explicit boolean or ternary when a number could leak into the DOM. Do not uniformly replace every already-boolean `&&`.
- After splitting or optimizing, verify affected contracts for controlled inputs, Korean IME composition, form submission, labels, keyboard interaction, focus, and disabled behavior. Do not expand into React Native or a full design audit.

## Adding a consumer or screen variant

When adding a screen variant or another consumer, distinguish shared product decisions from local draft, focus, and interaction state. Extract shared rules without making them depend on component state. Consult [composition.md](composition.md) when consumers need a new composition or shared-state boundary. Check that one instance can be edited or reset without changing another, and that the added variant preserves existing input and selection behavior.

## Select verification

Choose checks that match the symptom: editing while props change, rapid input and reordered responses, mount→cleanup→remount, reordering a list while preserving input, or retrying a failed request. Snapshots or setter-call counts alone do not verify real behavior.
