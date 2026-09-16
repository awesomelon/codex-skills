import { labelRecord } from "../shared/label.mjs";
export function exportLabel(record) { return `${labelRecord(record)}.csv`; }
