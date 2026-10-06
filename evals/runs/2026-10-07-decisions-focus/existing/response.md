Implemented `timeout_seconds` with precedence over `timeout`, preserving the 30-second default and indefinite legacy support. Updated the README and preserved the existing ADR.

Verified eight behavior cases, including defaults, precedence, zero, and explicit `None` values.
