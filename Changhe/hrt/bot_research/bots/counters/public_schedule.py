"""Several declared purchases, with defense against a public policy model.

The schedule is fixed before play. Purchases are capped by current gold and
may be strategically ineffective. The model uses only public observations;
its prediction accuracy is a separate, recorded property of each campaign.
"""
from __future__ import annotations
from bot_research.bots.counters.public_factory import PublicFactoryModel, DEFAULT_MODEL
from bot_research.bots.counters.forecast_timing import ForecastTiming, predict
from bot_research.bots.economy.frozen.v2.defense_plan import defend, saturate


class PublicSchedule(ForecastTiming):
    def __init__(self, schedule=(), model_spec=DEFAULT_MODEL, model_parameters=None, **parameters):
        super().__init__(**parameters)
        self.schedule = tuple((int(rnd), str(tier), int(count)) for rnd, tier, count in schedule)
        if any(not 1 <= rnd <= 50 or count < 0 or tier not in
               ('tier1', 'tier2', 'tier3', 'tier4', 'tier5') for rnd, tier, count in self.schedule):
            raise ValueError('Invalid declared purchase schedule.')
        self.model = PublicFactoryModel(model_spec, model_parameters)

    def decide(self, observation):
        rnd = observation['round']
        me = observation['players'][observation['player']]
        rules = observation['rules']
        predicted, enemy = predict(observation, self.model)
        threat = [entry.type for entry in enemy.roster if entry.active(rnd)]
        buildings = [(b['x'], b['y'], b['type']) for b in me['buildings']]
        gold, actions = me['gold'], []
        residual = 0
        if self.defense_first:
            more, buildings, gold, residual = defend(buildings, gold, threat, 0, rules, reserve=1600)
            actions.extend(more)
        purchases = []
        for scheduled_round, tier, requested in self.schedule:
            if scheduled_round != rnd:
                continue
            cost = rules['minions'][tier]['cost']
            count = min(requested, gold // cost, self.count_cap - len(purchases))
            if count > 0:
                purchases.extend([tier] * count)
                gold -= cost * count
        actions.extend({'op': 'buy_minion', 'type': kind} for kind in purchases)
        if not self.defense_first:
            more, buildings, gold, residual = defend(buildings, gold, threat, 0, rules, reserve=1600)
            actions.extend(more)
        if rnd >= self.saturate_round:
            more, buildings, gold, _ = saturate(buildings, gold, 1500, rules)
            actions.extend(more)
        if rnd < 48:
            actions.extend([{'op': 'buy_factory'}] * min(self.max_factories, gold // rules['globals']['factory_cost']))
        self.trace.append({'round': rnd, 'predicted_actions': predicted,
                           'attack_count': len(purchases), 'selected_sequence': purchases,
                           'forecast_residual_damage': residual})
        return actions


def make(**parameters):
    return PublicSchedule(**parameters).decide
