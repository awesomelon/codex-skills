# Add a status-filtered records view

Design an optional status filter shared by the records list and its preloader. Existing calls still return all records for the tenant. Status counts should refresh after saving a record, along with lists whose membership may change. The detail view keeps its complete-response update. The filtered screen has its own presentation and may choose a different refresh interval.

The supplied code uses TanStack Query v5. Explain the affected definitions, readers, writers, and verification. Preserve every file: this is design only. Use supplied local files without package installation, network calls, or unrelated query changes.
