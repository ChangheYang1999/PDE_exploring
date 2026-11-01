"""Losslessly compress completed JSON checks from closed topics before final packaging."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import gzip,json,sys,time
sys.dont_write_bytecode=True
from read_evidence_bytes import read_bytes

start=time.monotonic()
now=datetime.now(timezone.utc)
manifest=Path('artifacts/storage')/('json_compression_'+now.strftime('%Y%m%dT%H%M%SZ')+'.json')
rows=[]
protected={r["path"] for r in json.loads(Path("artifacts/current_certified_radii.json").read_text())["rows"]}
for topic in sorted(Path('research').glob('*')):
    try:n=int(topic.name.split('_')[0])
    except ValueError:continue
    if not 1<=n<=245:continue
    for p in sorted(topic.rglob('*.json')):
        if not 10000<=p.stat().st_size<40000 or str(p) in protected or 'admission' in p.name:continue
        raw=p.read_bytes();packed=gzip.compress(raw,compresslevel=9,mtime=0)
        assert gzip.decompress(packed)==raw
        archive=p.with_name(p.name+'.gz');assert not archive.exists()
        archive.write_bytes(packed)
        assert gzip.decompress(archive.read_bytes())==raw
        row=dict(original=str(p),archive=str(archive),original_bytes=len(raw),archive_bytes=len(packed),original_sha256=sha256(raw).hexdigest(),archive_sha256=sha256(packed).hexdigest(),byte_exact_roundtrip=True)
        rows.append(row)
        manifest.write_text(json.dumps(dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),rows=rows,bytes_saved=sum(r['original_bytes']-r['archive_bytes'] for r in rows),actual_elapsed_s=time.monotonic()-start),indent=2)+'\n')
        p.unlink();assert sha256(read_bytes(p)).hexdigest()==row['original_sha256']
        with (p.parent/'STORAGE.md').open('a') as f:
            f.write('\n'+p.name+' is retained losslessly as '+archive.name+'. Raw and compressed hashes are in '+str(manifest)+'. Read its original bytes with code/read_evidence_bytes.py. No numerical value changed.\n')
with Path('artifacts/storage/README.md').open('a') as f:f.write('\n- '+manifest.name+'\n')
print(json.dumps(dict(files=len(rows),bytes_saved=sum(r['original_bytes']-r['archive_bytes'] for r in rows),manifest=str(manifest),actual_elapsed_s=time.monotonic()-start)))
