"""Independent original-engine regression of the frozen v18 wrap repair."""
from __future__ import annotations
import argparse
from copy import deepcopy
from dataclasses import asdict
import hashlib
import json
from pathlib import Path
from td_game.actions import apply_action
from td_game.combat import simulate_map
from td_game.config import balanced_config
from td_game.engine import Engine
from td_game.state import RosterEntry
from bot_research.bots.defense.frozen.v17 import plan as old
from bot_research.bots.defense.frozen.v18 import plan as new
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation_strict import now
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    fixture_path = Path('bot_research/runs/validation/roster-wrap-check-001.json')
    fixture = json.loads(fixture_path.read_text())
    game = Engine(balanced_config(), ('defender', 'attacker'))
    game.players[0].gold = 10000
    for action in fixture['construction_actions']:
        assert apply_action(game.players[0], action, 1, game.config)['accepted']
    game.players[0].gold = 1000
    game.players[1].gold = 1400
    game.players[1].roster = [RosterEntry(i, 'tier1', 1, 12) for i in range(200)]
    game.players[1].next_roster_id = 200
    observation = game.observation(0)
    rules = new.gk.Rules.from_observation(observation)
    attack = ['tier1'] * 50 + ['tier5']
    rows = []
    for label, policy in (('v17', old), ('v18', new)):
        comps = policy.threat_compositions(observation)
        actions = policy.plan_defense(observation, 1000, threat_types=comps)
        defender = deepcopy(game.players[0])
        for action in actions:
            assert apply_action(defender, action, 1, game.config)['accepted']
        damage_before, damage_after = [], []
        for types in comps:
            attacker = deepcopy(game.players[1])
            for kind in types[200:]:
                assert apply_action(attacker, {'op': 'buy_minion', 'type': kind}, 1, game.config)['accepted']
            damage_before.append(simulate_map(attacker, deepcopy(game.players[0]), game.path(0), 1, game.config).damage)
            path = new.gk.route({(b.x, b.y) for b in defender.buildings})
            damage_after.append(simulate_map(deepcopy(attacker), deepcopy(defender), path, 1, game.config).damage)
        attacker = deepcopy(game.players[1])
        for kind in attack:
            assert apply_action(attacker, {'op': 'buy_minion', 'type': kind}, 1, game.config)['accepted']
        path = new.gk.route({(b.x, b.y) for b in defender.buildings})
        corrected = simulate_map(attacker, deepcopy(defender), path, 1, game.config)
        rows.append({'version': label, 'compositions': len(comps),
                     'contains_counterexample': ['tier1'] * 200 + attack in comps,
                     'largest_sampled_damage_before': max(damage_before),
                     'largest_sampled_damage_after': max(damage_after),
                     'defense_actions': actions, 'defense_cost': 1000 - defender.gold,
                     'counterexample_after_defense': asdict(corrected)})
    assert rows[0]['largest_sampled_damage_before'] == 0 and rows[0]['defense_actions'] == []
    assert rows[0]['counterexample_after_defense']['damage'] == 140
    assert rows[1]['contains_counterexample'] and rows[1]['largest_sampled_damage_before'] == 140
    alternatives = []
    for y in range(12):
        for x in range(12):
            defender = deepcopy(game.players[0])
            action = {'op': 'build_turret', 'type': 'gun3', 'x': x, 'y': y}
            if not apply_action(defender, action, 1, game.config)['accepted']:
                continue
            path = new.gk.route({(b.x, b.y) for b in defender.buildings})
            test_attacker = deepcopy(game.players[1])
            for kind in attack:
                assert apply_action(test_attacker, {'op': 'buy_minion', 'type': kind}, 1, game.config)['accepted']
            actual = simulate_map(test_attacker, deepcopy(defender), path, 1, game.config)
            if actual.damage:
                continue
            damages = []
            for types in new.threat_compositions(observation):
                test_attacker = deepcopy(game.players[1])
                for kind in types[200:]:
                    assert apply_action(test_attacker, {'op': 'buy_minion', 'type': kind}, 1, game.config)['accepted']
                damages.append(simulate_map(test_attacker, deepcopy(defender), path, 1, game.config).damage)
            alternatives.append({'action': action, 'cost': 1000 - defender.gold,
                                 'corrected_attack_damage': actual.damage,
                                 'all_sampled_damage': damages, 'all_sampled_stopped': not any(damages)})
    boundaries = []
    for n in (0, 1, 199, 200, 249, 250, 251, 499, 500, 501, 749):
        bundles = new.wrap_bundles(30000, n, rules)
        t5 = next(t for t in bundles if 'tier5' in t)
        pad = t5.index('tier5')
        assert (n + pad) % 250 == 0
        boundaries.append({'visible': n, 'v18_padding': pad, 'least_nonnegative_padding': (-n) % 250,
                           'first_heavy_spawn_tick': (n + pad) % 250})
    paths = set(static_closure({'bot_research.experiments.validation.check_roster_wrap_repair'}))
    paths |= {fixture_path, Path('td_game/balanced.json')}
    output = {'time_utc': now(), 'source_sha256': {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
              'defender_budget': 1000, 'results': rows, 'boundaries': boundaries, 'all_passed': True,
              'single_gun3_alternatives': alternatives,
              'planner_stopped_corrected_attack': rows[1]['counterexample_after_defense']['damage'] == 0,
              'scope': 'Synthetic component regression with legal construction and original combat. No standard-start reachability or full-bot strength claim.'}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({'all_passed': True, 'results': rows, 'boundaries': boundaries, 'single_gun3_alternatives': alternatives}))


if __name__ == '__main__':
    main()
