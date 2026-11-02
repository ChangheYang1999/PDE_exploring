"""A finite-catalogue identifier with an explicit first-round growth policy.

The inner identifier still observes round 1 and predicts the enemy's action.
Only its own first submission is replaced. Subsequent decisions use the
actual public state, preserving the identification hypothesis on that state.
"""
from __future__ import annotations
from bot_research.bots.counters.identifying_counter import IdentifyingCounter


class OpeningIdentifier:
    def __init__(self,opening='factories',**parameters):
        if opening not in ('factories','tier1','tier2','tier3'):
            raise ValueError('Unknown first-round opening.')
        self.opening=opening
        self.inner=IdentifyingCounter(**parameters)

    @property
    def trace(self):
        return self.inner.trace

    def decide(self,observation):
        actions=self.inner.decide(observation)
        if observation['round']!=1:
            return actions
        gold=observation['players'][observation['player']]['gold']
        rules=observation['rules']
        actions=[]
        if self.opening!='factories':
            cost=rules['minions'][self.opening]['cost']
            if gold>=cost:
                actions.append({'op':'buy_minion','type':self.opening})
                gold-=cost
        actions.extend([{'op':'buy_factory'}]*(gold//rules['globals']['factory_cost']))
        return actions


def make(**parameters):
    return OpeningIdentifier(**parameters).decide
