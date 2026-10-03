export function encodePreference(input) {
  return { key: input.key, enabled: input.enabled ?? true };
}
export function decodePreference(payload) {
  return { key: payload.key, enabled: payload.enabled };
}
