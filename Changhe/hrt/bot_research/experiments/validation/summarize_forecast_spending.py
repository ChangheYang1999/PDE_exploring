"""Describe accepted attack spending and hits on replay-verified forecast histories."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json

from td_game.config import balanced_config
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--histories', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    digest = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
    path = Path(args.histories)
    histories = json.loads(path.read_text())
    for key in ('all_replayed', 'all_observations_unchanged', 'all_fresh_actions_legal',
                'exact_counter_policy_reproduction', 'no_internal_rejections'):
        assert histories[key], key
    hashes = dict(histories['input_sha256'])
    hashes[str(path)] = digest(path)
    for p in static_closure({'bot_research.experiments.validation.summarize_forecast_spending'}):
        if str(p) in hashes:
            assert hashes[str(p)] == digest(p)
        hashes[str(p)] = digest(p)
    cfg = balanced_config()
    cases = []
    for case in histories['cases']:
        condition = case['condition']
        assert condition['candidate_id'] == 'P5TNUB'
        assert not case['policy_action_differences']
        assert not case['model_action_differences']
        assert not case['model_purchase_difference_rounds']
        row_path = Path(case['result'])
        assert str(row_path) in hashes
        row = json.loads(row_path.read_text())
        rounds = case['rounds']
        assert len(rounds) == row['rounds']
        post = [r for r in rounds if r['switched']]
        assert post
        handoff = post[0]['round']
        assert [r['round'] for r in post] == list(range(handoff, row['rounds']+1))
        sequence = []
        for r in post:
            purchases = r['actual_target_purchases']
            count = Counter(a['type'] for a in purchases)
            cost = sum(cfg.minions[a['type']].cost for a in purchases)
            assert cost == r['actual_target_purchase_cost']
            sequence.append(dict(round=r['round'], purchase_counts=dict(count),
                attack_cost=cost, defense_cost=r['defense_cost'],
                incoming_damage=r['actual_counter_incoming_damage'],
                counter_hp_after=r['actual_counter_hp_after'],
                target_hp_after=r['actual_target_hp_after']))
        cases.append(dict(condition=condition, result=case['result'],
            rounds=row['rounds'], target_outcome=('D' if row['result']['winner'] is None
                else 'W' if row['result']['winner'] == condition['candidate_side'] else 'L'),
            target_counter_hp=[row['hp'][condition['candidate_side']],
                               row['hp'][1-condition['candidate_side']]],
            handoff_round=handoff,
            post_handoff_zero_damage=all(r['incoming_damage'] == 0 for r in sequence),
            total_post_handoff_attack_cost=sum(r['attack_cost'] for r in sequence),
            total_post_handoff_defense_cost=sum(r['defense_cost'] for r in sequence),
            purchase_rounds=[r['round'] for r in sequence if r['attack_cost']],
            purchased_copy_count=sum(sum(r['purchase_counts'].values()) for r in sequence),
            purchase_rounds_without_immediate_hits=[r['round'] for r in sequence
                if r['attack_cost'] and r['incoming_damage'] == 0],
            total_post_handoff_damage=sum(r['incoming_damage'] for r in sequence),
            sequence=sequence))
    assert len(cases) == 8
    pairs = {}
    for case in cases:
        c = case['condition']
        pairs.setdefault(c['opponent_id'], []).append(case)
    assert len(pairs) == 4
    for pair in pairs.values():
        assert len(pair) == 2
        assert {c['condition']['candidate_side'] for c in pair} == {0, 1}
        for key in ('rounds', 'handoff_round', 'target_counter_hp',
                    'post_handoff_zero_damage', 'total_post_handoff_attack_cost',
                    'total_post_handoff_defense_cost', 'purchase_rounds',
                    'purchased_copy_count', 'purchase_rounds_without_immediate_hits',
                    'total_post_handoff_damage', 'sequence'):
            assert pair[0][key] == pair[1][key], key
    assert all(digest(p) == sha for p, sha in hashes.items())
    output = dict(time_utc=datetime.now(timezone.utc).isoformat(), input_sha256=hashes,
        all_histories_verified=True, all_model_actions_agree=True,
        assignment_pairs=4, identical_spending_and_damage_pairs=4, cases=cases,
        scope='Eight registered P5TNUB conditions, all retained. Costs are accepted purchase '
              'deductions; zero damage over all remaining played rounds means no purchased '
              'copy arrived during those rounds. Opponent construction costs and induced '
              'future changes prevent interpreting this as zero economic value. '
              'Forecast versus visible is a full-policy intervention, not a one-round effect.')
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({k: output[k] for k in ('time_utc', 'assignment_pairs',
                                           'identical_spending_and_damage_pairs')}))
    for name, pair in pairs.items():
        c = pair[0]
        print(json.dumps(dict(opponent=name, hp=c['target_counter_hp'],
            rounds=c['rounds'], purchase_rounds=c['purchase_rounds'],
            attack_cost=c['total_post_handoff_attack_cost'],
            defense_cost=c['total_post_handoff_defense_cost'],
            damage=c['total_post_handoff_damage'])))


if __name__ == '__main__':
    main()
