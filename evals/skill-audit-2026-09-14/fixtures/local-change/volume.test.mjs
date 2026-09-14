import test from 'node:test';
import assert from 'node:assert/strict';
import {clampVolume} from './volume.mjs';

test('volume stays between zero and one hundred', () => {
  for (const [value, expected] of [[-5, 0], [0, 0], [40, 40], [100, 100], [150, 100]]) {
    assert.equal(clampVolume(value), expected);
  }
});
