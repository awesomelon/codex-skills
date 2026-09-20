# Document exchange

Export v2 as {version: 2, entries: [{id, title, isArchived}]}. In-memory rows
use {id, title, archived}; omitted or undefined archived exports as
isArchived: false. Keep entry fields ordered as id, title, isArchived.

Import legacy v1 {version: 1, items: [{id, title}]} into rows with archived:
false. Import v2 entries by mapping isArchived to archived, defaulting an
omitted isArchived to false. The earlier, unshipped v2 wire spelling archived
does not need compatibility support.

Preserve row order, Unicode, and caller-owned data. Unsupported versions raise
TypeError. The partner has confirmed this revised v2 contract; complete and
verify export and import together.
