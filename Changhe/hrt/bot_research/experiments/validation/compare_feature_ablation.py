"""Compare a feature intervention with unchanged-policy repeat controls."""
from __future__ import annotations
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def records(case):
    side = case['condition']['candidate_side']
    rows = [json.loads(line) for line in Path(case['replay_path']).read_text().splitlines()]
    for row in rows:
        row.pop('match', None)
        row['player'] ^= side
        row['snapshot']['name'] = 'counter' if row['player'] == 0 else 'opponent'
        for event in row['event']:
            event.pop('order', None)
        if row.get('result', {}).get('winner') is not None:
            row['result']['winner'] ^= side
    return sorted(rows, key=lambda row: (row['round'], row['player']))


def action_summary(row):
    actions = [event['action'] for event in row['event'] if event['kind'] == 'action']
    return {'actions': actions,
            'minions': dict(Counter(a['type'] for a in actions if a['op'] == 'buy_minion')),
            'factories_purchased': sum(a['op'] == 'buy_factory' for a in actions),
            'ending_gold': row['snapshot']['gold'],
            'ending_factories': row['snapshot']['n_factories'],
            'ending_hp': row['snapshot']['hp']}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bluff', required=True)
    parser.add_argument('--ablation', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    original = json.loads(Path(args.bluff).read_text())
    ablated = json.loads(Path(args.ablation).read_text())
    assert original['valid_conditions'] == 20 and not original['unresolved']
    assert ablated['valid_conditions'] == 24 and not ablated['unresolved']
    def index(audit):
        return {(c['condition']['candidate_id'], c['condition']['opponent_id'],
                 c['condition']['candidate_side']): c for c in audit['cases']}
    old, new = index(original), index(ablated)
    repeats = []
    interventions = []
    used = set()
    for (name, opponent, side), case in new.items():
        if opponent != 'guard_normal':
            continue
        control = old[(name, 'guard_economy13', side)]
        same = records(control) == records(case)
        assert same, (name, side)
        repeats.append({'candidate': name, 'side': side, 'same_complete_trajectory': same,
                        'original': control['replay_path'], 'repeat': case['replay_path']})
        used.update((control['replay_path'], case['replay_path']))
        if name not in ('off_route_r3_eco6', 'useful_r3_eco6'):
            continue
        ignored = new[(name, 'guard_ignore_turret_signal', side)]
        normal_rows, ignored_rows = records(case), records(ignored)
        before = [r for r in normal_rows if r['round'] <= 3]
        assert before == [r for r in ignored_rows if r['round'] <= 3]
        normal_by_key = {(r['round'], r['player']): r for r in normal_rows}
        ignore_by_key = {(r['round'], r['player']): r for r in ignored_rows}
        differences = sorted(k for k in normal_by_key.keys() & ignore_by_key.keys()
                             if normal_by_key[k] != ignore_by_key[k])
        assert differences[0] == (4, 0) or differences[0] == (4, 1)
        # The actual opponent policy actions first differ in round four.
        first_action_difference = next(r for r in range(1, 8)
            if action_summary(normal_by_key[(r, 1)])['actions'] !=
               action_summary(ignore_by_key[(r, 1)])['actions'])
        assert first_action_difference == 4
        interventions.append({'candidate': name, 'side': side,
            'identical_real_history_through_round': 3,
            'first_opponent_action_difference_round': first_action_difference,
            'normal_outcome': case['outcome'], 'normal_hp': case['hp_candidate_first'],
            'ignore_feature_outcome': ignored['outcome'],
            'ignore_feature_hp': ignored['hp_candidate_first'],
            'round4_normal_guard': action_summary(normal_by_key[(4, 1)]),
            'round4_ignore_feature_guard': action_summary(ignore_by_key[(4, 1)])})
        used.add(ignored['replay_path'])
    assert len(repeats) == 8 and len(interventions) == 4
    used.update((args.bluff, args.ablation))
    output = {'time_utc': datetime.now(timezone.utc).isoformat(),
              'checker_sha256': digest(__file__),
              'input_sha256': {p: digest(p) for p in sorted(used)},
              'repeat_controls': repeats, 'feature_interventions': interventions,
              'interpretation': 'These matched policy interventions isolate the ignored public '
                 'turret-count signal while holding real history through round three fixed. '
                 'They are development conditions. Ignoring a feature is a different policy; '
                 'neither real game state nor engine observations were altered.'}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({'repeat_controls': len(repeats), 'matched_interventions': len(interventions),
                      'all_passed': True}))


if __name__ == '__main__':
    main()
