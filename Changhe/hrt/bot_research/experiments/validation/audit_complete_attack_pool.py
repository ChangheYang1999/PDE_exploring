"""Rerank every member of selected finite attack pools using original combat."""
from copy import deepcopy
from datetime import datetime, timezone
from fractions import Fraction
import argparse
import hashlib
import json
from pathlib import Path
import time

from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.adaptive_catalogue import purchase_pool, pool_digest
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.audit_adaptive_attacks import combat, audit_attack
from bot_research.experiments.validation.source_closure import static_closure


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def rerank(observation, actions, trace):
    selected_check = audit_attack(observation, actions, trace)
    assert selected_check['enabled']
    rnd, side, rules = observation['round'], observation['player'], observation['rules']
    config = config_from_dict(rules)
    detail = trace['adaptive_attack']
    own = player_from_snapshot(observation['players'][side])
    for action in actions:
        if action['op'] not in ('buy_factory', 'buy_minion'):
            assert apply_action(own, action, rnd, config)['accepted']
    targets = {}
    for name, forecast in trace['predictions'].items():
        target = player_from_snapshot(observation['players'][1-side])
        for action in forecast['actions']:
            assert apply_action(target, action, rnd, config)['accepted']
        targets[name] = target
    if not targets:
        targets['visible_fallback'] = player_from_snapshot(observation['players'][1-side])
    baseline = {name: combat(own, target, rnd, config) for name, target in targets.items()}
    incoming = {name: combat(target, own, rnd, config) for name, target in targets.items()}
    safe = max(incoming.values()) < own.hp
    pool = [()] if detail['all_current_maps_immune'] else purchase_pool(
        rules, detail['budget'], detail['count_cap'], detail['evaluation_limit'])
    assert pool_digest(pool) == detail['pool_sha256']
    values = []
    for index, sequence in enumerate(pool):
        attacker = deepcopy(own)
        for tier in sequence:
            assert apply_action(attacker, dict(op='buy_minion', type=tier), rnd, config)['accepted']
        damage = {name: combat(attacker, target, rnd, config) for name, target in targets.items()}
        gains = {name: damage[name]-baseline[name] for name in targets}
        gain = min(gains.values())
        cost = own.gold-attacker.gold
        utility = Fraction(gain) if rnd == rules['globals']['max_rounds'] else Fraction(detail['weight'])*gain-cost
        lethal = safe and min(damage.values()) >= observation['players'][1-side]['hp']
        # The final component reproduces the documented stable first-maximum
        # tie rule without calling any planner or fast combat routine.
        rank = (lethal, utility, gain, -cost, -len(sequence), -index)
        values.append(dict(index=index, sequence=list(sequence), damage=damage,
                           gains=gains, cost=cost, utility=str(utility), safe_lethal=lethal,
                           rank=rank))
    best = max(values, key=lambda value: value['rank'])
    assert best['index'] == detail['selected']['index'], 'Original-combat maximizer differs.'
    assert best['sequence'] == detail['sequence'], 'Original-combat selected sequence differs.'
    for value in values:
        value.pop('rank')
    return dict(round=rnd, selected_index=best['index'], pool_size=len(pool),
                outgoing_combat_evaluations=len(pool)*len(targets), values=values,
                scope='Exact maximizer over the recorded finite pool and retained target models, including visible fallback when present. This is not an optimality claim over unenumerated actions or future rounds.')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--manifest', required=True)
    parser.add_argument('--case-index', type=int, required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    manifest = json.loads(Path(args.manifest).read_text())
    entry = manifest['cases'][args.case_index]
    inputs = {args.manifest: digest(args.manifest)}
    for path, expected in manifest['input_sha256'].items():
        assert digest(path) == expected, 'Declared audit source changed.'
        inputs[path] = expected
    path = entry['result_path']
    assert digest(path) == entry['result_sha256']
    inputs[path] = entry['result_sha256']
    row = json.loads(Path(path).read_text())
    assert digest(row['replay_path']) == row['trajectory_sha256']
    inputs[row['replay_path']] = row['trajectory_sha256']
    source = {str(p): digest(p) for p in static_closure({'bot_research.experiments.validation.audit_complete_attack_pool'})}
    source['td_game/balanced.json'] = digest('td_game/balanced.json')
    records = [json.loads(line) for line in Path(row['replay_path']).read_text().splitlines()]
    side = row['condition']['candidate_side']
    results = []
    for trace in row['catalogue_trace']:
        rnd = trace['round']
        if rnd not in manifest['rounds']:
            continue
        observation = dict(round=rnd, player=side, rules=row['rules'],
                           players=[records[2*(rnd-1)+i]['snapshot'] for i in (0, 1)])
        actions = [e['action'] for e in records[2*rnd+side]['event'] if e['kind'] == 'action']
        result = rerank(observation, actions, trace)
        results.append(result)
        print(json.dumps(dict(round=rnd, pool_size=result['pool_size'], all_passed=True)), flush=True)
    assert [r['round'] for r in results] == [r for r in manifest['rounds'] if r <= row['rounds']]
    assert all(digest(p) == h for p, h in {**inputs, **source}.items())
    output = dict(time_utc=datetime.now(timezone.utc).isoformat(), runtime_seconds=time.perf_counter()-started,
                  condition=row['condition'], input_sha256=inputs, source_sha256=source,
                  all_passed=True, cases=results)
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps(dict(all_passed=True, decisions=len(results), runtime_seconds=output['runtime_seconds'])), flush=True)


if __name__ == '__main__':
    main()
