"""Explain one Lead17 insurance decision on its preserved public history.

This is component diagnosis, not a new full-game policy score. Actual-roster
plans use hindsight and are labelled separately from public threat sampling.
"""
from __future__ import annotations
import argparse
from copy import deepcopy
import json
from pathlib import Path
import time
from urllib.parse import parse_qsl
from td_game.actions import apply_action
from td_game.combat import simulate_map
from td_game.config import config_from_dict
from td_game.pathfinding import shortest_path
from td_game.state import PlayerState, RosterEntry
from bot_research.bots.counters.snapshots import lead_seventeen_001 as target
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation_strict import digest, now, read_result
from bot_research.experiments.validation.search_timing_equivalence import observations_and_actions
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--result', required=True)
    parser.add_argument('--round', type=int, default=3)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    path = Path(args.result)
    directory = path.parent.parent
    metadata = json.loads((directory / 'freeze.json').read_text())
    job = json.loads((directory / 'jobs' / (path.stem + '.json')).read_text())
    row = read_result(path, job, metadata['source_sha256'])
    assert not any(row['bot_errors']) and not any(row['rejected_actions'])
    assert not row['source_changed_during_match']
    assert digest(row['replay_path']) == row['trajectory_sha256']
    side = 1 - row['condition']['candidate_side']
    spec = job['bots'][side]['spec']
    entry, _, query = spec.partition('?')
    assert entry == 'bot_research.bots.counters.snapshots.lead_seventeen_001:@make'
    params = {k: json.loads(v) for k, v in parse_qsl(query)}
    obs_by_round, submissions = observations_and_actions(row, side)
    _, enemy_actions = observations_and_actions(row, 1-side)
    actual, probe = target.make(**params), target.make(**params)
    started = time.perf_counter()
    sources = {str(p): digest(p) for p in static_closure({
        'bot_research.experiments.validation.diagnose_lead_seventeen'})}
    for rnd in range(1, args.round):
        assert actual(deepcopy(obs_by_round[rnd])) == submissions[rnd]
        assert probe(deepcopy(obs_by_round[rnd])) == submissions[rnd]
    obs = obs_by_round[args.round]
    frozen_observation = deepcopy(obs)
    chosen = actual(deepcopy(obs))
    assert chosen == submissions[args.round]
    underlying = target.v16.Lead16.__call__(probe, deepcopy(obs))
    assert probe.alt is None, 'This diagnostic is for the native branch.'
    base = probe.base
    rules = target.gk.Rules.from_observation(obs)
    kept = [a for a in underlying if a['op'] != 'buy_factory']
    left = obs['players'][side]['gold'] - target.v15._cost_of(kept, rules)
    planned_obs = target.v15._with_buildings(obs, kept, left)
    comps = [c for c in base.P.threat_compositions(obs)
             if all(rules.minions[t]['hp'] <= probe.mid_hp for t in c)]
    share = base.p['spec_share'] if probe.mid_share is None else probe.mid_share
    ins = {'allow_guns': False} if (base.p['splash_insurance'] or base.fortress) else {}
    cfg = config_from_dict(obs['rules'])
    attacker = player_from_snapshot(obs['players'][1-side])
    for action in enemy_actions[args.round]:
        assert apply_action(attacker, action, args.round, cfg)['accepted']
    actual_types = [entry.type for entry in attacker.roster if entry.active(args.round)]

    def check(actions, types):
        defender = player_from_snapshot(obs['players'][side])
        cost = 0
        for action in actions:
            event = apply_action(defender, action, args.round, cfg)
            assert event['accepted'], event
            cost += event.get('cost', 0)
        route = shortest_path(cfg.globals.width, cfg.globals.height,
            {(b.x, b.y) for b in defender.buildings}, cfg.globals.spawn, cfg.globals.base)
        assert route is not None
        enemy = PlayerState('diagnostic_attacker', 800, 0)
        enemy.roster = [RosterEntry(i, t, args.round, args.round) for i, t in enumerate(types)]
        combat = simulate_map(enemy, defender, route, args.round, cfg)
        return dict(damage=combat.damage, hits=combat.hits, cost=cost, route_length=len(route)-1)

    alternatives = []
    for label, budget, threats in (
        ('sampled_with_recorded_share', int(left*share), comps),
        ('sampled_with_all_remaining_gold', left, comps),
        ('hindsight_actual_roster_recorded_share', int(left*share), [actual_types]),
        ('hindsight_actual_roster_all_gold', left, [actual_types])):
        start = time.perf_counter()
        plan = base._plan(deepcopy(planned_obs), budget, threat_types=threats,
                          layout=base.layout, partial='none', **ins)
        alternatives.append(dict(label=label, budget=budget, additional_actions=plan,
            additional_cost=target.v15._cost_of(plan, rules),
            planner_runtime_seconds=time.perf_counter()-start,
            actual_roster=check(kept+plan, actual_types),
            sampled_damage=[check(kept+plan, c)['damage'] for c in comps]))
    for label, budget in (
        ('public_replan_from_initial_map_recorded_share', int(obs['players'][side]['gold']*share)),
        ('public_replan_from_initial_map_all_gold', obs['players'][side]['gold'])):
        start = time.perf_counter()
        plan = base._plan(deepcopy(obs), budget, threat_types=comps,
                          layout=base.layout, partial='none', **ins)
        alternatives.append(dict(label=label, budget=budget, additional_actions=plan,
            additional_cost=target.v15._cost_of(plan, rules),
            planner_runtime_seconds=time.perf_counter()-start,
            actual_roster=check(plan, actual_types),
            sampled_damage=[check(plan, c)['damage'] for c in comps]))
    assert obs == frozen_observation
    assert all(digest(p) == sha for p, sha in sources.items())
    output = dict(time_utc=now(), runtime_seconds=time.perf_counter()-started,
        result=args.result, round=args.round, side=side, parameters=params,
        observation=obs, chosen_actions=chosen, underlying_actions=underlying,
        mid_rounds=actual.mid_rounds, poke_condition=probe._poke_condition(obs, rules),
        fortress=base.fortress, planner_options=ins, remaining_gold=left, share=share,
        sampled_compositions=comps, actual_incoming_types=actual_types,
        worst_sampled_before_extra=target.v15._worst_leak(planned_obs, rules, comps),
        recorded_action_combat=check(chosen, actual_types), alternatives=alternatives,
        input_sha256={str(p): digest(p) for p in (path, directory/'freeze.json',
            directory/'jobs'/(path.stem+'.json'), Path(row['replay_path']))},
        source_sha256=sources,
        scope='Public-history component diagnosis. Hindsight alternatives are not legal-information policies. No full-game improvement is inferred.')
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({k: output[k] for k in ('time_utc', 'runtime_seconds', 'remaining_gold',
        'poke_condition', 'fortress', 'share', 'mid_rounds', 'worst_sampled_before_extra', 'alternatives')}))


if __name__ == '__main__':
    main()
