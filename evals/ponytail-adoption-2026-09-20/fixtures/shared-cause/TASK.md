# Fix duplicate record IDs

Exporting IDs sometimes returns duplicates when an ID has surrounding whitespace. Fix this bug in this small import/export package and add appropriate regression coverage. Preserve the existing public exports, wire shape, first-occurrence order, input immutability, validation rules and error types. No new package is needed for deployment; keep the package dependency-free. Complete the implementation and report actual verification.
