import { currentTenant } from "../features/session.mjs";

export function labelRecord(record) {
  return `${currentTenant()}:${record.id}`;
}
