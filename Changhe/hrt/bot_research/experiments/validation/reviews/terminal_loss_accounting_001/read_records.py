"""Read retained JSON and source bytes only. No project imports or simulations."""
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import os

OUT = Path('bot_research/experiments/validation/reviews/terminal_loss_accounting_001')
BASE = Path('bot_research/runs/validation/reserved-D-final-001')
VER = Path('bot_research/experiments/validation/analysis/terminal_reserved_validation/verification')
START = datetime.now(timezone.utc).isoformat()
inputs, issues, edge_count = {}, [], 0

def raw(path, expected=None):
    path = Path(path)
    if path.is_absolute() or '..' in path.parts:
        raise ValueError('Nonrelative evidence path')
    data = path.read_bytes()
    got = hashlib.sha256(data).hexdigest()
    if expected is not None and got != expected:
        issues.append({'path': str(path), 'issue': 'identity_mismatch', 'expected': expected, 'actual': got})
    if str(path) in inputs and inputs[str(path)]['sha256'] != got:
        issues.append({'path': str(path), 'issue': 'changed_during_read'})
    inputs[str(path)] = {'sha256': got, 'bytes': len(data)}
    return data

def load(path, expected=None):
    return json.loads(raw(path, expected))

def need(condition, text):
    if not condition:
        issues.append({'issue': text})

def edges(mapping):
    global edge_count
    for name, digest in mapping.items():
        raw(name, digest)
        edge_count += 1

strict = load(str(BASE) + '-strict.json')
replay = load(str(BASE) + '-replay.json')
loss_receipt = load(str(BASE) + '-losses.json')
for receipt in [strict, replay, loss_receipt]:
    edges(receipt['input_sha256'])
freeze = load(BASE / 'freeze.json')
supp = load(VER / 'dependency_supplement_001.json')
pre = load(VER / 'dependency_supplement_pre_d_002.json')
need(pre['seal_sha256'] == inputs[str(VER / 'dependency_supplement_001.json')]['sha256'], 'pre_d_supplement_identity')
raw(supp['declaration'], supp['declaration_sha256'])
edges(supp['source_sha256'])
for name, expected in freeze['source_sha256'].items():
    raw(BASE / 'sources' / name, expected)
need(all(supp['source_sha256'].get(k) == v for k, v in freeze['source_sha256'].items()), 'freeze_subset_of_95_pins')
# Small supplementary archives already exist; bind their explicit exact identities.
for name, value in supp['source_archive'].items():
    if isinstance(value, str):
        raw(value, supp['source_sha256'][name])
    else:
        need(False, 'unexpected_supplement_source_archive_schema')
for receipt, source in [(strict, 'audit_terminal_campaign.py'), (replay, 'summarize_reserved_replays.py'), (loss_receipt, 'diagnose_reserved_losses.py')]:
    raw(Path('bot_research/experiments/validation') / source, receipt['checker_sha256'])
raw(Path(__file__).relative_to(Path.cwd()))

jobs = load(BASE / 'jobs.json')
jobmap = {j['id']: j for j in jobs}
need(len(jobs) == len(jobmap) == len(strict['cases']) == 96, '96_distinct_jobs_cases')
auditmap = {a['job']: a for a in replay['selected_replay_receipts']}
need(len(auditmap) == 96, '96_distinct_engine_audit_receipts')
by_start = defaultdict(list)
all_hashes, cases, losses = set(), [], []
groups = defaultdict(list)
summary_rounds = summary_records = 0

for case in strict['cases']:
    job = jobmap[case['job']]
    need(load(BASE / 'jobs' / (case['job'] + '.json')) == job, 'individual_job_' + case['job'])
    result = load(case['result_path'])
    data = raw(case['replay_path'], result['trajectory_sha256'])
    records = [json.loads(line) for line in data.splitlines()]
    side = case['condition']['candidate_side']
    rounds = case['rounds']
    need(result['condition'] == job['condition'] == case['condition'], 'condition_' + case['job'])
    need(len(records) == 2 * (rounds + 1), 'record_count_' + case['job'])
    index = {(r['round'], r['player']): r for r in records}
    need(len(index) == len(records) and set(index) == {(r, p) for r in range(rounds + 1) for p in (0, 1)}, 'record_coordinates_' + case['job'])
    need(not any(result['bot_errors']) and not any(result['rejected_actions']) and not result['source_changed_during_match'], 'result_errors_' + case['job'])
    for field in ('source_sha256', 'source_sha256_at_end'):
        need(all(freeze['source_sha256'].get(k) == v for k, v in result[field].items()), 'loaded_source_identity_' + field + '_' + case['job'])
    accepted = [Counter(), Counter()]
    final_hp = [index[(rounds, p)]['snapshot']['hp'] for p in (0, 1)]
    need(final_hp == result['hp'] and final_hp[::1 if side == 0 else -1] == case['hp_candidate_first'], 'final_hp_' + case['job'])
    expected_outcome = 'D' if result['result']['winner'] is None else ('W' if result['result']['winner'] == side else 'L')
    need(expected_outcome == result['candidate_outcome'] == case['outcome'], 'outcome_' + case['job'])
    timeline, damages = [], []
    for rnd in range(1, rounds + 1):
        rh = {'round': rnd, 'players': []}
        for p in (0, 1):
            record = index[(rnd, p)]
            snap, events = record['snapshot'], record['event']
            old = index[(rnd - 1, p)]['snapshot']
            actions = [e for e in events if e['kind'] == 'action']
            need(all(e['accepted'] for e in actions) and not any(e['kind'] == 'bot_error' for e in events), 'raw_errors_' + case['job'] + '_' + str(rnd))
            for event in actions:
                accepted[p][event['action']['op'] + ':' + event['action'].get('type', '')] += 1
            combat = [e for e in events if e['kind'] == 'combat']
            income = [e for e in events if e['kind'] == 'income']
            need(len(combat) == len(income) == 1, 'one_combat_income_' + case['job'])
            combat, income = combat[0], income[0]
            spent = sum(e.get('cost', 0) for e in actions)
            rules = result['rules']['globals']
            need(old['gold'] - spent + income['total'] == snap['gold'], 'gold_' + case['job'] + '_' + str(rnd))
            need(old['hp'] - combat['base_damage'] == snap['hp'], 'hp_' + case['job'] + '_' + str(rnd))
            need(income['factories'] == rules['factory_income'] * snap['n_factories'] and income['path'] == rules['path_income_per_step'] * snap['length_path'] and income['hits'] == rules['base_hit_bounty'] * combat['outgoing_hits'] and income['total'] == sum(income[k] for k in ('factories', 'path', 'hits')), 'income_' + case['job'] + '_' + str(rnd))
            need(old['n_factories'] + sum(e['action']['op'] == 'buy_factory' for e in actions) == snap['n_factories'], 'factory_count_' + case['job'] + '_' + str(rnd))
            summary = {k: snap[k] for k in ('hp', 'gold', 'n_factories', 'n_turrets', 'n_walls', 'length_path')}
            summary.update(roster=dict(Counter(e['type'] for e in snap['roster'])), combat=combat, income=income)
            rh['players'].append(summary)
            if case['outcome'] == 'L':
                role = p ^ side
                if combat['base_damage']:
                    damages.append({'round': rnd, 'role': role, 'damage': combat['base_damage'], 'incoming_hits': combat['incoming_hits'], 'hp_after': snap['hp'], 'prescribed': rnd <= len(job.get('prefixes', [[], []])[p])})
                if rnd in (1, 2, 3, 33, 34, 35):
                    timeline.append({'round': rnd, 'role': role, 'before': {k: old[k] for k in ('hp', 'gold', 'n_factories', 'n_turrets', 'n_walls', 'length_path')}, 'before_roster': dict(Counter(e['type'] for e in old['roster'])), 'actions_grouped': dict(Counter(json.dumps(e['action'], sort_keys=True, separators=(',', ':')) for e in actions)), 'actions_count': len(actions), 'accepted_count': sum(e['accepted'] for e in actions), 'gold_spent': spent, 'gold_after_purchases': old['gold'] - spent, 'after': summary, 'building_types_after': dict(Counter(e['type'] for e in snap['buildings'])), 'expiration_count': sum(len(e['roster_ids']) for e in events if e['kind'] == 'expiration')})
        need(rh == result['history'][rnd - 1], 'full_summary_' + case['job'] + '_' + str(rnd))
    need([dict(a) for a in accepted] == result['accepted_actions'], 'accepted_action_totals_' + case['job'])
    # Reproduce the declared JSON normalization without importing its implementation.
    for record in records:
        record.pop('match', None)
        record['player'] ^= side
        record['snapshot']['name'] = 'counter' if record['player'] == 0 else 'opponent'
        for event in record['event']:
            event.pop('order', None)
        if 'result' in record and record['result']['winner'] is not None:
            record['result']['winner'] ^= side
    records.sort(key=lambda r: (r['round'], r['player']))
    canonical = hashlib.sha256(json.dumps(records, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    need(canonical == case['canonical_replay_sha256'], 'canonical_digest_' + case['job'])
    audit = load(auditmap[case['job']]['audit_path'])
    edges(audit['input_sha256'])
    edges(audit['source_sha256'])
    need(audit['all_passed'] and audit['count'] == 1 and not audit['source_changed_during_run'], 'prior_engine_audit_' + case['job'])
    ac = audit['cases'][0]
    need(ac['passed'] and ac['trajectory_sha256'] == result['trajectory_sha256'] and ac['rounds'] == rounds and ac['records'] == len(records) and ac['condition'] == case['condition'], 'prior_engine_audit_binding_' + case['job'])
    cr = {'job': case['job'], 'scenario': case['condition']['scenario'], 'candidate_side': side, 'outcome': case['outcome'], 'rounds': rounds, 'hp_candidate_first': case['hp_candidate_first'], 'canonical_sha256': canonical, 'raw_sha256': result['trajectory_sha256']}
    cases.append(cr)
    by_start[cr['scenario']].append(cr)
    groups[(cr['scenario'], canonical)].append(case['job'])
    all_hashes.add(canonical)
    summary_rounds += rounds
    summary_records += len(records)
    if case['outcome'] == 'L':
        losses.append(dict(cr, condition=case['condition'], timeline=sorted(timeline, key=lambda r: (r['round'], r['role'])), damage_events=sorted(damages, key=lambda r: (r['round'], r['role'])), prefix_lengths_candidate_first=job['condition']['prefix_lengths_candidate_first'], bot_errors=result['bot_errors'], rejected_actions=result['rejected_actions']))

need({c['job'] for c in losses} == {c['job'] for c in loss_receipt['losses']}, 'loss_receipt_job_set')
need(len(all_hashes) == strict['distinct_canonical_trajectories'] == 44, 'distinct_44')
need(len({c['canonical_sha256'] for c in losses}) == 1, 'losses_one_canonical')
source_final_drift = []
for name, data in list(inputs.items()):
    if hashlib.sha256(Path(name).read_bytes()).hexdigest() != data['sha256']:
        source_final_drift.append(name)
need(not source_final_drift, 'end_input_drift')
output = {'started_utc': START, 'completed_utc': datetime.now(timezone.utc).isoformat(), 'reviewer_model': 'GPT-6 Astra', 'execution': {'cpu_affinity': sorted(os.sched_getaffinity(0)), 'nice': os.getpriority(os.PRIO_PROCESS, 0), 'project_imports': 0, 'policy_calls': 0, 'Engine_calls': 0, 'replay_calls': 0, 'existing_checker_calls': 0}, 'scope': 'Source and retained JSON read-only accounting. Existing engine replay receipts authenticated, not rerun. Fresh entry-point and terminal postchecks are outside this review.', 'issues': issues, 'input_edges_verified': edge_count, 'unique_inputs': len(inputs), '95_current_source_pins_verified': len(supp['source_sha256']), '79_campaign_source_archives_verified': len(freeze['source_sha256']), 'supplement_source_archives_verified': len(supp['source_archive']), 'rounds_compared': summary_rounds, 'records_compared': summary_records, 'cases': cases, 'distinct_complete_canonical_histories': len(all_hashes), 'by_start': {name: {'conditions': len(rows), 'distinct_histories': len({r['canonical_sha256'] for r in rows}), 'outcomes': dict(Counter(r['outcome'] for r in rows))} for name, rows in sorted(by_start.items())}, 'duplicate_groups_above_one_physical_pair': [dict(scenario=sc, canonical_sha256=h, jobs=ids) for (sc,h),ids in sorted(groups.items()) if len(ids)>2], 'losses': losses, 'final_input_drift': source_final_drift}
for path, obj in [(OUT/'input_manifest_001.json', {'time_utc': output['completed_utc'], 'files': inputs}), (OUT/'record_accounting_001.json', output)]:
    with path.open('x') as stream:
        json.dump(obj, stream, sort_keys=True, indent=2, allow_nan=False)
        stream.write('\n')
print(json.dumps({k: output[k] for k in ('started_utc','completed_utc','issues','unique_inputs','rounds_compared','records_compared','distinct_complete_canonical_histories','by_start','duplicate_groups_above_one_physical_pair')}, sort_keys=True))
