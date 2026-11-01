"""Losslessly archive frozen historical JSONL evidence, keeping raw hashes."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import gzip,json,re,time,sys
sys.dont_write_bytecode=True
from read_evidence_bytes import read_bytes
start=time.monotonic();now=datetime.now(timezone.utc);rows=[]
manifest=Path('artifacts/storage')/('json_compression_'+now.strftime('%Y%m%dT%H%M%SZ')+'.json')
paths=[]
for topic in Path('research').iterdir():
 match=re.match(r'^(\d+)_',topic.name)
 if not match or not 1<=int(match[1])<=245:continue
 paths.extend(p for p in topic.rglob('*.jsonl') if p.stat().st_size>200000)
for p in sorted(paths):
 raw=p.read_bytes();packed=gzip.compress(raw,compresslevel=9,mtime=0);archive=p.with_name(p.name+'.gz')
 assert not archive.exists();archive.write_bytes(packed);assert gzip.decompress(archive.read_bytes())==raw
 rows.append(dict(original=str(p),archive=str(archive),original_bytes=len(raw),archive_bytes=len(packed),original_sha256=sha256(raw).hexdigest(),archive_sha256=sha256(packed).hexdigest(),byte_exact_roundtrip=True))
 manifest.write_text(json.dumps(dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),rows=rows,bytes_saved=sum(r['original_bytes']-r['archive_bytes'] for r in rows),actual_elapsed_s=time.monotonic()-start),indent=2)+'\n')
 p.unlink();assert read_bytes(p)==raw
 with (p.parent/'STORAGE.md').open('a') as f:f.write('\n'+p.name+' is stored byte-exactly as '+archive.name+'. Both hashes and the round-trip check are in '+str(manifest)+'. Use code/read_evidence_bytes.py for the original path.\n')
if rows:
 with Path('artifacts/storage/README.md').open('a') as f:f.write('\n- '+manifest.name+' (frozen historical JSONL sources)\n')
print(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(timespec='seconds'),files=len(rows),bytes_saved=sum(r['original_bytes']-r['archive_bytes'] for r in rows),manifest=str(manifest),actual_elapsed_s=time.monotonic()-start)))
