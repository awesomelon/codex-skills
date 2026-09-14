> English translation of a historical record. [Original at the pre-translation commit](https://github.com/awesomelon/codex-skills/blob/ce11c34e3d1da77140087300218b776594bb65cf/evals/skill-audit-2026-09-14/outputs/react.md). Reported runs, hashes, and counts describe the original work, not this translation.

Updated DocumentPicker.tsx.

- Sorted the filtered array to avoid mutating original `documents`.
- Removed derived state and the Effect so search/prop changes are reflected directly during rendering.
- Preserved public props, display text, and input/selection handlers.

Executed the actual source calculation in Node to verify ascending titles, case-insensitive and Korean search, empty results, prop replacement, and source immutability.

React interactions, type checking, and build were unavailable without runtime dependencies and a test environment. Changed only this file without network or installation.
