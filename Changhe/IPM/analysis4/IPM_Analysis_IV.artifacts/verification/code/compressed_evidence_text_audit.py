"""Stream compressed evidence text and large text omitted by the small-file audit."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import gzip,json,re,time,os
begin=time.monotonic();paths=[]
for root in ('research','artifacts'):
 for directory,dirs,files in os.walk(root):
  for name in files:
   p=Path(directory)/name
   if p.name.endswith(('.json.gz','.jsonl.gz','.log.gz','.out.gz')) or (p.suffix in ('.json','.jsonl','.txt','.out','.log','.md') and p.stat().st_size>=4*1024**2):paths.append(p)
patterns={'absolute_local_path':re.compile(rb'(?:\\?/)(?:mnt|home|efs|tmp)(?:\\?/)'),'em_dash':re.compile(b'\xe2\x80\x94')}
rows=[];hits=[];errors=[]
for p in sorted(paths):
 if time.monotonic()-begin>520:break
 start=time.monotonic();raw_hash=sha256();size=0;found={k:[] for k in patterns};counts={k:0 for k in patterns};carry=b''
 try:
  with (gzip.open(p,'rb') if p.suffix=='.gz' else p.open('rb')) as f:
   while block:=f.read(1024**2):
    raw_hash.update(block);data=carry+block;offset=size-len(carry)
    for kind,pattern in patterns.items():
     for match in pattern.finditer(data):
      absolute=offset+match.start()
      if absolute+len(match[0])<=size:continue
      counts[kind]+=1
      if len(found[kind])<12:found[kind].append(absolute)
    size+=len(block);carry=data[-32:]
  row=dict(path=str(p),decompressed_bytes=size,decompressed_sha256=raw_hash.hexdigest(),hit_counts=counts,first_byte_offsets=found,actual_elapsed_s=time.monotonic()-start);rows.append(row)
  if any(counts.values()):hits.append(row)
 except Exception as e:errors.append(dict(path=str(p),error_type=type(e).__name__))
now=datetime.now(timezone.utc);out=Path('artifacts/final_audit')/('compressed_text_'+now.strftime('%Y%m%dT%H%M%SZ')+'.json')
result=dict(at=now.isoformat(timespec='seconds'),scope='Compressed JSON/JSONL/log/output evidence under research and artifacts, plus plain evidence text at least4MiB. Binary pickle archives and source code are outside this text scan. No deserialization or execution is performed.',scheduled_files=len(paths),checked_files=len(rows),checked_decompressed_bytes=sum(r['decompressed_bytes'] for r in rows),files_with_hits=len(hits),errors=errors,complete=len(rows)+len(errors)==len(paths),rows=rows,actual_elapsed_s=time.monotonic()-begin)
out.write_text(json.dumps(result,indent=2)+'\n');Path('artifacts/final_audit/latest_compressed_text_audit.json').write_text(json.dumps(dict(path=str(out)),indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
for r in hits:print(json.dumps(r))
