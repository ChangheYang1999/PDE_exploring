"""Archive exact recovered input bytes and rederive every joined numeric table.

This is metadata analysis only. It imports no policy or engine code.
"""
from collections import Counter
from datetime import datetime, timezone
import gzip
import hashlib
import json
from pathlib import Path

HERE = Path('bot_research/experiments/validation/reviews')
PREFIX = HERE / 'economy-gate-846-review-001'
RECOVERY = Path(str(PREFIX) + '.inputs.json')
SEALED = Path(str(PREFIX) + '.json')
OUTPUT = Path(str(PREFIX) + '.archive-recheck.json')
START = datetime.now(timezone.utc).isoformat()

def sha(b):
    return hashlib.sha256(b).hexdigest()

assert sha(SEALED.read_bytes()) == 'd243192a3d235f2c38d4a9707c9ddfd0287fbfd9006dedd616b5daed37d95af7'
assert sha(RECOVERY.read_bytes()) == '08ccc530c0065a04c1cff8eeb25869ec6a6a19dca3c67d39845bea0abfdea85d'
receipt = json.loads(SEALED.read_bytes())
recovery = json.loads(RECOVERY.read_bytes())
archives, cache = {}, {}
for source, info in recovery['files'].items():
    original = Path(info['archive'])
    target = Path(str(original) + '.gz')
    if target.exists():
        packed = target.read_bytes()
        raw = gzip.decompress(packed)
    else:
        raw = original.read_bytes()
        assert len(raw) == info['bytes'] and sha(raw) == info['sha256'], source
        packed = gzip.compress(raw, compresslevel=6, mtime=0)
        with target.open('xb') as f:
            f.write(packed)
    assert gzip.decompress(packed) == raw
    assert len(raw) == info['bytes'] and sha(raw) == info['sha256'], source
    assert receipt['inputs'][source] == {'bytes': len(raw), 'sha256': sha(raw)}
    archives[source] = {'gzip_archive': str(target), 'gzip_bytes': len(packed),
        'gzip_sha256': sha(packed), 'uncompressed_bytes': len(raw),
        'uncompressed_sha256': sha(raw),
        'recovered_from_appended_prefix': info['recovered_from_appended_prefix']}
    if source.endswith('.jsonl'):
        cache[source] = {i: json.loads(line) for i, line in enumerate(raw.splitlines(), 1) if line.strip()}
assert sum(a['gzip_bytes'] for a in archives.values()) < 100_000_000

# Every selected outcome is independently reconstructed from archived full result rows.
verified = 0
for entry in receipt['matrix']:
    side = entry['candidate_side']
    for role, p in [('base', entry['base'])] + list(entry['candidates'].items()):
        row = cache[p['input']][p['line']]
        candidate = row['spec_a' if side == 0 else 'spec_b']
        opponent = row['spec_b' if side == 0 else 'spec_a']
        assert row['candidate_side'] == side
        assert candidate == p['candidate_spec']
        assert opponent == entry['opponent_spec'] and row.get('scenario') == entry['scenario']
        if role != 'base':
            assert candidate == receipt['specs'][role]
        actual_outcome = 'D' if row['winner'] is None else 'W' if row['winner'] == side else 'L'
        assert actual_outcome == p['outcome']
        assert row['hp_diff_a'] * (1 if side == 0 else -1) == p['hp_difference']
        assert row['rounds'] == p['rounds']
        verified += 1

rank = {'W': 2, 'D': 1, 'L': 0}
selection = {'GROWERS', 'GUARDED_MAZE', 'HANDOFF', 'f5t'}
matrix = receipt['matrix']
def key(e):
    return (e['opponent_spec'], json.dumps(e['scenario'], sort_keys=True), e['candidate_side'])
def dedup(rows):
    out = {}
    for e in rows:
        k = key(e)
        if k in out:
            for role in ('base', 'V29', 'g1', 'g0'):
                a = e['base'] if role == 'base' else e['candidates'][role]
                b = out[k]['base'] if role == 'base' else out[k]['candidates'][role]
                assert (a['outcome'], a['hp_difference'], a['rounds']) == (b['outcome'], b['hp_difference'], b['rounds'])
        else:
            out[k] = e
    return list(out.values())
selected_keys = {key(e) for e in matrix if e['pool'] in selection}
groups = {'full_weighted846': matrix,
          'full_distinct804': dedup(matrix),
          'other_weighted448': [e for e in matrix if e['pool'] not in selection],
          'other_distinct416': dedup(e for e in matrix if e['pool'] not in selection),
          'other_disjoint406': dedup(e for e in matrix if e['pool'] not in selection and key(e) not in selected_keys)}
def compare(rows, name):
    ca = Counter(e['candidates'][name]['outcome'] for e in rows)
    ba = Counter(e['base']['outcome'] for e in rows)
    return {'n': len(rows), 'candidate_wdl': [ca[o] for o in 'WDL'],
            'base_wdl': [ba[o] for o in 'WDL'],
            'better': sum(rank[e['candidates'][name]['outcome']] > rank[e['base']['outcome']] for e in rows),
            'worse': sum(rank[e['candidates'][name]['outcome']] < rank[e['base']['outcome']] for e in rows)}
totals = {g: {n: compare(rows, n) for n in receipt['specs']} for g, rows in groups.items()}
for name in receipt['specs']:
    for new, old in [('full_weighted846', receipt['comparisons'][name]['full']),
                     ('other_weighted448', receipt['comparisons'][name]['subset448']),
                     ('full_distinct804', receipt['supplementary']['full_unique804'][name]),
                     ('other_distinct416', receipt['supplementary']['other_pool_unique416'][name]),
                     ('other_disjoint406', receipt['supplementary']['other_pool_excluding_selection_unique406'][name])]:
        assert all(old[k] == v for k, v in totals[new][name].items())

# Preserve the current report separately. It is not represented as the unavailable old report.
current_source = Path('bot_research/reports/REPORT.md')
current_raw = current_source.read_bytes()
current_read = datetime.now(timezone.utc).isoformat()
current_target = Path(str(PREFIX) + '.current-report-20261031T2218.gz')
current_packed = gzip.compress(current_raw, compresslevel=6, mtime=0)
with current_target.open('xb') as f:
    f.write(current_packed)
assert gzip.decompress(current_target.read_bytes()) == current_raw
result = {'started_utc': START, 'completed_utc': datetime.now(timezone.utc).isoformat(),
    'method': 'No policy or engine imports or calls. Hash-checked gzip recovery and exact archived result-row reconstruction.',
    'sealed_receipt': {'path': str(SEALED), 'sha256': sha(SEALED.read_bytes())},
    'recovery_manifest': {'path': str(RECOVERY), 'sha256': sha(RECOVERY.read_bytes())},
    'script': {'path': str(Path(__file__).relative_to(Path.cwd())), 'sha256': sha(Path(__file__).read_bytes())},
    'archives': archives, 'archived_inputs': len(archives),
    'compressed_bytes': sum(a['gzip_bytes'] for a in archives.values()),
    'uncompressed_bytes': sum(a['uncompressed_bytes'] for a in archives.values()),
    'unavailable_old_inputs': recovery.get('unavailable', recovery.get('unrecoverable', [])),
    'archived_row_payloads_verified_with_pool_repetitions': verified,
    'rederived_tables': totals,
    'current_report_separate_snapshot': {'read_utc': current_read, 'source': str(current_source),
        'gzip_archive': str(current_target), 'gzip_sha256': sha(current_packed),
        'uncompressed_sha256': sha(current_raw), 'uncompressed_bytes': len(current_raw),
        'source_changed_during_read': sha(current_source.read_bytes()) != sha(current_raw)},
    'scope': 'All numeric aggregation input bytes recovered exactly; the full old REPORT.md prose bytes were unavailable. Its challenged sentence is quoted in the sealed review. The current report snapshot is not substituted for the old input.'}
# Unavailable details are copied verbatim using the actual recovery manifest key.
result['recovery_manifest_nonfile_metadata'] = {k: v for k, v in recovery.items() if k != 'files'}
with OUTPUT.open('x') as f:
    f.write(json.dumps(result, indent=2, sort_keys=True) + '\n')
# Exact uncompressed recovery manifest is retained; gzip mapping replaces the transient raw copies.
for info in recovery['files'].values():
    original = Path(info['archive'])
    if original.exists():
        original.unlink()
print(json.dumps({'receipt': str(OUTPUT), 'sha256': sha(OUTPUT.read_bytes()),
                  'archived_inputs': len(archives), 'compressed_bytes': result['compressed_bytes'],
                  'joined_payloads_verified': verified, 'tables': totals}, indent=2))
