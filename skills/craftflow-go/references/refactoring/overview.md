# Behavior-preserving refactoring

Reuse the established structural difficulty and chosen transformation. Preserve observable values, errors, public signatures, stored data, and relevant effect order/count. A discovered bug is separate work unless its correction is also authorized; continue independent in-scope work.

Use [transformations](transformations.md) for substantive changes, baseline checks, external consumers, effect sequencing, and regression recovery. A mechanically clear local rename needs no full workflow. Extract, inline, and move are alternatives, not a required sequence. For unfamiliar mechanics, consult the relevant catalog entry in [sources](sources.md).

Judge success by resolving the structural difficulty with preserved behavior, not fewer lines or files. Reuse valid baseline evidence; check changed conditions and required gates. In review or planning scope, recommend transformations and verification without changing the implementation.
