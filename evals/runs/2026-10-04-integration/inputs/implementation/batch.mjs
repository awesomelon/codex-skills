export function buildBatch(rows, timeout) {
  const selected = rows.filter(row => row.active).map((row, index) => ({
    key: `${index}:${row.id}`,
    value: row.value,
  }));
  const items = selected.reduce((all, item) => all.concat([item]), []);
  const options = { ...(timeout ? { timeout } : {}) };
  return { items, options };
}
