"""Authenticate the reviewed navigation snapshot and publish a minimal index supplement."""
from datetime import datetime, timezone
import difflib
import gzip
import hashlib
import json
from pathlib import Path
import re

ROOT = Path('bot_research/experiments/validation/reviews/final_navigation_001')
INDEX = Path('bot_research/experiments/validation/analysis/README.md')
OUT = ROOT / 'root_publication_001'

def sha(data):
    return hashlib.sha256(data).hexdigest()

def stamp():
    return datetime.now(timezone.utc).isoformat()

started = stamp()
assert not OUT.exists(), 'Preserve earlier publication evidence.'
expected = {
    'REVIEW.md': '5f5f37b566145b0a3634c064e0ad81b63d39d860f1ce8f34a883863e309d41db',
    'MINIMUM_ADDITIONS.md': 'fce11bda8b7ac7e42606608275ac98b7178128dbe4c5292ade20e904a09e4430',
    'REVIEW_RECEIPT.json': 'f6d3e7f479c02d1bb82b81f7c4e2f3c35bba3f50eff6562fb53533f5283c31ad',
    'scan_navigation.py': '0288e80622c5dd96bb87ea21ded4d65df993b912727d1adbdd5df8154804ce18',
    'inspection-001/INSPECTION.json': '5027da354614bfc3ca7184fce5c762803db96c66465df6b1898b9b724cb5e298',
}
for name, wanted in expected.items():
    assert sha((ROOT / name).read_bytes()) == wanted, name
inspection = json.loads((ROOT / 'inspection-001/INSPECTION.json').read_text())
inputs = inspection['input_documents']
assert len(inputs) == 384
current_matches = 0
for name, rec in inputs.items():
    packed = Path(rec['archive']).read_bytes()
    assert sha(packed) == rec['archive_sha256'], name
    data = gzip.decompress(packed)
    assert sha(data) == rec['sha256'] and len(data) == rec['bytes'], name
    assert Path(name).read_bytes() == data, name
    current_matches += 1
assert not inspection['missing_links'] and not inspection['missing_anchors']
assert len(inspection['edges']) == 331
for edge in inspection['edges']:
    assert edge['exists'] and not edge['outside_project'], edge
    assert Path(edge['resolved']).exists(), edge
before = INDEX.read_bytes()
assert sha(before) == 'd11e35db633f34a867bdc0deb1e6b4394ac2194cdd49de994dc4d0145d5532c9'
proposal = (ROOT / 'MINIMUM_ADDITIONS.md').read_text()
block = re.search(r'```markdown\n(.*?)\n```', proposal, re.S).group(1)
assert block.count('\n- ') == 3
published = stamp()
block = block.replace('## Completed evidence and finite-matrix supplements',
                      '## Completed evidence and finite-matrix supplements\n\nPublished ' + published + '.')
added_links = []
for label, target in re.findall(r'\[([^\]]+)\]\(([^)]+)\)', block):
    p = INDEX.parent / target
    assert p.exists(), target
    data = p.read_bytes()
    added_links.append({'label': label, 'target_relative_to_analysis': target,
                        'project_path': str(p.resolve().relative_to(Path.cwd())),
                        'sha256': sha(data)})
after = before.rstrip(b'\n') + b'\n\n' + block.encode() + b'\n'
OUT.mkdir()
(OUT / 'index_before.md.gz').write_bytes(gzip.compress(before, mtime=0))
(OUT / 'index_after.md.gz').write_bytes(gzip.compress(after, mtime=0))
(OUT / 'index.diff').write_text(''.join(difflib.unified_diff(before.decode().splitlines(keepends=True), after.decode().splitlines(keepends=True), fromfile='analysis/README.md before', tofile='analysis/README.md after')))
INDEX.write_bytes(after)
assert INDEX.read_bytes() == after
receipt = {
    'schema': 'root-navigation-publication-001', 'started_utc': started,
    'published_utc': published, 'completed_utc': stamp(), 'verdict': 'CONFIRMED',
    'review_inputs': expected, 'archived_markdown_inputs_authenticated': len(inputs),
    'current_markdown_inputs_equal_archived_bytes': current_matches,
    'existing_link_occurrences_checked_for_existence': len(inspection['edges']),
    'index_path': str(INDEX), 'index_before_sha256': sha(before),
    'index_after_sha256': sha(after), 'added_links': added_links,
    'scope': 'Append only the three reviewed navigation bullets; preserve all sealed proofs, guides, results and dated preparation pages. AF5 extension remains pending its own seal and independent review.',
    'not_performed': ['policy imports', 'policy calls', 'Engine calls', 'games', 'replays', 'tests', 'JavaScript/TypeScript', 'servers', 'cluster or remote compute'],
    'script_sha256': sha(Path(__file__).read_bytes()),
}
(OUT / 'RECEIPT.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps({'receipt': str(OUT / 'RECEIPT.json'), 'sha256': sha((OUT / 'RECEIPT.json').read_bytes()), 'completed_utc': receipt['completed_utc'], 'index_after_sha256': sha(after), 'new_links': len(added_links)}, indent=2))
