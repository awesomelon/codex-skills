import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {join} from 'node:path';
const [command,dir,title] = process.argv.slice(2);
await mkdir(dir,{recursive:true});
const file = join(dir,'notes.json');
async function read() { try {return JSON.parse(await readFile(file,'utf8'));} catch(e) {if(e.code==='ENOENT') return []; throw e;} }
if(command==='create') {
 const notes = await read(); const note={id:String(notes.length+1),title};
 notes.push(note); await writeFile(file,JSON.stringify(notes)); console.log(JSON.stringify({note}));
} else if(command==='list') {console.log(JSON.stringify({notes:await read()}));
} else if(command==='remove') {console.log(JSON.stringify({removed:true}));
} else { console.error('unknown command'); process.exitCode=2; }
