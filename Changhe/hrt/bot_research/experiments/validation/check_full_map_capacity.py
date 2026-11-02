"""Check construction obstruction and the proved fixed-map arrival lower bound."""
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
from td_game.pathfinding import shortest_path
from td_game.state import PlayerState, RosterEntry
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation_strict import now
from bot_research.experiments.validation.source_closure import static_closure


FIXTURES = Path('bot_research/experiments/validation/analysis/full_map_capacity/verification/fixtures.json')
PROOF = Path('bot_research/experiments/validation/analysis/full_map_capacity/PROOF.md')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    data = json.loads(FIXTURES.read_text())
    cfg = balanced_config()
    g = cfg.globals
    ticks = g.ticks_per_round
    checks, maps, cases = {}, [], []
    for fixture in data['maps']:
        label = fixture['name']
        corridor = {(x, 0) for x in range(g.width)} | {(g.width - 1, y) for y in range(g.height)}
        turrets = {(x, y): kind for kind, x, y in fixture['turrets']}
        actions = []
        for y in range(g.height):
            for x in range(g.width):
                if (x, y) in corridor:
                    continue
                action = {'op': 'build_turret', 'type': turrets[x, y], 'x': x, 'y': y} if (x, y) in turrets else {'op': 'build_wall', 'x': x, 'y': y}
                actions.append(action)
        cost = sum(cfg.turrets[a['type']].cost if a['op'] == 'build_turret' else cfg.wall_cost for a in actions)
        engine = Engine(cfg, (label, 'idle'))
        prefix = []
        while engine.players[0].gold < cost:
            purchase = [{'op': 'buy_factory'}] * (engine.players[0].gold // g.factory_cost)
            records = engine.play_round([purchase, []])
            assert all(e['accepted'] for r in records for e in r['event'] if e['kind'] == 'action')
            prefix.append(purchase)
            assert engine.result is None
        records = engine.play_round([actions, []])
        checks[label + '_legal_construction'] = all(e['accepted'] for r in records for e in r['event'] if e['kind'] == 'action')
        defender = engine.players[0]
        blocked = {(b.x, b.y) for b in defender.buildings}
        route = shortest_path(g.width, g.height, blocked, g.spawn, g.base)
        assert route is not None
        length = len(route) - 1
        checks[label + '_full_map'] = len(blocked) + len(route) == g.width * g.height
        checks[label + '_declared_corridor'] = set(route) == corridor
        rejected = 0
        for y in range(g.height):
            for x in range(g.width):
                for kind in ['wall', *cfg.turrets]:
                    clone = deepcopy(defender)
                    # A component allowance removes affordability from this legality test.
                    clone.gold = max(clone.gold, 1000000)
                    before = asdict(clone)
                    action = {'op': 'build_wall', 'x': x, 'y': y} if kind == 'wall' else {'op': 'build_turret', 'type': kind, 'x': x, 'y': y}
                    result = apply_action(clone, action, engine.round + 1, cfg)
                    assert not result['accepted'], (label, action, result)
                    assert asdict(clone) == before
                    rejected += 1
        checks[label + '_all_constructions_rejected_without_mutation'] = rejected == g.width * g.height * (len(cfg.turrets) + 1)
        splash = 0
        gun_capacity = 0
        for building in defender.buildings:
            if building.type == 'wall':
                continue
            turret = cfg.turrets[building.type]
            if turret.aoe == 8:
                splash += turret.damage * sum(max(abs(x-building.x), abs(y-building.y)) == 1 for x, y in route[:-1])
            else:
                gun_capacity += turret.damage
        hp = cfg.minions['tier5'].hp
        assert splash < hp
        for count in data['roster_sizes']:
            for expired_prefix in (False, True):
                roster = [RosterEntry(900000, 'tier4', 1, 1)] if expired_prefix else []
                roster.extend(RosterEntry(1000 + 3*i, 'tier5', 2, None) for i in range(count))
                attacker = PlayerState('attacker', 800, 0, roster=roster)
                target = deepcopy(defender)
                target.hp = 1000000
                result = simulate_map(attacker, target, route, 2, cfg)
                eligible = (count // ticks) * (ticks - length) + min(count % ticks, ticks - length)
                death_bound = ticks * gun_capacity // (hp - splash)
                lower = max(0, eligible - death_bound)
                passed = result.hits >= lower and result.damage >= lower * cfg.minions['tier5'].damage and result.spawned == count and result.hits + result.killed + result.cleared == count
                if gun_capacity == 0:
                    passed = passed and result.hits == eligible and result.killed == 0 and result.cleared == count - eligible
                checks[f'{label}_{count}_expired{int(expired_prefix)}'] = passed
                cases.append({'map': label, 'active_count': count, 'expired_prefix': expired_prefix,
                    'route_steps': length, 'splash_exposure': splash, 'gun_damage_per_tick': gun_capacity,
                    'eligible_entries': eligible, 'selected_death_bound': death_bound,
                    'arrival_lower_bound': lower, 'actual': asdict(result), 'passed': passed})
        maps.append({'name': label, 'legal_factory_prefix': prefix, 'construction_actions': actions,
                     'constructed_in_round': engine.round, 'route': route, 'construction_rejections_checked': rejected,
                     'splash_exposure': splash, 'gun_damage_per_tick': gun_capacity})
    paths = set(static_closure({'bot_research.experiments.validation.check_full_map_capacity'}))
    paths.update((FIXTURES, PROOF, Path('td_game/balanced.json')))
    output = {'time_utc': now(), 'checks': checks, 'all_passed': all(checks.values()), 'maps': maps, 'cases': cases,
        'source_sha256': {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        'scope': 'Legally reached maps; exhaustive construction attempts with ample component gold; original-engine combat cases. The bound does not assert roster affordability or policy strength.'}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({'all_passed': output['all_passed'], 'checks': len(checks), 'combats': len(cases),
                      'construction_attempts': sum(m['construction_rejections_checked'] for m in maps)}))
    if not output['all_passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
