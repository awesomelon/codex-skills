# Add JSON document export

Design JSON export for the existing download and email consumers. Both must support CSV and JSON, selected by the caller. Existing calls without a format must keep CSV output. Downloads and email attachments keep their different filename conventions.

Only these two formats are required. Explain the proposed changes using the supplied modules and relevant verification. This is design only: preserve every file and do not implement the feature. Use only supplied local files; no dependencies or runtime setup are needed.
