"""Authenticate retained AF5 reviews and independently recount their closed records."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import gzip
import hashlib
import json

BASE = Path('bot_research/experiments/validation/reviews/economy_final_gate_001')
started = datetime.now(timezone.utc).isoformat()
def sha(data):
    return hashlib.sha256(data).hexdigest()
def load(path):
    return json.loads(Path(path).read_bytes())
def checked(path, digest):
    raw = Path(path).read_bytes()
    assert sha(raw) == digest, str(path)
    return json.loads(raw)
def archive_map(path):
    manifest = load(path)
    result = {}
    for name, pin in manifest['inputs'].items():
        assert not Path(name).is_absolute() and '..' not in Path(name).parts
        packed = Path(pin['snapshot']).read_bytes()
        assert sha(packed) == pin['gzip_sha256'], name
        raw = gzip.decompress(packed)
        assert sha(raw) == pin['sha256'] and len(raw) == pin['bytes'], name
        result[name] = raw
    assert len(result) == manifest['all_archives_verified']
    return result

authenticated_files = {}
for name, digest in [
    ('afrr_review_manifest_006.json', '2c6d3a9db5f2c42c96366f6f68f4ae27136b4521ea037656c75be717c8ef1506'),
    ('afrep_review_manifest_011.json', '6d9b2c55f21b4a8353f85e3f666f8b9011246dfbc927e218fdb619e8de682976'),
]:
    manifest = checked(BASE/name, digest)
    for path, pin in manifest['files'].items():
        raw = Path(path).read_bytes()
        assert sha(raw) == pin['sha256'] and len(raw) == pin['bytes'], path
        authenticated_files[path] = pin

rrpath = BASE/'afrr-20261031T233750162131Z'
rr = checked(rrpath/'inspection.json', '6659ba2e0bb9a8c7ac693b1898099a34b9c9d2899f66cb57deb1d63e9112aa43')
rrraw = archive_map(rrpath/'inputs.json')
reppath = BASE/'afrep-20261031T234033189508Z'
rep = checked(reppath/'inspection.json', '89af3548237a33784b3fdfb8499d33b940804194dafc05cf9ce2937b647fc9e8')
repraw = archive_map(reppath/'inputs.json')
scopepath = BASE/'late-scope-20261031T233852012599Z'
scope = checked(scopepath/'inspection.json', 'bfa321158bea17737ae1ce7372ab0411a5f8cf1f54c8e9c8889f676597aa7c33')
scoperaw = archive_map(scopepath/'inputs.json')
assert [len(rrraw), len(repraw), len(scoperaw)] == [94, 68, 23]
assert not rr['problems'] and not rep['problems'] and not scope['problems']

def rows(raw):
    return [json.loads(line) for line in raw.splitlines() if line.strip()]
def normalize(row):
    side = row['candidate_side']
    assert side in (0, 1) and row['winner'] in (None, 0, 1)
    assert row['hp_a'] - row['hp_b'] == row['hp_diff_a']
    assert not row.get('error') and not row.get('source_changed')
    assert not any(row.get('scenario_errors', []))
    assert all(not p['bot_errors'] and p['n_rejected'] == 0 for p in row['players'])
    candidate = row['spec_a' if side == 0 else 'spec_b']
    opponent = row['spec_b' if side == 0 else 'spec_a']
    value = [0.5 if row['winner'] is None else float(row['winner'] == side),
             row['hp_diff_a'] * (1 if side == 0 else -1), row['rounds']]
    return candidate, (opponent, row.get('scenario'), side), value
rrrows = rows(rrraw['bot_research/runs/economy/afrr/results.jsonl'])
assert len(rrrows) == 20
rrtable = {}
for row in rrrows:
    candidate, key, value = normalize(row)
    assert candidate == rr['candidate_spec'] and key[1] is None and key not in rrtable
    rrtable[key] = value
counts = Counter(v[0] for v in rrtable.values())
assert [counts[1.0], counts[.5], counts[0.0]] == rr['wdl'] == [16, 0, 4]
for item in rr['per_opponent']:
    pair = [rrtable[(item['opponent'], None, side)] for side in (0, 1)]
    assert pair[0] == pair[1]
    assert pair == [o['value'] for o in item['observations']]
assert len(rr['per_opponent']) == 10
assert not rr['hypotheses']['H18_28a_on_completed_afrr']
assert rr['hypotheses']['H18_28b_on_completed_afrr']
repeat_checks = 0
for item in rr['exact_fresh56_repeats']:
    key = (item['opponent'], None, item['candidate_side'])
    ref = item['afq56_ref']
    path = 'bot_research/runs/economy/' + ref['run'] + '/results.jsonl'
    candidate, actual_key, value = normalize(rows(rrraw[path])[ref['line'] - 1])
    assert candidate == rr['candidate_spec'] and actual_key == key
    assert value == rrtable[key] == item['afq56'] == item['afrr']
    repeat_checks += 1
assert repeat_checks == 8

reprows = rows(repraw['bot_research/runs/economy/afrep/results.jsonl'])
assert len(reprows) == 2
hp_histories = []
action_events = 0
for row in reprows:
    candidate, key, value = normalize(row)
    assert candidate == rr['candidate_spec'] and value == rrtable[key] == [1.0, 410, 50]
    side = key[2]
    log = rows(repraw[row['log']])
    assert len(log) == 102
    states = {}
    for entry in log:
        turn, player = entry['round'], entry['player']
        assert (turn, player) not in states
        states[turn, player] = entry['snapshot']
        assert entry['snapshot']['name'] == row['spec_a' if player == 0 else 'spec_b']
        if turn == 0:
            assert entry['match']['research_specs'] == [row['spec_a'], row['spec_b']]
            assert entry['match']['research_scenario'] is None
        else:
            for event in entry['event']:
                if event['kind'] == 'action':
                    assert event['accepted'] is True
                    action_events += 1
    assert set(states) == {(turn, player) for turn in range(51) for player in (0, 1)}
    hp = [(states[t, side]['hp'], states[t, 1-side]['hp']) for t in range(51)]
    changes = [(t, pair) for t, pair in enumerate(hp) if t == 0 or pair != hp[t-1]]
    assert changes == [(0, (800,800)), (1, (785,795)), (9, (785,655)), (10, (785,375))]
    for player in (0, 1):
        for field in ('hp', 'gold', 'n_factories', 'n_turrets', 'n_walls', 'length_path'):
            assert states[50, player][field] == row['players'][player][field]
    hp_histories.append({'candidate_side': side, 'changes': changes, 'log': row['log'], 'sha256': sha(repraw[row['log']])})
assert rep['H18_33'] is True
assert max(row['decide_max_seconds'][row['candidate_side']] for row in reprows) == rep['recorded_max_af5_call_seconds'] == .5154
assert max(row['decide_max_seconds'][1-row['candidate_side']] for row in reprows) == rep['recorded_max_best_v9e_call_seconds'] == 2.9551

# Recount the selection-stage partition from the separately authenticated gate rows.
gate = checked(BASE/'final-gate-20261031T233546260787Z/inspection.json', '3c06e23be7a4944fd25b3a8b20c2820fbd1c3c4c826ebe69ac4f155979473c6e')
gatemap = load(BASE/'final-gate-20261031T233546260787Z/inputs.json')['inputs']
gateraw = {}
def gate_rows(path):
    if path not in gateraw:
        pin = gatemap[path]
        packed = Path(pin['snapshot']).read_bytes()
        assert sha(packed) == pin['gzip_sha256']
        raw = gzip.decompress(packed)
        assert sha(raw) == pin['sha256'] and len(raw) == pin['bytes']
        gateraw[path] = rows(raw)
    return gateraw[path]
joined = {(r['opponent'], r['scenario'], r['candidate_side']): r for r in gate['joined_conditions']}
stages = {name: {'memberships':0, 'keys':set(), 'wdl':{tag:[0,0,0] for tag in ('af5','g1','v29','base')}} for name in ('afs5','afg5')}
for refs in gate['base_membership_refs'].values():
    for item in refs:
        key, ref = tuple(item['condition']), item['ref']
        _, observed, basevalue = normalize(gate_rows(ref['path'])[ref['line']-1])
        assert key == observed
        row = joined[key]
        stage = stages[row['refs']['af5']['run']]
        stage['memberships'] += 1
        stage['keys'].add(key)
        values = row['values'] | {'base':basevalue}
        for tag, value in values.items():
            stage['wdl'][tag][(1.0,.5,0.0).index(value[0])] += 1
partition = {tag: {'memberships':value['memberships'], 'unique_conditions':len(value['keys']), 'exact_specs':len({k[0] for k in value['keys']}), 'wdl':value['wdl']} for tag,value in stages.items()}
assert partition == scope['sampling_stage_partition']

result = {'started_utc':started, 'completed_utc':datetime.now(timezone.utc).isoformat(), 'status':'CONFIRMED', 'reviewer':'GPT-6 Astra root independent recount', 'archive_edges':185, 'additional_gate_base_archives':len(gateraw), 'review_files_checked':len(authenticated_files), 'afrr_wdl':[16,0,4], 'exact_repeat_checks':repeat_checks, 'afrep_logs':hp_histories, 'afrep_action_events':action_events, 'stage_partition':partition, 'inputs':authenticated_files, 'script_sha256':sha(Path(__file__).read_bytes()), 'scope':'Retained source/result/log authentication and independent arithmetic only. No policy, constructor, Engine, match or replay. Reproduction does not identify load causally or imply future equivalence.'}
output=BASE/'root_afrr_afrep_review_001.json'
assert not output.exists()
output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps({k:result[k] for k in ('completed_utc','status','archive_edges','review_files_checked','afrr_wdl','exact_repeat_checks','afrep_action_events','stage_partition')},indent=2))
print('receipt_sha256',sha(output.read_bytes()))
