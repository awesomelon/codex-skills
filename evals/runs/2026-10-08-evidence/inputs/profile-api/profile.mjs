export function parseName(input) {
  if (typeof input !== 'string' || input.trim() === '') {
    throw new Error('Expected a nonempty name');
  }
  return input.trim();
}
