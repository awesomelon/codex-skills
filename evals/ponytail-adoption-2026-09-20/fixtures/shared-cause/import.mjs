import { normalizeIds } from './ids.mjs';
export function importRecords(json) {
  return normalizeIds(JSON.parse(json).ids);
}
