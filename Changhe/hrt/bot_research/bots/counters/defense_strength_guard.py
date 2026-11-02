"""Use visible in-range turret expenditure to qualify the open-map signal.

The threshold is a policy feature, not a lower bound on defensive strength.
Physical buildings and all other observation fields stay intact. The inherited
continuation remembers any qualified turret observation for the rest of a game.
"""
from __future__ import annotations
from copy import deepcopy
from bot_research.bots.counters.guard_continuation import GuardContinuation
from bot_research.harness import gamekit as gk


def covered_turret_cost(observation):
    opponent = observation['players'][1 - observation['player']]
    route = gk.route_cached(gk.cells_of(opponent['buildings']))
    if route is None:
        raise ValueError('Valid observations must have a route.')
    catalog = observation['rules']['turrets']
    total = 0
    for building in opponent['buildings']:
        if building['type'] not in catalog:
            continue
        turret = catalog[building['type']]
        offsets = [(x - building['x'], y - building['y']) for x, y in route[:-1]]
        if turret['aoe'] == 8:
            covered = any(max(abs(dx), abs(dy)) == 1 for dx, dy in offsets)
        else:
            covered = any(dx * dx + dy * dy <= turret['range'] ** 2 for dx, dy in offsets)
        if covered:
            total += turret['cost']
    return total


class DefenseStrengthGuard:
    def __init__(self, minimum_cost=60, continuation='economy15', parameters=None):
        if type(minimum_cost) is not int or minimum_cost < 0:
            raise ValueError('minimum_cost must be a nonnegative integer.')
        self.minimum_cost = minimum_cost
        self.policy = GuardContinuation(continuation=continuation,
            parameters=({'free_fallback': 'leak'} if continuation == 'economy15' else {})
                       if parameters is None else parameters)

    def decide(self, observation):
        local = deepcopy(observation)
        cost = covered_turret_cost(observation)
        local['players'][1 - local['player']]['n_turrets'] = int(cost > 0 and cost >= self.minimum_cost)
        return self.policy.decide(local)


def make(**parameters):
    return DefenseStrengthGuard(**parameters).decide
