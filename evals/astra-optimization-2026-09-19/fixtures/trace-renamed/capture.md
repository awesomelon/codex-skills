One local development capture on a laptop, cold search for `invoice`, 12,000 records. No production baseline, warm repeat, CPU/network throttling, or React profiler capture is available.

Observed event log, elapsed milliseconds from input:

| Start | End | Observation |
| --- | --- | --- |
| 0 | 2 | input handler |
| 2 | 302 | debounce timer scheduled for 300 ms |
| 302 | 311 | synchronous filterRecords block |
| 312 | 814 | request `/api/search` in flight |
| 818 | 842 | next browser rendering interval |

The screenshot at 843 ms shows the final result. A sampled CPU stack has filterRecords as its largest application frame (38% of sampled application CPU); that percentage is not an elapsed-time measurement. The trace does not break the request into DNS, transport, server, or response processing.

```js
function onInput(text) {
  clearTimeout(timer);
  timer = setTimeout(async () => {
    const local = filterRecords(records, text);
    const remote = await fetchSearch(text);
    showResults(mergeResults(local, remote));
  }, 300);
}
```
