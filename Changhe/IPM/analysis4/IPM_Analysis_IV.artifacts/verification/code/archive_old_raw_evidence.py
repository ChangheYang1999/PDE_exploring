"""Lossless storage of completed raw evidence; original bytes are recoverable."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import gzip,json,time

start=time.monotonic()
paths=[
 'research/69_log_degree_gap/verification/Q3_M9.pkl',
 'research/69_log_degree_gap/verification/Q3_M5.pkl',
 'research/21_logarithmic_data_audit/sources/lead_exact_log_data.json',
 'research/23_correlation_audit/sources/sqrt5_sin1_selected_midpoints.json',
]
root=Path('evidence_archives');root.mkdir(exist_ok=True)
manifest=root/'raw_gzip_manifest.json'
data=json.loads(manifest.read_text()) if manifest.exists() else dict(archives=[])
for name in paths:
 src=Path(name)
 if not src.exists():continue
 dst=src.with_suffix(src.suffix+'.gz');assert not dst.exists()
 raw=src.read_bytes();digest=sha256(raw).hexdigest()
 packed=gzip.compress(raw,compresslevel=6,mtime=0);dst.write_bytes(packed)
 restored=gzip.decompress(dst.read_bytes())
 assert len(restored)==len(raw) and sha256(restored).hexdigest()==digest
 row=dict(original_path=str(src),archive_path=str(dst),original_bytes=len(raw),
          archive_bytes=len(packed),original_sha256=digest,
          archive_sha256=sha256(packed).hexdigest(),
          verified_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'))
 data['archives'].append(row);data['actual_elapsed_s']=time.monotonic()-start
 manifest.write_text(json.dumps(data,indent=2)+'\n')
 src.unlink();print(json.dumps(row),flush=True)
(root/'RAW_GZIP_README.md').write_text('''# Lossless raw evidence archives

The files listed in raw_gzip_manifest.json are gzip representations of unchanged original bytes. Each archive was decompressed and compared by length and SHA256 before removing its raw original. Prior audit hashes therefore still identify the same source data.

Read with Python gzip.open, or restore the exact original filename using gzip -dc. Original frozen audit scripts may require that restoration. Account for the lane disk limit before restoring a large file. This storage change introduces no mathematical claim.
''')
print(json.dumps(dict(complete=True,actual_elapsed_s=time.monotonic()-start)),flush=True)
