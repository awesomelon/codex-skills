# Verify notes

`CONTRACT.md` is authoritative. In a fresh disposable data directory, verify these commands in order:

1. `node app.mjs create <directory> hello` returns `{"note":{"id":"1","title":"hello"}}` and saves the note.
2. `node app.mjs list <directory>` returns `{"notes":[{"id":"1","title":"hello"}]}`.
3. `node app.mjs remove <directory>` returns `{"removed":true}` and deletes all notes.
4. `node app.mjs list <directory>` returns `{"notes":[]}`.

`node verify.mjs` automates these assertions using separate CLI processes and cleans its disposable data even if an assertion fails. A successful remove response alone does not prove deletion; the final list must be empty. Any failure exits nonzero; the success message appears only after all assertions pass.

Run from the task folder with `TMPDIR` inside it, and remove that temporary directory afterward:

```sh
(
  verify_tmp=$(mktemp -d "$PWD/.verify-tmp.XXXXXX") || exit 1
  trap 'rm -r "$verify_tmp"' EXIT
  export TMPDIR="$verify_tmp"
  node verify.mjs
)
```
