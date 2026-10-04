export function buildBatch(rows, timeout) {
  const items = [];

  rows.forEach(row => {
    if (row.active) {
      items.push({
        key: `${items.length}:${row.id}`,
        value: row.value,
      });
    }
  });

  const options = {};

  if (timeout !== undefined) {
    options.timeout = timeout;
  }

  return { items, options };
}
