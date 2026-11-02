"""Use isolated-copy route exposure to qualify the open-map attack signal.

The damage sum is exact for one isolated standard-speed copy on a fixed map.
Its use as an adaptation feature is heuristic: guns share their attacks across
multiple copies, and future defensive purchases remain unknown.
"""
from __future__ import annotations
from copy import deepcopy
from bot_research.bots.counters.guard_continuation import GuardContinuation
from bot_research.harness import gamekit as gk


def single_copy_exposure(buildings, rules):
    route = gk.route_cached(gk.cells_of(buildings))
    if route is None:
        raise ValueError('A legal map must have a route.')
    total = 0
    for building in buildings:
        if building['type'] == 'wall':
            continue
        turret = rules['turrets'][building['type']]
        offsets = [(x - building['x'], y - building['y']) for x, y in route[:-1]]
        if turret['aoe'] == 8:
            count = sum(max(abs(dx), abs(dy)) == 1 for dx, dy in offsets)
        else:
            count = sum(dx * dx + dy * dy <= turret['range'] ** 2 for dx, dy in offsets)
        total += count * turret['damage']
    return total


class ExposureGuard:
    def __init__(self, minimum_hp=70, continuation='economy15', parameters=None):
        if type(minimum_hp) is not int or minimum_hp < 1:
            raise ValueError('minimum_hp must be a positive integer.')
        self.minimum_hp = minimum_hp
        self.policy = GuardContinuation(continuation=continuation,
            parameters=({'free_fallback': 'leak'} if continuation == 'economy15' else {})
                       if parameters is None else parameters)

    def decide(self, observation):
        local = deepcopy(observation)
        opponent = local['players'][1 - local['player']]
        exposure = single_copy_exposure(opponent['buildings'], local['rules'])
        opponent['n_turrets'] = int(exposure >= self.minimum_hp)
        return self.policy.decide(local)


def make(**parameters):
    return ExposureGuard(**parameters).decide
