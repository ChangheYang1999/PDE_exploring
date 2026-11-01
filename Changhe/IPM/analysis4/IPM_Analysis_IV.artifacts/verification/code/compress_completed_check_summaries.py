"""Lossless gzip storage of completed large historical check summaries."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import gzip,json,time,sys
sys.dont_write_bytecode=True
from read_evidence_bytes import read_bytes
start=time.monotonic();now=datetime.now(timezone.utc);stamp=now.strftime('%Y%m%dT%H%M%SZ')
manifest=Path('artifacts/storage')/('json_compression_'+stamp+'.json');rows=[]
paths=[]
for topic in ['64_log_precision_updates','102_edge_recurrence_reference']:
    paths.extend(p for p in (Path('research')/topic/'verification').glob('*/checks.json') if p.stat().st_size>1_000_000)
for p in sorted(paths):
    raw=p.read_bytes();compressed=gzip.compress(raw,compresslevel=9,mtime=0)
    assert gzip.decompress(compressed)==raw
    archive=p.with_name(p.name+'.gz');assert not archive.exists();archive.write_bytes(compressed)
    row=dict(original=str(p),archive=str(archive),original_bytes=len(raw),archive_bytes=len(compressed),original_sha256=sha256(raw).hexdigest(),archive_sha256=sha256(compressed).hexdigest(),byte_exact_roundtrip=True)
    rows.append(row)
    manifest.write_text(json.dumps(dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),rows=rows,bytes_saved=sum(r['original_bytes']-r['archive_bytes'] for r in rows),actual_elapsed_s=time.monotonic()-start),indent=2)+'\n')
    p.unlink();assert sha256(read_bytes(p)).hexdigest()==row['original_sha256']
    (p.parent/'STORAGE.md').write_text('The completed historical checks.json is stored as checks.json.gz. Its original bytes and original manifest hash are preserved. The storage receipt '+str(manifest)+' gives both hashes and sizes. Use code/read_evidence_bytes.py or decompress the gzip archive and verify its raw hash. No numerical value changed.\n')
print(json.dumps(dict(files=len(rows),bytes_saved=sum(r['original_bytes']-r['archive_bytes'] for r in rows),manifest=str(manifest),actual_elapsed_s=time.monotonic()-start)))
