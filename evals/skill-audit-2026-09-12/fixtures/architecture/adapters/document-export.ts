import { documentStore } from '../features/documents/store';

export function exportTitles() {
  return documentStore.documents.map(document => document.title).join('\n');
}
