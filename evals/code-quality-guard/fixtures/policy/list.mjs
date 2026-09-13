export function showArchiveButton(document) {
  return (document.status === 'completed' || document.status === 'cancelled')
    && !document.locked;
}
