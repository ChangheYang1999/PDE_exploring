"""Publish the declared screened-guard transfer and matched controls."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
from bot_research.experiments.validation.artifact_io import atomic_json

E = Path('bot_research/experiments/validation')
R = Path('bot_research/runs/validation')
A = E / 'analysis/screened_guard_transfer'
RANK = {'L': 0, 'D': 1, 'W': 2}


def main():
    inputs = {}
    def read(path):
        path = Path(path)
        inputs[str(path)] = hashlib.sha256(path.read_bytes()).hexdigest()
        return json.loads(path.read_text())
    declared = read(E / 'screened-guard-transfer-campaigns-001.json')
    for p, h in declared['input_sha256'].items():
        assert hashlib.sha256(Path(p).read_bytes()).hexdigest() == h
        inputs[p] = h
    rows = []
    calls = 0
    paired = []
    for campaign in declared['campaigns']:
        name = campaign['name']
        expected = campaign['expected']
        audits = {k: read(R / (name + '-' + k + '.json'))
                  for k in ('strict', 'replay', 'summary', 'data', 'fresh')}
        strict, fresh = audits['strict'], audits['fresh']
        assert strict['valid_conditions'] == expected
        assert strict['attempt_counts'] == {'valid': expected}
        assert not strict['unresolved'] and not strict['repeat_disagreements']
        assert audits['replay']['all_passed'] and audits['data']['all_passed']
        assert fresh['exact_policy_reproduction']
        assert fresh['all_observations_unchanged'] and fresh['all_fresh_actions_legal']
        assert len(fresh['cases']) == expected
        calls += sum(sum(map(len, x['decision_seconds'])) for x in fresh['cases'])
        paired.extend(strict['pairs'])
        for case in strict['cases']:
            row = read(case['result_path'])
            side = row['condition']['candidate_side']
            hp = row['hp'][::1 if side == 0 else -1]
            rows.append(dict(candidate=row['condition']['candidate_id'],
                opponent=row['condition']['opponent_id'], side=side,
                outcome=row['candidate_outcome'], hp=hp, rounds=row['rounds'],
                decision_seconds=row['decision_seconds'][side], result=case['result_path']))
    assert len(rows) == declared['new_games'] == 24
    lookup = {(r['candidate'], r['opponent'], r['side']): r for r in rows}
    comparisons = []
    for opponent in declared['opponent_ids']:
        for side in (0, 1):
            g = lookup['guard', opponent, side]
            u = lookup['control', opponent, side]
            comparisons.append(dict(opponent=opponent, side=side,
                guarded_outcome=g['outcome'], control_outcome=u['outcome'],
                rank_difference=RANK[g['outcome']] - RANK[u['outcome']]))
    h1 = all(lookup['guard', 'AS1C', s]['outcome'] == 'W' for s in (0, 1))
    h2 = all(c['rank_difference'] >= 0 for c in comparisons)
    now = datetime.now(timezone.utc).isoformat()
    result = dict(time_utc=now, new_games=24, fresh_policy_calls=calls,
        h1='CONFIRMED' if h1 else 'REFUTED', h2='CONFIRMED' if h2 else 'REFUTED',
        comparisons=comparisons, rows=rows, assignment_pairs=paired,
        all_assignment_histories_equal=all(p['same_complete_trajectory'] for p in paired),
        input_sha256=inputs, scope='Selected development transfer; no pool D use.')
    assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest() == h for p, h in inputs.items())
    atomic_json(A / 'verification/full_check.json', result, exclusive=True)
    lines = ['# Screened-guard transfer', '', f'Completed {now}.', '',
        f'H1, the guard wins both AS1C assignments: **{result["h1"]}**. '
        f'H2, the guard never worsens W/D/L relative to its matched control: **{result["h2"]}**.', '',
        '| Opponent | Guard, seat 0 | Control, seat 0 | Guard, seat 1 | Control, seat 1 |',
        '| --- | --- | --- | --- | --- |']
    for opponent in declared['opponent_ids']:
        cells = []
        for side in (0, 1):
            for candidate in ('guard', 'control'):
                r = lookup[candidate, opponent, side]
                cells.append(f"{r['outcome']} {r['hp'][0]}:{r['hp'][1]} r{r['rounds']}")
        lines.append('| ' + opponent + ' | ' + ' | '.join(cells) + ' |')
    lines += ['', f'All 24 new games pass strict accounting, original-engine replay, source/archive checks and {calls} fresh policy calls. '
        f'{sum(p["same_complete_trajectory"] for p in paired)} of {len(paired)} assignment pairs have identical normalized histories.', '',
        'The opponent set and both policies were fixed before these games. The guard was selected against best_v9e earlier; this transfer set consists of known development finalists and a newly proposed attack-budget variant. '
        'It does not estimate performance against an untouched opponent distribution. Final best.py and pool D are unchanged. '
        'The Fortress search includes a wall-clock cutoff, so exact reproduction here does not promise timing-invariant behavior on other runs.', '']
    with (A / 'RESULTS.md').open('x') as stream:
        stream.write('\n'.join(lines))
    counts = {c: Counter(r['outcome'] for r in rows if r['candidate'] == c) for c in ('guard', 'control')}
    with Path('bot_research/notes/validation.md').open('a') as stream:
        stream.write(f'\n## {now}: Screened-guard transfer complete\n\n'
            f'Claim and verdict: both AS1C wins {result["h1"]}; no W/D/L regression against matched controls {result["h2"]}. '
            f'Method: 24 declared new games, both assignments, complete replay and {calls} fresh policy calls. '
            f'Result: guard {dict(counts["guard"])}, control {dict(counts["control"])}. '
            'The full per-opponent table and limitations are in experiments/validation/analysis/screened_guard_transfer/RESULTS.md. '
            'These games are separate from the lead\'s H14 gate and do not modify the selected final bot or reserved D.\n')
    print(json.dumps({k: result[k] for k in ('time_utc', 'new_games', 'fresh_policy_calls', 'h1', 'h2')}))

if __name__ == '__main__':
    main()
