"""Reconstruct a hash-bound line-replacement snapshot without a live source."""
from pathlib import Path
from hashlib import sha256
import json

def reconstruct(path, active=None):
    path=Path(path)
    active=set() if active is None else active
    key=str(path.resolve())
    if key in active:
        raise ValueError('cyclic delta dependency')
    active.add(key)
    try:
        d=json.loads(path.read_text())
        if 'base_delta' in d:
            r=d['base_delta'];raw=Path(r['path']).read_bytes()
            assert sha256(raw).hexdigest()==r['sha256']
            base=reconstruct(r['path'],active)
            assert sha256(base).hexdigest()==d['base_sha256']
        else:
            r=d['base'];base=Path(r['path']).read_bytes()
            assert sha256(base).hexdigest()==r['sha256']
        lines=base.decode().splitlines(keepends=True)
        prev_end=0
        for r in d['changes']:
            assert prev_end<=r['start']<=r['stop']<=len(lines)
            prev_end=r['stop']
            if 'removed' in r:
                assert lines[r['start']:r['stop']]==r['removed']
        for r in reversed(d['changes']):
            lines[r['start']:r['stop']]=r['replacement']
        result=''.join(lines).encode()
        assert sha256(result).hexdigest()==d['result_sha256']
        return result
    finally:
        active.remove(key)
