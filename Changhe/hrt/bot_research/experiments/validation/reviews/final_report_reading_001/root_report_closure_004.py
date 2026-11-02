"""Check the final report's added H14 comparison and output-only wording."""
from pathlib import Path
from datetime import datetime, timezone
import gzip
import hashlib
import json


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat()


start = now()
base = Path('bot_research/experiments/validation/reviews/final_report_reading_001')
out = base / 'closure_004'
assert not (out / 'RECEIPT.json').exists()
cap = json.loads((out / 'CAPTURE.json').read_bytes())
packed = Path(cap['archive']).read_bytes()
report = gzip.decompress(packed)
assert sha(packed) == cap['archive_sha256']
assert sha(report) == cap['sha256'] == '5112420e67012772c368ac38c057a7f01fd02891045d7c2f2290c9eab79cb0c5'
assert sha((out / 'changes.diff').read_bytes()) == cap['diff_sha256']
parent = Path('bot_research/experiments/validation/reviews/economy_final_gate_001')
gate_path = parent / 'final-gate-20261031T233546260787Z/inputs.json'
gate_raw = gate_path.read_bytes()
assert sha(gate_raw) == '31523d876f0443867d30fcbfab3620d77e9577811db92c207cab324d373c7b15'
gate = json.loads(gate_raw)['inputs']
inputs = {str(gate_path): gate_raw}
rows = []
for run, length in [('afs5', 290), ('afg5', 514)]:
    path = f'bot_research/runs/economy/{run}/results.jsonl'
    pin = gate[path]
    packed = Path(pin['snapshot']).read_bytes()
    raw = gzip.decompress(packed)
    assert sha(packed) == pin['gzip_sha256'] and sha(raw) == pin['sha256']
    inputs[path] = raw
    selected = [json.loads(line) for line in raw.splitlines()]
    assert len(selected) == length
    for index, row in enumerate(selected, 1):
        side = row['candidate_side']
        candidate = row['spec_a' if side == 0 else 'spec_b']
        assert candidate.endswith('&attack_from=5')
        rows.append({'run': run, 'line': index, 'seat': side,
                     'opponent': row['spec_b' if side == 0 else 'spec_a'],
                     'scenario': row['scenario'],
                     'maximum_seconds': row['decide_max_seconds'][side]})
assert len({(r['opponent'], r['scenario'], r['seat']) for r in rows}) == 804
slow = [r for r in rows if r['maximum_seconds'] >= 3.0]
assert len(slow) == 3 and {r['run'] for r in slow} == {'afs5'}
assert max(r['maximum_seconds'] for r in slow) == 3.7738
historical_path = parent / 'historical-base-20261031T233659004971Z/inspection.json'
historical = historical_path.read_bytes()
inputs[str(historical_path)] = historical
h = json.loads(historical)
assert h['af5_worse_distinct_conditions'] == 30
assert h['af5_worse_distinct_specs'] == 15
assert len(h['af5_worse_than_base_memberships']) == 32
root_gate = parent / 'root_gate_review_008.json'
inputs[str(root_gate)] = root_gate.read_bytes()
assert sha(inputs[str(root_gate)]) == 'a2e397edcdda875d58dbac67f2c5edabc2eccd15f04bae1d70257fac7283fb87'
notes = Path('../hrt-lead/NOTES_FOR_TEAM.md').read_bytes()
inputs['../hrt-lead/NOTES_FOR_TEAM.md'] = notes
text = notes.decode()
start_h14 = text.index('## 2026-10-31T20:19:29Z')
end_h14 = text.index('\n## ', start_h14 + 3)
section = text[start_h14:end_h14]
assert '846' in section and '3 s' in section and 'AS1C' in section
inputs[str(base / 'closure_003/RECEIPT.json')] = (base / 'closure_003/RECEIPT.json').read_bytes()
assert sha(inputs[str(base / 'closure_003/RECEIPT.json')]) == '2401af1c9e3b376598112521c5389eeb51352b75f619cdf4c605fecaecf2ee4c'
archives = []
for number, (name, raw) in enumerate(inputs.items(), 1):
    path = out / f'input-{number:02d}.gz'
    with path.open('xb') as stream:
        stream.write(gzip.compress(raw, mtime=0))
    assert gzip.decompress(path.read_bytes()) == raw
    archives.append({'source': name, 'bytes': len(raw), 'sha256': sha(raw),
                     'archive': str(path), 'archive_sha256': sha(path.read_bytes())})
receipt = {
    'schema': 'root-report-closure-004', 'started_utc': start, 'completed_utc': now(),
    'actual_model': 'GPT-6 Astra', 'verdict': 'CONFIRMED for the bounded report delta',
    'report_sha256': sha(report), 'capture': cap, 'inputs': archives,
    'gate_rows_reduced': len(rows), 'calls_at_least_3_seconds': slow,
    'retained_base_adverse_memberships': 32, 'retained_base_adverse_distinct_conditions': 30,
    'manual_review': 'Root read the full diff. The added H14 numerical check is supported. The frr7 wording now states winner/HP/length equality, and the section reference changed from5.13 to5.14.',
    'scope': 'The original H14 rule names AS1C; applying those thresholds to AF5 is a later descriptive comparison, not an independently predeclared AF5 selection rule. Historical base predecessor-identity qualifications remain. No new policy, Engine, game, replay or test call; later report edits are outside this dated capture.',
    'script_sha256': sha(Path(__file__).read_bytes()),
}
path = out / 'RECEIPT.json'
path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + '\n')
print(json.dumps({'receipt': str(path), 'sha256': sha(path.read_bytes()), 'completed_utc': receipt['completed_utc'], 'slow_calls': slow}, indent=2))
