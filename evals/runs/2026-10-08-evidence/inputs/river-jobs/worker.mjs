import { readFileSync } from 'node:fs';
const contract = JSON.parse(readFileSync(new URL('./contract.json', import.meta.url)));

export function acknowledge(packet) {
  const token = packet[contract.acknowledgmentField];
  if (typeof token !== 'string' || token.length === 0) {
    throw new Error('Missing acknowledgment token');
  }
  return { id: packet.id, token };
}
