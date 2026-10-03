import {spawnSync} from 'node:child_process';
import {mkdtemp,rm} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {fileURLToPath} from 'node:url';
import assert from 'node:assert/strict';
const app=fileURLToPath(new URL('./app.mjs',import.meta.url));
const dir=await mkdtemp(join(tmpdir(),'notes-'));
function run(command,...args) {
 const result=spawnSync(process.execPath,[app,command,dir,...args],{encoding:'utf8'});
 if(result.error) throw result.error;
 assert.equal(result.status,0,`${command} failed: ${result.stderr}`);
 return JSON.parse(result.stdout);
}
try {
 const created=run('create','hello');
 assert.deepEqual(created,{note:{id:'1',title:'hello'}},'create must return the saved note');
 assert.deepEqual(run('list'),{notes:[{id:'1',title:'hello'}]},'list must contain the saved note');
 assert.deepEqual(run('remove'),{removed:true},'remove must acknowledge deletion');
 assert.deepEqual(run('list'),{notes:[]},'list after remove must be empty');
 console.log('create/list/remove verified');
} finally {await rm(dir,{recursive:true,force:true});}
