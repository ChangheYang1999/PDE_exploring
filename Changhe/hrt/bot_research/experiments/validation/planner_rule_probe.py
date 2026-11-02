"""Check two numerical bounds used in archived lead Planner v1."""
from __future__ import annotations
import itertools
import json
from datetime import datetime, timezone
from pathlib import Path
from td_game.config import balanced_config
from td_game.engine import Engine
from td_game.combat import simulate_map
from td_game.state import PlayerState, RosterEntry
from bot_research.harness import gamekit as gk
from bot_research.bots.counters.snapshots.lead_planner_001 import Planner, WALLS, SLOTS
from bot_research.experiments.validation.evaluate import source_hashes


def main():
    config = balanced_config()
    obs = Engine(config, ('A', 'B')).observation(0)
    rules = gk.Rules.from_observation(obs)
    slots = set(SLOTS)
    all_cells = set(WALLS) | slots
    max_case = None
    cases = 0
    for n in (1, 2, 3):
        for missing in itertools.combinations(SLOTS, n):
            occupied = all_cells - set(missing)
            buildings = [{'x': x, 'y': y, 'type': 'splash' if (x, y) in slots else 'wall'}
                         for x, y in sorted(occupied)]
            path = gk.route_cached(occupied)
            initial = gk.splash_total(path, buildings, rules)
            for cell in missing:
                final_buildings = buildings + [{'type': 'splash', 'x': cell[0], 'y': cell[1]}]
                final_path = gk.route_cached(occupied | {cell})
                final = gk.splash_total(final_path, final_buildings, rules)
                cases += 1
                row = {'before_buildings': buildings, 'add_splash': list(cell),
                       'before_route': path, 'after_route': final_path,
                       'before_splash': initial, 'after_splash': final, 'increase': final-initial}
                if max_case is None or row['increase'] > max_case['increase']:
                    max_case = row
    planner = Planner()
    bound_cases = []
    for gold in (1500, 7500, 15000):
        n = gold // rules.minions['tier1']['cost']
        path = gk.route_cached(set())
        actual = gk.simulate_defense(['tier1']*n, path, [], rules)
        predicted = planner._potential_damage(0, gold, len(path)-1, 0, rules)
        bound_cases.append({'gold': gold, 'pure_tier1_count': n,
                            'planner_potential': predicted, 'pure_tier1_actual': actual.damage})
    result = {'time_utc': datetime.now(timezone.utc).isoformat(), 'sources': source_hashes(),
              'route_change_conditions': cases, 'largest_one_splash_change': max_case,
              'potential_damage_cases': bound_cases,
              'scope': 'synthetic legal maps and rosters, not complete-game strength'}
    with Path('bot_research/runs/validation/planner-rule-probe-001.json').open('x') as stream:
        json.dump(result, stream, sort_keys=True, indent=2)
        stream.write('\n')
    print(json.dumps({'route_change_conditions': cases,
                      'largest_increase': max_case['increase'], 'potential_damage_cases': bound_cases}))


if __name__ == '__main__':
    main()
