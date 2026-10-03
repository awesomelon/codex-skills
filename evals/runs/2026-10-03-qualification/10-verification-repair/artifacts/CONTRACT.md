# Notes CLI

Run node app.mjs <command> <data-directory> [title]. Commands are create, list, and remove. create returns {"note":{"id":"1","title":"..."}} and saves the note. list returns {"notes":[...]}. remove deletes all notes and returns {"removed":true}. A subsequent list must be empty. Commands use only the supplied data directory.
