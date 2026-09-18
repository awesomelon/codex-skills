export function shouldInvalidate(key, tenantId, documentId) {
  return key[0] === 'document' && key[1] === tenantId && key[2] === documentId;
}
