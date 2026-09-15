# JSON export design

## Scope and current behavior

Add opt-in JSON export to downloads and email attachments. This document is a design only; implementation is deferred.

Observed dependencies are `download.mjs → document-export.mjs` and `email.mjs → document-export.mjs`. Both callers import `toCsv(documents)`. The serializer owns content formatting; each caller owns its delivery-specific filename. There are no mutable shared state, delivery transports, MIME fields, or validation checks in the supplied project. These boundaries are inferred from the code, not prescribed by a separate architecture rule.

`toCsv` exports only `id` and `title`, quotes every value, doubles embedded quotes, and joins records with `\n`. It emits no header or trailing newline and returns an empty string for an empty collection. Its current implementation expects string fields and throws for values without `replaceAll`.

## Proposed ownership and API

Keep the three-module structure. In `document-export.mjs`, retain the existing exported `toCsv` unchanged and add an exported `serializeDocuments(documents, format = 'csv')` that selects CSV or JSON and returns a string. JSON serialization can be a private helper in that module. Accept exactly `'csv'` and `'json'`; reject other explicit values with `RangeError` before serializing. Omitted or `undefined` format means CSV; do not silently normalize unknown formats.

Extend the existing entry points with a final optional argument:

| Entry point | Default or explicit CSV filename | JSON filename |
| --- | --- | --- |
| `createDownload(documents, format = 'csv')` | `documents.csv` | `documents.json` |
| `createAttachment(documents, month, format = 'csv')` | `report-${month}.csv` | `report-${month}.json` |

Both callers delegate content generation to `serializeDocuments` and then use the validated format as the extension of their own filename. Preserve their return shape, `{filename, content}`, with string content. Keep the attachment's `month` argument in its current position and preserve its interpolation behavior. The serialization module must not import either caller or know about months, downloads, or email.

The proposed JSON contract is compact `JSON.stringify` output of an array of objects projected to `{id, title}`, preserving input record order and string values. For example, one record becomes `[{"id":"1","title":"Example"}]`; no records becomes `[]`. Project fields explicitly rather than serializing whole document objects, so JSON exposes the same fields as CSV and does not accidentally include additional properties. Add no wrapper object or trailing newline. The supported input remains documents with string `id` and `title`; broader input validation or coercion is outside this change.

## Design judgment

Adding format branches independently to both delivery modules would duplicate the concrete CSV/JSON selection and error policy. A small selector in the existing serialization owner avoids that duplication without adding a module or framework. A generic delivery/export object factory would also absorb the distinct naming policies, which change for different reasons and should remain local. No registry, delivery strategy layer, shared state, or dependency inversion is needed for these two formats.

## Compatibility and rollout

- Existing calls `createDownload(documents)` and `createAttachment(documents, month)` must produce exactly the same CSV filenames and content. Explicit `'csv'` must do the same. Keep direct imports of `toCsv` working, including its existing behavior for invalid inputs; do not add coercion, CSV sanitization, headers, a BOM, or line-ending changes.
- JSON is opt-in and its array shape and field projection become an external contract. Consumers must select `'json'` and parse the string; the delivery functions do not return parsed objects. Extra document fields stay excluded. Nothing in the supplied code establishes a need for additional JSON fields.
- Update the serializer before or together with its two callers so new imports resolve. Enable JSON selection in any downstream consumers only after the updated entry points are available. No such consumers or deployment configuration are supplied, so their rollout cannot be verified here.
- The existing result object has no MIME property. Preserve that contract. If an external HTTP or mail transport sets content types, check that it selects `application/json` for JSON while preserving its existing CSV metadata; transport changes cannot be specified from these files alone.

## Verification planned for implementation

1. Compare old and new default CSV results through both entry points, including empty input, multiple records, commas, embedded quotes, and embedded newlines. Check exact strings, filenames, return shape, and representative existing non-string failure behavior. Verify explicit `'csv'` and direct `toCsv` calls too.
2. Through both entry points, request `'json'`, parse the content, and verify ordered `{id, title}` records, Unicode and escaped characters, exclusion of extra fields, empty-array output, and the two distinct JSON filenames. Confirm inputs remain unchanged.
3. Verify omitted and `undefined` format select CSV, while unsupported values (including `null` and uppercase variants) throw consistently before a delivery result is returned. Confirm the attachment's second argument still controls its report month.

Planning validation consisted of inspecting all three supplied modules and tracing their direct imports and return contracts. No implementation or runtime tests were performed; compatibility risks above remain prospective until these checks run against the implementation.
