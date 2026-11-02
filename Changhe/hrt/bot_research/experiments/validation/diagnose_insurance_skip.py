"""Compare full and partial insurance on one replayed public observation.

No modified full-game outcome is inferred. Each returned plan is applied and
its incoming damage checked with the unchanged original combat simulator.
"""
from __future__ import annotations
import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import time
from td_game.actions import apply_action
from td_game.combat import simulate_map
from td_game.config import config_from_dict
from td_game.pathfinding import shortest_path
from td_game.state import PlayerState, RosterEntry
from bot_research.bots.counters.snapshots import lead_seven_001 as target
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation_strict import now, read_result
from bot_research.experiments.validation.search_timing_equivalence import observations_and_actions
from bot_research.experiments.validation.source_closure import static_closure


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--result', required=True)
    parser.add_argument('--round', type=int, required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    path = Path(args.result)
    directory = path.parent.parent
    metadata = json.loads((directory/'freeze.json').read_text())
    job = json.loads((directory/'jobs'/(path.stem+'.json')).read_text())
    row = read_result(path, job, metadata['source_sha256'])
    assert not any(row['bot_errors']) and not any(row['rejected_actions'])
    assert digest(row['replay_path']) == row['trajectory_sha256']
    defender_side = 1-row['condition']['candidate_side']
    observations, submissions = observations_and_actions(row, defender_side)
    _, attacks = observations_and_actions(row, 1-defender_side)
    obs = observations[args.round]
    original = deepcopy(obs)
    cfg = config_from_dict(obs['rules'])
    params = dict(big_threat=100, attack_mode='robust', poke_insurance=False, gun_cap=120)
    policy = target.make(**params)
    actual = policy(obs)
    assert actual == submissions[args.round]
    model = target.Lead7(**params)
    rules = target.gk.Rules.from_observation(obs)
    stages = model.P.plan_walls(obs, obs['players'][defender_side]['gold'], layout=model.layout, stage=0)
    left = obs['players'][defender_side]['gold'] - target._cost_of(stages, rules)
    planned_obs = target._with_buildings(obs, stages, left)
    visible = model.P.active_opponent_types(obs)
    if visible:
        mandatory = model._plan(planned_obs, left, threat_types=[visible], layout=model.layout, partial='best')
        stages += mandatory
        left -= target._cost_of(mandatory, rules)
        planned_obs = target._with_buildings(obs, stages, left)
    comps = model.P.threat_compositions(obs)
    attacker = player_from_snapshot(obs['players'][1-defender_side])
    for action in attacks[args.round]:
        assert apply_action(attacker, action, args.round, cfg)['accepted']
    attack_types = [entry.type for entry in attacker.roster if entry.active(args.round)]

    def damage(actions, types):
        defender = player_from_snapshot(obs['players'][defender_side])
        cost = 0
        for action in actions:
            result = apply_action(defender, action, args.round, cfg)
            assert result['accepted'], (action,result)
            cost += result.get('cost',0)
        route = shortest_path(cfg.globals.width,cfg.globals.height,
                              {(b.x,b.y) for b in defender.buildings},cfg.globals.spawn,cfg.globals.base)
        assert route is not None
        enemy = PlayerState('component_attacker', 800, 0)
        enemy.roster = [RosterEntry(i,t,args.round,args.round) for i,t in enumerate(types)]
        total = simulate_map(enemy,defender,route,args.round,cfg)
        return {'damage':total.damage,'hits':total.hits,'cost':cost,'route_length':len(route)-1}

    checked = []
    choices = [('recorded_action',None,None),('full_zero_leak','none',comps),
               ('full_partial','best',comps),('actual_roster_zero_leak','none',[attack_types])]
    for name, mode, threats in choices:
        start = time.perf_counter()
        actions = actual if name == 'recorded_action' else stages + model._plan(
            planned_obs,left,threat_types=threats,layout=model.layout,partial=mode)
        runtime = time.perf_counter()-start
        actual_damage = damage(actions, attack_types)
        tested = [damage(actions, types)['damage'] for types in comps]
        checked.append({'name':name,'actions':actions,'planner_runtime_seconds':runtime,
                        'actual_roster_result':actual_damage,'sampled_damage':tested,
                        'worst_sampled_damage':max(tested,default=0)})
    assert obs == original
    sources = static_closure({'bot_research.experiments.validation.diagnose_insurance_skip'})
    result = {'time_utc':now(),'source_result':args.result,'round':args.round,
              'observation':obs,'target_parameters':params,'remaining_gold_after_mandatory':left,
              'sampled_compositions':comps,'actual_attack_types':attack_types,'plans':checked,
              'input_sha256':{str(p):digest(p) for p in (path,directory/'freeze.json',directory/'jobs'/(path.stem+'.json'),Path(row['replay_path']))},
              'source_sha256':{str(p):digest(p) for p in sorted(sources)},
              'scope':'Single-observation component diagnosis. Actual-roster plan uses hindsight and is not a legal-information policy recommendation. Partial insurance uses public affordable compositions. No full-game improvement follows.'}
    atomic_json(args.output,result,exclusive=True)
    print(json.dumps({'round':args.round,'plans':[{k:p[k] for k in ('name','actual_roster_result','worst_sampled_damage','planner_runtime_seconds')} for p in checked]}))


if __name__ == '__main__':
    main()
