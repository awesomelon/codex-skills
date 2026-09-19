# Search controller

`createSearch(load, publish)` provides the controller for a search field. Every call represents the user's latest intent, including an empty query. Only that latest intent may publish completion or error state. Loading states are immediate. Clearing publishes idle without calling the loader.

Keep the exported function, its arguments, and state shapes compatible. The loader returns a promise and does not support cancellation. Errors of the active request publish an error state; the returned search promise completes after handling the load. The controller may be tested without a browser using `node --test search.test.mjs`.
