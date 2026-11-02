"""Original-engine component witness; supplied budgets, not a strength game."""
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import time

from td_game.actions import apply_action
from td_game.combat import simulate_map
from td_game.config import balanced_config
from td_game.pathfinding import shortest_path
from td_game.state import PlayerState
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--output', required=True)
    a = p.parse_args()
    start = time.perf_counter()
    cfg = balanced_config()
    files = set(static_closure({'bot_research.experiments.validation.check_splash_converse'}))
    files.add(Path('td_game/balanced.json'))
    files.add(Path('bot_research/experiments/validation/analysis/splash_converse/PROOF.md'))
    digest = lambda f: hashlib.sha256(Path(f).read_bytes()).hexdigest()
    hashes = {str(f): digest(f) for f in sorted(files)}
    attacker = PlayerState('component attacker', 800, 650)
    defender = PlayerState('component defender', 800, 1000)
    events = [apply_action(attacker, {'op': 'buy_minion', 'type': 'tier5'}, 1, cfg)]
    for x in range(3, 8):
        events.append(apply_action(defender, {'op': 'build_turret', 'type': 'gun3', 'x': x, 'y': 1}, 1, cfg))
    assert all(e['accepted'] for e in events)
    path = shortest_path(12, 12, ((b.x, b.y) for b in defender.buildings), (0, 0), (11, 11))
    expected = [(x, 0) for x in range(12)] + [(11, y) for y in range(1, 12)]
    assert path == expected
    damage = sum(cfg.turrets[b.type].damage * sum((x-b.x)**2+(y-b.y)**2 <= cfg.turrets[b.type].range**2 for x,y in path[:-1]) for b in defender.buildings)
    assert damage >= 1925
    totals = simulate_map(attacker, defender, path, 1, cfg)
    assert totals.hits == totals.damage == totals.cleared == 0
    assert totals.spawned == totals.killed == 1 and defender.hp == 800
    empty = PlayerState('empty control', 800, 0)
    control = simulate_map(attacker, empty, expected, 1, cfg)
    assert control.damage == 140 and control.hits == control.spawned == 1
    assert all(digest(f) == h for f, h in hashes.items())
    out = dict(time_utc=datetime.now(timezone.utc).isoformat(), runtime_seconds=time.perf_counter()-start,
               all_passed=True, scope='Explicitly funded component states, not standard-start matches.',
               source_sha256=hashes, supplied_gold=dict(attacker=650, defender=1000),
               actions=events, path=path, splash_exposure=0, isolated_copy_potential_damage=damage,
               defended=asdict(totals), empty_control=asdict(control))
    atomic_json(a.output, out, exclusive=True)
    print({k: out[k] for k in ('time_utc', 'runtime_seconds', 'all_passed', 'isolated_copy_potential_damage')})

if __name__ == '__main__':
    main()
