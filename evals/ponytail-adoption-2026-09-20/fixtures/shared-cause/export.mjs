import { normalizeIds } from './ids.mjs';
export function exportRecords(ids) {
  return JSON.stringify({ version: 1, ids: normalizeIds(ids) });
}
