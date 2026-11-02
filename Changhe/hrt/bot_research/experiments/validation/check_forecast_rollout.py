"""Check observable-state reconstruction before using full-game local rollouts."""
from __future__ import annotations
import argparse
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from td_game.engine import Engine
from td_game.config import balanced_config
from bot_research.bots.counters.forecast_rollout import reconstruct
from bot_research.bots.counters.archetypes import make


def normalized(game):
    snapshots = [game.snapshot(i) for i in (0, 1)]
    for snapshot in snapshots:
        for entry in snapshot['roster']:
            entry.pop('id')
    return {'round': game.round, 'players': snapshots, 'result': game.result}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--output', required=True)
    args = p.parse_args()
    checks = []
    # Include empty-roster periods after prior purchases expire, and both sides.
    for schedule in ('persistent', 'gap'):
        game = Engine(balanced_config(), ('side0', 'side1'))
        for rnd in range(1, 31):
            observations = [game.observation(i) for i in (0, 1)]
            rebuilt = [reconstruct(o) for o in observations]
            for i, clone in enumerate(rebuilt):
                assert clone.observation(i) == observations[i]
            actions = []
            for side in (0, 1):
                orders = []
                if rnd == 1:
                    orders = [{'op': 'buy_factory'}] * 4
                elif rnd == 2:
                    orders = [{'op': 'build_turret', 'type': 'splash', 'x': 1, 'y': 1}]
                elif (schedule == 'persistent' and rnd % 4 == 0) or rnd in (3, 20):
                    orders = [{'op': 'buy_minion', 'type': 'tier2'}] * (1 + side)
                actions.append(orders)
            game.play_round(deepcopy(actions))
            for clone in rebuilt:
                clone.play_round(deepcopy(actions))
                assert normalized(clone) == normalized(game)
            checks.append({'schedule': schedule, 'round': rnd,
                           'both_observations_reconstructed': True,
                           'both_next_states_match_up_to_roster_ids': True})
            if game.result:
                break
    sources = ['bot_research/bots/counters/forecast_rollout.py',
               'bot_research/bots/counters/visible_search.py',
               'bot_research/experiments/validation/check_forecast_rollout.py',
               'td_game/engine.py', 'td_game/state.py', 'td_game/actions.py']
    result = {'time_utc': datetime.now(timezone.utc).isoformat(), 'checks': checks,
              'all_checks_passed': True,
              'scope': 'observable state equality and one-step transition equality up to roster ID renaming',
              'sources': {f: hashlib.sha256(Path(f).read_bytes()).hexdigest() for f in sources}}
    with Path(args.output).open('x') as f:
        json.dump(result, f, sort_keys=True, indent=2)
        f.write('\n')
    print(json.dumps({'all_checks_passed': True, 'checked_rounds': len(checks)}))


if __name__ == '__main__':
    main()
