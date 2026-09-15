import {toCsv} from './document-export.mjs';

export function createAttachment(documents, month) {
  return {filename: `report-${month}.csv`, content: toCsv(documents)};
}
