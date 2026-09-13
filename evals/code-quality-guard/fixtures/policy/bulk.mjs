export function archiveIds(documents) {
  return documents
    .filter(document => (document.status === 'completed' || document.status === 'cancelled')
      && !document.locked)
    .map(document => document.id);
}
