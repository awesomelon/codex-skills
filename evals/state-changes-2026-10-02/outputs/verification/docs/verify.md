# Verify notes

Run these commands from the project directory using a disposable data directory.
The expected behavior comes from [CONTRACT.md](../CONTRACT.md).

1. Run `node app.mjs create <data-directory> hello`. It must return
   `{"note":{"id":"1","title":"hello"}}` and save the note.
2. Run `node app.mjs list <data-directory>`. It must return
   `{"notes":[{"id":"1","title":"hello"}]}`.
3. Run `node app.mjs remove <data-directory>`. It must return `{"removed":true}`
   and delete all notes.
4. Run `node app.mjs list <data-directory>` again. It must return `{"notes":[]}`.

`node verify.mjs` automates these checks in a fresh temporary data directory.
It prints `create/list/remove verified` only after all assertions pass and exits
nonzero if a response or saved state violates the contract. It cleans up its
temporary data on success or failure. A successful removal response alone does
not verify deletion; the final list must be empty.
