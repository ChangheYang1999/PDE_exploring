"""Root receipt: independent standard-library reduction of the archived bvf table."""
from pathlib import Path
from datetime import datetime, timezone
import gzip
import hashlib
import json
import random

D = Path('bot_research/experiments/validation/reviews/economy_final_gate_001')
PHASE = D / 'bvf-20261031T232428135728Z'
OUTPUT = D / 'root_bvf_review_004.json'

def sha(data):
    return hashlib.sha256(data).hexdigest()

def main():
    assert not OUTPUT.exists()
    started = datetime.now(timezone.utc).isoformat()
    manifest_path = D / 'bvf_review_manifest_004.json'
    manifest = json.loads(manifest_path.read_bytes())
    for path, pin in manifest['files'].items():
        raw = Path(path).read_bytes()
        assert (len(raw), sha(raw)) == (pin['bytes'], pin['sha256']), path
    pins = json.loads((PHASE / 'inputs.json').read_bytes())['inputs']
    raw_inputs = {}
    for path, pin in pins.items():
        assert not Path(path).is_absolute() and '..' not in Path(path).parts
        packed = Path(pin['snapshot']).read_bytes()
        raw = gzip.decompress(packed)
        assert (sha(packed), sha(raw), len(raw)) == (pin['gzip_sha256'], pin['sha256'], pin['bytes']), path
        raw_inputs[path] = raw
    inspection = json.loads((PHASE / 'inspection.json').read_bytes())
    assert inspection['audit_completed_without_findings'] and not inspection['problems']
    specs = inspection['specs']
    tables = {tag: {} for tag in specs}
    E = 'bot_research/experiments/economy/'
    R = 'bot_research/runs/economy/'
    opponents = [s for s in raw_inputs[E + 'opp_fresh56.txt'].decode().splitlines() if s and not s.startswith('#')]
    pools = json.loads(raw_inputs[E + 'opp_fresh56_pools.json'])
    for run, tags in [('bvf', ['best_v9e']), ('afq56', ['af5']), ('fresh5a', ['g1', 'v29']), ('fresh6', ['g1', 'v29'])]:
        for line in raw_inputs[R + run + '/results.jsonl'].splitlines():
            row = json.loads(line)
            side = row['candidate_side']
            assert side in (0, 1)
            candidate = row['spec_a' if side == 0 else 'spec_b']
            for tag in tags:
                if candidate != specs[tag]:
                    continue
                key = (row['spec_b' if side == 0 else 'spec_a'], row['scenario'], side)
                assert key not in tables[tag]
                assert not row.get('error') and not row.get('source_changed')
                assert all(not p['bot_errors'] and p['n_rejected'] == 0 for p in row['players'])
                assert row['hp_a'] - row['hp_b'] == row['hp_diff_a']
                score = 1 if row['winner'] == side else .5 if row['winner'] is None else 0
                tables[tag][key] = (score, row['hp_diff_a'] * (1 if side == 0 else -1), row['rounds'])
    expected = {(opponent, None, side) for opponent in opponents for side in (0, 1)}
    assert len(expected) == 86
    assert all(set(t) == expected for t in tables.values())
    for row in inspection['joined_conditions']:
        key = (row['opponent'], row['scenario'], row['candidate_side'])
        assert all(list(tables[tag][key]) == value for tag, value in row['values'].items())
    checked = {}
    for family in ('ALL', 'LEAD', 'W1_FORTRESS', 'W3_COUNTERS', 'LEAD_PLUS_FORTRESS'):
        selected = sorted(o for o in opponents if family == 'ALL' or family in pools[o] or
                          family == 'LEAD_PLUS_FORTRESS' and bool(set(pools[o]) & {'LEAD', 'W1_FORTRESS'}))
        keys = [(o, None, side) for o in selected for side in (0, 1)]
        wdl = {tag: [sum(t[k][0] == s for k in keys) for s in (1, .5, 0)] for tag, t in tables.items()}
        target = inspection['family_tables'][family]
        assert wdl == target['wdl']
        intervals = {}
        for tag in ('af5', 'g1', 'v29'):
            differences = [sum(tables[tag][(o, None, side)][0] - tables['best_v9e'][(o, None, side)][0] for side in (0, 1)) / 2 for o in selected]
            rng = random.Random(1)
            samples = sorted(sum(rng.choice(differences) for _ in differences) / len(differences) for _ in range(4000))
            observed = (sum(differences) / len(differences), samples[100], samples[3899])
            reported = target['paired'][tag + '-best_v9e']
            assert all(abs(a - b) < 1e-12 for a, b in zip(observed, (reported['mean'], reported['lo'], reported['hi'])))
            intervals[tag + '-best_v9e'] = dict(zip(('mean', 'lo', 'hi'), observed))
        checked[family] = dict(conditions=len(keys), wdl=wdl, intervals=intervals)
    result = dict(started_utc=started, completed_utc=datetime.now(timezone.utc).isoformat(),
                  all_passed=True, archives_verified=len(pins), manifest_files_verified=len(manifest['files']),
                  exact_conditions=86, independently_reduced_families=checked,
                  scope='Root read the inspector, helper and review. Independent archived-byte checks and table/bootstrap reduction; no policy, engine, constructor or strength trials. LEAD_PLUS_FORTRESS is provenance only. Outcome repetition alone does not identify a causal load effect.',
                  input_sha256={str(path): sha(path.read_bytes()) for path in [Path(__file__).relative_to(Path.cwd()), manifest_path, PHASE / 'inputs.json', PHASE / 'inspection.json']})
    with OUTPUT.open('x') as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write('\n')
    print(json.dumps({k: result[k] for k in ('completed_utc', 'all_passed', 'archives_verified', 'manifest_files_verified', 'exact_conditions')}))

if __name__ == '__main__':
    main()
