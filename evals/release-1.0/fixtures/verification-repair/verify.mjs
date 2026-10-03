import {spawnSync} from 'node:child_process';
import {mkdtemp,rm} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import assert from 'node:assert/strict';
const dir=await mkdtemp(join(tmpdir(),'notes-'));
function run(command,...args) {
 const result=spawnSync(process.execPath,['app.mjs',command,dir,...args],{encoding:'utf8'});
 assert.equal(result.status,0,result.stderr);
 return JSON.parse(result.stdout);
}
try {
 const created=run('create','hello');
 assert.equal(typeof created.id,'string');
 assert.deepEqual(run('list').notes,[{id:created.id,title:'hello'}]);
 run('remove');
 assert.deepEqual(run('list').notes,[]);
 console.log('create/list/remove verified');
} finally {await rm(dir,{recursive:true,force:true});}
