import {
  CURRENT_VERSION,
  COLLECTION_FIELD,
  LEGACY_VERSION,
  LEGACY_COLLECTION_FIELD,
} from './contract.mjs';
export function deserialize(text) {
  const packet = JSON.parse(text);
  if (packet.version === LEGACY_VERSION) {
    return packet[LEGACY_COLLECTION_FIELD].map(({ id, title }) => ({ id, title, archived: false }));
  }
  if (packet.version === CURRENT_VERSION) {
    return packet[COLLECTION_FIELD].map(({ id, title, archived = false }) => ({ id, title, archived }));
  }
  throw new TypeError('Unsupported version');
}
