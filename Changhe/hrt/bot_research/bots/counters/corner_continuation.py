"""A checked gun opening with an explicitly selected frozen continuation.

The opening is inherited unchanged from GuardGeometry. Economy19 adds the
capacity-race and saturation-reachability heuristics. A failed heuristic search
for immunity is not treated here as a proof that immunity is impossible.
"""
from bot_research.bots.counters.guard_geometry import GuardGeometry
from bot_research.bots.economy.frozen.v17.econ17 import make as economy17
from bot_research.bots.economy.frozen.v19.econ19 import make as economy19


class GuardContinuation:
    def __init__(self, roster=('tier1',), x=9, y=1, version='econ19', parameters=None):
        if version not in ('econ17', 'econ19'):
            raise ValueError('Unknown frozen continuation.')
        self.factory = economy17 if version == 'econ17' else economy19
        self.parameters = dict(free_fallback='zero', foreign_attack_from=11)
        if version == 'econ19':
            self.parameters.update(doom='next', fac_cap=400, sat_reach=True)
        self.parameters.update(parameters or {})
        self.opening = GuardGeometry(roster=roster, x=x, y=y)
        self.policy = self.factory(**self.parameters)

    def decide(self, observation):
        if observation['round'] == 1:
            self.policy = self.factory(**self.parameters)
            return self.opening.decide(observation)
        return self.policy(observation)


def make(**parameters):
    return GuardContinuation(**parameters).decide
