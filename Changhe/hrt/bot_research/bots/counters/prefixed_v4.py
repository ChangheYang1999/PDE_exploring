"""Known-development-opening wrappers for stateful V4 counter screens.

The target and its private model are called every round, including opening
rounds. The forecast trace covers actual submitted opening actions as well.
"""
from copy import deepcopy
from bot_research.harness.scenarios import make_overrides
from bot_research.bots.counters.snapshots.lead_fifteen_001 import Lead15
from bot_research.bots.counters.stateful_public import StatefulPublicTiming
from bot_research.bots.counters.stateful_schedule import StatefulSchedule

PARAMETERS = dict(big_threat=100, gun_cap=120, poke_until=3, big_partial=True,
                  r1_poke=3, attack_mode='adaptive', poke_reactive='turret',
                  fortress_n=4, immune_attack=True)
MODEL = 'bot_research.bots.counters.prefixed_v4:@lead15'


class OpeningPolicy:
    def __init__(self, policy, scenario):
        self.policy = policy
        self.overrides = make_overrides(scenario) if scenario else (None, None)
        self.calls = 0
        self.opening_calls = 0

    @property
    def trace(self):
        return getattr(self.policy, 'trace', [])

    def decide(self, observation):
        override = self.overrides[observation['player']]
        scripted = override(deepcopy(observation)) if override else None
        proposed = self.policy.decide(observation) if hasattr(self.policy, 'decide') else self.policy(observation)
        self.calls += 1
        self.opening_calls += scripted is not None
        return scripted if scripted is not None else proposed

    __call__ = decide


def lead15(scenario=None):
    return OpeningPolicy(Lead15(**PARAMETERS), scenario)


def timing(scenario=None, **parameters):
    policy = StatefulPublicTiming(model_spec=MODEL,
                                  model_parameters={'scenario': scenario}, **parameters)
    return OpeningPolicy(policy, scenario).decide


def schedule(scenario=None, **parameters):
    policy = StatefulSchedule(model_spec=MODEL,
                             model_parameters={'scenario': scenario}, **parameters)
    return OpeningPolicy(policy, scenario).decide
