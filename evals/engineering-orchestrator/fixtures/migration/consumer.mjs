import { CURRENT_VERSION, COLLECTION_FIELD } from './contract.mjs';
export function deserialize(text) {
  const packet = JSON.parse(text);
  if (packet.version !== CURRENT_VERSION) throw new TypeError('Unsupported version');
  return packet[COLLECTION_FIELD].map(({ id, title }) => ({ id, title }));
}
