No simplification is needed. [parseName](/private/tmp/workspace-36n2vr7j/profile-api/profile.mjs:1) matches the documented boundary contract: reject nonstrings and blank names, then return a trimmed string. The type check is necessary for untrusted JSON and safely prevents calling `.trim()` on other values.

Trimming once could remove minor duplication, but that is optional cleanup, not a defect. No schema or abstraction is warranted.

Verified 4 valid and 13 invalid input cases. Every file remains unchanged.