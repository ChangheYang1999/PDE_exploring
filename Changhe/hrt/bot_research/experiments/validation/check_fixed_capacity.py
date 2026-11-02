"""Independent set-based and original-combat checks of gun-support bounds."""
from __future__ import annotations
import argparse
from collections import Counter
from dataclasses import asdict
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import time
from td_game.actions import apply_action
from td_game.combat import spawn_schedule, combat_tick
from td_game.config import balanced_config
from td_game.pathfinding import shortest_path
from td_game.state import Building, PlayerState, RosterEntry
from bot_research.bots.counters.fixed_capacity import describe, phase_table, minimum_count, lower_bound
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation import now
from bot_research.experiments.validation.source_closure import static_closure

CONDITIONS = Path('bot_research/experiments/validation/analysis/fixed_gun_support/verification/conditions.json')
PROOF = Path('bot_research/experiments/validation/analysis/fixed_gun_support/PROOF.md')


def set_bound(path, buildings, existing, n, hp, cfg):
    # Explicit coordinate sets, independent of the bit-mask implementation.
    starts = {(existing+j) % cfg.globals.ticks_per_round for j in range(n)
              if (existing+j) % cfg.globals.ticks_per_round + len(path)-1 < cfg.globals.ticks_per_round}
    eligible = sum((existing+j) % cfg.globals.ticks_per_round + len(path)-1 < cfg.globals.ticks_per_round
                   for j in range(n))
    exposure = capacity = 0
    for building in buildings:
        if building.type == 'wall':
            continue
        turret = cfg.turrets[building.type]
        if turret.aoe == 8:
            exposure += turret.damage * sum(max(abs(x-building.x), abs(y-building.y)) == 1 for x, y in path[:-1])
        else:
            indices = [i for i, (x, y) in enumerate(path[:-1])
                       if (x-building.x)**2 + (y-building.y)**2 <= turret.range**2]
            times = {s+i for s in starts for i in indices}
            capacity += turret.damage * len(times)
    return eligible, capacity, max(0, eligible-capacity//(hp-exposure)) if hp > exposure else 0


def actual_package_damage(buildings, existing, count, tier, cycle, cfg):
    defender = PlayerState('defender', 10**8, 0, buildings=deepcopy(buildings))
    path = shortest_path(cfg.globals.width, cfg.globals.height,
                         {(b.x, b.y) for b in buildings}, cfg.globals.spawn, cfg.globals.base)
    roster = [RosterEntry(-1, 'tier5', 1, 1)]  # expired, must not occupy a phase
    roster += [RosterEntry(1000+3*j, cycle[j % len(cycle)], 2, None) for j in range(existing)]
    selected_ids = set(range(100000, 100000+count))
    roster += [RosterEntry(i, tier, 2, None) for i in sorted(selected_ids)]
    schedule = spawn_schedule(roster, 2, cfg.globals.ticks_per_round)
    entities = []
    package_damage = 0
    total = Counter()
    for tick, spawning in enumerate(schedule):
        arriving = [e for e in entities if e.born_tick < tick and e.path_index+1 == len(path)-1]
        package_damage += sum(e.damage for e in arriving if e.roster_id in selected_ids)
        entities, stats = combat_tick(tick, entities, spawning, path, defender, cfg)
        assert stats.damage == sum(e.damage for e in arriving)
        total.update(asdict(stats))
    assert total['damage'] == 10**8-defender.hp
    return package_damage, dict(total)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    conditions = json.loads(CONDITIONS.read_text())
    fixtures = json.loads(Path(conditions['source_maps']).read_text())
    cfg = balanced_config()
    rules = cfg.to_dict()
    tier = conditions['combat_tier']
    unit = cfg.minions[tier]
    started = time.perf_counter()
    maps, tables, minima, combats = [], [], [], []
    for fixture in fixtures['maps']:
        corridor = {(x, 0) for x in range(cfg.globals.width)} | {(cfg.globals.width-1, y) for y in range(cfg.globals.height)}
        turrets = {(x, y): kind for kind, x, y in fixture['turrets']}
        defender = PlayerState(fixture['name'], 10**8, 10**8)
        for y in range(cfg.globals.height):
            for x in range(cfg.globals.width):
                if (x, y) in corridor:
                    continue
                action = ({'op': 'build_turret', 'type': turrets[x, y], 'x': x, 'y': y}
                          if (x, y) in turrets else {'op': 'build_wall', 'x': x, 'y': y})
                assert apply_action(defender, action, 1, cfg)['accepted']
        buildings = [asdict(b) for b in defender.buildings]
        path = shortest_path(cfg.globals.width, cfg.globals.height,
                             {(b.x, b.y) for b in defender.buildings}, cfg.globals.spawn, cfg.globals.base)
        mapping = describe(buildings, rules)
        assert mapping.full
        maps.append({'name': fixture['name'], 'mapping': asdict(mapping), 'buildings': buildings})
        for offset in conditions['table_offsets']:
            counts, capacities = phase_table(mapping, offset)
            independent = [set_bound(path, defender.buildings, offset, n, unit.hp, cfg)
                           for n in range(cfg.globals.ticks_per_round+1)]
            assert counts == [r[0] for r in independent]
            assert capacities == [r[1] for r in independent]
            tables.append({'map': fixture['name'], 'offset': offset,
                           'checked_prefixes': len(independent), 'full_capacity': capacities[-1]})
            for required in conditions['requested_damage']:
                certificate = minimum_count(mapping, offset, unit.hp, unit.damage, required)
                assert certificate is not None
                # Enumerate every smaller package against independently formed supports.
                # Periodic counts are evaluated by direct index iteration in set_bound.
                n = certificate['count']
                brute = [set_bound(path, defender.buildings, offset, k, unit.hp, cfg)[2] * unit.damage
                         for k in range(n+1)]
                assert brute[n] >= required and all(d < required for d in brute[:n])
                assert certificate['damage_lower_bound'] == brute[n]
                minima.append({'map': fixture['name'], 'offset': offset,
                               'required_damage': required, 'certificate': certificate,
                               'smaller_counts_excluded': n})
        for offset in conditions['combat_offsets']:
            for count in conditions['combat_counts']:
                certificate = lower_bound(mapping, offset, count, unit.hp, unit.damage)
                observed, totals = actual_package_damage(defender.buildings, offset, count, tier,
                                                          conditions['prefix_cycle'], cfg)
                assert certificate['damage_lower_bound'] <= observed
                combats.append({'map': fixture['name'], 'offset': offset, 'count': count,
                                'certificate': certificate, 'actual_package_damage': observed,
                                'totals': totals})
                print(json.dumps({'map': fixture['name'], 'offset': offset, 'count': count,
                                  'bound': certificate['damage_lower_bound'], 'actual': observed}), flush=True)
    paths = set(static_closure({'bot_research.experiments.validation.check_fixed_capacity'}))
    paths.update((CONDITIONS, PROOF, Path(conditions['source_maps']), Path('td_game/balanced.json')))
    result = {'time_utc': now(), 'runtime_seconds': time.perf_counter()-started,
              'all_passed': True, 'maps': maps, 'tables': tables, 'minima': minima, 'combats': combats,
              'source_sha256': {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
              'scope': 'Finite component checks on legal full maps, not policy outcomes. Independent set unions, brute minimum search and original combat code. No claim of least actual lethal package.'}
    atomic_json(args.output, result, exclusive=True)
    print(json.dumps({k: result[k] for k in ('time_utc', 'runtime_seconds', 'all_passed')}))


if __name__ == '__main__':
    main()
