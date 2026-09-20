# Saved review response excerpts

The following preserves wording from the fresh review agent's final response. It is an agent report, not a full tool trace.

> The behavior change is **not complete**.

> Verification used Node v24.19.0 against the supplied source. `node --test exchange.test.mjs` passed both existing tests. Additional in-memory checks failed for exact v2 wire output, literal v2 import, legacy archive defaults, and nonempty archive-preserving round trips. Checks for Unicode and row order, nonmutation, public entrypoints/string I/O, and unsupported-version `TypeError` passed.

> The remaining plan, using one local owner and the existing modules, is:
>
> 1. **Settle the shared format identifiers in `contract.mjs`.** Define v2/`entries` while retaining explicit v1/`items` identifiers for compatibility. Simply replacing the current constants would make the consumer reject legacy packets.
> 2. **Implement both public entrypoints against that contract.** Export ordered `{id, title, archived}` rows with an omitted-value default of `false`. Import v2 archive values unchanged; map every v1 row to `archived: false`; reject unsupported versions with `TypeError`.
> 3. **Extend `exchange.test.mjs` and verify the integrated behavior.** Assert exact parsed output against a literal expected v2 packet independently of `deserialize`. Cover explicit `true`, explicit `false`, omitted archive values, multiple rows in deliberately unsorted order, literal v1/v2 inputs, nonempty round trips, Unicode, nonmutation, and the existing empty/error cases.
> 4. **Reconcile the existing records after verification.** Treat all three work items as outstanding now. Once implemented and verified, update the accepted specification with v2 export and dual-version import behavior, preserving every unaffected guarantee. Record the actual verification command and result in the existing work record; no new document or process is needed.

> Neither the current v1 implementation nor the unsupported completion claim overrides that intent. No blocking product decision remains.
>
> All project files and supplied skill resources were preserved.

The omitted findings table identified the current v1 export, rejected v2 import, missing legacy archive default, and inadequate existing tests/specification. Parent hash checks are recorded separately.
