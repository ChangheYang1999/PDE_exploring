"""Fresh public-model shadows and original replay for early-heavy handoff games."""
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs
import argparse
import hashlib
import json
import time

from td_game.actions import apply_action
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.early_heavy_handoff import EarlyHeavyHandoff
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.replay_audit import normalized
from bot_research.experiments.validation.source_closure import static_closure


def purchases(actions):
    return [a for a in actions if a['op'] == 'buy_minion']


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--campaign', required=True)
    parser.add_argument('--candidate-ids', nargs='+', required=True)
    parser.add_argument('--opponent-ids', nargs='+')
    parser.add_argument('--expected', type=int, required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    start = time.perf_counter()
    digest = lambda path: hashlib.sha256(Path(path).read_bytes()).hexdigest()
    hashes = {str(p): digest(p) for p in static_closure(
        {'bot_research.experiments.validation.check_early_heavy_histories'})}
    root = Path(args.campaign)
    for path, sha in json.loads((root / 'freeze.json').read_text())['source_sha256'].items():
        assert digest(path) == sha
        if path in hashes:
            assert hashes[path] == sha
        hashes[path] = sha
    jobs = root / 'jobs.json'
    hashes[str(jobs)] = digest(jobs)
    cases = []
    for job in json.loads(jobs.read_text()):
        condition = job['condition']
        if condition['candidate_id'] not in args.candidate_ids:
            continue
        if args.opponent_ids and condition['opponent_id'] not in args.opponent_ids:
            continue
        path = root / 'results' / (job['id'] + '.json')
        checked_row(str(path), hashes)
        row = json.loads(path.read_text())
        records = [json.loads(line) for line in Path(row['replay_path']).read_text().splitlines()]
        counter_side = 1 - condition['candidate_side']
        target_side = condition['candidate_side']
        cfg = balanced_config()
        engine = Engine(cfg, tuple(row['bot_specs']))
        assert normalized(engine.initial_records(tuple(row['bot_specs']))) == records[:2]
        spec = condition['opponent_spec']
        assert spec.partition(':')[0] == 'bot_research.bots.counters.early_heavy_handoff'
        params = {key: json.loads(value[0]) for key, value in parse_qs(spec.partition('?')[2]).items()}
        policy = EarlyHeavyHandoff(**params)
        differences, prediction_differences, purchase_differences, rounds = [], [], [], []
        for rnd in range(1, row['rounds'] + 1):
            observation = engine.observation(counter_side)
            saved = deepcopy(observation)
            t = time.perf_counter()
            fresh = policy.decide(observation)
            seconds = time.perf_counter() - t
            assert observation == saved
            state = player_from_snapshot(observation['players'][counter_side])
            assert all(apply_action(state, action, rnd, cfg)['accepted'] for action in fresh)
            assert not policy.switched or not purchases(fresh)
            pair = records[2*rnd:2*rnd+2]
            actual = [[event['action'] for event in record['event'] if event['kind'] == 'action']
                      for record in pair]
            trace = policy.trace[-1]
            assert trace['round'] == rnd
            if fresh != actual[counter_side]:
                differences.append(dict(round=rnd, recorded_actions=actual[counter_side],
                                        fresh_actions=fresh))
            predicted = trace['predicted_actions']
            if predicted != actual[target_side]:
                prediction_differences.append(dict(round=rnd, predicted_actions=predicted,
                                                    actual_actions=actual[target_side]))
            if purchases(predicted) != purchases(actual[target_side]):
                purchase_differences.append(rnd)
            assert normalized(engine.play_round(actual)) == pair
            incoming = next(event['base_damage'] for event in pair[counter_side]['event']
                            if event['kind'] == 'combat')
            bought = purchases(actual[target_side])
            rounds.append(dict(trace, decision_seconds=seconds, actual_target_purchases=bought,
                actual_target_purchase_cost=sum(cfg.minions[a['type']].cost for a in bought),
                actual_counter_incoming_damage=incoming,
                actual_counter_hp_after=pair[counter_side]['snapshot']['hp'],
                actual_target_hp_after=pair[target_side]['snapshot']['hp'],
                model_all_actions_agree=predicted == actual[target_side],
                model_purchases_agree=purchases(predicted) == bought,
                fresh_counter_actions_agree=fresh == actual[counter_side]))
        assert engine.result == row['result']
        cases.append(dict(condition=condition, result=str(path), rounds=rounds,
            replayed=True, observations_unchanged=True, fresh_actions_legal=True,
            policy_action_differences=differences, model_action_differences=prediction_differences,
            model_purchase_difference_rounds=purchase_differences,
            internal_rejected_proposals=policy.rejected_proposals, strike_trace=policy.strike_trace,
            filtered_parent_proposals=policy.filtered_parent_proposals,
            post_handoff_purchase_rounds=[r['round'] for r in rounds if r['switched']
                                         and r['actual_target_purchases']],
            post_handoff_purchase_with_no_hit_rounds=[r['round'] for r in rounds if r['switched']
                and r['actual_target_purchases'] and r['actual_counter_incoming_damage'] == 0]))
        print(json.dumps(dict(time_utc=datetime.now(timezone.utc).isoformat(),
            finished=job['id'], candidate=condition['candidate_id'], opponent=condition['opponent_id'],
            policy_differences=len(differences), model_differences=len(prediction_differences),
            purchase_differences=len(purchase_differences))), flush=True)
    assert len(cases) == args.expected
    assert all(digest(path) == sha for path, sha in hashes.items())
    output = dict(time_utc=datetime.now(timezone.utc).isoformat(),
        runtime_seconds=time.perf_counter()-start, input_sha256=hashes, cases=cases,
        all_replayed=True, all_observations_unchanged=True, all_fresh_actions_legal=True,
        exact_counter_policy_reproduction=all(not case['policy_action_differences'] for case in cases),
        no_internal_rejections=all(not case['internal_rejected_proposals'] for case in cases),
        scope='Fresh public-model shadows on recorded observations. Original submissions drive replay. '
              'Clock-limited model and policy discrepancies are retained. Purchases with zero immediate '
              'damage may affect later rounds, so their cost is not automatically a full-game loss. '
              'This diagnostic is not an independent strength sample.')
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({key: output[key] for key in ('time_utc', 'runtime_seconds',
        'exact_counter_policy_reproduction', 'no_internal_rejections')}))


if __name__ == '__main__':
    main()
