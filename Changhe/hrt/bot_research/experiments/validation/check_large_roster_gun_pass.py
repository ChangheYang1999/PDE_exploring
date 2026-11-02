"""Separate the roster-size cutoff from the gun search on a fixed fixture.

Calls the published private planning helper directly, without modifying its
module globals or the engine. All returned actions and damage outcomes are
checked through the unchanged engine.
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
from td_game.config import balanced_config
from td_game.engine import Engine
from td_game.state import RosterEntry
from bot_research.bots.defense.frozen.v18 import plan
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation_strict import now
from bot_research.experiments.validation.source_closure import static_closure


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    args = ap.parse_args()
    start = time.monotonic()
    fixture = Path('bot_research/runs/validation/roster-wrap-check-001.json')
    game = Engine(balanced_config(), ('defender', 'attacker'))
    game.players[0].gold = 10000
    for action in json.loads(fixture.read_text())['construction_actions']:
        assert apply_action(game.players[0], action, 1, game.config)['accepted']
    game.players[0].gold = 1000
    game.players[1].gold = 1400
    game.players[1].roster = [RosterEntry(i, 'tier1', 1, 12) for i in range(200)]
    game.players[1].next_roster_id = 200
    obs = game.observation(0)
    comps = plan.threat_compositions(obs)
    _, rules, buildings, blocked = plan.observe(obs)
    route = plan.gk.route(blocked)
    gun_candidates = {
        kind: plan._gun_candidates(blocked, plan.LAYOUT, route, rules, kind, buildings=buildings)
        for kind in ('gun1', 'gun2', 'gun3')}
    full_actions = plan.plan_defense(obs, 1000, threat_types=comps, time_budget=300)
    helper_result = plan._gun_pass(deepcopy(buildings), set(blocked), rules, [], 0,
                                   1000, comps, plan.LAYOUT, max_steps=12, deadline=None)
    rows = []
    for label, actions in (('published_plan', full_actions), ('direct_gun_helper', helper_result[0])):
        defender = deepcopy(game.players[0])
        for action in actions:
            assert apply_action(defender, action, 1, game.config)['accepted']
        path = plan.gk.route({(b.x, b.y) for b in defender.buildings})
        damages = []
        for kinds in comps:
            attacker = deepcopy(game.players[1])
            for kind in kinds[200:]:
                assert apply_action(attacker, {'op': 'buy_minion', 'type': kind}, 1, game.config)['accepted']
            damages.append(simulate_map(attacker, deepcopy(defender), path, 1, game.config).damage)
        rows.append({'method': label, 'actions': actions, 'cost': 1000 - defender.gold,
                     'damage_by_composition': damages, 'maximum_damage': max(damages)})
    paths = set(static_closure({'bot_research.experiments.validation.check_large_roster_gun_pass'}))
    paths |= {fixture, Path('td_game/balanced.json')}
    result = {'time_utc': now(), 'runtime_seconds': time.monotonic() - start,
              'source_sha256': {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
              'gun_candidates': gun_candidates, 'compositions': len(comps),
              'maximum_composition_length': max(map(len, comps)),
              'published_cutoff': plan.GUN_PASS_MAX_ENTITIES,
              'direct_helper_internal_spent_score_hits': list(helper_result[1:]), 'results': rows,
              'scope': 'Fixed synthetic component state. No monkeypatching, no policy-game outcome, no claim that changing only the cutoff is sufficient in other states.'}
    atomic_json(args.output, result, exclusive=True)
    print(json.dumps({k: v for k, v in result.items() if k != 'source_sha256'}))


if __name__ == '__main__':
    main()
