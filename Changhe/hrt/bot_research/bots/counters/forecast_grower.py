"""Declared growth and flood policy with delayed public-model defense.

This probes whether cheap prediction-based defense preserves a passive grower's
advantage against an adaptive target. It is a targeted development counter.
All construction and purchase proposals are checked on a private player copy.
"""
from __future__ import annotations
from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.forecast_timing import predict
from bot_research.bots.counters.stateful_public import PersistentFactoryModel
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.bots.economy.frozen.v2.defense_plan import defend


class ForecastGrower:
    def __init__(self, model_spec, model_parameters=None, turret_round=2,
                 defend_from=6, growth_rounds=6, tier='tier5',
                 factory_cap=2000, purchase_cap=1000):
        self.model=PersistentFactoryModel(model_spec,model_parameters)
        self.turret_round=int(turret_round)
        self.defend_from=int(defend_from)
        self.growth_rounds=int(growth_rounds)
        self.tier=str(tier)
        self.factory_cap=int(factory_cap)
        self.purchase_cap=int(purchase_cap)
        self.trace=[]
        if min(self.turret_round,self.defend_from,self.growth_rounds,self.factory_cap,self.purchase_cap)<0:
            raise ValueError('Round and purchase limits must be nonnegative.')
        if self.tier not in ('tier1','tier2','tier3','tier4','tier5'):
            raise ValueError('Unknown minion tier.')

    def decide(self, observation):
        rnd=observation['round']
        predicted,enemy=predict(observation,self.model)
        state=player_from_snapshot(observation['players'][observation['player']])
        rules=observation['rules']
        config=config_from_dict(rules)
        actions=[]
        attempted=0
        rejected=0

        def add(action):
            nonlocal attempted,rejected
            attempted+=1
            accepted=apply_action(state,action,rnd,config)['accepted']
            if accepted:
                actions.append(action)
            else:
                rejected+=1
            return accepted

        if rnd==self.turret_round:
            add({'op':'build_turret','type':'gun1','x':0,'y':11})
        residual=None
        if rnd>=self.defend_from:
            buildings=[(b.x,b.y,b.type) for b in state.buildings]
            threat=[e.type for e in enemy.roster if e.active(rnd)]
            proposals,_,_,residual=defend(buildings,state.gold,threat,0,rules,reserve=1600)
            for action in proposals:
                if not add(action):
                    raise ValueError('Defense proposal failed private legality check.')
        count=0
        if rnd<=self.growth_rounds:
            maximum=min(max(0,self.factory_cap-state.n_factories),state.gold//config.globals.factory_cost)
            for _ in range(maximum):
                if not add({'op':'buy_factory'}):
                    raise ValueError('Factory proposal failed private legality check.')
        else:
            maximum=min(self.purchase_cap,state.gold//config.minions[self.tier].cost)
            for _ in range(maximum):
                if not add({'op':'buy_minion','type':self.tier}):
                    raise ValueError('Minion proposal failed private legality check.')
                count+=1
        self.trace.append({'round':rnd,'predicted_actions':predicted,'attack_count':count,
                           'attack_tier':self.tier,'forecast_residual_damage':residual,
                           'private_legality_attempts':attempted,'private_legality_rejections':rejected})
        return actions


def make(**parameters):
    return ForecastGrower(**parameters).decide
