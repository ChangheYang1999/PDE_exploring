"""Losslessly archive older selected coefficient JSON with byte-level verification."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import gzip,json,time
start=time.monotonic()
root=Path('research/64_log_precision_updates/verification')
paths=sorted(root.glob('*/selected_packed_coefficients.json'))
manifest_path=root/'ARCHIVE_MANIFEST.json'
manifest=json.loads(manifest_path.read_text()) if manifest_path.exists() else dict(format='lossless gzip archives of unchanged original bytes',archives=[])
for path in paths:
 out=path.with_suffix(path.suffix+'.gz')
 assert not out.exists(),str(out)
 raw=path.read_bytes();digest=sha256(raw).hexdigest();packed=gzip.compress(raw,compresslevel=1,mtime=0)
 out.write_bytes(packed)
 restored=gzip.decompress(out.read_bytes())
 assert len(restored)==len(raw) and sha256(restored).hexdigest()==digest
 record=dict(original_path=str(path),archive_path=str(out),uncompressed_bytes=len(raw),compressed_bytes=len(packed),uncompressed_sha256=digest,archive_sha256=sha256(packed).hexdigest(),verified_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'))
 manifest['archives'].append(record)
 manifest['actual_elapsed_s']=time.monotonic()-start
 manifest_path.write_text(json.dumps(manifest,indent=2)+'\n')
 path.unlink()
 print(json.dumps(record),flush=True)
(root/'ARCHIVE_README.md').write_text('''# Lossless coefficient evidence archives

Older selected coefficient JSON files are stored as gzip archives. ARCHIVE_MANIFEST.json records each original relative path, both SHA256 hashes and byte counts. Every archive was decompressed and checked against the original bytes before the original file was removed. This changes storage only; the enclosed coefficient intervals and all prior raw-content hashes are unchanged.

Read an archive with Python gzip.open, or restore one exact original with the shell command `gzip -dc selected_packed_coefficients.json.gz > selected_packed_coefficients.json` in its containing directory. Restore only when needed and account for the lane disk limit. Source scripts frozen with older results retain their original expected filenames; restore the matching input before rerunning one of those scripts.
''')
print(json.dumps(dict(complete=True,archives=len(manifest['archives']),actual_elapsed_s=time.monotonic()-start)),flush=True)
