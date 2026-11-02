"""Independent bounded verification of the final summary review archives."""
from datetime import datetime, timezone
from pathlib import Path
import gzip
import hashlib
import json


def now():
    return datetime.now(timezone.utc).isoformat()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


start = now()
parent = Path('bot_research/experiments/validation/reviews/economy_final_gate_001')
base = parent / 'final_summary_019_001'
manifest_bytes = (base / 'manifest_001.json').read_bytes()
manifest = json.loads(manifest_bytes)
for name, pin in manifest['files'].items():
    raw = Path(name).read_bytes()
    assert sha(raw) == pin['sha256'] and len(raw) == pin['bytes'], name
inputs = json.loads((base / 'inputs.json').read_bytes())['inputs']
data = {}
for name, pin in inputs.items():
    packed = Path(pin['snapshot']).read_bytes()
    raw = gzip.decompress(packed)
    assert sha(packed) == pin['gzip_sha256'], name
    assert sha(raw) == pin['sha256'] and len(raw) == pin['bytes'], name
    assert not Path(name).is_absolute(), name
    data[name] = raw
assert len(data) == 25
inspection = json.loads((base / 'inspection.json').read_bytes())
gate = json.loads(data[str(parent / 'final-gate-20261031T233546260787Z/inspection.json')])
joined = gate['joined_conditions']
assert len(joined) == 804
key = lambda row: (row['opponent'], row['scenario'], row['candidate_side'])
assert len({key(row) for row in joined}) == 804
worse = [row for row in joined if row['values']['af5'][0] < row['values']['g1'][0]]
assert len(worse) == 8 and sum(len(r['pool_memberships']) for r in worse) == 8
assert worse == inspection['af5_worse_g1']['conditions']
checked = []
for comparison in worse:
    for tag in ('af5', 'g1'):
        ref = comparison['refs'][tag]
        name = f"bot_research/runs/economy/{ref['run']}/results.jsonl"
        row = json.loads(data[name].splitlines()[ref['line'] - 1])
        side = row['candidate_side']
        candidate = row['spec_a' if side == 0 else 'spec_b']
        opponent = row['spec_b' if side == 0 else 'spec_a']
        score = 0.5 if row['winner'] is None else float(row['winner'] == side)
        value = [score, row['hp_diff_a'] * (1 if side == 0 else -1), row['rounds']]
        assert candidate == gate['specs'][tag]
        assert (opponent, row['scenario'], side) == key(comparison)
        assert value == comparison['values'][tag]
        assert row['error'] is None and not row['source_changed']
        checked.append({'tag': tag, 'path': name, 'line': ref['line'], 'value': value})
assert len(checked) == 16
excluded = {'GROWERS', 'GUARDED_MAZE', 'HANDOFF', 'f5t'}
ten = [r for r in joined if set(r['pool_memberships']) - excluded]
assert len(ten) == 416
assert len({r['opponent'] for r in ten}) == 208
assert sum(len(set(r['pool_memberships']) - excluded) for r in ten) == 448
outside = [r for r in joined if not set(r['pool_memberships']) & excluded]
assert len(outside) == 406
assert inspection['afrr_exact_fresh56_repeat_count'] == {'conditions': 8, 'same_complete_value': 8, 'specs': 4}
assert len(inspection['afrr_source_alias']['comparisons']) == 2
for comparison in inspection['frr7_comparisons'].values():
    assert comparison['matched_conditions'] == comparison['same_canonical_history'] == 24
entry = json.loads((base / 'entry19_snapshot.json').read_bytes())['text']
notes = data['bot_research/notes/economy.md'].decode()
assert entry == notes[notes.index('## Entry 19 '):]
result = {
    'schema': 'root-final-summary-019-001', 'started_utc': start, 'completed_utc': now(),
    'actual_model': 'GPT-6 Astra', 'verdict': 'CONFIRMED for the bounded review corrections',
    'manifest_sha256': sha(manifest_bytes), 'sealed_files_verified': len(manifest['files']),
    'archives_verified': len(data), 'gate_unique_rows_checked': len(joined),
    'af5_worse_g1_unique_conditions': len(worse), 'af5_worse_g1_memberships': 8,
    'raw_rows_rejoined': checked,
    'ten_pool_scope': {'memberships': 448, 'distinct_conditions': 416, 'specs': 208,
                       'distinct_conditions_exclusive_of_four_selection_pools': 406},
    'manual_review': 'Root read the entire review, inspection and reader. Count, repeat, provenance, scenario, runtime and matrix-scope corrections agree with the archived records and previously checked evidence.',
    'scope': 'Archives and16 original adverse rows newly verified. Earlier complete archive graphs, policy behavior, runtime counterfactuals and mathematical certificates are not rerun. No bot, Engine, game, replay or test import/call.',
    'script_sha256': sha(Path(__file__).read_bytes()),
}
out = parent / 'root_final_summary_019_001.json'
with out.open('x') as stream:
    stream.write(json.dumps(result, indent=2, sort_keys=True) + '\n')
print(json.dumps({'receipt': str(out), 'sha256': sha(out.read_bytes()), 'completed_utc': result['completed_utc']}, indent=2))
