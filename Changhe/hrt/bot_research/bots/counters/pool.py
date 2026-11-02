"""Additional bounded counter archetypes and factory entry points.

Tuning entry points: archetype, turtle, mirror, random_legal, stacker.
Reserved seed/parameter combinations live in the prospective holdout manifest.
Every decision depends only on public observations and this instance's history.
"""
from __future__ import annotations
from copy import deepcopy
import random

from td_game.pathfinding import shortest_path
from bot_research.bots.counters.archetypes import Archetype, Profile, PROFILES, legal_tower


def archetype(name='rush_t1', **kwargs):
    if kwargs:
        if 'roster' in kwargs:
            kwargs['roster'] = tuple(kwargs['roster'])
        return Archetype(Profile(**kwargs)).decide
    return Archetype(PROFILES[name]).decide


def _factories(gold, own, rules, cap=2000, per_round_cap=1000):
    count = min(gold // rules['globals']['factory_cost'], max(0, cap - own['n_factories']), per_round_cap)
    return [{'op': 'buy_factory'} for _ in range(count)]


def turtle(kind='splash', defense_share=0.6, max_towers=35, factory_cap=2000):
    def decide(observation):
        obs = deepcopy(observation)
        own = obs['players'][obs['player']]
        rules = obs['rules']
        gold = own['gold']
        budget = int(gold * defense_share)
        cost = rules['turrets'][kind]['cost']
        actions = []
        current = sum(b['type'] != 'wall' for b in own['buildings'])
        for _ in range(min(8, max_towers - current)):
            if budget < cost:
                break
            action = legal_tower(obs, kind)
            if action is None:
                break
            actions.append(action)
            own['buildings'].append({k: action[k] for k in ('type', 'x', 'y')})
            gold -= cost
            budget -= cost
        return actions + _factories(gold, own, rules, factory_cap)
    return decide


def stacker(growth_rounds=8, tier='tier1', initial_splash=True, batch_cap=1000):
    return Archetype(Profile(growth_rounds=growth_rounds, roster=(tier,),
        defense='splash' if initial_splash else '', defense_count=int(initial_splash),
        purchase_cap=batch_cap, factory_cap=2000)).decide


def random_legal(seed=130, action_cap=35, attack_bias=0.3):
    def decide(observation):
        rng = random.Random(int(seed) * 1000003 + observation['round'])
        own = observation['players'][observation['player']]
        rules = observation['rules']
        g = rules['globals']
        gold = own['gold']
        factories = own['n_factories']
        blocked = {(b['x'], b['y']) for b in own['buildings']}
        actions = []
        for _ in range(int(action_cap)):
            if gold < min(rules['wall_cost'], g['factory_cost']):
                break
            choice = rng.random()
            if choice < attack_bias:
                affordable = [t for t in rules['minions'] if rules['minions'][t]['cost'] <= gold]
                if affordable:
                    kind = rng.choice(affordable)
                    actions.append({'op': 'buy_minion', 'type': kind})
                    gold -= rules['minions'][kind]['cost']
            elif choice < attack_bias + 0.35:
                if gold >= g['factory_cost'] and factories < 2000:
                    actions.append({'op': 'buy_factory'})
                    gold -= g['factory_cost']
                    factories += 1
            else:
                options = [(x, y) for y in range(g['height']) for x in range(g['width'])
                           if (x, y) not in blocked and (x, y) not in (tuple(g['spawn']), tuple(g['base']))]
                if not options:
                    continue
                x, y = rng.choice(options)
                if shortest_path(g['width'], g['height'], blocked | {(x, y)}, tuple(g['spawn']), tuple(g['base'])) is None:
                    continue
                affordable = [t for t in rules['turrets'] if rules['turrets'][t]['cost'] <= gold]
                if affordable and choice < 0.9:
                    kind = rng.choice(affordable)
                    actions.append({'op': 'build_turret', 'type': kind, 'x': x, 'y': y})
                    gold -= rules['turrets'][kind]['cost']
                elif gold >= rules['wall_cost']:
                    actions.append({'op': 'build_wall', 'x': x, 'y': y})
                    gold -= rules['wall_cost']
                else:
                    continue
                blocked.add((x, y))
        return actions
    return decide


def mirror(attack_floor=0.1, defense_share=0.3, factory_cap=2000):
    previous = {'factory_count': 0, 'buildings': set()}
    def decide(observation):
        obs = deepcopy(observation)
        own = obs['players'][obs['player']]
        enemy = obs['players'][1 - obs['player']]
        rules = obs['rules']
        if obs['round'] == 1:
            previous['factory_count'] = 0
            previous['buildings'] = set()
        new_roster = [e for e in enemy['roster'] if e['bought_round'] == obs['round'] - 1]
        attack_spend = sum(rules['minions'][e['type']]['cost'] for e in new_roster)
        factory_spend = max(0, enemy['n_factories'] - previous['factory_count']) * rules['globals']['factory_cost']
        new_buildings = {(b['type'], b['x'], b['y']) for b in enemy['buildings']} - previous['buildings']
        defense_spend = sum(rules['wall_cost'] if kind == 'wall' else rules['turrets'][kind]['cost'] for kind, x, y in new_buildings)
        previous['factory_count'] = enemy['n_factories']
        previous['buildings'] = {(b['type'], b['x'], b['y']) for b in enemy['buildings']}
        share = max(float(attack_floor), attack_spend / max(1, attack_spend + factory_spend + defense_spend))
        gold = own['gold']
        actions = []
        cost = rules['turrets']['splash']['cost']
        desired = min(12, 1 + len(enemy['roster']) // 20)
        current = sum(b['type'] == 'splash' for b in own['buildings'])
        if current < desired and gold >= cost and (current == 0 or gold * defense_share >= cost):
            action = legal_tower(obs, 'splash')
            if action:
                actions.append(action)
                gold -= cost
        # Match observed offensive composition by one dominant purchase type.
        counts = {name: sum(e['type'] == name for e in new_roster) for name in rules['minions']}
        tier = max(counts, key=lambda name: (counts[name], -rules['minions'][name]['cost']))
        attack_gold = int(gold * share)
        count = min(1000, attack_gold // rules['minions'][tier]['cost'])
        actions.extend({'op': 'buy_minion', 'type': tier} for _ in range(count))
        gold -= count * rules['minions'][tier]['cost']
        return actions + _factories(gold, own, rules, int(factory_cap))
    return decide


def rush_t5():
    return Archetype(Profile(roster=('tier5',))).decide
