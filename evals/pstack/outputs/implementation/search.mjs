export function createSearch(load, publish) {
  let latestRequest = 0;
  return async function search(query) {
    const request = ++latestRequest;
    if (!query) {
      publish({ status: 'idle', query: '', results: [] });
      return;
    }
    publish({ status: 'loading', query, results: [] });
    try {
      const results = await load(query);
      if (request === latestRequest) {
        publish({ status: 'ready', query, results });
      }
    } catch (error) {
      if (request === latestRequest) {
        publish({ status: 'error', query, results: [], error });
      }
    }
  };
}
