# Reporting records — synthetic fixture

The platform exports transaction rows with account ID, event time, posting time, amount, currency, region, and consent status. Export supports date filters and stable pagination. It has no report composer.

Finance runs a monthly Python script over posting-time exports. It preserves account IDs and individual entries, reconciles reversals, and produces an auditable ledger. A failed reconciliation blocks month-end sign-off. Its owner reports two hours of exception review each month; the script itself runs in four minutes. They rejected the marketing dashboard because it groups by event date and drops transaction identities.

Marketing runs a weekly spreadsheet macro over event-time exports. It excludes accounts without consent, suppresses groups under ten people, and aggregates by region. Its owner reports forty minutes of manual column mapping weekly. They rejected the finance report because its identities and unfiltered population are not approved for campaign analysis.

Both owners independently mention that a renamed export column broke their local mapping last quarter. Export versioning is undocumented. No other reporting consumers were interviewed.

A proposal says: "Both teams merge CSVs; replace both workarounds with one company-wide report, using whichever script is easier to port." No common report policy has been approved. The team has one engineer-week available before its next planning meeting.
