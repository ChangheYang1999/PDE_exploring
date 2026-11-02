"""Replay saved bound counterexamples through the unchanged combat engine."""
from __future__ import annotations
from dataclasses import asdict
from datetime import datetime, timezone
import json
from pathlib import Path
from td_game.config import balanced_config
from td_game.combat import simulate_map
from td_game.pathfinding import shortest_path
from td_game.state import Building, PlayerState, RosterEntry
from bot_research.experiments.validation.evaluate import source_hashes


def run(buildings, kind, n):
    cfg = balanced_config()
    defender = PlayerState('defender', 10**8, 0, buildings=[Building(**b) for b in buildings])
    attacker = PlayerState('attacker', 800, 0, roster=[RosterEntry(i, kind, 1, 12) for i in range(n)])
    path = shortest_path(12, 12, [(b.x, b.y) for b in defender.buildings], (0, 0), (11, 11))
    assert path is not None
    return asdict(simulate_map(attacker, defender, path, 1, cfg))


def main():
    saved = json.loads(Path('bot_research/runs/validation/planner-rule-probe-001.json').read_text())
    c = saved['largest_one_splash_change']
    after = c['before_buildings'] + [{'type': 'splash', 'x': c['add_splash'][0], 'y': c['add_splash'][1]}]
    rows = []
    for n in (1, 100, 501):
        before_result = run(c['before_buildings'], 'tier5', n)
        after_result = run(after, 'tier5', n)
        assert before_result['hits'] > 0 and after_result['hits'] == 0
        rows.append({'tier': 'tier5', 'count': n, 'before': before_result, 'after': after_result})
    thousand = run([], 'tier1', 1000)
    assert thousand['damage'] == 4560
    output = {'time_utc': datetime.now(timezone.utc).isoformat(), 'sources': source_hashes(),
              'input_case': 'runs/validation/planner-rule-probe-001.json',
              'single_splash_reroute': rows, 'empty_map_1000_tier1': thousand}
    with Path('bot_research/runs/validation/planner-bound-engine-check-001.json').open('x') as stream:
        json.dump(output, stream, sort_keys=True, indent=2)
        stream.write('\n')
    print(json.dumps(output, sort_keys=True))


if __name__ == '__main__':
    main()
