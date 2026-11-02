"""Extended adaptive development catalogue, with approximate timed models.

Later fortress and economy policies use wall-clock-bounded planners. Their
predictions are hypotheses, not deterministic-forecast certificates. The
same exact observed-signature filter is used, with reset on contradiction.
"""
from __future__ import annotations
from bot_research.bots.counters.identifying_counter import IdentifyingCounter
from bot_research.bots.counters.archetypes import make as archetype
from bot_research.bots.defense.frozen.v11.fortress import make as fortress11
from bot_research.bots.economy.frozen.v6.econ6 import make as economy6
from bot_research.bots.economy.frozen.v7.econ7 import make as economy7


class FreshPolicy:
    def __init__(self,factory,parameters=None):
        self.factory=factory
        self.parameters=dict(parameters or {})

    def __call__(self,observation):
        # The sole economy flag, ever-owned-turrets, is reconstructed by the
        # policy from current n_turrets. Buildings cannot be removed.
        return self.factory(**self.parameters)(observation)


class FrontierIdentifier(IdentifyingCounter):
    def __init__(self,opening='factories',include_archetypes=True,**parameters):
        if opening not in ('factories','robust','tier1','tier2','tier3'):
            raise ValueError('Unknown opening.')
        super().__init__(**parameters)
        self.opening=opening
        self.models.update({
            'fortress11':FreshPolicy(fortress11),
            'fortress11_annealed':FreshPolicy(fortress11,{'layout':'annealed25'}),
            'economy6':FreshPolicy(economy6),
            'economy7':FreshPolicy(economy7),
        })
        if include_archetypes:
            for name in ('rush_t1','rush_t2','rush_t3','eco6_t5','mixed5'):
                self.models[name]=archetype(name).decide
        self.active=list(self.models)

    def decide(self,observation):
        actions=super().decide(observation)
        if observation['round']!=1 or self.opening=='robust':
            return actions
        rules=observation['rules']
        gold=observation['players'][observation['player']]['gold']
        actions=[]
        if self.opening!='factories':
            cost=rules['minions'][self.opening]['cost']
            if gold>=cost:
                actions.append({'op':'buy_minion','type':self.opening})
                gold-=cost
        actions.extend([{'op':'buy_factory'}]*(gold//rules['globals']['factory_cost']))
        return actions


def make(**parameters):
    return FrontierIdentifier(**parameters).decide
