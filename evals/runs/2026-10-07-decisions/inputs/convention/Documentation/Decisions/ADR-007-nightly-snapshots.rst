ADR-007: Nightly snapshots
=========================

State
-----
Accepted

Background
----------
Storage cost was the binding constraint at launch. A day of data loss was acceptable then.

Choice
------
Take one nightly snapshot.

Tradeoffs
---------
Low storage cost, but recovery can lose up to 24 hours of data.
