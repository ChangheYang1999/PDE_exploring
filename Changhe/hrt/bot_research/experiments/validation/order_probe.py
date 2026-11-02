"""Test whether roster order changes damage at fixed cost and composition."""
from __future__ import annotations
import argparse
from collections import Counter
import json
from pathlib import Path
from td_game.actions import apply_action
from td_game.combat import simulate_map
from td_game.config import balanced_config
from td_game.pathfinding import shortest_path
from td_game.state import PlayerState, RosterEntry


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    cfg = balanced_config()
    maps = {
        'gun_line': [('gun2', x, 1) for x in (1, 4, 7, 10)],
        'gun_cluster': [('gun3', x, 1) for x in (1, 2, 3)],
        'mixed': [('splash', 1, 1), ('gun2', 4, 1), ('gun2', 7, 1)],
        'splash_line': [('splash', x, 1) for x in (1, 4, 7, 10)],
    }
    cases = []
    for light in ('tier1', 'tier2', 'tier3'):
        for heavy in ('tier4', 'tier5'):
            for count in (10, 100, 250, 500):
                hcount = max(1, count // 10)
                front = [heavy] * hcount + [light] * count
                back = [light] * count + [heavy] * hcount
                interleave = []
                for k in range(count):
                    if k % 10 == 0:
                        interleave.append(heavy)
                    interleave.append(light)
                assert Counter(interleave) == Counter(front)
                cases.append((light, heavy, count, [('heavy_front', front), ('heavy_back', back), ('interleave', interleave)]))
    with Path(args.output).open('x') as stream:
        for map_name, towers in maps.items():
            for light, heavy, count, orders in cases:
                for order_name, roster in orders:
                    defender = PlayerState('defender', 800, 100000)
                    for tier, x, y in towers:
                        assert apply_action(defender, {'op': 'build_turret', 'type': tier, 'x': x, 'y': y}, 1, cfg)['accepted']
                    route = shortest_path(12, 12, [(b.x, b.y) for b in defender.buildings], (0, 0), (11, 11))
                    attacker = PlayerState('attacker', 800, 0,
                        roster=[RosterEntry(i, tier, 1, 12) for i, tier in enumerate(roster)])
                    result = simulate_map(attacker, defender, route, 1, cfg)
                    record = {'map': map_name, 'towers': towers, 'light': light, 'heavy': heavy, 'light_count': count,
                        'composition': dict(Counter(roster)), 'order': order_name,
                        'damage': result.damage, 'hits': result.hits, 'killed': result.killed, 'cleared': result.cleared,
                        'cost': sum(cfg.minions[t].cost for t in roster)}
                    stream.write(json.dumps(record, sort_keys=True) + '\n')
                    stream.flush()
    print(args.output)


if __name__ == '__main__':
    main()
