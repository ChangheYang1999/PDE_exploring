"""Check legality, reproducibility and original-combat scores of package search."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import time
from td_game.config import balanced_config
from td_game.combat import simulate_map
from td_game.pathfinding import shortest_path
from td_game.state import Building, PlayerState, RosterEntry
from bot_research.bots.counters.package_search import search_package
from bot_research.bots.economy.frozen.v2.fastsim import MapModel, simulate
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation import now
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--evaluations', type=int, default=64)
    args = parser.parse_args()
    cfg = balanced_config()
    rules = cfg.to_dict()
    maps = [[], [(2, 2, 'gun1')], [(1, 1, 'splash'), (3, 2, 'gun2')],
            [(2, 1, 'gun3'), (4, 1, 'gun2'), (6, 1, 'gun1'), (1, 1, 'splash')]]
    budgets = [0, 100, 400, 1000, 4000, 30000]
    prefixes = [[], ['tier1'] * 249, ['tier3', 'tier1'] * 125]
    frozen = {str(path): hashlib.sha256(path.read_bytes()).hexdigest() for path in static_closure({
        'bot_research.experiments.validation.check_package_search'})}
    rows = []
    started = time.perf_counter()
    for index in range(24):
        buildings = maps[index % len(maps)]
        budget = budgets[index % len(budgets)]
        prefix = prefixes[index % len(prefixes)]
        package, trace = search_package(buildings, rules, prefix, budget,
            evaluations=args.evaluations, seed=61031 + index, count_cap=200)
        duplicate, trace2 = search_package(buildings, rules, prefix, budget,
            evaluations=args.evaluations, seed=61031 + index, count_cap=200)
        assert (package, trace) == (duplicate, trace2), 'Seeded search changed on exact repetition.'
        assert trace['evaluations'] <= args.evaluations
        assert len(package) <= 200
        cost = sum(rules['minions'][kind]['cost'] for kind in package)
        assert cost <= budget and trace['cost'] == cost
        types = prefix + package
        path = shortest_path(12, 12, {(x, y) for x, y, _ in buildings}, (0, 0), (11, 11))
        defender = PlayerState('defender', 10**9, 0, buildings=[Building(*b) for b in buildings])
        attacker = PlayerState('attacker', 800, 0,
            roster=[RosterEntry(i, kind, 1, 12) for i, kind in enumerate(types)])
        authoritative = simulate_map(attacker, defender, path, 1, cfg)
        assert authoritative.damage == trace['predicted_damage']
        local = MapModel(buildings, rules)
        pure_scores = []
        for kind, spec in rules['minions'].items():
            maximum = min(200, budget // spec['cost'])
            for count in sorted({1, maximum // 2, maximum}):
                if 0 < count <= maximum:
                    pure_scores.append(simulate(local, prefix + [kind] * count, rules)[1])
        assert trace['predicted_damage'] >= max(pure_scores, default=trace['baseline_damage'])
        rows.append({'index': index, 'buildings': buildings, 'budget': budget,
                     'prefix': prefix, 'trace': trace, 'authoritative_damage': authoritative.damage,
                     'best_pure_damage': max(pure_scores, default=trace['baseline_damage'])})
    drift = [name for name, value in frozen.items() if hashlib.sha256(Path(name).read_bytes()).hexdigest() != value]
    result = {'time_utc': now(), 'conditions': len(rows), 'cases': rows,
              'runtime_seconds': time.perf_counter() - started, 'source_sha256': frozen,
              'source_drift': drift, 'all_checks_passed': not drift,
              'scope': '24 selected legal map/roster/budget conditions; no game-strength conclusion.'}
    atomic_json(args.output, result, exclusive=True)
    print(json.dumps({k: result[k] for k in ('time_utc', 'conditions', 'runtime_seconds', 'source_drift', 'all_checks_passed')}))
    assert not drift


if __name__ == '__main__':
    main()
