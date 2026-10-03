# Work coordination

## Dispatch ready work

Use the current runtime's actual spawn, message, and wait capabilities and configured model defaults. Do not require named model families, custom agent definitions, or global configuration changes. User-owned conversations are not substitute subagents unless requested. Without delegation tools, execute feasible work locally and disclose the unavailable parallel execution.

Keep concurrency within available capacity and any user budget. Launch ready tasks whose outputs can be reconciled; do not fill slots with duplicate work or start dependent implementation against an unsettled contract. Give a worker another useful task or retire it when its result is accepted. Further delegation needs a concrete coordination benefit, permitted scope, and available capacity.

A concise assignment conveys:

- The outcome and observable acceptance condition.
- The relevant source artifacts, starting revision, local changes, and any selected skill location.
- Owned paths or responsibilities, read/write scope, shared contracts, and prerequisites.
- The expected handoff: changed artifacts, checks with results, assumptions, and unresolved issues.

Pass enough raw context to execute the task, without copying unrelated history or predetermining an independent review's conclusions. Workers share a workspace unless isolated; tell them to preserve others' edits and report changes needed outside their ownership. Plan-only and read-only constraints apply to every delegate. Delegation carries no broader authority than the parent task.

When a worker lacks context, request the specific missing contract, caller, or observation and return its source location and remaining uncertainty. Expand retrieval from that gap rather than restarting a broad repository survey or requiring a fixed number of search rounds.

## Coordinate changes

Different paths can still depend on the same schema, generated output, lockfile, fixture, or running service. Route shared changes through their owner and communicate revised contracts to affected workers before integration. Worktrees isolate filesystem changes, not semantic dependencies or external side effects. Do not combine competing implementations mechanically; compare equivalent inputs and acceptance conditions before selecting one.

Track assigned work with its owner, dependency, and current state such as ready, running, blocked, or accepted. Use the existing plan or a concise note; no orchestration database or mandatory file format is needed. When a blocker appears, continue unaffected work and change the plan only where the new evidence requires it.

If work stalls, inspect its status or partial artifacts and narrow the unresolved problem before retrying. Avoid blind restarts and repeated identical delegation. A timeout does not prove a worker stopped: confirm it cannot keep writing, or isolate the replacement, before transferring ownership. State when an old worker's shutdown is unconfirmed and keep its output out of the accepted result.

## Pending tool results

When the host supports asynchronous execution, continue work independent of a running tool and wait before decisions or actions that require its result. Use the returned operation handle to collect completion; a queued request or timeout is not a completed check. Prefer the host's completion notification or bounded wait over repeated status polling. Without asynchronous support, use the ordinary synchronous path.

Associate a result with the inputs it actually exercised: the relevant revision and local edits, build or snapshot, and material runtime conditions. Work performed while a check runs can make its result stale. If input identity is uncertain, resolve it before accepting the result; a passing run started before later edits does not establish their correctness. Apply [verification evidence](verification.md) to decide which affected checks must run again, and account for pending owned operations before the final report.

## Accept and integrate

Inspect each handoff against its assigned outcome. Check material claims using the actual artifact, relevant revision, and reported commands/results. Request a focused correction or mark a blocked outcome explicitly instead of treating a completion message as success.

Reconcile overlapping findings into one supported decision. When workers disagree, inspect the contract or run the smallest observation that distinguishes their claims. Agreement and review count are not verification evidence.

After accepting handoffs, apply [verification evidence](verification.md) to the assembled behavior and reused checks. Close assignments as accepted, canceled, or explicitly blocked; account for owned processes and remaining writers before reporting completion.
