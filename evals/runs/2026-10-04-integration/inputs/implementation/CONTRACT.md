# Batch contract

`buildBatch(rows, timeout)` returns `{ items, options }`.
Only active rows appear. Item keys are `<index among active rows>:<id>` and values are retained by reference. Do not mutate input arrays or rows. Preserve input order.
The optional timeout is a nonnegative number. Omit the property when the argument is undefined. Zero is a valid timeout and must remain present. No new argument validation or dependencies are required.
The runtime is Node.js 18 or later. Public exports must remain compatible.
