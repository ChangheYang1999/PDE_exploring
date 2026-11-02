"""Timed offense with a sampled affordable-roster envelope for defense.

This policy does not simulate an opponent policy. Round one uses a fixed
three-tier1 prior; later rounds cover the existing roster plus the frozen
planner's attack-package family up to a fraction of visible opponent gold.
That finite family is a heuristic, not a certificate against every purchase.
"""
from bot_research.bots.economy.frozen.v2.defense_plan import defend, saturate
from bot_research.bots.economy.frozen.v2.fastsim import MapModel, simulate
from bot_research.bots.economy.frozen.v2.threat import active_types


class BudgetTiming:
    def __init__(self, attack_round=5, tier='tier4', budget_fraction=0.5,
                 attack_share=1.0, count_cap=200, envelope_cap=200,
                 saturate_round=20, max_factories=80):
        if not 0 <= budget_fraction <= 1 or not 0 <= attack_share <= 1:
            raise ValueError('Budget fractions must lie in [0,1].')
        if tier not in ('tier1', 'tier2', 'tier3', 'tier4', 'tier5'):
            raise ValueError('Unknown tier.')
        self.attack_round = int(attack_round)
        self.tier = tier
        self.budget_fraction = float(budget_fraction)
        self.attack_share = float(attack_share)
        self.count_cap = int(count_cap)
        self.envelope_cap = int(envelope_cap)
        self.saturate_round = int(saturate_round)
        self.max_factories = int(max_factories)
        self.trace = []

    def decide(self, observation):
        rnd = observation['round']
        me = observation['players'][observation['player']]
        enemy = observation['players'][1-observation['player']]
        rules = observation['rules']
        buildings = [(b['x'], b['y'], b['type']) for b in me['buildings']]
        gold, actions = me['gold'], []
        threat = ['tier1']*3 if rnd == 1 else active_types(enemy['roster'], rnd)
        threat_gold = 0 if rnd == 1 else int(enemy['gold'] * self.budget_fraction)
        count, gain = 0, 0
        if rnd == self.attack_round:
            cost = rules['minions'][self.tier]['cost']
            count = min(self.count_cap, int(gold*self.attack_share)//cost)
            if count:
                model = MapModel([(b['x'], b['y'], b['type']) for b in enemy['buildings']], rules)
                active = active_types(me['roster'], rnd)
                gain = simulate(model, active+[self.tier]*count, rules)[1]-simulate(model, active, rules)[1]
                if gain <= 0:
                    count = 0
            actions.extend([{'op':'buy_minion', 'type':self.tier}]*count)
            gold -= count*cost
        more, buildings, gold, residual = defend(buildings, gold, threat, threat_gold,
                                                rules, cap=self.envelope_cap, reserve=1600)
        actions.extend(more)
        if rnd >= self.saturate_round:
            more, buildings, gold, _ = saturate(buildings, gold, 1500, rules)
            actions.extend(more)
        if rnd < 48:
            actions.extend([{'op':'buy_factory'}]*min(self.max_factories, gold//rules['globals']['factory_cost']))
        self.trace.append(dict(round=rnd, threat_gold=threat_gold, visible_or_prior_roster=threat,
                               attack_count=count, attack_tier=self.tier,
                               visible_map_attack_gain=gain, sampled_residual_damage=residual))
        return actions


def make(**parameters):
    return BudgetTiming(**parameters).decide
