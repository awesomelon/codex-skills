import test from 'node:test';
import assert from 'node:assert/strict';
import { encodePreference, decodePreference } from './preferences.mjs';

test('disabled preference survives a save and reload', () => {
  assert.deepEqual(decodePreference(encodePreference({ key: 'email', enabled: false })),
    { key: 'email', enabled: false });
});
test('enabled preference survives a save and reload', () => {
  assert.deepEqual(decodePreference(encodePreference({ key: 'email', enabled: true })),
    { key: 'email', enabled: true });
});
test('omitted preference keeps the established enabled default', () => {
  assert.deepEqual(encodePreference({ key: 'email' }), { key: 'email', enabled: true });
});
