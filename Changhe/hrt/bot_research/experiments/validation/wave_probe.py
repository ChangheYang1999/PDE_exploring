"""Mechanics probes on fixed legal maps, not whole-match strength evidence."""
from __future__ import annotations
import argparse
import json
import time
from datetime import datetime, timezone
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
        'one_gun1': [('gun1', 1, 1)],
        'three_gun1': [('gun1', 1, 1), ('gun1', 2, 1), ('gun1', 3, 1)],
        'one_gun3': [('gun3', 1, 1)],
        'three_gun3': [('gun3', 1, 1), ('gun3', 2, 1), ('gun3', 3, 1)],
        'one_splash': [('splash', 1, 1)],
        'three_splash': [('splash', 1, 1), ('splash', 4, 1), ('splash', 7, 1)],
        'mixed': [('splash', 1, 1), ('gun3', 4, 1), ('gun3', 7, 1)],
    }
    with Path(args.output).open('x') as stream:
        for name, towers in maps.items():
            for tier in cfg.minions:
                for count in (1, 5, 20, 100, 228, 250, 251, 500, 750):
                    defender = PlayerState('fixed_defense', 800, 100000)
                    for kind, x, y in towers:
                        result = apply_action(defender, {'op': 'build_turret', 'type': kind, 'x': x, 'y': y}, 1, cfg)
                        assert result['accepted']
                    route = shortest_path(12, 12, [(b.x, b.y) for b in defender.buildings], (0, 0), (11, 11))
                    attacker = PlayerState('fixed_wave', 800, 0,
                                roster=[RosterEntry(i, tier, 1, 12) for i in range(count)])
                    started = time.perf_counter()
                    result = simulate_map(attacker, defender, route, 1, cfg)
                    row = {'time_utc': datetime.now(timezone.utc).isoformat(), 'map': name,
                           'towers': towers, 'defense_cost': 100000 - defender.gold,
                           'tier': tier, 'count': count, 'attack_cost': count * cfg.minions[tier].cost,
                           'path_length': len(route) - 1, 'hits': result.hits, 'damage': result.damage,
                           'killed': result.killed, 'cleared': result.cleared,
                           'runtime_seconds': time.perf_counter() - started}
                    stream.write(json.dumps(row, sort_keys=True) + '\n')
                    stream.flush()
    print(args.output)


if __name__ == '__main__':
    main()
