"""Identify a fixed public policy without receiving its identity.

All active clones are advanced exactly once per round. Public purchase
signatures permanently eliminate contradicted members. Empty-catalogue
fallback uses only the visible roster and map. See the standalone proof in
experiments/validation/analysis/stateful_catalogue/PROOF.md.
"""
from copy import deepcopy
from bot_research.experiments.lead.frozen.best_v9b import make as best_v9b
from bot_research.bots.economy.frozen.v17.econ17 import make as economy17
from bot_research.bots.economy.frozen.v19.econ19 import make as economy19
from bot_research.bots.counters.forecast_timing import predict
from bot_research.bots.counters.identifying_counter import purchase_signature
from bot_research.bots.counters.free_forecast import FreeForecast
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.bots.economy.frozen.v2.defense_plan import saturate
from bot_research.bots.economy.frozen.v2.fastsim import MapModel, simulate
from bot_research.bots.economy.frozen.v2.threat import active_types

BEST_FACTORY = 'bot_research.experiments.lead.frozen.best_v9b:@make'
CATALOGUE = {
    'best_v9b': (best_v9b, {}),
    'economy17': (economy17, dict(free_fallback='zero', foreign_attack_from=11)),
    'economy19': (economy19, dict(free_fallback='zero', foreign_attack_from=11,
                               doom='next', fac_cap=400, sat_reach=True)),
}


class StatefulCatalogue:
    def __init__(self, catalogue_ids=None, attack_round=3, tier='tier3',
                 attack_share=1.0, count_cap=1000, max_factories=80,
                 saturate_round=20, defense_first=False, free_steps=15):
        self.ids = tuple(CATALOGUE if catalogue_ids is None else catalogue_ids)
        if not self.ids or len(set(self.ids)) != len(self.ids) or any(n not in CATALOGUE for n in self.ids):
            raise ValueError('Require distinct known catalogue members.')
        self.attack_round, self.tier = int(attack_round), str(tier)
        self.attack_share, self.count_cap = float(attack_share), int(count_cap)
        if not 1 <= self.attack_round <= 50 or self.tier not in ('tier1', 'tier2', 'tier3', 'tier4', 'tier5'):
            raise ValueError('Invalid timing condition.')
        if not 0 <= self.attack_share <= 1 or not 0 < self.count_cap <= 1000:
            raise ValueError('Invalid attack budget or count cap.')
        self.max_factories, self.saturate_round = int(max_factories), int(saturate_round)
        self.defense_first = bool(defense_first)
        # Only the pure defensive method is used. This object's model is never queried.
        self.defender = FreeForecast(model_spec=BEST_FACTORY, free_steps=free_steps)
        self._reset()

    def _reset(self):
        self.models = {name: CATALOGUE[name][0](**CATALOGUE[name][1]) for name in self.ids}
        self.active = list(self.ids)
        self.pending = {}
        self.calls = {name: 0 for name in self.ids}
        self.last_round = 0
        self.player = None
        self.trace = []

    def defense(self, observation, buildings, gold, threats):
        # A singleton is exactly the FreeForecast defensive controller.
        proposals = []
        unique = list(dict.fromkeys(tuple(t) for t in threats))
        for threat in unique:
            actions, built, left, _, detail = self.defender.defense(observation, buildings, gold, list(threat))
            model = MapModel(built, observation['rules'])
            residuals = [simulate(model, list(t), observation['rules'])[1] for t in unique]
            proposals.append((max(residuals), gold-left, actions, built, left, detail, residuals))
        chosen = min(proposals, key=lambda p: (p[0], p[1]))
        return chosen[2], chosen[3], chosen[4], dict(
            residual=chosen[0], cost=chosen[1], against_threats=chosen[6],
            unique_threats=[list(t) for t in unique], source_proposal=chosen[5])

    def decide(self, observation):
        rnd, side = observation['round'], observation['player']
        if rnd == 1:
            self._reset()
        if rnd != self.last_round+1 or (self.player is not None and side != self.player):
            raise ValueError('Require one call per round and a fixed player assignment.')
        before_active = list(self.active)
        observed = None
        eliminated = []
        if self.pending:
            observed = purchase_signature(observation['players'][1-side], rnd-1)
            eliminated = [name for name in self.active if self.pending[name] != observed]
            self.active = [name for name in self.active if name not in eliminated]
        forecasts = {}
        for name in self.active:
            actions, state = predict(observation, self.models[name])
            self.calls[name] += 1
            assert self.calls[name] == rnd
            forecasts[name] = (actions, state)
        self.pending = {name: purchase_signature(state, rnd) for name, (_, state) in forecasts.items()}
        target_states = [state for _, state in forecasts.values()]
        fallback = not target_states
        if fallback:
            target_states = [player_from_snapshot(deepcopy(observation['players'][1-side]))]
        threats = [[e.type for e in state.roster if e.active(rnd)] for state in target_states]
        me, rules = observation['players'][side], observation['rules']
        buildings = [(b['x'], b['y'], b['type']) for b in me['buildings']]
        gold, actions, defense = me['gold'], [], None
        if self.defense_first:
            extra, buildings, gold, defense = self.defense(observation, buildings, gold, threats)
            actions.extend(extra)
        count, gains = 0, []
        if rnd == self.attack_round:
            cost = rules['minions'][self.tier]['cost']
            count = min(self.count_cap, int(gold*self.attack_share)//cost)
            if count:
                own = active_types(me['roster'], rnd)
                for target in target_states:
                    model = MapModel([(b.x, b.y, b.type) for b in target.buildings], rules)
                    gains.append(simulate(model, own+[self.tier]*count, rules)[1]-simulate(model, own, rules)[1])
                if min(gains) <= 0:
                    count = 0
                actions.extend([dict(op='buy_minion', type=self.tier)]*count)
                gold -= count*cost
        if not self.defense_first:
            extra, buildings, gold, defense = self.defense(observation, buildings, gold, threats)
            actions.extend(extra)
        if rnd >= self.saturate_round:
            extra, buildings, gold, _ = saturate(buildings, gold, 1500, rules)
            actions.extend(extra)
        if rnd < 48:
            actions.extend([dict(op='buy_factory')]*min(self.max_factories, gold//rules['globals']['factory_cost']))
        self.trace.append(dict(round=rnd, before_active=before_active, active=list(self.active),
                               eliminated=eliminated, observed_previous_signature=observed,
                               predictions={name: dict(actions=value[0], signature=self.pending[name])
                                            for name, value in forecasts.items()},
                               call_counts=dict(self.calls), fallback=fallback,
                               attack_count=count, attack_tier=self.tier, attack_gains=gains,
                               defense=defense))
        self.last_round, self.player = rnd, side
        return actions


def make(**parameters):
    return StatefulCatalogue(**parameters).decide
