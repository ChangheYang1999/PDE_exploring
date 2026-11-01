"""Recheck the four publication projections without changing source evidence."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json, re, time

start = time.monotonic()
now = datetime.now(timezone.utc)
manifest = Path('artifacts/publication/source_projection_manifest.json')
rows = []
for item in json.loads(manifest.read_text())['rows']:
    original = Path(item['original_local_path']).read_bytes()
    published = Path(item['publication_copy']).read_bytes()
    assert sha256(original).hexdigest() == item['original_sha256']
    assert sha256(published).hexdigest() == item['publication_sha256']
    before = original.decode().splitlines(keepends=True)
    after = published.decode().splitlines(keepends=True)
    assert len(before) == len(after)
    changed = [i for i, (a, b) in enumerate(zip(before, after), 1) if a != b]
    assert changed == item['redacted_line_numbers']
    for i in changed:
        a, b = before[i - 1], after[i - 1]
        if 'RuntimeWarning:' in a:
            assert a[a.index('RuntimeWarning:'):] == b[b.index('RuntimeWarning:'):]
            assert b.startswith('[local runtime path] RuntimeWarning:')
        else:
            assert a.startswith('  File \"') and b.startswith('  File \"[local runtime path]\", line ')
            assert a.split('\", line ', 1)[1] == b.split('\", line ', 1)[1]
    assert not re.search(r'/(?:mnt|home|efs|tmp)/', published.decode())
    rows.append(dict(original=item['original_local_path'], publication=item['publication_copy'],
                     original_sha256=item['original_sha256'], publication_sha256=item['publication_sha256'],
                     changed_lines=changed, unchanged_lines=len(before)-len(changed), all_checks_pass=True))
result = dict(at=now.isoformat(timespec='seconds'), manifest_sha256=sha256(manifest.read_bytes()).hexdigest(),
              scope='Byte identity of all lines except listed runtime-warning and traceback path fields. No mathematical data or admission is altered.',
              rows=rows, all_checks_pass=True, actual_elapsed_s=time.monotonic()-start)
out = Path('artifacts/final_audit') / now.strftime('%Y%m%dT%H%M%SZ')
out.mkdir(parents=True, exist_ok=True)
(out/'publication_projection_checks.json').write_text(json.dumps(result, indent=2)+'\n')
(out/'final_publication_projection_audit.py').write_bytes(Path(__file__).read_bytes())
print(json.dumps(dict(at=result['at'], all_checks_pass=True, projections=len(rows), changed_lines=sum(len(r['changed_lines']) for r in rows), unchanged_lines=sum(r['unchanged_lines'] for r in rows))))
