"""Summarize fixed-order continuation tests only after independent checks."""
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json

from bot_research.experiments.validation.artifact_io import atomic_json

E = Path('bot_research/experiments/validation')
R = Path('bot_research/runs/validation')
A = E / 'analysis/screened_roster_continuation'
ORDERS = {'screen': ['tier2', 'tier2', 'tier3'],
          'middle': ['tier2', 'tier3', 'tier2'],
          'front': ['tier3', 'tier2', 'tier2']}


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(records, side):
    values = deepcopy(records)
    for row in values:
        row.pop('match', None)
        row['player'] ^= side
        row['snapshot']['name'] = 'counter' if row['player'] == 0 else 'target'
        for event in row['event']:
            event.pop('order', None)
        if 'result' in row and row['result']['winner'] is not None:
            row['result']['winner'] ^= side
    return sorted(values, key=lambda r: (r['round'], r['player']))


def main():
    declaration = E / 'screened-roster-continuation-campaigns-001.json'
    declared = json.loads(declaration.read_text())
    inputs = {str(declaration): digest(declaration)}
    for p, h in declared['input_sha256'].items():
        assert digest(p) == h, p
    inputs.update(declared['input_sha256'])
    rows, prefixes, target_actions = [], [], []
    fresh_calls = 0
    for campaign in declared['campaigns']:
        name = campaign['name']
        audits = {}
        for kind in ('strict', 'replay', 'summary', 'data', 'fresh'):
            path = R / (name + '-' + kind + '.json')
            inputs[str(path)] = digest(path)
            audits[kind] = json.loads(path.read_text())
        strict, fresh = audits['strict'], audits['fresh']
        assert strict['valid_conditions'] == strict['expected_conditions'] == 6
        assert strict['attempt_counts'] == {'valid': 6}
        assert all(p['same_complete_trajectory'] for p in strict['pairs'])
        assert audits['replay']['all_passed'] and audits['data']['all_passed']
        assert fresh['exact_policy_reproduction']
        fresh_calls += sum(sum(len(x) for x in c['decision_seconds']) for c in fresh['cases'])
        for case in strict['cases']:
            path = Path(case['result_path'])
            inputs[str(path)] = digest(path)
            row = json.loads(path.read_text())
            replay = Path(row['replay_path'])
            assert digest(replay) == row['trajectory_sha256']
            inputs[str(replay)] = digest(replay)
            side = row['condition']['candidate_side']
            records = canonical([json.loads(s) for s in replay.read_text().splitlines()], side)
            prefixes.append(records[:12])
            assert row['rounds'] >= 6
            pair = records[12:14]
            actions = [[e['action'] for e in p['event'] if e['kind'] == 'action'] for p in pair]
            order = row['condition']['candidate_id'].split('_')[-1]
            expected = [{'op': 'buy_minion', 'type': tier} for tier in ORDERS[order]]
            assert actions[0] == expected
            target_actions.append(actions[1])
            before = [p['snapshot']['hp'] for p in records[10:12]]
            after = [p['snapshot']['hp'] for p in pair]
            assert before == [800, 800]
            assert after == [774, 774 if order == 'screen' else 800]
            hp = row['hp'][::1 if side == 0 else -1]
            rows.append(dict(continuation=campaign['continuation'], order=order, side=side,
                outcome=row['candidate_outcome'], hp=hp, margin=hp[0]-hp[1], rounds=row['rounds'],
                round6_hp=after, result=str(path), replay=str(replay)))
    assert len(rows) == 18
    assert all(p == prefixes[0] for p in prefixes)
    assert all(a == target_actions[0] for a in target_actions)
    witness = R / 'affordable-roster-coverage-001/witnesses/standard-02-side0-r6.jsonl'
    inputs[str(witness)] = digest(witness)
    original = canonical([json.loads(s) for s in witness.read_text().splitlines()], 1)
    assert original[:12] == prefixes[0]
    assert [e['action'] for e in original[13]['event'] if e['kind'] == 'action'] == target_actions[0]
    bykey = {(r['continuation'], r['order'], r['side']): r for r in rows}
    continuations = [c['continuation'] for c in declared['campaigns']]
    h1 = any(all(bykey[c, 'screen', s]['outcome'] == 'W' for s in (0, 1)) for c in continuations)
    comparisons = [dict(continuation=c, side=s, control=o,
        screen_margin=bykey[c, 'screen', s]['margin'], control_margin=bykey[c, o, s]['margin'],
        strictly_better=bykey[c, 'screen', s]['margin'] > bykey[c, o, s]['margin'])
        for c in continuations for s in (0, 1) for o in ('middle', 'front')]
    h2 = all(r['strictly_better'] for r in comparisons)
    assert all(digest(p) == h for p, h in inputs.items())
    stamp = datetime.now(timezone.utc).isoformat()
    result = dict(time_utc=stamp, input_sha256=inputs, games=18, assignment_pairs=9,
        fresh_policy_calls=fresh_calls, h1='CONFIRMED' if h1 else 'REFUTED',
        h2='CONFIRMED' if h2 else 'REFUTED', rows=rows, comparisons=comparisons,
        common_round1_to5_prefix=True, common_round6_target_actions=True,
        exact_round6_order_effect=True, original_witness_prefix_matched=True,
        scope='Selected development conditions, not a holdout or general best-response statement.')
    atomic_json(A/'verification/full_check.json', result, exclusive=True)
    lines = ['# Screened roster continuation results', '', f'Completed {stamp}.', '',
        f"H1 (a screened complete policy wins both seats): **{result['h1']}**. "
        f"H2 (screened order strictly improves final HP margin for every continuation): **{result['h2']}**.", '',
        f'All18 games completed with zero failed or invalid attempts. Strict accounting, original-engine replay, '
        f'source archives and {fresh_calls} fresh policy calls pass. All nine assignment pairs have identical '
        'normalized histories. Every round1-5 history and every target round6 action is identical across the18 games '
        'and matches the original selected C02 witness.', '',
        'Round6 always leaves the counter at774HP. The target is at774HP after the screened order and800HP '
        'after either control ordering. The equal-cost order intervention therefore has the predicted immediate effect.', '',
        '| Continuation | Order | Counter outcome | Final HP | Round |',
        '| --- | --- | --- | --- | --- |']
    for row in rows:
        if row['side'] == 0:
            lines.append(f"| {row['continuation']} | {row['order']} | {row['outcome']} | {row['hp'][0]}:{row['hp'][1]} | {row['rounds']} |")
    lines += ['', 'Both seats agree on every table entry. Later outcomes include the opponent response and '
        'continuation behavior; the one-round ordering effect alone does not determine the winner. These are '
        'selected development tests, and no terminal D condition was used. The frozen Fortress38 planner retains '
        'a wall-clock cutoff even though all fresh calls reproduced in this finite check.', '',
        'See PROOF.md, the exact manifests and verification/full_check.json for scope, inputs and comparisons.', '']
    with (A/'RESULTS.md').open('x') as f:
        f.write('\n'.join(lines))
    with Path('bot_research/notes/validation.md').open('a') as f:
        f.write(f"\n## {stamp}: Screened-roster continuation complete\n\nClaim: a complete counter converts the omitted-order leak into a win (H1), and the screened order improves every continuation's final HP margin (H2). Method: three equal-cost orders, three fixed continuations, both seats,18new games; full original-engine replay and {fresh_calls} fresh policy calls. Result: all checks pass, shared prefixes and round6 actions match, round6target damage26versus0. Verdict: H1{result['h1']}, H2{result['h2']}. All nine paired outcomes are in experiments/validation/analysis/screened_roster_continuation/RESULTS.md. This is selected development evidence; best.py and D remain unchanged.\n")
    print(json.dumps({k: result[k] for k in ('time_utc', 'games', 'fresh_policy_calls', 'h1', 'h2')}))


if __name__ == '__main__':
    main()
