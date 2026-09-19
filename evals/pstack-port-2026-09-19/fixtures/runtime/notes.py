import argparse
import json
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--data-dir', type=Path, required=True)
commands = parser.add_subparsers(dest='command', required=True)
add = commands.add_parser('add')
add.add_argument('text')
commands.add_parser('list')
export = commands.add_parser('export')
export.add_argument('--output', type=Path, required=True)
export.add_argument('--dry-run', action='store_true')
args = parser.parse_args()
store = args.data_dir / 'notes.json'
notes = json.loads(store.read_text()) if store.exists() else []
if args.command == 'add':
    args.data_dir.mkdir(parents=True, exist_ok=True)
    notes.append(args.text)
    store.write_text(json.dumps(notes))
    print('Saved')
elif args.command == 'list':
    print(json.dumps(notes))
else:
    args.data_dir.mkdir(parents=True, exist_ok=True)
    with (args.data_dir / 'exports.log').open('a') as log:
        log.write(str(args.output) + '\n')
    if args.dry_run:
        print(f'Would export {len(notes)} notes')
    else:
        args.output.write_text(json.dumps(notes))
        print('Exported')
