"""Compare the full recorded histories of the declared insurance ablation."""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.compare_feature_ablation import records
from bot_research.experiments.validation.final_validation_strict import now


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def summary(record):
    events = record['event']
    snapshot = record['snapshot']
    purchases = Counter()
    spent = 0
    for event in events:
        if event['kind'] != 'action':
            continue
        action = event['action']
        purchases[action['op']+':'+action.get('type','')] += 1
        spent += event.get('cost', 0)
    combat = next((e for e in events if e['kind'] == 'combat'), {})
    return {'round': record['round'], 'hp': snapshot['hp'], 'gold': snapshot['gold'],
            'factories': snapshot['n_factories'], 'path_length': snapshot['length_path'],
            'turrets': snapshot['n_turrets'], 'purchases': dict(purchases),
            'spent': spent, 'base_damage': combat.get('base_damage')}


def actions(record):
    return [e['action'] for e in record['event'] if e['kind'] == 'action']


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--audit', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    audit = json.loads(Path(args.audit).read_text())
    assert audit['valid_conditions'] == audit['expected_conditions'] == 24
    assert not audit['unresolved'] and not audit['repeat_disagreements']
    inputs = {args.audit: digest(args.audit)}
    index = {(c['condition']['candidate_id'],c['condition']['opponent_id'],
              c['condition']['candidate_side']):c for c in audit['cases']}
    comparisons = []
    for opponent in sorted({key[1] for key in index}):
        for side in (0,1):
            current = index[('lead7_current',opponent,side)]
            partial = index[('lead7_partial',opponent,side)]
            c = checked_row(current['result_path'],inputs)
            p = checked_row(partial['result_path'],inputs)
            cr = records(current)
            pr = records(partial)
            ci = {(r['round'],r['player']):r for r in cr}
            pi = {(r['round'],r['player']):r for r in pr}
            common = sorted(ci.keys() & pi.keys())
            changed = [k for k in common if ci[k] != pi[k]]
            action_changes = [k for k in common if actions(ci[k]) != actions(pi[k])]
            first = changed[0][0] if changed else None
            trace_rounds = sorted(set(range(0, min(12,current['rounds'],partial['rounds'])+1)) |
                                  ({first-1, first} if first is not None else set()))
            timelines = {}
            for label, rows in (('current',ci),('partial',pi)):
                timelines[label] = [{'round':rnd,'players':[summary(rows[(rnd,s)]) for s in (0,1)]}
                                    for rnd in trace_rounds if all((rnd,s) in rows for s in (0,1))]
            comparisons.append({'opponent':opponent,'side':side,'current':c,'partial':p,
                'same_complete_trajectory':c['canonical_replay_sha256']==p['canonical_replay_sha256'],
                'first_state_difference_round':first,
                'first_candidate_action_difference_round':next((k[0] for k in action_changes if k[1]==0),None),
                'first_opponent_action_difference_round':next((k[0] for k in action_changes if k[1]==1),None),
                'timelines':timelines})
    result = {'time_utc':now(),'checker_sha256':digest(__file__),'input_sha256':inputs,
              'comparisons':comparisons,
              'scope':'Whole-policy intervention from the first round, not a local round-eight action replacement. Timelines explain observed paths; they do not prove a general causal economic model.'}
    atomic_json(args.output,result,exclusive=True)
    print(json.dumps({'pairs':len(comparisons),'identical':sum(c['same_complete_trajectory'] for c in comparisons)}))


if __name__ == '__main__':
    main()
