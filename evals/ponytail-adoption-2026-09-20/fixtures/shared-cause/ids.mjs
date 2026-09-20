export function normalizeId(value) {
  if (typeof value !== 'string') throw new TypeError('ID must be a string');
  const id = value.trim();
  if (!/^[a-z][a-z0-9-]*$/.test(id)) throw new RangeError('Invalid ID');
  return id;
}

export function normalizeIds(values) {
  return [...new Set(values)].map(normalizeId);
}
