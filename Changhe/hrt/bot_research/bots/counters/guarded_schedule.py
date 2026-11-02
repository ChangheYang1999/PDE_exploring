"""Fixed purchase schedule with a small opening prior and visible-roster defense.

The first round defends against a declared two-tier1 opening. Later rounds
use only the opponent's already visible active roster. No opponent policy is
loaded or simulated, so newly purchased hidden units are not anticipated.
This policy is intended as an ablation of the public-model schedule.
"""
from __future__ import annotations
from bot_research.bots.economy.frozen.v2.defense_plan import defend, saturate
from bot_research.bots.economy.frozen.v2.threat import active_types


class GuardedSchedule:
    def __init__(self, schedule=(), initial_threat=('tier1', 'tier1'), count_cap=200,
                 saturate_round=20, max_factories=80, defense_first=False):
        self.schedule = tuple((int(r), str(t), int(n)) for r, t, n in schedule)
        self.initial_threat = tuple(str(t) for t in initial_threat)
        self.count_cap = int(count_cap)
        self.saturate_round = int(saturate_round)
        self.max_factories = int(max_factories)
        self.defense_first = bool(defense_first)
        kinds = ('tier1', 'tier2', 'tier3', 'tier4', 'tier5')
        if any(not 1 <= r <= 50 or n < 0 or t not in kinds for r,t,n in self.schedule):
            raise ValueError('Invalid declared purchase schedule.')
        if any(t not in kinds for t in self.initial_threat):
            raise ValueError('Invalid initial threat type.')
        if self.count_cap < 0 or self.max_factories < 0:
            raise ValueError('Purchase caps must be nonnegative.')

    def decide(self, observation):
        rnd = observation['round']
        me = observation['players'][observation['player']]
        op = observation['players'][1 - observation['player']]
        rules = observation['rules']
        threat = list(self.initial_threat) if rnd == 1 else active_types(op['roster'], rnd)
        buildings = [(b['x'], b['y'], b['type']) for b in me['buildings']]
        gold, actions = me['gold'], []
        if self.defense_first:
            more, buildings, gold, _ = defend(buildings, gold, threat, 0, rules, reserve=1600)
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
            more, buildings, gold, _ = defend(buildings, gold, threat, 0, rules, reserve=1600)
            actions.extend(more)
        if rnd >= self.saturate_round:
            more, buildings, gold, _ = saturate(buildings, gold, 1500, rules)
            actions.extend(more)
        if rnd < 48:
            actions.extend([{'op': 'buy_factory'}] * min(self.max_factories, gold // rules['globals']['factory_cost']))
        return actions


def make(**parameters):
    return GuardedSchedule(**parameters).decide
