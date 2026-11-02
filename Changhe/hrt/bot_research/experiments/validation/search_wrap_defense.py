"""Bounded exact-engine search for a gun-only response to the wrap fixture."""
from __future__ import annotations
import argparse
from copy import deepcopy
from dataclasses import asdict
import hashlib
from itertools import combinations
import json
from pathlib import Path
import time
from td_game.actions import apply_action
from td_game.combat import simulate_map
from td_game.config import balanced_config
from td_game.engine import Engine
from td_game.state import RosterEntry
from bot_research.bots.defense.frozen.v18 import plan
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation_strict import now
from bot_research.experiments.validation.source_closure import static_closure


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    ap.add_argument('--max-seconds', type=float, default=240)
    ap.add_argument('--max-evaluations', type=int, default=10000)
    args = ap.parse_args()
    started = time.monotonic()
    fixture = Path('bot_research/runs/validation/roster-wrap-check-001.json')
    game = Engine(balanced_config(), ('defender', 'attacker'))
    game.players[0].gold = 10000
    for action in json.loads(fixture.read_text())['construction_actions']:
        assert apply_action(game.players[0], action, 1, game.config)['accepted']
    game.players[0].gold = 1000
    game.players[1].gold = 1400
    game.players[1].roster = [RosterEntry(i, 'tier1', 1, 12) for i in range(200)]
    game.players[1].next_roster_id = 200
    observation = game.observation(0)
    comps = plan.threat_compositions(observation)
    targets = []
    for kinds in comps:
        attacker = deepcopy(game.players[1])
        for kind in kinds[200:]:
            assert apply_action(attacker, {'op': 'buy_minion', 'type': kind}, 1, game.config)['accepted']
        targets.append(attacker)
    attackers = [deepcopy(game.players[1])]
    for kind in ['tier1'] * 50 + ['tier5']:
        assert apply_action(attackers[0], {'op': 'buy_minion', 'type': kind}, 1, game.config)['accepted']
    candidates = []
    for y in range(12):
        for x in range(12):
            a = {'op': 'build_turret', 'type': 'gun3', 'x': x, 'y': y}
            if apply_action(deepcopy(game.players[0]), a, 1, game.config)['accepted']:
                candidates.append(a)
    rows, solutions, counts, stopped = [], [], 0, None
    for size in range(1, 6):
        for group in combinations(range(len(candidates)), size):
            if time.monotonic() - started >= args.max_seconds or counts >= args.max_evaluations:
                stopped = 'declared_search_limit'
                break
            defender = deepcopy(game.players[0])
            acts = [candidates[i] for i in group]
            if not all(apply_action(defender, a, 1, game.config)['accepted'] for a in acts):
                continue
            path = plan.gk.route({(b.x, b.y) for b in defender.buildings})
            actual = simulate_map(deepcopy(attackers[0]), deepcopy(defender), path, 1, game.config)
            counts += 1
            row = {'actions': acts, 'cost': 1000 - defender.gold, 'corrected_attack': asdict(actual), 'route_length': len(path) - 1}
            rows.append(row)
            if not actual.damage:
                damages = [simulate_map(deepcopy(a), deepcopy(defender), path, 1, game.config).damage for a in targets]
                row['sampled_damage'] = damages
                row['stops_all_samples'] = not any(damages)
                solutions.append(row)
        if stopped or solutions:
            break
    paths = set(static_closure({'bot_research.experiments.validation.search_wrap_defense'}))
    paths |= {fixture, Path('td_game/balanced.json')}
    result = {'time_utc': now(), 'runtime_seconds': time.monotonic() - started,
              'source_sha256': {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
              'initial_legal_gun3_actions': candidates, 'evaluations': counts,
              'stopped': stopped, 'solutions': solutions, 'examined': rows,
              'scope': 'Synthetic legal-construction component state, not a standard-start game. Subsets of initially legal gun3 placements only, stopping after the first successful cardinality or declared resource bound. A found solution is checked on the unchanged engine.'}
    atomic_json(args.output, result, exclusive=True)
    print(json.dumps({k: result[k] for k in ('time_utc', 'runtime_seconds', 'evaluations', 'stopped', 'initial_legal_gun3_actions', 'solutions')}))


if __name__ == '__main__':
    main()
