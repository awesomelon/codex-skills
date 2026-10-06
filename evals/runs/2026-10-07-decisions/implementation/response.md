Implemented `timeout_seconds` with precedence over legacy `timeout`, preserving the 30-second default and indefinite alias support.

Updated the README and recorded the rationale and rejected coordinated rollout in the [compatibility decision](/var/folders/wv/426zj9m13q34bhblrxtylth80000gn/T/tact-decisions-p5yv7ib4/implementation/workspace/docs/decisions/0001-timeout-key-compatibility.md).

All six behavior checks passed, covering both keys, precedence, the default, and zero values. Documentation links resolve; `notes.txt` is unchanged.
