"""Commit early to a cheap long route, then grow and attack.

This deliberately trades future high-adjacency turret sites for immediate path
income. It is a pressure counter, not a claim of an indefinitely safe fortress.
"""
from __future__ import annotations
from copy import deepcopy

from td_game.pathfinding import shortest_path
from bot_research.bots.counters.archetypes import Archetype, Profile


class MazePressure:
    def __init__(self, growth_rounds=4, tier='tier3', n_lines=4, orientation='h',
                 defense='splash', defense_count=1, defense_start=1,
                 keep_investing=0.0, purchase_cap=1000):
        if int(n_lines) not in (2, 4):
            raise ValueError('Use two or four barrier lines.')
        if orientation not in ('h', 'v'):
            raise ValueError('Unknown orientation.')
        self.n_lines = int(n_lines)
        self.orientation = orientation
        self.policy = Archetype(Profile(growth_rounds=int(growth_rounds), roster=(tier,),
            defense=defense, defense_count=int(defense_count), defense_start=int(defense_start),
            keep_investing=float(keep_investing), purchase_cap=int(purchase_cap)))

    def decide(self, observation):
        obs = deepcopy(observation)
        own = obs['players'][obs['player']]
        rules = obs['rules']
        g = rules['globals']
        blocked = {(b['x'], b['y']) for b in own['buildings']}
        actions = []
        for j, line in enumerate(range(1, 2 * self.n_lines, 2)):
            gap = 11 if j % 2 == 0 else 0
            for k in range(12):
                if k == gap:
                    continue
                cell = (k, line) if self.orientation == 'h' else (line, k)
                if cell in blocked or own['gold'] < rules['wall_cost']:
                    continue
                if shortest_path(g['width'], g['height'], blocked | {cell}, tuple(g['spawn']), tuple(g['base'])) is None:
                    continue
                action = {'op': 'build_wall', 'x': cell[0], 'y': cell[1]}
                actions.append(action)
                blocked.add(cell)
                own['buildings'].append({'type': 'wall', 'x': cell[0], 'y': cell[1]})
                own['gold'] -= rules['wall_cost']
                own['n_walls'] += 1
        own['length_path'] = len(shortest_path(g['width'], g['height'], blocked, tuple(g['spawn']), tuple(g['base']))) - 1
        return actions + self.policy.decide(obs)


def make(growth_rounds=4, tier='tier3', n_lines=4, orientation='h',
         defense='splash', defense_count=1, defense_start=1,
         keep_investing=0.0, purchase_cap=1000):
    return MazePressure(growth_rounds, tier, n_lines, orientation, defense,
                        defense_count, defense_start, keep_investing, purchase_cap).decide
