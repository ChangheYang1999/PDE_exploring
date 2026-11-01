"""Lossless storage compaction of three independently retained historical artifacts."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import gzip,json,time

def main():
    start=time.monotonic();rows=[]
    names=['research/53_stream_precision/verification/checks.json','research/56_sqrt5_residuals/verification/evaluated_coefficients.json','research/21_logarithmic_data_audit/sources/numerics_log_prefix73.pkl']
    for name in names:
        p=Path(name);raw=p.read_bytes();packed=gzip.compress(raw,compresslevel=9,mtime=0)
        assert gzip.decompress(packed)==raw
        used=sum(q.stat().st_size for q in Path('.').rglob('*') if q.is_file())
        assert used+len(packed)<3_000_000_000
        archive=p.with_name(p.name+'.gz');archive.write_bytes(packed)
        row=dict(original=str(p),archive=str(archive),original_bytes=len(raw),archive_bytes=len(packed),original_sha256=sha256(raw).hexdigest(),archive_sha256=sha256(packed).hexdigest(),byte_exact_roundtrip=True)
        rows.append(row)
        manifest=Path('artifacts/storage/json_compression_20261031T1328.json')
        manifest.write_text(json.dumps(dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),rows=rows,bytes_saved=sum(r['original_bytes']-r['archive_bytes'] for r in rows),actual_elapsed_s=time.monotonic()-start),indent=2)+'\n')
        p.unlink()
        (p.parent/'STORAGE.md').write_text('The historical artifact in this folder is stored in a byte-exact gzip archive. Its original path remains a virtual evidence path. The storage receipt in artifacts/storage/json_compression_20261031T1328.json records raw and compressed sizes and SHA256 hashes. Use code/read_evidence_bytes.py to recover the original bytes, or decompress the archive and check its raw hash. No numerical value has changed.\n')
        print(json.dumps(row),flush=True)
    from read_evidence_bytes import read_bytes
    for row in rows:assert sha256(read_bytes(row['original'])).hexdigest()==row['original_sha256']
    print(json.dumps(dict(all_roundtrips_pass=True,bytes_saved=sum(r['original_bytes']-r['archive_bytes'] for r in rows),actual_elapsed_s=time.monotonic()-start)),flush=True)
if __name__=='__main__':main()
