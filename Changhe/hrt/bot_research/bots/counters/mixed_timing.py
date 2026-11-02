"""A forecast-guided timed purchase with mixed tiers and order search."""
from bot_research.bots.counters.timed_frontier import TimedKnown
from bot_research.bots.counters.forecast_timing import predict
from bot_research.bots.counters.package_search import search_package
from bot_research.bots.economy.frozen.v2.defense_plan import defend, saturate
from bot_research.bots.economy.frozen.v2.threat import active_types


class MixedTiming(TimedKnown):
    def __init__(self, evaluations=192, seed=0, **parameters):
        super().__init__(**parameters)
        self.evaluations = int(evaluations)
        self.seed = int(seed)

    def decide(self, observation):
        rnd = observation['round']
        me = observation['players'][observation['player']]
        rules = observation['rules']
        predicted, enemy = predict(observation, self.model)
        threat = [entry.type for entry in enemy.roster if entry.active(rnd)]
        buildings = [(b['x'], b['y'], b['type']) for b in me['buildings']]
        gold, actions = me['gold'], []
        residual, search = 0, None
        if self.defense_first:
            more, buildings, gold, residual = defend(buildings, gold, threat, 0, rules, reserve=1600)
            actions.extend(more)
        if rnd == self.attack_round:
            package, search = search_package(
                [(b.x, b.y, b.type) for b in enemy.buildings], rules,
                active_types(me['roster'], rnd), int(gold * self.attack_share),
                evaluations=self.evaluations, seed=self.seed + rnd, count_cap=self.count_cap)
            actions.extend({'op': 'buy_minion', 'type': kind} for kind in package)
            gold -= search['cost']
        if not self.defense_first:
            more, buildings, gold, residual = defend(buildings, gold, threat, 0, rules, reserve=1600)
            actions.extend(more)
        if rnd >= self.saturate_round:
            more, buildings, gold, _ = saturate(buildings, gold, 1500, rules)
            actions.extend(more)
        if rnd < 48:
            actions.extend([{'op': 'buy_factory'}] * min(self.max_factories, gold // rules['globals']['factory_cost']))
        self.trace.append({'round': rnd, 'predicted_actions': predicted, 'search': search,
                           'forecast_residual_damage': residual})
        return actions


def make(**parameters):
    return MixedTiming(**parameters).decide
