"""Check the explicit pure-tier counterexample with unchanged combat."""
from __future__ import annotations
import argparse
from dataclasses import asdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from td_game.config import balanced_config
from td_game.combat import simulate_map
from td_game.pathfinding import shortest_path
from td_game.state import Building, PlayerState, RosterEntry
from bot_research.experiments.validation.artifact_io import atomic_json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    input_path = Path('bot_research/experiments/validation/analysis/pure_tier_threat/verification/input.json')
    case = json.loads(input_path.read_text())
    config = balanced_config()
    catalog = config.to_dict()['minions']
    buildings = [Building(**v) for v in case['buildings']]
    path = shortest_path(12, 12, [(b.x, b.y) for b in buildings], (0, 0), (11, 11))
    pre = [case['existing_roster']['type']] * case['existing_roster']['count']

    def run(extra):
        roster = [RosterEntry(i, t, 1, 12) for i, t in enumerate(pre+extra)]
        attack = PlayerState('attacker', 800, 0, roster=roster)
        defense = PlayerState('defender', 100000, 0, buildings=buildings)
        return asdict(simulate_map(attack, defense, path, case['evaluation_round'], config))

    pure = {}
    for tier, spec in catalog.items():
        n = case['purchase_budget'] // spec['cost']
        pure[tier] = {'copies': n, 'result': run([tier]*n)}
    mixed = [t for t, n in case['mixed_purchase_runs'] for _ in range(n)]
    result = run(mixed)
    cost = sum(catalog[t]['cost'] for t in mixed)
    assert max(v['result']['damage'] for v in pure.values()) == case['expected_pure_max_damage']
    assert result['damage'] == case['expected_mixed_damage']
    assert cost == case['expected_mixed_cost'] <= case['purchase_budget']
    sources = ('td_game/combat.py', 'td_game/pathfinding.py', 'td_game/state.py', 'td_game/balanced.json',
               'bot_research/experiments/validation/verify_pure_tier_bound.py', str(input_path))
    row = {'time_utc': datetime.now(timezone.utc).isoformat(), 'input': str(input_path),
           'pure_tier_results': pure, 'mixed_result': result, 'mixed_cost': cost, 'route': path,
           'sources': {name: hashlib.sha256(Path(name).read_bytes()).hexdigest() for name in sources},
           'scope': case['scope'], 'all_checks_passed': True}
    atomic_json(args.output, row, exclusive=True)
    print(json.dumps(row, sort_keys=True))


if __name__ == '__main__':
    main()
