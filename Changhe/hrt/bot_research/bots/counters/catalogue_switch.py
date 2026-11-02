"""Public-observation changepoint opponents for adaptation stress tests.

These policies deliberately violate fixed catalogue membership. They choose
between already public, reconstructible decision rules using only the round.
No held-out profile is used.
"""
from __future__ import annotations
from bot_research.bots.counters.identifying_counter import CATALOGUE
from bot_research.bots.counters.known_policy import ObservationModel as LegacyModel
from bot_research.bots.counters.known_frontier import ObservationModel as FrontierModel
from bot_research.bots.counters.archetypes import make as archetype


def decision_rule(name):
    for key,family,model,parameters in CATALOGUE:
        if key==name:
            return (LegacyModel if family=='known' else FrontierModel)(model,parameters)
    if name.startswith('archetype:'):
        return archetype(name.partition(':')[2]).decide
    raise ValueError('Unknown development decision rule: '+name)


class CatalogueSwitch:
    def __init__(self,prefix='economy',after='archetype:eco6_t5',switch_round=7,period=0):
        self.prefix=decision_rule(prefix)
        self.after=decision_rule(after)
        self.switch_round=int(switch_round)
        self.period=int(period)
        self.trace=[]

    def decide(self,observation):
        rnd=observation['round']
        after=rnd>=self.switch_round
        if after and self.period>0:
            after=((rnd-self.switch_round)//self.period)%2==0
        self.trace.append({'round':rnd,'phase':'after' if after else 'prefix'})
        return (self.after if after else self.prefix)(observation)


def make(**parameters):
    return CatalogueSwitch(**parameters).decide
