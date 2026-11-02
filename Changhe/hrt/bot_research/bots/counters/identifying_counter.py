"""Identify a fixed public policy from observed purchases, then forecast it.

Catalogue membership is an explicit experimental assumption. Elimination is
exact inside the catalogue; defense, attack valuation and reset after an
unexpected observation are heuristics. See the standalone proof in
experiments/validation/analysis/model_identification/PROOF.md.
"""
from __future__ import annotations
from bot_research.bots.counters.forecast_timing import predict
from bot_research.bots.counters.known_policy import ObservationModel as LegacyModel
from bot_research.bots.counters.known_frontier import ObservationModel as FrontierModel
from bot_research.bots.economy.frozen.v2.defense_plan import defend, saturate
from bot_research.bots.economy.frozen.v2.fastsim import MapModel, simulate
from bot_research.bots.economy.frozen.v2.threat import active_types

CATALOGUE = (
    ('planner', 'known', 'planner003', {}),
    ('economy', 'known', 'econ_v4', {'late_round':6,'phi':0.0}),
    ('economy_guard', 'known', 'econ_v4',
     {'late_round':6,'phi':0.0,'r1_guard':30,'early_attack_frac':0.3}),
    ('fortress', 'known', 'fortress_v6', {}),
    ('fortress_gun', 'known', 'fortress_v6', {'round1':'gun2'}),
    ('fortress_splash', 'known', 'fortress_v6', {'round1':'splash'}),
    ('fortress_annealed', 'frontier', 'fortress_v8', {'layout':'annealed25'}),
    ('lead_four', 'frontier', 'lead_four_001', {}),
)


def purchase_signature(player, round_number):
    if isinstance(player, dict):
        return (player['n_factories'],
                tuple((b['type'],b['x'],b['y']) for b in player['buildings']),
                tuple(e['type'] for e in player['roster'] if e['bought_round']==round_number))
    return (player.n_factories,
            tuple((b.type,b.x,b.y) for b in player.buildings),
            tuple(e.type for e in player.roster if e.bought_round==round_number))


def robust_defense(buildings, gold, threats, rules):
    """Repeatedly answer the worst currently leaking forecast, within budget."""
    actions=[]
    for _ in range(len(threats)):
        model=MapModel(buildings,rules)
        leaks=[simulate(model,types,rules)[1] for types in threats]
        if not leaks or max(leaks)<=0 or gold<=0:
            break
        threat=threats[max(range(len(leaks)),key=lambda i:leaks[i])]
        more,new_buildings,new_gold,_=defend(buildings,gold,list(threat),0,rules,reserve=1600)
        if not more:
            break
        actions.extend(more)
        buildings,gold=new_buildings,new_gold
    model=MapModel(buildings,rules)
    residual=max((simulate(model,types,rules)[1] for types in threats),default=0)
    return actions,buildings,gold,residual


class IdentifyingCounter:
    def __init__(self, attack_from=6, attack_share=1.0, cost_penalty=0.1,
                 count_cap=200, max_factories=80, saturate_round=20,
                 catalogue_ids=None, fixed_id=None):
        self.attack_from=int(attack_from)
        self.attack_share=float(attack_share)
        self.cost_penalty=float(cost_penalty)
        self.count_cap=int(count_cap)
        self.max_factories=int(max_factories)
        self.saturate_round=int(saturate_round)
        ids=set(catalogue_ids) if catalogue_ids is not None else {x[0] for x in CATALOGUE}
        if fixed_id is not None:
            ids={fixed_id}
        self.models={name:(LegacyModel if family=='known' else FrontierModel)(model,params)
                     for name,family,model,params in CATALOGUE if name in ids}
        if set(self.models)!=ids or not self.models:
            raise ValueError('Unknown or empty policy catalogue.')
        self.active=list(self.models)
        self.pending={}
        self.trace=[]

    def decide(self,obs):
        rnd=obs['round']
        side=obs['player']
        if rnd==1:
            self.active=list(self.models)
            self.pending={}
            self.trace=[]
        reset=False
        if not self.active:
            self.active=list(self.models)
            self.pending={}
            reset=True
        eliminated=[]
        if self.pending:
            actual=purchase_signature(obs['players'][1-side],rnd-1)
            retained=[name for name in self.active if self.pending.get(name)==actual]
            eliminated=[name for name in self.active if name not in retained]
            if retained:
                self.active=retained
            else:
                self.active=list(self.models)
                reset=True
        forecasts={}
        forecast_errors=[]
        for name in self.active:
            try:
                actions,state=predict(obs,self.models[name])
            except (ValueError,KeyError,IndexError,TypeError) as error:
                forecast_errors.append({'model':name,'error_type':type(error).__name__})
                continue
            forecasts[name]=(actions,state)
        self.pending={name:purchase_signature(state,rnd) for name,(_,state) in forecasts.items()}
        self.active=list(forecasts)
        me=obs['players'][side]
        rules=obs['rules']
        buildings=[(b['x'],b['y'],b['type']) for b in me['buildings']]
        threats=[tuple(e.type for e in state.roster if e.active(rnd)) for _,state in forecasts.values()]
        threats=list(dict.fromkeys(threats))
        if not threats:
            # Uncatalogued exceptional input: documented visible-roster fallback.
            threats=[tuple(active_types(obs['players'][1-side]['roster'],rnd))]
        actions,buildings,gold,residual=robust_defense(buildings,me['gold'],threats,rules)
        own_types=active_types(me['roster'],rnd)
        target_models=[MapModel([(b.x,b.y,b.type) for b in state.buildings],rules)
                       for _,state in forecasts.values()]
        bases=[simulate(model,own_types,rules)[1] for model in target_models]
        choice=None
        if rnd>=self.attack_from and target_models:
            budget=int(gold*self.attack_share)
            for tier,stats in rules['minions'].items():
                maximum=min(self.count_cap,budget//stats['cost'])
                counts=sorted({1,maximum//2,maximum}) if maximum else []
                for count in counts:
                    if count<=0 or count>maximum:
                        continue
                    gains=[simulate(model,own_types+[tier]*count,rules)[1]-base
                           for model,base in zip(target_models,bases)]
                    gain=min(gains)
                    cost=count*stats['cost']
                    value=gain-self.cost_penalty*cost
                    if gain<=0 or value<=0:
                        continue
                    rank=(value,gain,-cost)
                    if choice is None or rank>choice[0]:
                        choice=(rank,tier,count,cost,gains)
            if choice:
                _,tier,count,cost,_=choice
                actions.extend([{'op':'buy_minion','type':tier}]*count)
                gold-=cost
        if rnd>=self.saturate_round:
            more,buildings,gold,_=saturate(buildings,gold,1500,rules)
            actions.extend(more)
        if rnd<48:
            factories=min(self.max_factories,gold//rules['globals']['factory_cost'])
            actions.extend([{'op':'buy_factory'}]*factories)
        self.trace.append({'round':rnd,'active':list(self.active),'eliminated':eliminated,
                           'catalogue_reset':reset,'forecast_errors':forecast_errors,
                           'predicted_actions':{name:acts for name,(acts,_) in forecasts.items()},
                           'forecast_residual_damage':residual,
                           'attack':None if choice is None else {
                               'tier':choice[1],'count':choice[2],'cost':choice[3],'gains':choice[4]}})
        return actions


def make(**parameters):
    return IdentifyingCounter(**parameters).decide
