"""Exact-public-model counter with a legal-cell defensive fallback.

The original template plan remains the default. Only when that plan still
leaks do we compare two layout-free alternatives, with a deterministic step
limit. These are private plans from public observations, never live state.
"""
from copy import deepcopy
from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.forecast_timing import predict
from bot_research.bots.counters.stateful_public import StatefulPublicTiming
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.bots.economy.frozen.v2.defense_plan import defend, saturate
from bot_research.bots.economy.frozen.v2.fastsim import MapModel, simulate
from bot_research.bots.economy.frozen.v2.threat import active_types
from bot_research.bots.economy.frozen.v17.freeplan import free_plan


class FreeForecast(StatefulPublicTiming):
    def __init__(self, schedule=None, free_steps=15, **parameters):
        super().__init__(**parameters)
        self.schedule = None if schedule is None else tuple(
            (int(r), str(t), int(n)) for r, t, n in schedule)
        if self.schedule is not None and any(
                not 1 <= r <= 50 or t not in ('tier1', 'tier2', 'tier3', 'tier4', 'tier5') or n < 0
                for r, t, n in self.schedule):
            raise ValueError('Invalid declared schedule.')
        self.free_steps = int(free_steps)
        if not 0 < self.free_steps <= 60:
            raise ValueError('Require 1..60 deterministic free-plan steps.')

    def defense(self, observation, buildings, gold, threat):
        rules = observation['rules']
        original, final, left, residual = defend(
            buildings, gold, threat, 0, rules, reserve=1600)
        candidates = [('template', original)]
        if residual > 0:
            for label, prefix, current, budget in (
                    ('free_initial', [], buildings, gold),
                    ('free_after_template', original, final, left)):
                if budget < min(t['cost'] for t in rules['turrets'].values()):
                    continue
                copied = deepcopy(observation)
                own = copied['players'][copied['player']]
                own['buildings'] = [dict(x=x, y=y, type=t) for x, y, t in current]
                own['gold'] = budget
                extra = free_plan(copied, budget, [threat], partial='best', max_steps=self.free_steps)
                candidates.append((label, prefix + extra))
        checked = []
        for label, actions in candidates:
            own = deepcopy(observation['players'][observation['player']])
            own['buildings'] = [dict(x=x, y=y, type=t) for x, y, t in buildings]
            own['gold'] = gold
            state = player_from_snapshot(own)
            config = config_from_dict(rules)
            for action in actions:
                event = apply_action(state, action, observation['round'], config)
                if not event['accepted']:
                    raise ValueError('Defensive proposal is not legal: ' + event['reason'])
            built = [(b.x, b.y, b.type) for b in state.buildings]
            damage = simulate(MapModel(built, rules), threat, rules)[1]
            checked.append(dict(label=label, actions=actions, buildings=built,
                                gold=state.gold, residual=damage, cost=gold-state.gold))
        selected = min(checked, key=lambda c: (c['residual'], c['cost']))
        detail = dict(selected=selected['label'], alternatives=[
            {k: c[k] for k in ('label', 'cost', 'residual')} for c in checked])
        return selected['actions'], selected['buildings'], selected['gold'], selected['residual'], detail

    def decide(self, observation):
        rnd = observation['round']
        me = observation['players'][observation['player']]
        rules = observation['rules']
        predicted, enemy = predict(observation, self.model)
        threat = [e.type for e in enemy.roster if e.active(rnd)]
        buildings = [(b['x'], b['y'], b['type']) for b in me['buildings']]
        gold, actions = me['gold'], []
        residual, detail = 0, None
        if self.defense_first:
            extra, buildings, gold, residual, detail = self.defense(observation, buildings, gold, threat)
            actions.extend(extra)
        purchases, gain = [], 0
        if self.schedule is None:
            if rnd == self.attack_round:
                cost = rules['minions'][self.tier]['cost']
                count = min(self.count_cap, int(gold*self.attack_share)//cost)
                if count:
                    model = MapModel([(b.x, b.y, b.type) for b in enemy.buildings], rules)
                    own_types = active_types(me['roster'], rnd)
                    baseline = simulate(model, own_types, rules)[1]
                    gain = simulate(model, own_types+[self.tier]*count, rules)[1]-baseline
                    if gain > 0:
                        purchases = [self.tier]*count
                        gold -= count*cost
        else:
            for scheduled_round, tier, requested in self.schedule:
                if scheduled_round == rnd:
                    cost = rules['minions'][tier]['cost']
                    count = min(requested, gold//cost, self.count_cap-len(purchases))
                    if count > 0:
                        purchases.extend([tier]*count)
                        gold -= count*cost
        actions.extend(dict(op='buy_minion', type=t) for t in purchases)
        if not self.defense_first:
            extra, buildings, gold, residual, detail = self.defense(observation, buildings, gold, threat)
            actions.extend(extra)
        if rnd >= self.saturate_round:
            extra, buildings, gold, _ = saturate(buildings, gold, 1500, rules)
            actions.extend(extra)
        if rnd < 48:
            actions.extend([dict(op='buy_factory')]*min(self.max_factories, gold//rules['globals']['factory_cost']))
        self.trace.append(dict(round=rnd, predicted_actions=predicted,
                               attack_count=len(purchases), selected_sequence=purchases,
                               forecast_attack_gain=gain, forecast_residual_damage=residual,
                               defense=detail))
        return actions


def make(**parameters):
    return FreeForecast(**parameters).decide
