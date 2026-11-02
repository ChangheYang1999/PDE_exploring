"""Observation-only opponents with distinct timing, rosters and defenses.

These policies are intentionally simple development baselines.  The policy
parameters, not a nominal engine seed, distinguish deterministic games.
"""
from __future__ import annotations
from dataclasses import asdict, dataclass
from typing import Any

from td_game.pathfinding import shortest_path


@dataclass(frozen=True)
class Profile:
    growth_rounds: int = 0
    roster: tuple[str, ...] = ('tier1',)
    defense: str = ''
    defense_count: int = 0
    defense_start: int = 1
    keep_investing: float = 0.0
    pulse_period: int = 1
    pulse_phase: int = 0
    factory_cap: int = 2000
    purchase_cap: int = 1000

    def describe(self) -> dict[str, Any]:
        return asdict(self)


PROFILES = {
    'rush_t1': Profile(),
    'rush_t2': Profile(roster=('tier2',)),
    'rush_t3': Profile(roster=('tier3',)),
    'heavy_t4': Profile(roster=('tier4',)),
    'eco3_t1': Profile(growth_rounds=3),
    'eco5_t1': Profile(growth_rounds=5),
    'eco5_t3': Profile(growth_rounds=5, roster=('tier3',)),
    'eco6_t5': Profile(growth_rounds=6, roster=('tier5',)),
    'splash_t2': Profile(growth_rounds=4, roster=('tier2',), defense='splash', defense_count=1),
    'splash3_t4': Profile(growth_rounds=5, roster=('tier4',), defense='splash', defense_count=3),
    'gun_t3': Profile(growth_rounds=4, roster=('tier3',), defense='gun1', defense_count=3),
    'mixed5': Profile(growth_rounds=5, roster=('tier4', 'tier2', 'tier1', 'tier1', 'tier1')),
}


def legal_tower(observation: dict, type_name: str) -> dict | None:
    """Choose a legal location with maximum route exposure on the resulting map."""
    own = observation['players'][observation['player']]
    rules = observation['rules']
    g = rules['globals']
    occupied = {(b['x'], b['y']) for b in own['buildings']}
    spawn, base = tuple(g['spawn']), tuple(g['base'])
    turret = rules['turrets'][type_name]
    best = None
    for y in range(g['height']):
        for x in range(g['width']):
            if (x, y) in occupied or (x, y) in (spawn, base):
                continue
            route = shortest_path(g['width'], g['height'], occupied | {(x, y)}, spawn, base)
            if route is None:
                continue
            if turret['aoe'] == 8:
                covered = [i for i, (xx, yy) in enumerate(route[:-1]) if max(abs(xx-x), abs(yy-y)) == 1]
            else:
                covered = [i for i, (xx, yy) in enumerate(route[:-1]) if (xx-x)**2 + (yy-y)**2 <= turret['range']**2]
            # Prefer long exposure, early hits and deterministic coordinates.
            score = (len(covered), -sum(covered), len(route), -y, -x)
            if best is None or score > best[0]:
                best = (score, {'op': 'build_turret', 'type': type_name, 'x': x, 'y': y})
    return None if best is None else best[1]


class Archetype:
    def __init__(self, profile: Profile):
        self.profile = profile

    def decide(self, observation: dict) -> list[dict]:
        from copy import deepcopy
        profile = self.profile
        obs = deepcopy(observation)
        own = obs['players'][obs['player']]
        gold = own['gold']
        rules = obs['rules']
        actions: list[dict] = []
        round_number = obs['round']
        if profile.defense and round_number >= profile.defense_start:
            current = sum(b['type'] == profile.defense for b in own['buildings'])
            cost = rules['turrets'][profile.defense]['cost']
            for _ in range(profile.defense_count - current):
                if gold < cost:
                    break
                action = legal_tower(obs, profile.defense)
                if action is None:
                    break
                actions.append(action)
                own['buildings'].append({'type': profile.defense, 'x': action['x'], 'y': action['y']})
                gold -= cost
        factory_cost = rules['globals']['factory_cost']
        if round_number <= profile.growth_rounds:
            factories = min(gold // factory_cost, max(0, profile.factory_cap - own['n_factories']))
            actions.extend({'op': 'buy_factory'} for _ in range(factories))
            return actions
        factory_gold = int(gold * profile.keep_investing)
        factories = min(factory_gold // factory_cost, max(0, profile.factory_cap - own['n_factories']))
        actions.extend({'op': 'buy_factory'} for _ in range(factories))
        gold -= factories * factory_cost
        if (round_number - profile.pulse_phase) % profile.pulse_period:
            return actions
        for k in range(profile.purchase_cap):
            type_name = profile.roster[k % len(profile.roster)]
            cost = rules['minions'][type_name]['cost']
            if gold < cost:
                break
            actions.append({'op': 'buy_minion', 'type': type_name})
            gold -= cost
        return actions


def make(name: str) -> Archetype:
    return Archetype(PROFILES[name])


def rush_t1(observation: dict) -> list[dict]:
    return make('rush_t1').decide(observation)


def rush_t2(observation: dict) -> list[dict]:
    return make('rush_t2').decide(observation)


def eco5_t1(observation: dict) -> list[dict]:
    return make('eco5_t1').decide(observation)


def eco5_t3(observation: dict) -> list[dict]:
    return make('eco5_t3').decide(observation)


def splash_t2(observation: dict) -> list[dict]:
    return make('splash_t2').decide(observation)


def mixed5(observation: dict) -> list[dict]:
    return make('mixed5').decide(observation)
