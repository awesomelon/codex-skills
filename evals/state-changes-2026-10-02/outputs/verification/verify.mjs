import { spawnSync } from 'node:child_process';
import { mkdtemp, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import assert from 'node:assert/strict';

const dir = await mkdtemp(join(tmpdir(), 'notes-'));

function run(command, ...args) {
  const result = spawnSync(process.execPath, ['app.mjs', command, dir, ...args], {
    encoding: 'utf8',
  });
  assert.equal(result.status, 0, result.stderr);
  return JSON.parse(result.stdout);
}

try {
  const expectedNote = { id: '1', title: 'hello' };
  assert.deepEqual(run('create', 'hello'), { note: expectedNote }, 'create response');
  assert.deepEqual(run('list'), { notes: [expectedNote] }, 'create must save the note');
  assert.deepEqual(run('remove'), { removed: true }, 'remove response');
  assert.deepEqual(run('list'), { notes: [] }, 'remove must delete all saved notes');
  console.log('create/list/remove verified');
} finally {
  await rm(dir, { recursive: true, force: true });
}
