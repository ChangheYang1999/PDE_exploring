"""Independent boundary-heavy comparison of two planning simulators to combat.py."""
from __future__ import annotations
import argparse
from dataclasses import asdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import random
import time

from td_game.combat import simulate_map
from td_game.config import balanced_config
from td_game.pathfinding import shortest_path
from td_game.state import Building, PlayerState, RosterEntry
from bot_research.harness import gamekit
from bot_research.bots.economy import fastsim


def generated_map(rng, index):
    if index % 4 == 0:
        # Legal serpentine; turret substitution preserves the occupied-cell map.
        blocked = [(x, y) for j, x in enumerate((1, 3, 5, 7, 9))
                   for y in range(12) if y != (11 if j % 2 == 0 else 0)]
    elif index % 4 == 1:
        blocked = [(x, 1) for x in (1, 2, 3)]
    else:
        blocked = []
        candidates = [(x, y) for x in range(12) for y in range(12) if (x, y) not in ((0, 0), (11, 11))]
        rng.shuffle(candidates)
        target = rng.choice((0, 5, 15, 35, 65, 90))
        for cell in candidates:
            if len(blocked) == target:
                break
            if shortest_path(12, 12, blocked + [cell], (0, 0), (11, 11)):
                blocked.append(cell)
    kinds = ('wall', 'wall', 'splash', 'splash', 'gun1', 'gun2', 'gun3')
    return [{'x': x, 'y': y, 'type': rng.choice(kinds)} for x, y in blocked]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--cases', type=int, default=240)
    parser.add_argument('--seed', type=int, default=83071)
    args = parser.parse_args()
    cfg = balanced_config()
    rules_dict = cfg.to_dict()
    rules = gamekit.Rules.from_observation({'rules': rules_dict})
    rng = random.Random(args.seed)
    sizes = (0, 1, 2, 226, 227, 228, 229, 249, 250, 251, 499, 500, 501, 749, 750, 751, 1251)
    paths = ('td_game/combat.py', 'bot_research/harness/gamekit.py',
             'bot_research/bots/economy/fastsim.py', 'bot_research/experiments/validation/check_simulators.py')
    hashes = {p: hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in paths}
    started = time.perf_counter()
    with Path(args.output).open('x') as out:
        for index in range(args.cases):
            buildings = generated_map(rng, index)
            path = shortest_path(12, 12, [(b['x'], b['y']) for b in buildings], (0, 0), (11, 11))
            assert path is not None
            n = sizes[index % len(sizes)]
            kinds = list(cfg.minions)
            if index % 3 == 0:
                types = [kinds[(k + index) % 5] for k in range(n)]
            elif index % 3 == 1:
                types = [kinds[index % 5]] * n
            else:
                types = [rng.choice(kinds) for _ in range(n)]
            defender = PlayerState('defender', 10000000, 0,
                                  buildings=[Building(b['x'], b['y'], b['type']) for b in buildings])
            attacker = PlayerState('attacker', 800, 0, roster=[RosterEntry(k, t, 1, 12) for k, t in enumerate(types)])
            reference = simulate_map(attacker, defender, path, 1, cfg)
            result = gamekit.simulate_defense(types, path, buildings, rules)
            model = fastsim.MapModel([(b['x'], b['y'], b['type']) for b in buildings], rules_dict)
            economy = fastsim.simulate(model, types, rules_dict, detail=True)
            fields = ('hits', 'damage', 'spawned', 'killed', 'cleared')
            equal = all(getattr(reference, k) == getattr(result, k) for k in fields) and economy[:2] == (reference.hits, reference.damage)
            equal = equal and len(economy[2]) == reference.hits and sum(cfg.minions[types[k]].damage for k in economy[2]) == reference.damage
            row = {'index': index, 'seed': args.seed, 'n_roster': n, 'path_length': len(path) - 1,
                   'n_buildings': len(buildings), 'reference': asdict(reference), 'agree': equal,
                   'condition_sha256': hashlib.sha256(json.dumps([buildings, types], sort_keys=True).encode()).hexdigest()}
            if not equal:
                row.update(buildings=buildings, types=types, gamekit=asdict(result), economy=economy)
            out.write(json.dumps(row, sort_keys=True) + '\n')
            out.flush()
            if not equal:
                raise AssertionError(f'Planning simulator mismatch in case {index}; see relative output path.')
    final_hashes = {p: hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in paths}
    metadata = {'completed_utc': datetime.now(timezone.utc).isoformat(), 'cases': args.cases,
                'seed': args.seed, 'runtime_seconds': time.perf_counter() - started,
                'source_sha256': hashes, 'source_changed': hashes != final_hashes,
                'rules': rules_dict, 'scope': 'synthetic legal static maps; no game-strength claim'}
    Path(args.output).with_suffix('.meta.json').write_text(json.dumps(metadata, sort_keys=True, indent=2) + '\n')
    print(json.dumps(metadata, sort_keys=True), flush=True)
    assert not metadata['source_changed'], 'Simulator changed while checking it.'


if __name__ == '__main__':
    main()
