import { CURRENT_VERSION, COLLECTION_FIELD } from './contract.mjs';
export function serialize(rows) {
  return JSON.stringify({
    version: CURRENT_VERSION,
    [COLLECTION_FIELD]: rows.map(({ id, title, archived = false }) => ({ id, title, archived })),
  });
}
