# Notes CLI

Use Python 3; no dependencies or network. All application data must be under a disposable directory supplied through `--data-dir`.

```sh
python3 notes.py --data-dir /path/to/scratch/data add 'Release note'
python3 notes.py --data-dir /path/to/scratch/data list
python3 notes.py --data-dir /path/to/scratch/data export --output /path/to/scratch/export.json --dry-run
```

Adding a note must persist it for a later process to list. Export writes all notes to the requested output file. With `--dry-run`, export describes the planned operation and must leave both the data directory and output file unchanged.
