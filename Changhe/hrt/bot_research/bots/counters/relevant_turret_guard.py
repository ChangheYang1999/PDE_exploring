"""Cheap guard with a geometric filter on its opponent-turret signal.

All buildings remain visible to planning and simulation. Only the feature
that activates the continuation's conservative attack mode is filtered:
a turret counts when at least one nonterminal cell of the current enemy
route lies in its attack region. This is a new policy, not a change to the
engine observation. Current coverage does not establish effective defense
against a particular roster or against future route changes.
"""
from __future__ import annotations
from copy import deepcopy
from bot_research.bots.counters.guard_continuation import GuardContinuation
from bot_research.harness import gamekit as gk


def covered_turret_count(observation):
    opponent = observation['players'][1 - observation['player']]
    route = gk.route_cached(gk.cells_of(opponent['buildings']))
    if route is None:
        raise ValueError('Valid observations must have a route.')
    catalog = observation['rules']['turrets']
    count = 0
    for building in opponent['buildings']:
        if building['type'] not in catalog:
            continue
        turret = catalog[building['type']]
        deltas = [(x - building['x'], y - building['y']) for x, y in route[:-1]]
        if turret['aoe'] == 8:
            covered = any(max(abs(dx), abs(dy)) == 1 for dx, dy in deltas)
        else:
            covered = any(dx * dx + dy * dy <= turret['range'] ** 2 for dx, dy in deltas)
        count += covered
    return count


class RelevantTurretGuard:
    def __init__(self, filter_signal=True, continuation='economy15', parameters=None):
        self.filter_signal = bool(filter_signal)
        self.policy = GuardContinuation(continuation=continuation,
            parameters=({'free_fallback': 'leak'} if continuation == 'economy15' else {})
                       if parameters is None else parameters)

    def decide(self, observation):
        if not self.filter_signal:
            return self.policy.decide(observation)
        local = deepcopy(observation)
        local['players'][1 - local['player']]['n_turrets'] = covered_turret_count(observation)
        return self.policy.decide(local)


def make(**parameters):
    return RelevantTurretGuard(**parameters).decide
