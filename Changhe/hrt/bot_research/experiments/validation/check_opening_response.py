"""Exact first-round bound and fixed-opening legality on the original engine."""
from __future__ import annotations
import argparse
from copy import deepcopy
from dataclasses import asdict
import hashlib
import json
from pathlib import Path
from td_game.actions import apply_action
from td_game.combat import simulate_map
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.opening_response import OpeningResponse
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation_strict import now
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    config = balanced_config()
    costs = {k: v.cost for k, v in config.minions.items()}
    rosters = []
    def visit(prefix, remaining):
        rosters.append(prefix)
        for kind, cost in costs.items():
            if cost <= remaining:
                visit(prefix + [kind], remaining - cost)
    visit([], 100)
    assert len(rosters) == 27
    fixture = Path('bot_research/runs/validation/roster-wrap-check-001.json')
    all_walls = [{'op': 'build_wall', 'x': a['x'], 'y': a['y']} for a in json.loads(fixture.read_text())['construction_actions']]
    geometry = []
    for count in (0, 20, len(all_walls)):
        for side in (0, 1):
            game = Engine(config, ('a', 'b'))
            for action in all_walls[:count]:
                assert apply_action(game.players[1-side], action, 1, config)['accepted']
            damage = []
            for types in rosters:
                attacker = deepcopy(game.players[side])
                for kind in types:
                    assert apply_action(attacker, {'op': 'buy_minion', 'type': kind}, 1, config)['accepted']
                actual = simulate_map(attacker, deepcopy(game.players[1-side]), game.path(1-side), 1, config)
                assert actual.damage == sum(config.minions[k].damage for k in types)
                damage.append(actual.damage)
            assert max(damage) == 32
            winners = [types for types, value in zip(rosters, damage) if value == 32]
            assert len(winners) == 5 and all(t.count('tier1') == 4 and t.count('tier2') == 1 for t in winners)
            geometry.append({'walls': count, 'side': side, 'route_length': len(game.path(1-side))-1,
                             'rosters': len(rosters), 'largest_damage': max(damage), 'maximizers': winners})
    openings = []
    for variant in ('mixed32', 'guard22', 'guard_poke5', 'factories'):
        for side in (0, 1):
            game = Engine(config, ('a', 'b'))
            observation = game.observation(side)
            before = deepcopy(observation)
            policy = OpeningResponse(opening=variant)
            actions = policy.decide(observation)
            assert observation == before
            pair = [[], []]
            pair[side] = actions
            pair[1-side] = [{'op':'buy_minion', 'type':'tier1'}] * 2
            records = game.play_round(pair)
            assert not any(e['kind'] == 'action' and not e['accepted'] for r in records for e in r['event'])
            hp = [p.hp for p in game.players][::1 if side == 0 else -1]
            if variant == 'mixed32':
                assert hp == [790, 768]
            elif variant == 'guard22':
                assert hp == [800, 778]
            elif variant == 'guard_poke5':
                assert hp == [800, 795]
            else:
                assert hp == [790, 800]
            openings.append({'variant': variant, 'side': side, 'actions': actions, 'hp_candidate_first': hp,
                             'factories': game.players[side].n_factories})
    paths = set(static_closure({'bot_research.experiments.validation.check_opening_response'}))
    paths |= {fixture, Path('td_game/balanced.json')}
    output = {'time_utc': now(), 'source_sha256': {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
              'all_passed': True, 'geometry_checks': geometry, 'opening_checks': openings,
              'scope': '162 original-engine combat checks and eight first-round policy checks. No full-game strength assertion.'}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({'all_passed': True, 'combat_checks': len(geometry)*len(rosters), 'opening_checks': openings}))


if __name__ == '__main__':
    main()
