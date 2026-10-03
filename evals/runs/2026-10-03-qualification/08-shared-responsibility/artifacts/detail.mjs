export function documentActions(document) {
  const actions = ['open'];
  if ((document.status === 'completed' || document.status === 'cancelled')
      && !document.locked) {
    actions.push('archive');
  }
  return actions;
}

export function canPin(document) {
  return (document.status === 'completed' || document.status === 'cancelled')
    && !document.locked;
}
