export function toCsv(documents) {
  return documents
    .map(document => [document.id, document.title]
      .map(value => `"${value.replaceAll('"', '""')}"`).join(','))
    .join('\n');
}
