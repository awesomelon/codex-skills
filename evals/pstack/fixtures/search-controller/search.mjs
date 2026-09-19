export function createSearch(load, publish) {
  return async function search(query) {
    if (!query) {
      publish({ status: 'idle', query: '', results: [] });
      return;
    }
    publish({ status: 'loading', query, results: [] });
    try {
      const results = await load(query);
      publish({ status: 'ready', query, results });
    } catch (error) {
      publish({ status: 'error', query, results: [], error });
    }
  };
}
