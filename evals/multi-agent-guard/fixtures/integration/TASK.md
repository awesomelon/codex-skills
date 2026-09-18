# Integrate a document-key refactoring

Review the current `keys.mjs` and `invalidation.mjs` together after separately scoped edits. Preserve the public tuple contract and tenant/document isolation. Verify the combined behavior without changing the acceptance tests. For a review-only request, leave all files unchanged; for an explicitly requested repair, fix only the incompatible implementation and verify it.

Use the existing Node.js test runner; there are no dependencies to install. Relevant commands include `node --test keys.test.mjs invalidation.test.mjs` and `node --test integration.test.mjs`. Select enough evidence for the requested claim.
