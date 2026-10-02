import {readFile, writeFile} from 'node:fs/promises';
import {join} from 'node:path';
export async function credit(dir, {accountId, amount, operationKey}) {
  const file = join(dir, 'provider.json');
  const state = JSON.parse(await readFile(file, 'utf8'));
  const existing = operationKey && state.receipts[operationKey];
  if (existing) {
    if (existing.accountId !== accountId || existing.amount !== amount) throw new Error('operation key conflict');
    return existing;
  }
  const receipt = {id: state.effects.length + 1, accountId, amount};
  state.effects.push(receipt);
  state.balances[accountId] = (state.balances[accountId] || 0) + amount;
  if (operationKey) state.receipts[operationKey] = receipt;
  await writeFile(file, JSON.stringify(state));
  return receipt;
}
