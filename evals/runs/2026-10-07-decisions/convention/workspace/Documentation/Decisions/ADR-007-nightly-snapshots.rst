ADR-007: Nightly snapshots
=========================

State
-----
Superseded by `ADR-008: Point-in-time recovery <ADR-008-point-in-time-recovery.rst>`_.

Background
----------
Storage cost was the binding constraint at launch. A day of data loss was acceptable then.

Choice
------
Take one nightly snapshot.

Tradeoffs
---------
Low storage cost, but recovery can lose up to 24 hours of data.
