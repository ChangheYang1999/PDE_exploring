"""Integer gun-support certificates for fixed maps, with full-map scope checks.

The accompanying informal proof is analysis/fixed_gun_support/PROOF.md.
No strength, survival, affordability or changing-map guarantee is implicit.
"""
from __future__ import annotations
from dataclasses import dataclass
from td_game.config import config_from_dict
from td_game.pathfinding import shortest_path


@dataclass(frozen=True)
class FixedMap:
    ticks: int
    length: int
    splash: int
    guns: tuple[tuple[int, int], ...]
    full: bool


def describe(buildings, rules):
    config = config_from_dict(rules)
    grid = config.globals
    for building in buildings:
        x, y = building['x'], building['y']
        if type(x) is not int or type(y) is not int or not (0 <= x < grid.width and 0 <= y < grid.height):
            raise ValueError('Building coordinates must be in-grid integers.')
        if (x, y) in (grid.spawn, grid.base):
            raise ValueError('Spawn and base cannot contain buildings.')
        if building['type'] != 'wall' and building['type'] not in config.turrets:
            raise ValueError('Unknown building type.')
    blocked = {(b['x'], b['y']) for b in buildings}
    if len(blocked) != len(buildings):
        raise ValueError('Building cells must be distinct.')
    path = shortest_path(grid.width, grid.height, blocked, grid.spawn, grid.base)
    if path is None:
        raise ValueError('A legal selected route is required.')
    length = len(path) - 1
    if not 0 < length < grid.ticks_per_round:
        raise ValueError('The route must permit an arrival in this horizon.')
    splash = 0
    guns = []
    for building in buildings:
        kind = building['type']
        if kind == 'wall':
            continue
        turret = config.turrets[kind]
        x, y = building['x'], building['y']
        if turret.aoe == 8:
            splash += turret.damage * sum(max(abs(px-x), abs(py-y)) == 1
                                           for px, py in path[:-1])
        else:
            mask = sum(1 << i for i, (px, py) in enumerate(path[:-1])
                       if (px-x)**2 + (py-y)**2 <= turret.range**2)
            guns.append((turret.damage, mask))
    return FixedMap(grid.ticks_per_round, length, splash, tuple(guns),
                    len(blocked) + len(path) == grid.width * grid.height)


def phase_table(mapping, existing):
    """n and C for every prefix through one complete dense spawn cycle."""
    if type(existing) is not int or existing < 0:
        raise ValueError('Existing active-entry count must be a nonnegative int.')
    support = [0] * len(mapping.guns)
    counts = [0]
    capacities = [0]
    count = 0
    for j in range(mapping.ticks):
        birth = (existing + j) % mapping.ticks
        if birth + mapping.length < mapping.ticks:
            count += 1
            for index, (_, mask) in enumerate(mapping.guns):
                support[index] |= mask << birth
        counts.append(count)
        capacities.append(sum(damage * mask.bit_count()
                              for (damage, _), mask in zip(mapping.guns, support)))
    return counts, capacities


def lower_bound(mapping, existing, count, hp, damage):
    if type(count) is not int or count < 0:
        raise ValueError('Package count must be a nonnegative int.')
    if hp <= mapping.splash:
        return {'applicable': False, 'damage_lower_bound': 0,
                'reason': 'HP does not exceed splash exposure.'}
    counts, capacities = phase_table(mapping, existing)
    cycles, remainder = divmod(count, mapping.ticks)
    eligible = cycles * counts[-1] + counts[remainder]
    capacity = capacities[-1] if cycles else capacities[remainder]
    kill_bound = capacity // (hp - mapping.splash)
    hits = max(0, eligible - kill_bound)
    return {'applicable': True, 'count': count, 'existing_active': existing,
            'eligible': eligible, 'gun_capacity': capacity,
            'gun_death_bound': kill_bound, 'arrival_lower_bound': hits,
            'damage_lower_bound': damage * hits,
            'response_robust': mapping.full, 'splash_exposure': mapping.splash,
            'route_steps': mapping.length}


def minimum_count(mapping, existing, hp, damage, required_damage):
    """Least count meeting this certificate; not least actual damaging count."""
    if damage <= 0 or required_damage <= 0:
        raise ValueError('Positive unit and requested base damage required.')
    if hp <= mapping.splash:
        return None
    counts, capacities = phase_table(mapping, existing)
    need = (required_damage + damage - 1) // damage
    residual = hp - mapping.splash
    early = [n for n in range(mapping.ticks)
             if counts[n] - capacities[n] // residual >= need]
    if early:
        count = early[0]
    else:
        full_deaths = capacities[-1] // residual
        per_cycle = counts[-1]
        candidates = []
        for remainder in range(mapping.ticks):
            q = max(1, (need + full_deaths - counts[remainder] + per_cycle - 1) // per_cycle)
            candidates.append(q * mapping.ticks + remainder)
        count = min(candidates)
    return lower_bound(mapping, existing, count, hp, damage)


def certified_purchase(observation, budget, required_damage, *, require_full=True):
    """Cheapest sufficient homogeneous append among the catalog types.

    Default full-map requirement makes the certificate robust to legal same-round
    defender actions. A caller must still establish its own defensive survival.
    """
    config = config_from_dict(observation['rules'])
    side = observation['player']
    me, defender = observation['players'][side], observation['players'][1-side]
    mapping = describe(defender['buildings'], observation['rules'])
    if require_full and not mapping.full:
        return None
    rnd = observation['round']
    existing = sum(e['bought_round'] <= rnd and
                   (e.get('expires_after_round') is None or e['expires_after_round'] >= rnd)
                   for e in me['roster'])
    choices = []
    for kind, unit in config.minions.items():
        certificate = minimum_count(mapping, existing, unit.hp, unit.damage, required_damage)
        if certificate is None:
            continue
        cost = certificate['count'] * unit.cost
        if cost <= budget:
            choices.append((cost, certificate['count'], kind, certificate))
    if not choices:
        return None
    cost, count, kind, certificate = min(choices)
    return {**certificate, 'type': kind, 'cost': cost,
            'required_damage': required_damage,
            'scope': 'all legal defender submissions' if mapping.full else 'fixed current map only'}
