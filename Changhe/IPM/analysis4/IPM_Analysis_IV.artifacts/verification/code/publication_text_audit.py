"""Read-only hygiene inventory of reports and small uncompressed evidence text."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json, re, time
start=time.monotonic()
paths=[p for p in Path('.').glob('*.md') if p.name!='PROMPT.md']
paths += [p for p in Path('research').rglob('*') if p.is_file() and p.suffix in ['.md','.json','.txt','.log','.out'] and p.stat().st_size<4*1024**2]
paths += [p for p in Path('artifacts').rglob('*.md')]
patterns={'absolute_local_path':re.compile(r'/(?:mnt|home|efs|tmp)/[^\s\"\'<>`]*'), 'em_dash':re.compile('\u2014')}
hits=[];count=0;total=0
for p in sorted(set(paths)):
 raw=p.read_bytes()
 try:text=raw.decode()
 except UnicodeDecodeError:continue
 count+=1;total+=len(raw)
 found=[]
 for number,line in enumerate(text.splitlines(),1):
  kinds={k:len(pattern.findall(line)) for k,pattern in patterns.items() if pattern.search(line)}
  if kinds:found.append({'line':number,'kinds':kinds})
 if found:hits.append({'path':str(p),'sha256':sha256(raw).hexdigest(),'hits':found})
now=datetime.now(timezone.utc)
out={'at':now.isoformat(timespec='seconds'),'checked_text_files':count,'checked_bytes':total,'files_with_hits':len(hits),'hits':hits,'scope':'Current top-level Markdown except task specification; small uncompressed research text; artifact Markdown. Compressed evidence, code, scratch and raw shift transcripts are outside this scan. This is a text inventory, not a mathematical proof.','actual_elapsed_s':time.monotonic()-start}
p=Path('artifacts/final_audit')/('text_hygiene_'+now.strftime('%Y%m%dT%H%M%SZ')+'.json');p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='hits'}))
for hit in hits:print(json.dumps({'path':hit['path'],'affected_lines':len(hit['hits'])}))
