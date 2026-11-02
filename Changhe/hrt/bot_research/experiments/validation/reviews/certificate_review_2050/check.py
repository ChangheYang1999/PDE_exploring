"""Read-only independent checks of retained certificate artifacts; no games."""
from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
from urllib.parse import parse_qs
import gzip
import hashlib
import json
import math
import time

OUT = Path('bot_research/experiments/validation/reviews/certificate_review_2050')
BASE = Path('bot_research/experiments/validation/analysis')
started = time.perf_counter()
seen = {}
compressed = 0

def raw(name):
    global compressed
    p = Path(name)
    if p.is_file():
        return p.read_bytes()
    compressed += 1
    return gzip.decompress(Path(str(p)+'.gz').read_bytes())

def read(name):
    data = raw(name)
    digest = hashlib.sha256(data).hexdigest()
    assert str(name) not in seen or seen[str(name)] == digest
    seen[str(name)] = digest
    return json.loads(data)

def pins(mapping):
    for name, expected in mapping.items():
        digest = hashlib.sha256(raw(name)).hexdigest()
        assert digest == expected, name
        assert name not in seen or seen[name] == digest
        seen[name] = digest

def spec(name):
    module, _, query = name.partition('?')
    parsed = parse_qs(query)
    assert all(len(v) == 1 for v in parsed.values())
    args = {k: json.loads(v[0]) for k, v in parsed.items()}
    defaults = {
        'bot_research.bots.counters.delegated_defense:@make': {'mode': 'adaptive', 'delegate': 'econ20'},
        'bot_research.bots.counters.screened_roster_guarded:@make': {'continuation': 'fortress38'},
    }
    return module, defaults.get(module, {}) | args

ten = read(BASE/'ten_policy_game/verification/full_games.json')
parent = read(BASE/'screened_guard_minimum/verification/full_check.json')
reverse = read(BASE/'reverse_route_audit/verification/full_check.json')
for receipt in (ten, parent, reverse):
    for key in ('input_sha256', 'source_and_input_sha256', 'evidence_sha256'):
        pins(receipt.get(key, {}))
order = ten['order']
assert len(order) == len(set(order)) == 10
pairs = defaultdict(list)
assert len(ten['cases']) == len({c['result'] for c in ten['cases']}) == 110
new_calls = 0
for case in ten['cases']:
    result = read(case['result'])
    cond = result['condition']
    side = cond['candidate_side']
    assert side in (0, 1) and side == case['candidate_side']
    assert cond['initial_state'] == 'standard' and cond['pool'] == 'development'
    assert spec(cond['candidate_spec']) == spec(ten['policies'][case['a']]['spec'])
    assert spec(cond['opponent_spec']) == spec(ten['policies'][case['b']]['spec'])
    root = Path(case['result']).parent.parent
    job = read(root/'jobs'/(Path(case['result']).stem+'.json'))
    assert 'prefixes' not in job and job['condition'] == cond
    assert spec(job['bots'][side]['spec']) == spec(cond['candidate_spec'])
    assert spec(job['bots'][1-side]['spec']) == spec(cond['opponent_spec'])
    assert not any(result['bot_errors']) and not any(result['rejected_actions'])
    assert not result['source_changed_during_match']
    winner = result['result']['winner']
    outcome = 'D' if winner is None else ('W' if winner == side else 'L')
    assert outcome == case['outcome'] == result['candidate_outcome']
    assert case['hp_a_first'] == [result['hp'][side], result['hp'][1-side]]
    assert case['rounds'] == result['rounds']
    data = raw(result['replay_path'])
    assert hashlib.sha256(data).hexdigest() == result['trajectory_sha256']
    rows = [json.loads(line) for line in data.splitlines()]
    assert len(rows) == 2*(result['rounds']+1)
    assert [(r['round'],r['player']) for r in rows] == [(rnd,p) for rnd in range(result['rounds']+1) for p in (0,1)]
    assert all(r['result'] == result['result'] for r in rows[-2:])
    assert [r['snapshot']['hp'] for r in rows[-2:]] == result['hp']
    for row in rows:
        row.pop('match', None)
        row['player'] = (row['player'] - side) % 2
        row['snapshot']['name'] = ['counter','opponent'][row['player']]
        for event in row['event']:
            event.pop('order', None)
        if 'result' in row and row['result']['winner'] is not None:
            row['result']['winner'] = (row['result']['winner'] - side) % 2
    rows.sort(key=lambda row: (row['round'],row['player']))
    digest = hashlib.sha256(json.dumps(rows,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert digest == case['canonical_replay_sha256']
    pairs[tuple(sorted((case['a'],case['b'])))].append((case,digest))
    if not case['reused']:
        new_calls += 2*result['rounds']
assert len(pairs) == 55
matrix = [[None]*10 for _ in order]
for group in pairs.values():
    assert len(group) == 2 and {c['candidate_side'] for c,_ in group} == {0,1}
    left, right = [c for c,_ in group]
    assert left['a'] == right['a'] and left['b'] == right['b']
    assert group[0][1] == group[1][1]
    assert left['outcome'] == right['outcome']
    i,j = order.index(left['a']),order.index(left['b'])
    value = {'W':1,'D':0,'L':-1}[left['outcome']]
    if i == j:
        assert value == 0
    assert matrix[i][j] is None and matrix[j][i] is None
    matrix[i][j],matrix[j][i] = value,-value
assert matrix == ten['payoff']
assert new_calls == ten['fresh_calls'] == 1732
assert sum(not c['reused'] for c in ten['cases']) == ten['new_games'] == 34
weights = list(map(Fraction,ten['certificate']['weights']))
assert all(w >= 0 for w in weights) and sum(weights) == 1
lower = [sum(weights[i]*matrix[i][j] for i in range(10)) for j in range(10)]
upper = [sum(matrix[i][j]*weights[j] for j in range(10)) for i in range(10)]
assert min(lower) == max(upper) == 0
assert list(map(str,lower)) == ten['certificate']['column_payoffs']
prior = [Fraction(1,5) if k in ('B','G','H','J','L') else Fraction(0) for k in order]
prior_payoffs = [sum(prior[i]*matrix[i][j] for i in range(10)) for j in range(10)]
assert list(map(str,prior_payoffs)) == ten['prior_mixture_payoffs']
gaps = [matrix[order.index('N')][j]-matrix[order.index('B')][j] for j in range(8)]
assert gaps == ten['N_minus_B'] and min(gaps) == 0 and max(gaps) > 0
counts = [math.comb(138,k) for k in range(5)]
assert counts == parent['counts_by_cardinality'] == reverse['counts_by_cardinality']
assert sum(counts) == parent['total_wall_sets'] == reverse['records'] == 14901218
for key in ('invalid_by_cardinality','maximum_exposure_by_cardinality'):
    assert parent[key] == reverse[key]
for k in range(5):
    h = reverse['histogram_by_cardinality'][k]
    assert sum(h) == counts[k]
    assert h[0] == reverse['invalid_by_cardinality'][k]
    assert max(i-1 for i,c in enumerate(h) if c) == reverse['maximum_exposure_by_cardinality'][k]
    assert sum(s['cardinalities'][k]['count'] for s in reverse['shards']) == counts[k]
assert all(s['mismatches'] == 0 for s in reverse['shards'])
assert reverse['full_python_paths_checked'] == parent['original_python_router_checks'] == 11097
assert parent['original_engine_witnesses'][-1]['k'] == parent['minimum_walls'] == 5
assert parent['original_engine_witnesses'][-1]['incoming_damage'] == 0
result = dict(time_utc=datetime.now(timezone.utc).isoformat(), elapsed_seconds=time.perf_counter()-started,
    all_passed=True, checks='All recorded receipt input hashes; all 110 raw result conditions and job bot specifications; all normalized replay hashes and pair equality; matrix rebuilt from engine winner fields; exact rational bounds; route receipt totals and histograms.',
    distinct_hashed_inputs=len(seen), compressed_input_reads=compressed,
    cases=110, assignment_pairs=55, new_games_in_table=34, new_policy_calls_in_table=new_calls,
    certificate_weights=list(map(str,weights)), column_payoffs=list(map(str,lower)), row_payoffs=list(map(str,upper)),
    counts_by_cardinality=counts, record_count=sum(counts),
    scope='Read-only artifact recheck. No policy calls, engine replay, native recompilation, or full route score recomputation was performed by this review.',
    input_sha256=seen,
    checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
with (OUT/'result.json').open('x') as stream:
    json.dump(result,stream,indent=2,sort_keys=True)
    stream.write('\n')
print(json.dumps({k:v for k,v in result.items() if k != 'input_sha256'},indent=2))
