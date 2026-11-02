"""Modulo-aware additions for visible-state attack search."""
from __future__ import annotations
from td_game.pathfinding import shortest_path
from bot_research.bots.counters.visible_search import purchase_sequences, score_sequences


def phase_candidates(observation: dict, gold: int, cap: int = 1000) -> list[tuple[str, ...]]:
    rules = observation['rules']
    catalog = rules['minions']
    globals_ = rules['globals']
    own = observation['players'][observation['player']]
    enemy = observation['players'][1 - observation['player']]
    round_number = observation['round']
    active_count = sum(e['bought_round'] <= round_number and (e['expires_after_round'] is None or e['expires_after_round'] >= round_number) for e in own['roster'])
    route = shortest_path(globals_['width'], globals_['height'],
            [(b['x'], b['y']) for b in enemy['buildings']], tuple(globals_['spawn']), tuple(globals_['base']))
    assert route is not None
    ticks = globals_['ticks_per_round']
    length = len(route) - 1
    cheapest = min(catalog, key=lambda t: (catalog[t]['cost'], t))
    cheap_cost = catalog[cheapest]['cost']
    options = set(purchase_sequences(observation, gold, cap))
    for heavy in catalog:
        sequence = []
        money = gold
        while len(sequence) < cap:
            phase = (active_count + len(sequence)) % ticks
            if phase + length >= ticks:
                fill = ticks - phase
                if len(sequence) + fill >= cap or money < fill * cheap_cost + catalog[heavy]['cost']:
                    break
                sequence.extend([cheapest] * fill)
                money -= cheap_cost * fill
            else:
                cost = catalog[heavy]['cost']
                if money < cost:
                    break
                sequence.append(heavy)
                money -= cost
        options.add(tuple(sequence))
    return sorted(options, key=lambda seq: (len(seq), seq))


def choose(observation: dict, gold: int, cap: int = 1000) -> dict:
    scored = score_sequences(observation, phase_candidates(observation, gold, cap))
    return max(scored, key=lambda row: (row['damage'], row['hits'], -row['cost']))
