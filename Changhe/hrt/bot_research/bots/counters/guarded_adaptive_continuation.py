"""Replace only the opening of the existing adaptive catalogue continuation.

All catalogue clones are advanced on the opening observation. Later actions
are exactly the unchanged parent policy on this game's actual observations.
"""
from copy import deepcopy

from bot_research.bots.counters.adaptive_continuation import AdaptiveContinuation
from bot_research.bots.counters.guard_geometry import GuardGeometry


class GuardedAdaptiveContinuation(AdaptiveContinuation):
    def __init__(self, roster=('tier1',), x=10, y=1, **parameters):
        super().__init__(**parameters)
        self.opening = GuardGeometry(roster=roster, x=x, y=y)

    def decide(self, observation):
        actions = super().decide(observation)
        if observation['round'] != 1:
            return actions
        trace = self.trace[-1]
        trace['discarded_opening_proposal'] = {
            key: deepcopy(trace[key]) for key in
            ('adaptive_attack', 'defense', 'attack_count', 'attack_tier', 'attack_gains')
        }
        actions = self.opening.decide(observation)
        trace['guarded_opening'] = dict(
            roster=list(self.opening.roster), x=self.opening.x, y=self.opening.y)
        trace['adaptive_attack'] = dict(enabled=False, reason='prescribed_guard_opening')
        trace['defense'] = None
        trace['attack_count'] = sum(a['op'] == 'buy_minion' for a in actions)
        trace['attack_tier'] = 'prescribed_opening'
        trace['attack_gains'] = []
        return actions


def make(**parameters):
    return GuardedAdaptiveContinuation(**parameters).decide
