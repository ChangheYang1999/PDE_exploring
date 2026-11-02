"""Check a frozen threshold helper against original combat on a simple map."""
from copy import deepcopy
from datetime import datetime, timezone
import argparse
import hashlib
import json
from pathlib import Path
import time

from td_game.combat import simulate_map
from td_game.config import balanced_config
from td_game.engine import Engine
from td_game.pathfinding import shortest_path
from td_game.state import PlayerState, RosterEntry
from bot_research.harness.gamekit import Rules, simulate_defense
from bot_research.bots.defense.frozen.v28.fortress import _kill_threshold
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    files = set(static_closure({'bot_research.experiments.validation.check_kill_threshold_boundary'}))
    files.update(map(Path, ['td_game/balanced.json', 'bot_research/experiments/validation/analysis/kill_threshold_boundary/PROOF.md']))
    sources = {str(p): digest(p) for p in files}
    cfg = balanced_config()
    engine = Engine(cfg, ('component0', 'component1'))
    rules = Rules.from_observation(engine.observation(0))
    path = shortest_path(cfg.globals.width, cfg.globals.height, set(), cfg.globals.spawn, cfg.globals.base)
    assert len(path)-1 == 22
    damages = {}
    for count in range(1, 9):
        attacker = PlayerState('attacker', 800, 0, roster=[RosterEntry(i, 'tier5', 1, None) for i in range(count)])
        defender = PlayerState('defender', 800, 0)
        actual = simulate_map(deepcopy(attacker), deepcopy(defender), path, 1, cfg).damage
        model = simulate_defense(['tier5']*count, path, [], rules).damage
        assert actual == model == 140*count
        damages[count] = actual
    cases = []
    for hp, limit in [(5, 2000), (140, 2000), (141, 2000), (800, 2000), (5, 1), (800, 6), (800, 60)]:
        minimum = next((n for n in range(1, min(8, limit)+1) if damages[n] >= hp), None)
        returned = _kill_threshold(path, [], rules, hp, n_max=limit)
        expected = 2 if hp <= 140 and limit >= 60 else None if limit < 60 else minimum
        assert returned == expected
        cases.append(dict(hp=hp, n_max=limit, exact_minimum=minimum, helper_returned=returned, agrees=returned==minimum))
    assert all(digest(p)==h for p,h in sources.items())
    result = dict(time_utc=datetime.now(timezone.utc).isoformat(), runtime_seconds=time.perf_counter()-started,
        source_sha256=sources, all_checks_passed=True, path=path, original_damage=damages, cases=cases,
        verdict='REFUTED', claim='The frozen helper always returns the smallest lethal positive tier5 count up to n_max.',
        scope='Empty-map component checks only. Positive HP 5 and 140 expose the unchecked lower bound; small explicit n_max exposes the empty bracket. No observed full-game effect is claimed.')
    atomic_json(args.output,result,exclusive=True)
    print(json.dumps({k:result[k] for k in ['time_utc','runtime_seconds','all_checks_passed','verdict','cases']}),flush=True)


if __name__ == '__main__':
    main()
