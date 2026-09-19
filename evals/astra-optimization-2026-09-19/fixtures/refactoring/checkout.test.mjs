import assert from 'node:assert/strict';
import test from 'node:test';
import { checkout } from './checkout.mjs';

function setup(expedited = false) {
  const events = [];
  const order = Object.freeze({
    id: 'order-1', expedited,
    items: Object.freeze([Object.freeze({ sku: 'A', quantity: 2, privateNote: 'internal' })]),
  });
  const services = {
    async quote(items) { events.push(['quote', items]); return 120; },
    audit(event) { events.push(['audit', event]); },
    async reserve(id, amount) { events.push(['reserve', id, amount]); return { id: 'r-1' }; },
    async ship(reservation, delivery) { events.push(['ship', reservation, delivery]); return { id: 's-1' }; },
  };
  return { order, services, events };
}

for (const expedited of [false, true]) {
  test(`receipt and effect sequence, expedited=${expedited}`, async () => {
    const { order, services, events } = setup(expedited);
    const receipt = await checkout(order, services);
    const delivery = expedited ? 'express' : 'standard';
    assert.deepEqual(receipt, {
      orderId: 'order-1', amount: 120, reservationId: 'r-1', shipmentId: 's-1', delivery,
      items: [{ sku: 'A', quantity: 2 }],
    });
    assert.deepEqual(events, [
      ['quote', order.items],
      ['audit', { type: 'quoted', orderId: 'order-1', amount: 120 }],
      ['reserve', 'order-1', 120],
      ['ship', { id: 'r-1' }, delivery],
      ['audit', { type: 'completed', receipt }],
    ]);
    assert.equal(events[4][1].receipt, receipt);
    assert.notEqual(receipt.items, order.items);
    assert.notEqual(receipt.items[0], order.items[0]);
  });
}

test('empty orders perform no effects', async () => {
  const { order, services, events } = setup();
  await assert.rejects(checkout({ ...order, items: [] }, services), {
    name: 'RangeError', message: 'An order must contain an item',
  });
  assert.deepEqual(events, []);
});

for (const [failure, expected] of [
  ['quote', ['quote']],
  ['audit', ['quote', 'audit']],
  ['reserve', ['quote', 'audit', 'reserve']],
  ['ship', ['quote', 'audit', 'reserve', 'ship']],
]) {
  test(`${failure} failure stops subsequent effects and preserves the error`, async () => {
    const { order, services, events } = setup();
    const error = new Error(failure);
    services[failure] = () => { events.push([failure]); throw error; };
    await assert.rejects(checkout(order, services), caught => caught === error);
    assert.deepEqual(events.map(event => event[0]), expected);
  });
}

test('does not ship before reservation completes', async () => {
  const { order, services, events } = setup();
  let resolveReservation;
  const pendingReservation = new Promise(resolve => { resolveReservation = resolve; });
  services.reserve = (id, amount) => { events.push(['reserve', id, amount]); return pendingReservation; };
  const pendingCheckout = checkout(order, services);
  await new Promise(resolve => setImmediate(resolve));
  assert.deepEqual(events.map(event => event[0]), ['quote', 'audit', 'reserve']);
  resolveReservation({ id: 'r-1' });
  await pendingCheckout;
  assert.deepEqual(events.map(event => event[0]), ['quote', 'audit', 'reserve', 'ship', 'audit']);
});
