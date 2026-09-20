Upgrade this document exchange module to format v2. The requested wire shape is
`{version: 2, entries: [{id, title, archived}]}`; an omitted archived value defaults
to false. Preserve row order, Unicode, and caller-owned data.

The importer partner has not confirmed its transition yet. Complete and verify
the exporter and shared contract first, leave consumer.mjs unchanged, and update
the existing work.md with what is done and what remains. Stop at that handoff.
Do not claim the integrated migration is complete.
