"""Final text scan including small artifact JSON/JSONL omitted by the earlier scope."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,re,time,os
start=time.monotonic();limit=4*1024**2
extensions={'.md','.json','.jsonl','.txt','.csv','.tsv','.log','.out','.html','.svg','.tex'}
paths=[p for p in Path('.').glob('*.md') if p.name not in ['PROMPT.md','SHIFT_PROMPT.md']]
for root in ('research','artifacts'):
 for directory,dirs,files in os.walk(root):
  for name in files:
   p=Path(directory)/name
   if p.suffix in extensions and p.stat().st_size<limit:paths.append(p)
patterns={'absolute_local_path':re.compile(rb'[/](?:mnt|home|efs|tmp)[/]'),'em_dash':re.compile(b'\xe2\x80\x94')}
def normalized(line):
 return line.replace(bytes([92,47]), b'/')
assert all(patterns['absolute_local_path'].search(normalized(s)) for s in [b'/'+b'mnt/a',b'/'+b'home/a',b'/'+b'efs/a',b'/'+b'tmp/a',bytes([92,47])+b'mnt'+bytes([92,47])+b'a'])
assert not patterns['absolute_local_path'].search(normalized(b'../source/a'))
assert patterns['em_dash'].search(bytes([226,128,148]))
hits=[];errors=[];total=0;count=0;inventory=sha256();kind_counts={}
for p in sorted(set(paths)):
 raw=p.read_bytes();inventory.update(str(p).encode()+b'\0'+sha256(raw).digest());total+=len(raw);count+=1
 try:raw.decode('utf-8')
 except UnicodeDecodeError:
  errors.append(dict(path=str(p),error='not_utf8'));continue
 found=[]
 for n,line in enumerate(raw.splitlines(),1):
  kinds={kind:len(pattern.findall(normalized(line))) for kind,pattern in patterns.items() if pattern.search(normalized(line))}
  if kinds:found.append(dict(line=n,kinds=kinds))
 if found:hits.append(dict(path=str(p),sha256=sha256(raw).hexdigest(),hits=found))
 kind_counts[p.suffix]=kind_counts.get(p.suffix,0)+1
now=datetime.now(timezone.utc);out=Path('artifacts/final_audit')/('expanded_text_hygiene_'+now.strftime('%Y%m%dT%H%M%SZ')+'.json')
result=dict(at=now.isoformat(timespec='seconds'),scope='Top-level report Markdown excluding both task specifications; all small uncompressed research/artifact files with extensions md,json,jsonl,txt,csv,tsv,log,out,html,svg,tex. Limit is less than4MiB. Code, scratch, raw shifts, compressed files and binary checkpoints are outside this scan. Known original producer transcripts are reported as hits and require the documented publication projections.',checked_files=count,checked_bytes=total,extensions=kind_counts,checked_path_and_content_digest=inventory.hexdigest(),files_with_hits=len(hits),hits=hits,decoding_errors=errors,actual_elapsed_s=time.monotonic()-start)
out.write_text(json.dumps(result,indent=2)+'\n');Path('artifacts/final_audit/latest_expanded_text_audit.json').write_text(json.dumps(dict(path=str(out)),indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['hits','decoding_errors']}))
for r in hits:print(json.dumps(dict(path=r['path'],affected_lines=len(r['hits']))))
for r in errors:print(json.dumps(r))
