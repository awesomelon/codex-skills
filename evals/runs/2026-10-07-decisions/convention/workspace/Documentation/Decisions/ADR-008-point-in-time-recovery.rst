ADR-008: Point-in-time recovery
==============================

State
-----
Accepted

Background
----------
`ADR-007: Nightly snapshots <ADR-007-nightly-snapshots.rst>`_ prioritized storage cost and accepted up to a day of data loss. The agreed recovery point objective is now 15 minutes; higher storage cost is preferable to losing a day of data.

Choice
------
Replace nightly snapshots with point-in-time recovery, targeting no more than 15 minutes of data loss. This supersedes ADR-007.

Tradeoffs
---------
Accept higher storage cost to reduce potential data loss from 24 hours to 15 minutes. Retaining nightly snapshots would preserve their lower storage cost but would not meet the new recovery target.

This record captures the accepted decision; it does not establish that point-in-time recovery has been implemented or verified.
