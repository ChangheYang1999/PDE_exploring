"""Attack search using only the previous round's public defensive snapshot.

The official combat simulator evaluates counterfactual purchases on newly
constructed local states. No pending action or live game object is inspected.
This is a deliberately myopic counter, not an optimal-policy claim.
"""
from __future__ import annotations
from dataclasses import dataclass
from functools import lru_cache
import json

from td_game.combat import simulate_map
from td_game.config import config_from_dict
from td_game.pathfinding import shortest_path
from td_game.state import Building, PlayerState, RosterEntry

from bot_research.bots.counters.archetypes import Archetype, Profile


@lru_cache(maxsize=8)
def _config(serialized_rules: str):
    return config_from_dict(json.loads(serialized_rules))


def player_from_snapshot(snapshot: dict) -> PlayerState:
    roster = [RosterEntry(e['id'], e['type'], e['bought_round'], e['expires_after_round']) for e in snapshot['roster']]
    return PlayerState(snapshot['name'], snapshot['hp'], snapshot['gold'], snapshot['n_factories'],
                       [Building(b['x'], b['y'], b['type']) for b in snapshot['buildings']], roster,
                       max((e.id for e in roster), default=-1) + 1)


def purchase_sequences(observation: dict, gold: int, cap: int = 1000) -> list[tuple[str, ...]]:
    catalog = observation['rules']['minions']
    types = sorted(catalog, key=lambda name: catalog[name]['cost'])
    candidates: set[tuple[str, ...]] = {()}
    for type_name in types:
        candidates.add((type_name,) * min(cap, gold // catalog[type_name]['cost']))
    # Tough leaders can absorb the frontmost-target guns while cheaper followers
    # carry base damage. Also test the reverse order as a falsifiable control.
    for heavy in types[1:]:
        cost = catalog[heavy]['cost']
        for count in (1, 2, 4, 8):
            if count * cost > gold:
                break
            for light in types[:types.index(heavy)]:
                followers = min(cap - count, (gold - count * cost) // catalog[light]['cost'])
                if followers:
                    head = (heavy,) * count
                    tail = (light,) * followers
                    candidates.add(head + tail)
                    candidates.add(tail + head)
    return sorted(candidates, key=lambda seq: (len(seq), seq))


def score_sequences(observation: dict, sequences: list[tuple[str, ...]]) -> list[dict]:
    config = _config(json.dumps(observation['rules'], sort_keys=True))
    own = observation['players'][observation['player']]
    enemy = observation['players'][1 - observation['player']]
    round_number = observation['round']
    route = shortest_path(config.globals.width, config.globals.height,
                          {(b['x'], b['y']) for b in enemy['buildings']},
                          config.globals.spawn, config.globals.base)
    assert route is not None
    scored = []
    for sequence in sequences:
        attacker = player_from_snapshot(own)
        defender = player_from_snapshot(enemy)
        for type_name in sequence:
            expiration = round_number + config.globals.roster_lifespan - 1 if config.globals.roster_lifespan else None
            attacker.roster.append(RosterEntry(attacker.next_roster_id, type_name, round_number, expiration))
            attacker.next_roster_id += 1
        result = simulate_map(attacker, defender, route, round_number, config)
        cost = sum(config.minions[type_name].cost for type_name in sequence)
        scored.append({'sequence': sequence, 'damage': result.damage, 'hits': result.hits,
                       'killed': result.killed, 'cleared': result.cleared, 'cost': cost})
    return scored


@dataclass(frozen=True)
class SearchProfile:
    growth_rounds: int = 4
    defense: str = 'splash'
    defense_count: int = 1
    cap: int = 500
    selection: str = 'damage'


class VisibleSearch:
    def __init__(self, profile: SearchProfile = SearchProfile()):
        self.profile = profile

    def decide(self, observation: dict) -> list[dict]:
        from copy import deepcopy
        profile = self.profile
        opening = Archetype(Profile(growth_rounds=profile.growth_rounds, roster=('tier5',),
                            defense=profile.defense, defense_count=profile.defense_count,
                            purchase_cap=0)).decide(observation)
        if observation['round'] <= profile.growth_rounds:
            return opening
        own = observation['players'][observation['player']]
        gold = own['gold']
        local = deepcopy(observation)
        local_own = local['players'][local['player']]
        for action in opening:
            if action['op'] == 'build_turret':
                gold -= observation['rules']['turrets'][action['type']]['cost']
                local_own['buildings'].append({k: action[k] for k in ('x', 'y', 'type')})
        options = score_sequences(local, purchase_sequences(local, gold, profile.cap))
        if profile.selection == 'efficiency':
            baseline = next(row['damage'] for row in options if not row['sequence'])
            selected = max(options, key=lambda row: ((row['damage'] - baseline) / max(1, row['cost']), row['damage'], -row['cost']))
        else:
            selected = max(options, key=lambda row: (row['damage'], row['hits'], -row['cost']))
        if not selected['sequence']:
            # If every current option is stopped, save for a heavier future wave.
            # Investing half preserves some liquidity without adding weak units.
            n = min(1000, gold // 40)
            return opening + [{'op': 'buy_factory'} for _ in range(n)]
        return opening + [{'op': 'buy_minion', 'type': name} for name in selected['sequence']]


def decide(observation: dict) -> list[dict]:
    return VisibleSearch().decide(observation)
