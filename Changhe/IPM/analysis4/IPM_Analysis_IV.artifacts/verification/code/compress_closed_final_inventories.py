"""Losslessly archive superseded final inventories, retaining each current one."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import gzip,json,sys,time
sys.dont_write_bytecode=True
from read_evidence_bytes import read_bytes
start=time.monotonic()
now=datetime.now(timezone.utc)
base=Path('artifacts/final_audit')
paths=[]
for pattern in ['compressed_text_*.json','*/admission_reference_checks.json','*/local_reference_inventory.json']:
    group=sorted(base.glob(pattern),key=lambda p:p.stat().st_mtime_ns)
    paths.extend(group[:-1])
manifest=Path('artifacts/storage')/('json_compression_'+now.strftime('%Y%m%dT%H%M%SZ')+'.json')
rows=[]
for p in sorted(set(paths)):
    raw=p.read_bytes()
    packed=gzip.compress(raw,compresslevel=9,mtime=0)
    assert gzip.decompress(packed)==raw
    archive=p.with_name(p.name+'.gz')
    assert not archive.exists()
    archive.write_bytes(packed)
    assert gzip.decompress(archive.read_bytes())==raw
    rows.append(dict(original=str(p),archive=str(archive),original_bytes=len(raw),archive_bytes=len(packed),original_sha256=sha256(raw).hexdigest(),archive_sha256=sha256(packed).hexdigest(),byte_exact_roundtrip=True))
    manifest.write_text(json.dumps(dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),rows=rows,bytes_saved=sum(r['original_bytes']-r['archive_bytes'] for r in rows),actual_elapsed_s=time.monotonic()-start),indent=2)+'\n')
    p.unlink()
    assert read_bytes(p)==raw
with Path('artifacts/storage/README.md').open('a') as f:
    f.write('\n- '+manifest.name+': superseded final inventories; each newest inventory remains directly readable.\n')
print(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(timespec='seconds'),files=len(rows),bytes_saved=sum(r['original_bytes']-r['archive_bytes'] for r in rows),manifest=str(manifest),actual_elapsed_s=time.monotonic()-start)))
