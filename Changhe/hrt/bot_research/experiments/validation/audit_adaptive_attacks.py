"""Check selected adaptive attacks with the original combat procedure."""
from copy import deepcopy
from datetime import datetime, timezone
from fractions import Fraction
import argparse
import hashlib
import json
from pathlib import Path
import time

from td_game.actions import apply_action
from td_game.combat import simulate_map
from td_game.config import config_from_dict
from td_game.pathfinding import shortest_path
from bot_research.bots.counters.adaptive_catalogue import purchase_pool, pool_digest
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.replay_audit import check
from bot_research.experiments.validation.source_closure import static_closure


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def combat(attacker, defender, rnd, config):
    rules = config.globals
    path = shortest_path(rules.width, rules.height, [(b.x, b.y) for b in defender.buildings], rules.spawn, rules.base)
    check(path is not None, 'Original pathfinder found no legal route.')
    return simulate_map(deepcopy(attacker), deepcopy(defender), path, rnd, config).damage


def audit_attack(observation, actions, trace):
    detail = trace['adaptive_attack']
    if not detail['enabled']:
        return dict(enabled=False, checked_maps=0)
    rnd, side, rules = observation['round'], observation['player'], observation['rules']
    config = config_from_dict(rules)
    own = player_from_snapshot(observation['players'][side])
    for action in actions:
        if action['op'] not in ('buy_factory', 'buy_minion'):
            check(apply_action(own, action, rnd, config)['accepted'], 'Illegal construction in selected action list.')
    sequence = [a['type'] for a in actions if a['op'] == 'buy_minion']
    check(sequence == detail['sequence'], 'Recorded attack differs from submitted purchases.')
    check(detail['budget'] == int(own.gold * Fraction(detail['budget_share'])), 'Attack budget differs.')
    pool = [()] if detail['all_current_maps_immune'] else purchase_pool(rules, detail['budget'], detail['count_cap'], detail['evaluation_limit'])
    check(pool_digest(pool) == detail['pool_sha256'], 'Purchase pool digest differs.')
    check(len(pool) == detail['evaluated'] and len(pool) <= detail['evaluation_limit'], 'Evaluation count differs.')
    check(tuple(sequence) == pool[detail['selected']['index']], 'Selected pool entry differs.')
    attacker = deepcopy(own)
    for tier in sequence:
        check(apply_action(attacker, dict(op='buy_minion', type=tier), rnd, config)['accepted'], 'Unaffordable selected purchase.')
    cost = own.gold - attacker.gold
    check(cost == detail['selected']['cost'] and cost <= detail['budget'], 'Selected cost differs.')
    targets = {}
    for name, predicted in trace['predictions'].items():
        enemy = player_from_snapshot(observation['players'][1-side])
        for action in predicted['actions']:
            check(apply_action(enemy, action, rnd, config)['accepted'], 'Illegal forecast action.')
        targets[name] = enemy
    if not targets:
        targets['visible_fallback'] = player_from_snapshot(observation['players'][1-side])
    check(list(targets) == detail['targets'], 'Attack target set differs from retained catalogue.')
    baselines, damages, incoming = {}, {}, {}
    for name, target in targets.items():
        baselines[name] = combat(own, target, rnd, config)
        damages[name] = combat(attacker, target, rnd, config)
        incoming[name] = combat(target, own, rnd, config)
    check(baselines == detail['baseline_damage'], 'Baseline damage differs from original combat.')
    check(damages == detail['selected']['damage'], 'Selected damage differs from original combat.')
    check(incoming == detail['incoming_damage'], 'Incoming damage differs from original combat.')
    gains = {n: damages[n]-baselines[n] for n in targets}
    check(gains == detail['selected']['gains'], 'Marginal damage differs.')
    minimum = min(gains.values())
    check(minimum == detail['selected']['minimum_gain'], 'Minimum gain differs.')
    utility = Fraction(minimum) if rnd == rules['globals']['max_rounds'] else Fraction(detail['weight'])*minimum-cost
    check(utility == Fraction(detail['selected']['utility']), 'Rational utility differs.')
    own_safe = max(incoming.values()) < own.hp
    safe_lethal = own_safe and min(damages.values()) >= observation['players'][1-side]['hp']
    check(own_safe == detail['own_safe'], 'Own survival condition differs.')
    check(safe_lethal == detail['selected']['forecast_safe_lethal'], 'Forecast safe-lethal flag differs.')
    check(safe_lethal or utility >= 0, 'Selected nonlethal utility is below the empty purchase.')
    if detail['all_current_maps_immune']:
        check(all(v == 0 for v in damages.values()), 'Claimed current immunity allowed damage.')
    return dict(enabled=True, checked_maps=len(targets), purchased=len(sequence),
                cost=cost, minimum_gain=minimum, safe_lethal=safe_lethal,
                fallback='visible_fallback' in targets)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--strict-audit', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    start = time.perf_counter()
    strict = json.loads(Path(args.strict_audit).read_text())
    inputs = {args.strict_audit: digest(args.strict_audit)}
    sources = {str(p): digest(p) for p in static_closure({'bot_research.experiments.validation.audit_adaptive_attacks'})}
    sources['td_game/balanced.json'] = digest('td_game/balanced.json')
    cases = []
    for case in strict['cases']:
        path = case['result_path']
        check(digest(path) == strict['input_sha256'][path], 'Strict result bytes changed.')
        inputs[path] = digest(path)
        row = json.loads(Path(path).read_text())
        inputs[row['replay_path']] = digest(row['replay_path'])
        check(inputs[row['replay_path']] == row['trajectory_sha256'], 'Replay bytes changed.')
        records = [json.loads(line) for line in Path(row['replay_path']).read_text().splitlines()]
        side = row['condition']['candidate_side']
        details = []
        for trace in row['catalogue_trace']:
            rnd = trace['round']
            observation = dict(round=rnd, player=side, rules=row['rules'],
                players=[records[2*(rnd-1)+i]['snapshot'] for i in (0, 1)])
            actions = [e['action'] for e in records[2*rnd+side]['event'] if e['kind'] == 'action']
            details.append(dict(round=rnd, **audit_attack(observation, actions, trace)))
        cases.append(dict(result_path=path, condition=row['condition'], rounds=details))
        print(json.dumps(dict(checked=case['job'], checked_maps=sum(d['checked_maps'] for d in details))), flush=True)
    check(all(digest(p) == h for p, h in {**inputs, **sources}.items()), 'Audit input or source changed.')
    output = dict(time_utc=datetime.now(timezone.utc).isoformat(), runtime_seconds=time.perf_counter()-start,
        input_sha256=inputs, source_sha256=sources, all_passed=True, cases=cases,
        scope='Selected outgoing damage, no-purchase baseline and incoming damage are independently recomputed by original combat. Pool membership and utility arithmetic are checked. This does not exhaustively rerank the pool with original combat or establish full-game optimality.')
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps(dict(all_passed=True, games=len(cases), runtime_seconds=output['runtime_seconds'])), flush=True)


if __name__ == '__main__':
    main()
