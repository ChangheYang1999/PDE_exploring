"""Check bluff legality, empty-route exposure, and a baseline identity."""
from __future__ import annotations
import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path

from td_game.actions import apply_action
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.archetypes import make as archetype
from bot_research.bots.counters.feature_bluff import FeatureBluff
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation import now
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    config = balanced_config()
    cases = []
    for side in (0, 1):
        for params in ({'turret_round': 0}, {}, {'turret_round': 3},
                       {'turret_x': 3, 'turret_y': 1},
                       {'turret_round': 3, 'turret_x': 3, 'turret_y': 1}):
            game = Engine(config, ('a', 'b'))
            policy = FeatureBluff(**params)
            baseline = archetype('eco6_t5')
            recorded = []
            for rnd in range(1, 9):
                observation = game.observation(side)
                before = deepcopy(observation)
                actions = policy.decide(observation)
                assert observation == before
                if params.get('turret_round') == 0:
                    assert actions == baseline.decide(observation)
                pair = [[], []]
                pair[side] = actions
                records = game.play_round(pair)
                assert all(e['accepted'] for row in records for e in row['event'] if e['kind'] == 'action')
                recorded.append({'round': rnd, 'actions': actions})
            cases.append({'side': side, 'parameters': params, 'rounds': recorded})
    game = Engine(config, ('a', 'b'))
    original = game.path(0)
    assert apply_action(game.players[0], {'op': 'build_turret', 'type': 'gun1', 'x': 0, 'y': 11}, 1, config)['accepted']
    changed = game.path(0)
    turret = config.turrets['gun1']
    distances = [(x*x + (y-11)*(y-11)) for x, y in changed[:-1]]
    assert original == changed
    assert min(distances) > turret.range ** 2
    paths = set(static_closure({'bot_research.experiments.validation.check_feature_bluff'}))
    paths |= {Path('td_game/balanced.json'), Path('configs/balanced.json')}
    output = {'time_utc': now(), 'all_passed': True, 'cases': cases,
              'empty_route_check': {'unchanged': True, 'minimum_squared_distance': min(distances),
                                    'gun_range_squared': turret.range ** 2},
              'source_sha256': {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
              'scope': 'Ten eight-round original-engine legality checks; the no-turret policy equals eco6_t5 on all 16 tested observations. Empty-route geometry only, not a strength result.'}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({k: v for k, v in output.items() if k not in ('cases', 'source_sha256')}))


if __name__ == '__main__':
    main()
