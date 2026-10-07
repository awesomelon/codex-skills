export async function baseline(rows) {
  await new Promise(resolve => setTimeout(resolve, 12));
  return rows.map(row => ({ id: row.id, total: row.amount * 2 }));
}

export async function proposed(rows) {
  await new Promise(resolve => setTimeout(resolve, 12));
  return rows.map(row => ({ id: row.id, total: row.amount + row.amount }));
}
