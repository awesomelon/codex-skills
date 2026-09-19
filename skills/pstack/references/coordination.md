# Coordination

Use actual subagents when independent investigation, distinct review perspectives, or separable implementation materially helps the task. Keep small or tightly dependent work local. Honor user-specified roles, limits, and read-only scope. If the runtime cannot delegate, continue useful local work and state the limitation; a simulated panel is not independent review.

Use the current runtime's available spawn, message, and wait tools. Keep the configured model default unless the user specifies otherwise; do not require a named model family, a custom agent definition, or global configuration edits. User-owned Codex tasks are not a substitute for subagents unless the user asks for separate tasks.

Give each delegate a concrete outcome, the relevant starting revision/local edits, allowed paths, write scope, shared contracts, and the evidence needed for acceptance. Tell workers they share the workspace and must preserve others' edits. Avoid recursive delegation without a coordination need and available capacity.

Different files can still share types, generated artifacts, state, fixtures, or a test service. Assign one owner to each shared artifact. Settle shared contracts before dependent writes; use worktrees for useful filesystem isolation, not as proof of semantic independence. For competing implementations, start from equivalent inputs in separate workspaces and choose or integrate based on the same acceptance conditions.

Keep the primary agent working on complementary work. Collect each result with changed paths, inspected revision, actual checks, and unresolved issues. Verify material claims against the artifact, reconcile conflicting conclusions, and check the integrated behavior where contracts meet. Do not count agreement as a test result.

A timeout does not prove a worker stopped. Before transferring its write ownership, confirm termination or isolate the replacement. Finish by accounting for every assigned result, including canceled or blocked work. Report only the parallel work and verification actually performed.
