# Document exchange

Export v2 as `{version: 2, entries: [{id, title, isArchived}]}`. In-memory rows use `{id, title, archived}`; export maps `archived` to `isArchived`, defaulting an omitted or undefined value to `false`.

Import v2 `entries`, mapping `isArchived` back to `archived` and defaulting an omitted flag to `false`. Retain legacy v1 imports shaped as `{version: 1, items: [{id, title}]}`, producing rows with `archived: false`. Unsupported versions raise `TypeError`.

Preserve row order, Unicode and caller-owned data without mutation. Export only the declared wire fields, retaining the field order `id`, `title`, `isArchived`.

The importer partner has confirmed this revised v2 contract. The earlier v2 wire spelling `archived` never shipped and does not require compatibility support.
