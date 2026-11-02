"""Original-engine component counterexample for the frozen v17 wrap sampler."""
from __future__ import annotations
import argparse
from copy import deepcopy
from dataclasses import asdict
import hashlib
import json
from pathlib import Path
from td_game.actions import apply_action
from td_game.combat import simulate_map, spawn_schedule
from td_game.config import balanced_config
from td_game.engine import Engine
from td_game.state import RosterEntry
from bot_research.bots.defense.frozen.v17 import plan as P
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation_strict import now
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    game = Engine(balanced_config(), ('defender component', 'attacker component'))
    game.players[0].gold = 10000
    cells = sorted(P.LAYOUT.cells, key=lambda c: (-P.LAYOUT.final_adj[c], c))
    splash = set(cells[:9])
    construction = []
    for x, y in P.LAYOUT.cells:
        action = ({'op': 'build_turret', 'x': x, 'y': y, 'type': 'splash'}
                  if (x, y) in splash else {'op': 'build_wall', 'x': x, 'y': y})
        event = apply_action(game.players[0], action, 1, game.config)
        assert event['accepted'], event
        construction.append(action)
    game.players[0].gold = 100
    game.players[1].gold = 1400
    game.players[1].roster = [RosterEntry(i, 'tier1', 1, 12) for i in range(200)]
    game.players[1].next_roster_id = 200
    observation = game.observation(0)
    rules = P.gk.Rules.from_observation(observation)
    length = len(game.path(0)) - 1
    damage = P.splash_damage(observation['players'][0]['buildings'], rules)
    assert length > 49 and 560 <= damage < 1500
    compositions = P.threat_compositions(observation)
    samples = []
    for types in compositions:
        attacker = deepcopy(game.players[1])
        for kind in types[200:]:
            event = apply_action(attacker, {'op': 'buy_minion', 'type': kind}, 1, game.config)
            assert event['accepted'], event
        totals = simulate_map(attacker, deepcopy(game.players[0]), game.path(0), 1, game.config)
        samples.append({'new_types': types[200:], 'combat': asdict(totals)})
    corrected = ['tier1'] * 50 + ['tier5']
    attacker = deepcopy(game.players[1])
    for kind in corrected:
        event = apply_action(attacker, {'op': 'buy_minion', 'type': kind}, 1, game.config)
        assert event['accepted'], event
    actual = simulate_map(attacker, deepcopy(game.players[0]), game.path(0), 1, game.config)
    schedule = spawn_schedule(attacker.roster, 1, 250)
    assert any(e.id == 250 and e.type == 'tier5' for e in schedule[0])
    old_wrap = P.wrap_bundles(1400, 200, rules)
    old_t5 = next(t for t in old_wrap if 'tier5' in t)
    assert old_t5 == ['tier1'] * 49 + ['tier5']
    sampled_zero = all(s['combat']['damage'] == 0 for s in samples)
    assert sampled_zero and actual.damage == 140 and actual.hits == 1
    planned = P.plan_defense(observation, 100, threat_types=compositions)
    assert planned == []
    paths = set(static_closure({'bot_research.experiments.validation.check_roster_wrap'}))
    paths.add(Path('td_game/balanced.json'))
    output = {'time_utc': now(), 'source_sha256': {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
              'scope': 'Synthetic component state, not a full standard-start game. Construction actions are legal; full-state reachability is not asserted.',
              'observation': observation, 'construction_actions': construction,
              'route': game.path(0), 'route_length': length, 'splash_damage_per_copy': damage,
              'sampled_compositions': samples, 'sampled_all_zero_damage': sampled_zero,
              'old_tier5_wrap': old_t5, 'old_first_heavy_index': 249,
              'corrected_purchase': corrected, 'corrected_cost': 1400,
              'corrected_first_heavy_index': 250, 'corrected_combat': asdict(actual),
              'returned_defense': planned}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({'samples': len(samples), 'sampled_all_zero': sampled_zero,
                      'corrected_damage': actual.damage, 'route_length': length,
                      'splash_damage': damage, 'returned_defense': planned}))


if __name__ == '__main__':
    main()
