export async function checkout(order, services) {
  if (order.items.length === 0) {
    throw new RangeError('An order must contain an item');
  }
  const amount = await services.quote(order.items);
  services.audit({ type: 'quoted', orderId: order.id, amount });
  const reservation = await services.reserve(order.id, amount);
  if (order.expedited) {
    const shipment = await services.ship(reservation, 'express');
    const receipt = {
      orderId: order.id,
      amount,
      reservationId: reservation.id,
      shipmentId: shipment.id,
      delivery: 'express',
      items: order.items.map(item => ({ sku: item.sku, quantity: item.quantity })),
    };
    services.audit({ type: 'completed', receipt });
    return receipt;
  }
  const shipment = await services.ship(reservation, 'standard');
  const receipt = {
    orderId: order.id,
    amount,
    reservationId: reservation.id,
    shipmentId: shipment.id,
    delivery: 'standard',
    items: order.items.map(item => ({ sku: item.sku, quantity: item.quantity })),
  };
  services.audit({ type: 'completed', receipt });
  return receipt;
}
