import {readFile, writeFile} from 'node:fs/promises';
export async function loadProgress(file) { return JSON.parse(await readFile(file, 'utf8')); }
export async function saveProgress(file, snapshot, worker, value) {
  snapshot[worker] = value;
  await writeFile(file, JSON.stringify(snapshot));
}
export async function reserve(file) {
  const state = JSON.parse(await readFile(file, 'utf8'));
  if (state.available < 1) return false;
  state.available -= 1;
  await writeFile(file, JSON.stringify(state));
  return true;
}
