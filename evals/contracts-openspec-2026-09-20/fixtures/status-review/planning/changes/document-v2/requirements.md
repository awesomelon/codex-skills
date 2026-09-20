# Document exchange

Export JSON with version 2 and entries containing id, title, and archived. Preserve row order and default missing archived to false. Import both legacy version 1 items and version 2 entries, defaulting archived to false for legacy data. Reject unsupported versions with TypeError. Preserve the serialize/deserialize JSON-string API.

Existing export and import are both required; do not remove legacy import.
