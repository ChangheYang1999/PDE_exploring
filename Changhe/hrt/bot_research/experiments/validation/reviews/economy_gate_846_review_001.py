"""Read retained JSONL bytes and independently join exact specifications, scenarios, and seats.

No policy or engine imports, construction, decisions, or games. Run from the project root.
"""
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

HERE = Path('bot_research/experiments/validation/reviews')
OUT = HERE / 'economy-gate-846-review-001.json'
START = datetime.now(timezone.utc).isoformat()
GATES = [
    ('PCS', 'lead/g13pc', 'best_v9e:@make', 8),
    ('TIMING', 'lead/bse_tm', 'best_v9e:@make', 32),
    ('TIMING2', 'lead/tm2', 'foreign_target', 40),
    ('STRIKE1', 'economy/strike1b', 'best_v9e:@make', 40),
    ('TARGETED2', '../tmp/base_t8f_v18f.jsonl', 'fortress_guns=true&catch_up=true', 48),
    ('f5t', 'lead/ab1', 'best_v9e:@make', 76),
    ('PUNISH', 'lead/pu1', 'foreign_target', 34),
    ('BLUFFCOV', '../tmp/base_b9a_v18f.jsonl', 'foreign_target', 16),
    ('TARGETED3_P5TF', 'lead/t9k', 'foreign_target', 30),
    ('HANDOFF', 'lead/bse_hd', 'best_v9e:@make', 36),
    ('SCREENED', 'lead/bse_sg', 'best_v9e:@make', 60),
    ('GROWERS', 'lead/g9a', 'foreign_target', 142),
    ('GUARDED_MAZE', '../tmp/base_gm2_v18f.jsonl', 'foreign_target', 144),
    ('STAGED', '../tmp/base_st1_v18f.jsonl', 'foreign_target', 140),
]
RUNS = ['gate1', 'fam2b', 'g1chk', 'grow1', 'gmaze1', 'hand2', 'hand3', 'stdg', 'stdg2',
        'fresh5a', 'fresh5b', 'smoke31', 'g1fg', 'g1ff', 'g1fm', 'g1fc', 'pcs1', 'hand4',
        'afs6', 'afs5', 'fresh6']
SELECTION = {'GROWERS', 'GUARDED_MAZE', 'HANDOFF', 'f5t'}
inputs = {}
cache = {}


def read(path):
    path = str(path)
    b = Path(path).read_bytes()
    inputs[path] = {'sha256': hashlib.sha256(b).hexdigest(), 'bytes': len(b)}
    return b


def rows(path):
    path = str(path)
    if path not in cache:
        cache[path] = [(i, json.loads(line)) for i, line in enumerate(read(path).splitlines(), 1) if line.strip()]
    return cache[path]


specs = {name: read(Path('../hrt-w2/scratch') / (name.lower() + '.spec')).decode().strip()
         for name in ('V29', 'g1', 'g0')}
assert specs['g1'] == specs['V29'] + '&attack_from=7'
assert specs['g0'] == specs['V29'] + '&r1_units=0&attack_from=7'
by_spec = {s: n for n, s in specs.items()}


def identity(r):
    s = r['candidate_side']
    assert type(s) is int and s in (0, 1)
    candidate = r['spec_a' if s == 0 else 'spec_b']
    opponent = r['spec_b' if s == 0 else 'spec_a']
    scenario = json.dumps(r.get('scenario'), sort_keys=True, separators=(',', ':'))
    return candidate, (opponent, scenario, s)


def payload(path, line, r):
    s = r['candidate_side']
    w = r['winner']
    assert w is None or type(w) is int and w in (0, 1)
    signed = r['hp_diff_a'] * (1 if s == 0 else -1)
    assert r['hp_diff_a'] == r['hp_a'] - r['hp_b']
    p = r['players'][s]
    assert p['hp'] == r['hp_a' if s == 0 else 'hp_b']
    out = 'D' if w is None else 'W' if w == s else 'L'
    return {
        'input': path, 'line': line, 'candidate_spec': identity(r)[0],
        'outcome': out, 'hp_difference': signed, 'rounds': r['rounds'],
        'candidate_hash': r.get('hash_a' if s == 0 else 'hash_b'),
        'candidate_version': r.get('version_a' if s == 0 else 'version_b'),
        'opponent_hash': r.get('hash_b' if s == 0 else 'hash_a'),
        'opponent_version': r.get('version_b' if s == 0 else 'version_a'),
        'sources_sha256': hashlib.sha256(json.dumps(r.get('sources'), sort_keys=True,
                         separators=(',', ':')).encode()).hexdigest(),
        'engine_hash': r.get('sources', {}).get('td_game/engine.py'),
        'source_changed': r.get('source_changed'),
        'candidate_rejected': p['n_rejected'], 'candidate_bot_errors': p['bot_errors'],
        'opponent_rejected': r['players'][1-s]['n_rejected'],
        'opponent_bot_errors': r['players'][1-s]['bot_errors'],
        'scenario_errors': r.get('scenario_errors'),
        'max_decision_seconds': r['decide_max_seconds'][s], 'log': r.get('log'),
    }


def outcome_signature(p):
    return (p['outcome'], p['hp_difference'], p['rounds'])


def key_json(k):
    return {'opponent_spec': k[0], 'scenario': json.loads(k[1]), 'candidate_side': k[2]}


raw_candidates = {n: defaultdict(list) for n in specs}
missing_files, error_rows = [], []
for run in RUNS:
    path = f'bot_research/runs/economy/{run}/results.jsonl'
    if not Path(path).exists():
        missing_files.append(path)
        continue
    for line, r in rows(path):
        candidate, key = identity(r)
        if candidate not in by_spec:
            continue
        name = by_spec[candidate]
        if r.get('error'):
            error_rows.append({'name': name, 'input': path, 'line': line, 'error': r['error']})
        else:
            raw_candidates[name][key].append(payload(path, line, r))

raw_bases = {}
base_info = {}
for pool, suffix, substring, expected in GATES:
    path = ('bot_research/tmp/' + suffix.split('/')[-1] if suffix.startswith('../tmp/')
            else 'bot_research/runs/' + suffix + '/results.jsonl')
    dd = defaultdict(list)
    selected_errors = []
    for line, r in rows(path):
        candidate, key = identity(r)
        if substring not in candidate or 'catch_up_share=1.0' in candidate:
            continue
        if r.get('error'):
            selected_errors.append({'input': path, 'line': line, 'error': r['error']})
        else:
            dd[key].append(payload(path, line, r))
    raw_bases[pool] = dd
    base_info[pool] = {'input': path, 'selection_substring': substring, 'expected': expected,
        'conditions': len(dd), 'selected_rows': sum(map(len, dd.values())), 'errors': selected_errors,
        'selected_exact_specs': dict(Counter(p['candidate_spec'] for ps in dd.values() for p in ps)),
        'candidate_hashes': dict(Counter(p['candidate_hash'] for ps in dd.values() for p in ps)),
        'candidate_versions': dict(Counter(p['candidate_version'] for ps in dd.values() for p in ps))}


def duplicate_summary(dd):
    repeated = [(k, ps) for k, ps in dd.items() if len(ps) > 1]
    conflicts = [(k, ps) for k, ps in repeated if len({outcome_signature(p) for p in ps}) > 1]
    return {'unique_conditions': len(dd), 'rows': sum(map(len, dd.values())),
        'repeated_conditions': len(repeated), 'extra_rows': sum(len(ps)-1 for _, ps in repeated),
        'conflicts': [{'condition': key_json(k), 'rows': ps} for k, ps in conflicts],
        'repeats': [{'condition': key_json(k), 'rows': ps} for k, ps in repeated]}


cand_dup = {n: duplicate_summary(dd) for n, dd in raw_candidates.items()}
base_dup = {n: duplicate_summary(dd) for n, dd in raw_bases.items()}
candidates = {n: {k: ps[0] for k, ps in dd.items() if len({outcome_signature(p) for p in ps}) == 1}
              for n, dd in raw_candidates.items()}
# Require no baseline overwrite ambiguity before selecting any row.
assert not any(d['conflicts'] for d in base_dup.values()), 'Conflicting baseline duplicate: inspect receipt logic.'
assert not any(any(len({p['candidate_spec'] for p in ps}) > 1 for ps in dd.values())
               for dd in raw_bases.values()), 'Baseline alias duplicate: needs explicit adjudication.'
bases = {n: {k: ps[0] for k, ps in dd.items()} for n, dd in raw_bases.items()}
all_keys = set().union(*(set(b) for b in bases.values()))
memberships = defaultdict(list)
for pool, b in bases.items():
    for k in b:
        memberships[k].append(pool)
rank = {'W': 2, 'D': 1, 'L': 0}


def wdl(ps):
    c = Counter(p['outcome'] for p in ps)
    return [c[x] for x in 'WDL']


def compare(name, selected_pools):
    pairs = [(candidates[name][k], bases[pool][k]) for pool in selected_pools
             for k in bases[pool] if k in candidates[name]]
    return {'n': len(pairs), 'candidate_wdl': wdl(a for a, b in pairs),
            'base_wdl': wdl(b for a, b in pairs),
            'worse': sum(rank[a['outcome']] < rank[b['outcome']] for a, b in pairs),
            'better': sum(rank[a['outcome']] > rank[b['outcome']] for a, b in pairs),
            'equal_wdl': sum(a['outcome'] == b['outcome'] for a, b in pairs),
            'same_outcome_other_hp': sum(a['outcome'] == b['outcome'] and
                                         a['hp_difference'] != b['hp_difference'] for a, b in pairs)}


def seat_summary(dd):
    pairs = defaultdict(dict)
    for (opp, scenario, s), p in dd.items():
        pairs[opp, scenario][s] = p
    both = [d for d in pairs.values() if set(d) == {0, 1}]
    return {'opponent_scenario_pairs': len(pairs), 'both_seats': len(both),
        'unpaired': [{'opponent_spec': o, 'scenario': json.loads(sc), 'seats': sorted(d)}
                    for (o, sc), d in pairs.items() if set(d) != {0, 1}],
        'equal_wdl_both_seats': sum(d[0]['outcome'] == d[1]['outcome'] for d in both),
        'equal_wdl_hp_rounds_both_seats': sum(outcome_signature(d[0]) == outcome_signature(d[1]) for d in both)}


comparison = {name: {'full': compare(name, bases),
    'subset448': compare(name, [p for p in bases if p not in SELECTION]),
    'selection398': compare(name, [p for p in bases if p in SELECTION]),
    'pools': {pool: compare(name, [pool]) for pool in bases},
    'missing': {pool: [key_json(k) for k in sorted(set(b)-set(candidates[name]))]
                for pool, b in bases.items()},
    'extra_unique_outside_gate': len(set(candidates[name])-all_keys),
    'seat_summary_gate': seat_summary({k: p for k, p in candidates[name].items() if k in all_keys})}
    for name in specs}


def metadata_summary(ps):
    ps = list(ps)
    return {'rows': len(ps), 'candidate_rejected': sum(p['candidate_rejected'] for p in ps),
        'candidate_bot_errors': sum(len(p['candidate_bot_errors']) for p in ps),
        'opponent_rejected': sum(p['opponent_rejected'] for p in ps),
        'opponent_bot_errors': sum(len(p['opponent_bot_errors']) for p in ps),
        'source_changed_counts': dict(Counter(str(p['source_changed']) for p in ps)),
        'candidate_hashes': dict(Counter(p['candidate_hash'] for p in ps)),
        'candidate_versions': dict(Counter(p['candidate_version'] for p in ps)),
        'engine_hashes': dict(Counter(p['engine_hash'] for p in ps)),
        'source_map_hashes': dict(Counter(p['sources_sha256'] for p in ps)),
        'max_decision_seconds': max((p['max_decision_seconds'] for p in ps), default=None)}


matrix = [{'pool': pool, **key_json(k), 'base': bases[pool][k],
           'candidates': {n: candidates[n].get(k) for n in specs}}
          for pool in bases for k in sorted(bases[pool])]
opponent_version_mismatch = []
for row in matrix:
    for n, p in row['candidates'].items():
        if p is not None and (p['opponent_hash'] != row['base']['opponent_hash'] or
                              p['opponent_version'] != row['base']['opponent_version']):
            opponent_version_mismatch.append({'pool': row['pool'], 'opponent_spec': row['opponent_spec'],
                'scenario': row['scenario'], 'candidate_side': row['candidate_side'], 'candidate': n,
                'base_hash': row['base']['opponent_hash'], 'candidate_hash': p['opponent_hash'],
                'base_version': row['base']['opponent_version'], 'candidate_version': p['opponent_version']})

# Denominators and source-selection caveats are separate from the reproduced pool-weighted totals.
from urllib.parse import parse_qsl
import re

base_parameters = ('big_threat=100&gun_cap=120&poke_until=3&big_partial=true'
    '&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true'
    '&foreign_policy="econ17"&mid_until=5&fortress_guns=true&catch_up=true')
base_aliases = {
    'frozen': 'bot_research.experiments.lead.frozen.best_v9e:@make',
    'v18_standard_only': 'bot_research.experiments.lead.v18:@make?' + base_parameters,
    'v19_twin': 'bot_research.experiments.lead.v19:@make?' + base_parameters + '&foreign_target="econ20"',
}
for pool, info in base_info.items():
    alias = 'v18_standard_only' if pool == 'TARGETED2' else ('frozen' if
        pool in {'PCS','TIMING','STRIKE1','f5t','HANDOFF','SCREENED'} else 'v19_twin')
    assert info['selected_exact_specs'] == {base_aliases[alias]: info['expected']}

base_by_key = defaultdict(list)
for pool, dd in bases.items():
    for key, value in dd.items():
        base_by_key[key].append((pool, value))
base_cross_conflicts = [{'condition': key_json(k), 'rows': ps} for k, ps in base_by_key.items()
                        if len({outcome_signature(p) for pool, p in ps}) > 1]
assert not base_cross_conflicts, 'Cross-pool baseline outcomes differ: do not deduplicate silently.'
selection_keys = set().union(*(set(bases[p]) for p in SELECTION))
other_keys = set().union(*(set(bases[p]) for p in bases if p not in SELECTION))


def unique_comparison(keys):
    out = {}
    for n in specs:
        pairs = [(candidates[n][k], base_by_key[k][0][1]) for k in keys]
        out[n] = {'n': len(pairs), 'candidate_wdl': wdl(a for a,b in pairs),
            'base_wdl': wdl(b for a,b in pairs),
            'worse': sum(rank[a['outcome']] < rank[b['outcome']] for a,b in pairs),
            'better': sum(rank[a['outcome']] > rank[b['outcome']] for a,b in pairs)}
    return out


def parsed_spec(spec):
    module, _, rest = spec.partition(':')
    function, _, query = rest.partition('?')
    kwargs = {}
    for k, v in parse_qsl(query, keep_blank_values=True):
        try:
            kwargs[k] = json.loads(v)
        except json.JSONDecodeError:
            kwargs[k] = v
    return module, function, json.dumps(kwargs, sort_keys=True, separators=(',', ':'))


key5_path = 'bot_research/experiments/economy/opp_key5.txt'
key5 = [s.strip() for s in read(key5_path).decode().splitlines() if s.strip() and not s.lstrip().startswith('#')]
key5_parsed = {parsed_spec(s): s for s in key5}
key5_overlap = [{'condition': key_json(k), 'original_key5_spec': key5_parsed[parsed_spec(k[0])]}
                for k in sorted(other_keys) if parsed_spec(k[0]) in key5_parsed]
fresh_path = 'bot_research/experiments/economy/opp_fresh56_pools.json'
fresh_groups = json.loads(read(fresh_path))
read('bot_research/experiments/economy/opp_fresh56.txt')

# All recorded td_game/td_bots source entries on joined rows are checked against current bytes.
protected_record_hashes = defaultdict(set)
all_matched_rows = []
for pool, dd in raw_bases.items():
    all_matched_rows.extend(p for ps in dd.values() for p in ps)
for n, dd in raw_candidates.items():
    all_matched_rows.extend(p for k, ps in dd.items() if k in all_keys for p in ps)
for p in all_matched_rows:
    r = dict(cache[p['input']])[p['line']]
    for path, digest in r.get('sources', {}).items():
        if path.startswith(('td_game/', 'td_bots/')):
            protected_record_hashes[path].add(digest)
protected_current = {path: hashlib.sha256(read(path)).hexdigest() for path in protected_record_hashes}
protected_mismatch = {path: sorted(ds) for path, ds in protected_record_hashes.items()
                      if ds != {protected_current[path]}}

supplementary = {
    'baseline_exact_aliases': base_aliases,
    'cross_pool_base_outcome_hp_round_conflicts': base_cross_conflicts,
    'cross_pool_overlap_pattern_counts': dict(Counter('|'.join(ps) for ps in memberships.values() if len(ps)>1)),
    'selection_unique_conditions': len(selection_keys), 'other_pool_unique_conditions': len(other_keys),
    'other_pool_intersection_selection': [key_json(k) for k in sorted(other_keys & selection_keys)],
    'full_unique804': unique_comparison(all_keys),
    'other_pool_unique416': unique_comparison(other_keys),
    'other_pool_excluding_selection_unique406': unique_comparison(other_keys-selection_keys),
    'key5_exact_overlap_other_pools': [key_json(k) for k in sorted(other_keys) if k[0] in key5],
    'key5_parsed_kwargs_overlap_other_pools': key5_overlap,
    'fresh56_groups': dict(Counter(tag for tags in fresh_groups.values() for tag in tags)),
    'fresh56_distinct_specs': len(fresh_groups),
    'recorded_protected_hashes': {p: sorted(ds) for p,ds in protected_record_hashes.items()},
    'recorded_protected_vs_current_mismatches': protected_mismatch,
    'all_gate_rows_including_repeats_metadata': metadata_summary(all_matched_rows),
    'other_pool_selected_log_timestamp_ranges': {n: {
        'minimum': min(re.search(r'20261031T\d{6}', candidates[n][k]['log']).group() for k in other_keys),
        'maximum': max(re.search(r'20261031T\d{6}', candidates[n][k]['log']).group() for k in other_keys)}
        for n in specs},
    'caveat': 'Filename timestamps are retained provenance, not proof of prospectivity; source version hashes do not certify complete game histories or all non-Python data dependencies.',
}


reference_sources = ['bot_research/experiments/economy/gate_vs_base.py',
    'bot_research/tmp/h14_gate.py', 'bot_research/notes/economy.md', 'bot_research/reports/REPORT.md',
    'bot_research/experiments/lead/frozen/best_v9e.py', 'bot_research/experiments/lead/v16.py',
    'bot_research/experiments/lead/v17.py', 'bot_research/experiments/lead/v18.py',
    'bot_research/experiments/lead/v19.py', 'bot_research/tests/test_best.py',
    'bot_research/experiments/lead/same_actions.py', 'td_game/engine.py',
    'bot_research/harness/match.py', str(HERE / 'economy_gate_846_review_001.py')]
for path in reference_sources:
    read(path)
changed_inputs = [p for p, v in inputs.items() if hashlib.sha256(Path(p).read_bytes()).hexdigest() != v['sha256']]
receipt = {'review': 'economy-gate-846-review-001', 'started_utc': START,
    'completed_utc': datetime.now(timezone.utc).isoformat(),
    'method': 'Independent stdlib byte parsing; no policy/engine imports or calls; exact full-spec/scenario/seat joins.',
    'inputs': inputs, 'changed_inputs_during_aggregation': changed_inputs, 'specs': specs,
    'missing_run_files': missing_files, 'candidate_error_rows': error_rows,
    'base_info': base_info, 'supplementary': supplementary, 'candidate_duplicate_audit': cand_dup, 'base_duplicate_audit': base_dup,
    'distinct_gate_conditions': len(all_keys), 'gate_pool_memberships': len(matrix),
    'cross_pool_repeated_conditions': [{'condition': key_json(k), 'pools': ps}
                                       for k, ps in memberships.items() if len(ps) > 1],
    'scenarios': dict(Counter(k[1] for k in all_keys)), 'comparisons': comparison,
    'candidate_gate_metadata': {n: metadata_summary(p for k, p in d.items() if k in all_keys)
                                for n, d in candidates.items()},
    'base_gate_metadata': metadata_summary(p for d in bases.values() for p in d.values()),
    'base_seat_summaries': {pool: seat_summary(d) for pool, d in bases.items()},
    'opponent_version_mismatches': opponent_version_mismatch, 'matrix': matrix,
}
OUT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + '\n')
print(json.dumps({k: receipt[k] for k in ('started_utc', 'completed_utc', 'missing_run_files',
    'changed_inputs_during_aggregation', 'distinct_gate_conditions', 'gate_pool_memberships', 'scenarios')}, indent=2))
print('CANDIDATES', json.dumps({n: {k: d[k] for k in ('rows','unique_conditions','extra_rows','repeated_conditions')}
                              for n,d in cand_dup.items()}, indent=2))
print('BASES', json.dumps(base_info, indent=2))
print('TOTALS', json.dumps({n: {k: d[k] for k in ('full','subset448','selection398','seat_summary_gate','extra_unique_outside_gate')}
                          for n,d in comparison.items()}, indent=2))
print('OPPONENT VERSION MISMATCHES', len(opponent_version_mismatch))
print('OUTPUT_SHA256', hashlib.sha256(OUT.read_bytes()).hexdigest())
