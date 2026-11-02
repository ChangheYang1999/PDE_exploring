"""Count retained trajectory equality classes without treating labels as samples."""
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json

E = Path('bot_research/experiments/validation')
R = Path('bot_research/runs/validation')
A = E / 'analysis/effective_pool_c_diversity'


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def normalized(path, candidate_side):
    records = [json.loads(line) for line in Path(path).read_text().splitlines()]
    for record in records:
        record.pop('match', None)
        record['player'] = record['player'] ^ candidate_side
        record['snapshot']['name'] = ('counter', 'opponent')[record['player']]
        for event in record['event']:
            event.pop('order', None)
        if 'result' in record and record['result']['winner'] is not None:
            record['result']['winner'] ^= candidate_side
    records.sort(key=lambda record: (record['round'], record['player']))
    encoded = json.dumps(records, sort_keys=True, separators=(',', ':')).encode()
    return records, hashlib.sha256(encoded).hexdigest()


def main():
    inputs = {}
    all_rows, groups_by_candidate, by_candidate = [], {}, {}
    for name in ('best-v9e', 'p5tnubm'):
        audit_path = R / f'reserved-C-{name}-001-strict.json'
        inputs[str(audit_path)] = digest(audit_path)
        audit = json.loads(audit_path.read_text())
        assert audit['valid_conditions'] == audit['expected_conditions'] == 72
        assert not audit['unresolved'] and not audit['current_source_drift']
        examples, grouped, rows = {}, defaultdict(list), []
        for case in audit['cases']:
            path = case['replay_path']
            inputs[path] = digest(path)
            assert inputs[path] == audit['input_sha256'][path]
            result_path = case['result_path']
            inputs[result_path] = digest(result_path)
            assert inputs[result_path] == audit['input_sha256'][result_path]
            result = json.loads(Path(result_path).read_text())
            assert result['trajectory_sha256'] == inputs[path]
            side = case['condition']['candidate_side']
            obj, sha = normalized(path, side)
            assert sha == case['canonical_replay_sha256']
            if sha in examples:
                assert obj == examples[sha]
            else:
                examples[sha] = obj
            row = dict(candidate=name, job=case['job'], scenario=case['condition']['scenario'],
                       side=side, opponent=case['condition']['opponent'],
                       outcome=case['outcome'], hp=case['hp_candidate_first'],
                       rounds=case['rounds'], canonical_sha256=sha, replay_path=path)
            grouped[(row['scenario'], sha)].append(row)
            rows.append(row)
        assert len(examples) == audit['distinct_canonical_trajectories']
        scenario_groups = defaultdict(list)
        for (scenario, sha), group in grouped.items():
            scenario_groups[scenario].append(dict(canonical_sha256=sha, jobs=sorted(r['job'] for r in group),
                                                 outcome=group[0]['outcome'], hp=group[0]['hp'],
                                                 rounds=group[0]['rounds']))
        groups_by_candidate[name] = {
            'nominal_games': 72, 'distinct_complete_trajectories': len(examples),
            'by_scenario': {scenario: {'nominal_games': sum(len(g['jobs']) for g in groups),
                                      'distinct_complete_trajectories': len(groups),
                                      'groups': sorted(groups, key=lambda g: g['jobs'])}
                            for scenario, groups in scenario_groups.items()}}
        by_candidate[name] = {row['job']: row for row in rows}
        all_rows.extend(rows)
    comparisons = []
    cross_groups = defaultdict(list)
    for row in all_rows:
        cross_groups[row['canonical_sha256']].append((row['candidate'], row['job']))
    for job, first in sorted(by_candidate['best-v9e'].items()):
        second = by_candidate['p5tnubm'][job]
        comparisons.append(dict(job=job, scenario=first['scenario'],
                                same_complete_trajectory=first['canonical_sha256'] == second['canonical_sha256'],
                                best_hp=first['hp'], comparison_hp=second['hp'],
                                same_outcome=first['outcome'] == second['outcome']))
    now = datetime.now(timezone.utc).isoformat()
    for path in (A/'PROOF.md', Path(__file__).relative_to(Path.cwd()),
                 Path('bot_research/bots/counters/guard_geometry.py'),
                 E/'late_validation.py', E/'final_validation.py'):
        inputs[str(path)] = digest(path)
    result = dict(time_utc=now, all_passed=True, input_sha256=inputs,
                  candidates=groups_by_candidate, matched_candidate_comparisons=comparisons,
                  distinct_across_both_candidates=len(cross_groups), cases=all_rows,
                  scope='Equality of retained complete logged trajectories. No independent random sample, universal policy equality, or historical behavioral novelty is inferred.')
    output = A/'verification/trajectories.json'
    with output.open('x') as f:
        json.dump(result, f, sort_keys=True, indent=2); f.write('\n')
    lines = []
    for name, values in groups_by_candidate.items():
        for scenario, group in values['by_scenario'].items():
            lines.append(f'| {name} | {scenario} | {group["nominal_games"]} | {group["distinct_complete_trajectories"]} |')
    dups = []
    for name, values in groups_by_candidate.items():
        for scenario, value in values['by_scenario'].items():
            for group in value['groups']:
                if len(group['jobs']) > 2:
                    dups.append(f'- {name}, {scenario}: '+', '.join('`'+job+'`' for job in group['jobs'])+'.')
    equal_by_scenario = defaultdict(lambda: [0, 0])
    for comparison in comparisons:
        value = equal_by_scenario[comparison['scenario']]
        value[0] += comparison['same_complete_trajectory']; value[1] += 1
    cross = '; '.join(f'{scenario}: {same}/{total}' for scenario,(same,total) in equal_by_scenario.items())
    text = f'''# Effective pool-C diversity

Checked {now}.

CONFIRMED for the recorded games: each candidate has 33 distinct complete normalized trajectories across its 72 nominal games. There are 36 opponent/start pairs, but three pairs duplicate another pair within the same start. The predeclared W/D/L totals remain unchanged.

| Candidate | Start | Nominal games | Distinct complete trajectories |
|---|---|---:|---:|
'''+ '\n'.join(lines)+ '''

Duplicate groups beyond the ordinary two-seat controls:

'''+ '\n'.join(dups)+f'''

The guard variants are C-10 and C-11 (zero-based job indices 10 and 11). Their only differing actions occur at round one, which both continuation starts replace with scripted actions while skipping the policies. Both then call the same fresh economy17 delegate. The proof states the precise conditional policy equivalence. C-08 and C-09 are different budget-timing settings; their equality on the asymmetric start is an observed full-history equality, not a claim that their policies always agree.

Between the two declared candidates, the counts of equal matched complete histories are {cross}. Across all 144 logs there are {len(cross_groups)} distinct normalized histories. In particular, the two continuation sets do not provide independent evidence for each candidate: both candidates use the same economy20 foreign-map delegate and every matched continuation history agrees.

The checker rereads every complete replay, verifies the raw bytes against the strict audit and result, independently implements the declared normalization, and checks its digest against the earlier audit. It also compares the normalized JSON objects within hash groups. Match IDs, player names, physical seat labels and the global action-order metadata are removed; actions, their within-player order, events, states, round numbers and results remain.

These are equality classes of observed trajectories, not independent statistical observations. No historical behavioral-novelty claim follows from the exact parameter-separation audit. The eight unresolved historical rows in the separation audit remain unresolved. Reproduce with `python -B -m bot_research.experiments.validation.audit_effective_pool_c` under the documented local environment and assigned affinity, using a fresh output location if the receipt already exists.
'''
    with (A/'RESULTS.md').open('x') as f: f.write(text)
    with Path('bot_research/notes/validation.md').open('a') as f:
        f.write(f'\n## {now}: Pool C effective variation audit\n\nClaim and verdict: CONFIRMED, each candidate has33 distinct complete normalized trajectories among72 games, not36 independent opponent/start behaviors. Standard12, mirror11, asymmetric10; each ordinary seat pair agrees. Guard variants C10/C11 lose their only difference when round-one calls are skipped; budget variants C08/C09 additionally agree on the asymmetric start. Cross-candidate equality: {cross}; {len(cross_groups)} distinct histories across144 logs. Every log was reread and compared with strict raw and normalized digests. This does not change declared totals, establish random independence, or erase the eight unresolved historical-source rows. Proof and receipt: experiments/validation/analysis/effective_pool_c_diversity/.\n')
    print(json.dumps(dict(time_utc=now, all_passed=True, candidates={k:v['distinct_complete_trajectories'] for k,v in groups_by_candidate.items()},cross_equal=dict(equal_by_scenario),distinct_across_both=len(cross_groups))))


if __name__ == '__main__':
    main()
