"""Read ordinary evidence or its byte-verified gzip storage replacement."""
from pathlib import Path
from hashlib import sha256
import gzip,json


def read_bytes(path):
    path=Path(path)
    if path.exists():return path.read_bytes()
    tables=sorted(Path('artifacts/storage').glob('json_compression_*.json'))
    rows=[row for table in tables for row in json.loads(table.read_text())['rows']]
    entry=next(row for row in rows if row['original']==str(path))
    packed=Path(entry['archive']).read_bytes()
    assert sha256(packed).hexdigest()==entry['archive_sha256']
    raw=gzip.decompress(packed)
    assert len(raw)==entry['original_bytes']
    assert sha256(raw).hexdigest()==entry['original_sha256']
    return raw
