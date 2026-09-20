The partner has now confirmed a revised v2 contract: the wire entry field must
be `isArchived`, not `archived`. In-memory rows still use `archived`. The new v2
format has not shipped, so the earlier v2 spelling need not be supported.

Finish the migration: update export and import together, retain legacy v1
imports with archived defaulting to false, reject unsupported versions, and
preserve the earlier row-order, Unicode, and nonmutation guarantees. Reconcile
the existing requirements and work record with the actual implementation and
verification. Keep unrelated notes unchanged. Finish with the integrated result.
