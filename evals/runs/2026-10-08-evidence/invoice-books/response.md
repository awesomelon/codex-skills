Fixed [invoice.py](/private/tmp/workspace-36n2vr7j/invoice-books/invoice.py): totals now include every row, including repeated codes and the last item. Removed my provisional deduplication; preserved your `parse_price` changes and `notes.txt`.

Verified with five regression tests: four failed before the repair; all five now pass. The supplied invoice totals `20.00`, previously `12.50`.