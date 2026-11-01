"""Byte-preserving compression of closed selected JSON evidence."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import gzip,json,os,time
start=time.monotonic();rows=[];stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
paths=sorted(Path('research/96_profile_family_audit/verification').glob('*/*_selected.json'))
paths+=sorted(Path('research/03_resonances/verification/independent_first_resonances').glob('*.json'))
paths+=sorted(Path('research/64_log_precision_updates/verification').glob('*/growth_diagnostics.json'))
paths=[p for p in paths if p.stat().st_size>300000]
archives={}
for p in paths:
    raw=p.read_bytes();digest=sha256(raw).hexdigest();archive=p.with_suffix(p.suffix+'.gz')
    assert not archive.exists()
    if digest in archives:os.link(archives[digest],archive)
    else:
        packed=gzip.compress(raw,compresslevel=9,mtime=0);archive.write_bytes(packed);archives[digest]=archive
    packed=archive.read_bytes();assert gzip.decompress(packed)==raw
    rows.append(dict(original=str(p),original_bytes=len(raw),original_sha256=digest,archive=str(archive),archive_bytes=len(packed),archive_sha256=sha256(packed).hexdigest()))
    manifest=Path('artifacts/storage')/('json_compression_'+stamp+'.json')
    manifest.write_text(json.dumps(dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),rows=rows),indent=2)+'\n')
    p.unlink()
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),files=len(rows),logical_bytes_saved=sum(r['original_bytes']-r['archive_bytes'] for r in rows),actual_elapsed_s=time.monotonic()-start)
print(json.dumps(result),flush=True)
