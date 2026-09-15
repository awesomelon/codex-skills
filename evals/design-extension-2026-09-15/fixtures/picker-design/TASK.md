# Add a second document picker

Design a second use of the supplied DocumentPicker. The existing picker continues to allow every document. The new review picker receives eligible IDs from its parent; it shows all matching documents but disables selection for ineligible IDs. Search and display ordering stay the same. Two instances can be open together, with independent search input.

Use React 18.3.1. Explain an additive API and where the eligibility and search decisions belong, including checks for old and new consumers. Preserve every file: this is design only, with no package installation or runtime execution. Use only the supplied component and skill directory, including its linked references.
