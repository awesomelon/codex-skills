# Planning response excerpts

The following excerpts are from the independent agent's final response. Omitted sections expand the proposed implementation choices; they do not contain executed verification.

> The plan preserves both import formats, validates runtime data, and keeps editable drafts separate from cached server rows. No implementation or workers are needed for this planning task.
>
> I selected four catalog skills: architecture for contracts and ownership, TypeScript for runtime validation, React for draft lifetime, and TanStack Query for cache updates and workspace isolation.

| Recommendation | Decision | Contract basis |
|---|---|---|
| Remove the v1 import branch | Reject. Keep explicit v1 and v2 parsers. | Both formats must remain importable. |
| Cast parsed JSON to the v2 type | Reject. Treat parsed JSON and API responses as `unknown` until validated. | API responses are untrusted; casting performs no validation. |
| Replace drafts when refreshed rows arrive | Reject. Preserve independently edited titles across refreshes. | Drafts represent user input with their own lifetime. |

> **Cache behavior:** Preserve `['documents', workspaceId]` through a shared key helper. Import variables capture the originating workspace. Essential cache work belongs in configured mutation callbacks, so switching screens does not lose it or redirect it to another workspace.
>
> **Compatibility rollout:** Make readers accept v2 while retaining v1 support before switching the exporter to v2.
>
> Merge versus replacement, existing-ID collisions, duplicate IDs within a file, and established field/unknown-field rules remain unspecified. The contract owner must settle these before persistence behavior is implemented. The migration default also needs to be recorded in that contract. These decisions do not prevent planning validation, UI state separation, or cache identity.
>
> The following ownership describes useful work assignments; it does not start workers:

| Outcome and owner | Dependencies | Observable acceptance evidence |
|---|---|---|
| **Contract and format owner:** versioned schemas, normalization, compatibility fixtures, and unresolved import policies | Resolve persistence policies and migration default | Equivalent v1/v2 fixtures produce the intended canonical documents; invalid versions and fields are rejected |
| **API owner:** v2 export and workspace-scoped import persistence | Accepted format and persistence contract | Export has the exact v2 envelope; both versions import; validation failure causes no partial import |
| **Client data owner:** validated requests, shared list key, mutation lifecycle, cache refresh | API request/response contract | Import refreshes the intended list; malformed responses never enter the cache; another workspace remains unchanged |
| **React owner:** independent drafts, Import action, pending/error feedback | Canonical document model and client hook interface | Edited titles survive refresh and import; untouched titles follow refreshed rows; drafts remain isolated by workspace |
| **Integration owner:** combined behavior and rollout verification | All preceding outcomes | One end-to-end scenario verifies API persistence, Query data, and rendered behavior together |

> After contracts are agreed, server implementation and client work can proceed independently against shared fixtures. UI work can proceed against the agreed hook interface. The format owner alone owns shared schemas and fixtures; the client data owner alone owns shared query definitions.

The agent proposed five acceptance scenarios: legacy-to-v2 round trips, malformed wire/API responses, drafts surviving refresh and import, workspace switching during import, and import/refresh/race failures. It explicitly marked them as proposed checks.

> These are proposed checks, not executed verification. No application source or installed dependency types were inspected.
>
> Resources read: the request and catalog under `/tmp/orchestration-package-v9kdnymc`; the engineering-orchestrator entrypoint and its `references/expertise.md`; the architecture, TypeScript, React, and TanStack Query skill files; and their selected preflight, input-validation, React-correctness, cache-and-keys, and mutations references.
>
> Commands run: 13 read-only `cat` commands. Files changed: none. External services used: none. Workers started: none.
