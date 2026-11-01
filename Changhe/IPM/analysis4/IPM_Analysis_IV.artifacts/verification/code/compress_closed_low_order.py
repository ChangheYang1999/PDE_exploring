"""Lossless compression of closed low-order JSON evidence, excluding live inputs."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import gzip,json,re,time,sys
sys.dont_write_bytecode=True
from read_evidence_bytes import read_bytes
start=time.monotonic();stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ');rows=[]
manifest=Path('artifacts/storage')/('json_compression_'+stamp+'.json')
paths=[]
for folder in Path('research').iterdir():
    match=re.match(r'^(\d+)_',folder.name)
    if not match or not 1<=int(match[1])<=118:continue
    for p in folder.rglob('*.json'):
        if p.is_file() and p.stat().st_size>200000 and p.name!='MANIFEST.json':paths.append(p)
for p in sorted(paths):
    raw=p.read_bytes();packed=gzip.compress(raw,compresslevel=6,mtime=0);archive=p.with_name(p.name+'.gz')
    assert not archive.exists();archive.write_bytes(packed);assert gzip.decompress(archive.read_bytes())==raw
    rows.append(dict(original=str(p),original_bytes=len(raw),original_sha256=sha256(raw).hexdigest(),archive=str(archive),archive_bytes=len(packed),archive_sha256=sha256(packed).hexdigest(),byte_exact_roundtrip=True))
    manifest.write_text(json.dumps(dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),rows=rows,bytes_saved=sum(x['original_bytes']-x['archive_bytes'] for x in rows)),indent=2)+'\n')
    p.unlink();assert read_bytes(p)==raw
if rows:
    p=Path('artifacts/storage/README.md');text=p.read_text();anchor='Every original byte string'
    text=text.replace(anchor,'- '+manifest.name+'\n\n'+anchor);p.write_text(text)
print(json.dumps(dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),files=len(rows),bytes_saved=sum(x['original_bytes']-x['archive_bytes'] for x in rows),manifest=str(manifest) if rows else None,actual_elapsed_s=time.monotonic()-start)),flush=True)
