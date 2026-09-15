# Add an expired document status

Implement the new `expired` status in the existing document action module. Expired documents can be archived when unlocked, from the list button, detail menu, and bulk action. Expired documents cannot be pinned. All previous statuses and public functions retain their behavior, ordering, and input immutability.

Use only local files and existing tools. Complete the requested code change and verification. Keep TASK.md and both supplied test files unchanged; dependencies and configuration need no changes. Run `node --test policy.test.mjs extension.test.mjs`. Report the changed files and the checks actually performed.
