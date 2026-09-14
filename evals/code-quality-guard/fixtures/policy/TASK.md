# Document action module

Input is a valid array of documents. Each document has id (string), status (draft/completed/cancelled), and locked (boolean).

Product contracts:
- The list archive button, detail menu archive action, and bulk archive targets follow the same archive policy. Currently, a document can be archived only when its status is completed or cancelled and locked is false.
- The detail menu returns open first, followed by archive when allowed. Bulk target IDs preserve input order.
- Pinning is an independent product policy. Its conditions currently match archiving, but it must remain independently changeable.
- Every function leaves its input unchanged. Callers use the UI-facing names and module exports.

Validation: node --test policy.test.mjs
No external dependencies or AST/clone analyzers are included. These files are the current snapshot; there is no earlier version.
