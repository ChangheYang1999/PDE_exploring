"""Bounded attack search after stateful public-catalogue defense.

The finite score is a heuristic for future play. Exact retained forecasts
support only the current-round statement in catalogue_attack_selection.
"""
from fractions import Fraction
import hashlib
import json

from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.stateful_catalogue import StatefulCatalogue
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.bots.economy.frozen.v2.fastsim import MapModel, simulate
from bot_research.bots.economy.frozen.v2.threat import active_types


def purchase_pool(rules, budget, count_cap, evaluation_limit):
    """Empty, pure and ordered two-tier purchases, in a fixed finite order."""
    costs = {t: p['cost'] for t, p in rules['minions'].items()}
    tiers = sorted(costs, key=lambda t: (costs[t], t))
    result, seen = [], set()

    def add(sequence):
        sequence = tuple(sequence)
        if (sequence not in seen and len(result) < evaluation_limit
                and len(sequence) <= count_cap
                and sum(costs[t] for t in sequence) <= budget):
            seen.add(sequence)
            result.append(sequence)

    add(())
    for tier in tiers:
        maximum = min(count_cap, budget // costs[tier])
        for n in sorted({1, 2, 4, 8, maximum // 2, maximum}):
            if 0 < n <= maximum:
                add([tier] * n)
    # Heavy-first and light-first are distinct under dense spawn indexing.
    for fraction in (Fraction(1, 2), Fraction(1, 4), Fraction(3, 4)):
        for i, first in enumerate(tiers):
            for second in tiers[i+1:]:
                n = min(count_cap, int(budget * fraction) // costs[first])
                left = budget - n * costs[first]
                m = min(count_cap - n, left // costs[second])
                if n and m:
                    add([first] * n + [second] * m)
                    add([second] * m + [first] * n)
    return result


def pool_digest(pool):
    return hashlib.sha256(json.dumps(pool, separators=(',', ':')).encode()).hexdigest()


class AdaptiveCatalogue(StatefulCatalogue):
    def __init__(self, attack_weight=4, attack_budget_share=1, evaluation_limit=96,
                 search_enabled=True, attack_from=1, **parameters):
        if any(k in parameters for k in ('attack_share', 'attack_round', 'tier')):
            raise ValueError('Adaptive selection does not accept fixed timing parameters.')
        self.weight = Fraction(str(attack_weight))
        self.budget_share = Fraction(str(attack_budget_share))
        self.evaluation_limit = int(evaluation_limit)
        self.search_enabled = bool(search_enabled)
        self.attack_from = int(attack_from)
        if (self.weight < 0 or not 0 <= self.budget_share <= 1
                or not 32 <= self.evaluation_limit <= 256
                or not 1 <= self.attack_from <= 50):
            raise ValueError('Invalid finite attack-search parameters.')
        super().__init__(attack_share=0, **parameters)

    def decide(self, observation):
        original = super().decide(observation)
        trace = self.trace[-1]
        if not self.search_enabled or observation['round'] < self.attack_from:
            trace['adaptive_attack'] = dict(enabled=False)
            return original
        rnd, side, rules = observation['round'], observation['player'], observation['rules']
        config = config_from_dict(rules)
        kept = [a for a in original if a['op'] != 'buy_factory']
        own = player_from_snapshot(observation['players'][side])
        for action in kept:
            if not apply_action(own, action, rnd, config)['accepted']:
                raise ValueError('Parent construction was not legal.')
        targets = {}
        for name, predicted in trace['predictions'].items():
            enemy = player_from_snapshot(observation['players'][1-side])
            for action in predicted['actions']:
                if not apply_action(enemy, action, rnd, config)['accepted']:
                    raise ValueError('Retained forecast was not legal.')
            targets[name] = enemy
        if not targets:
            targets['visible_fallback'] = player_from_snapshot(observation['players'][1-side])
        own_types = active_types(observation['players'][side]['roster'], rnd)
        own_map = MapModel([(b.x, b.y, b.type) for b in own.buildings], rules)
        maps = {n: MapModel([(b.x, b.y, b.type) for b in p.buildings], rules)
                for n, p in targets.items()}
        baselines = {n: simulate(m, own_types, rules)[1] for n, m in maps.items()}
        incoming = {n: simulate(own_map, [e.type for e in p.roster if e.active(rnd)], rules)[1]
                    for n, p in targets.items()}
        own_safe = max(incoming.values()) < own.hp
        enemy_hp = observation['players'][1-side]['hp']
        immune = all(m.splash_total >= max(t['hp'] for t in rules['minions'].values())
                     for m in maps.values())
        budget = int(own.gold * self.budget_share)
        pool = [()] if immune else purchase_pool(rules, budget, self.count_cap, self.evaluation_limit)
        selected, selected_detail, best_rank = (), None, None
        for index, sequence in enumerate(pool):
            damages = baselines.copy() if not sequence else {
                n: simulate(m, own_types + list(sequence), rules)[1] for n, m in maps.items()}
            gains = {n: damages[n] - baselines[n] for n in maps}
            gain = min(gains.values())
            cost = sum(rules['minions'][t]['cost'] for t in sequence)
            utility = Fraction(gain) if rnd == rules['globals']['max_rounds'] else self.weight * gain - cost
            safe_lethal = own_safe and min(damages.values()) >= enemy_hp
            rank = (safe_lethal, utility, gain, -cost, -len(sequence))
            if best_rank is None or rank > best_rank:
                selected, best_rank = sequence, rank
                selected_detail = dict(index=index, cost=cost, damage=damages, gains=gains,
                                       minimum_gain=gain, utility=str(utility),
                                       forecast_safe_lethal=safe_lethal)
        gold = own.gold - selected_detail['cost']
        actions = kept + [dict(op='buy_minion', type=t) for t in selected]
        if rnd < 48:
            actions += [dict(op='buy_factory')] * min(self.max_factories, gold // rules['globals']['factory_cost'])
        trace['attack_count'] = len(selected)
        trace['attack_tier'] = 'ordered_package'
        trace['attack_gains'] = list(selected_detail['gains'].values())
        trace['adaptive_attack'] = dict(
            enabled=True, budget=budget, weight=str(self.weight), budget_share=str(self.budget_share),
            evaluation_limit=self.evaluation_limit, count_cap=self.count_cap,
            evaluated=len(pool), pool_sha256=pool_digest(pool), targets=list(targets),
            baseline_damage=baselines, incoming_damage=incoming, own_safe=own_safe,
            all_current_maps_immune=immune, sequence=list(selected), selected=selected_detail,
            guarantee_scope='Conditional on true catalogue membership and exact local combat; fallback has no forecast guarantee.')
        return actions


def make(**parameters):
    return AdaptiveCatalogue(**parameters).decide
