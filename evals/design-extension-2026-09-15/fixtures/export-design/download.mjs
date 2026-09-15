import {toCsv} from './document-export.mjs';

export function createDownload(documents) {
  return {filename: 'documents.csv', content: toCsv(documents)};
}
