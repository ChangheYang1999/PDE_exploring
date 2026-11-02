"""Check the geometric feature filter on legal engine-generated observations."""
from __future__ import annotations
import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.relevant_turret_guard import covered_turret_count, RelevantTurretGuard
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation_strict import now
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    checks, cases = {}, []
    for label, enemy_actions, expected in (
        ('empty', [], 0),
        ('off_route_gun', [{'op': 'build_turret', 'type': 'gun1', 'x': 0, 'y': 11}], 0),
        ('on_route_gun', [{'op': 'build_turret', 'type': 'gun1', 'x': 3, 'y': 1}], 1),
        ('mixed_guns', [{'op': 'build_turret', 'type': 'gun1', 'x': 0, 'y': 11},
                        {'op': 'build_turret', 'type': 'gun1', 'x': 3, 'y': 1}], 1),
        ('off_route_splash', [{'op': 'build_turret', 'type': 'splash', 'x': 0, 'y': 11}], 0),
        ('on_route_splash', [{'op': 'build_turret', 'type': 'splash', 'x': 3, 'y': 1}], 1),
    ):
        for side in (0, 1):
            engine = Engine(balanced_config(), ('filter_check_a', 'filter_check_b'))
            actions = [[], []]
            actions[1-side] = enemy_actions
            records = engine.play_round(actions)
            accepted = all(event['accepted'] for row in records for event in row['event'] if event['kind'] == 'action')
            observation = engine.observation(side)
            before = deepcopy(observation)
            found = covered_turret_count(observation)
            passed = accepted and found == expected and observation == before
            checks[f'{label}_side{side}'] = passed
            cases.append({'label': label, 'side': side, 'actions': enemy_actions, 'expected': expected,
                          'found': found, 'legal': accepted, 'observation_unchanged': observation == before})
    # A real policy call must also leave its supplied public observation intact.
    engine = Engine(balanced_config(), ('filter_check_a', 'filter_check_b'))
    original = engine.observation(0)
    before = deepcopy(original)
    action_list = RelevantTurretGuard().decide(original)
    checks['policy_does_not_mutate_input'] = original == before
    records = engine.play_round([action_list, []])
    checks['opening_actions_legal'] = all(event['accepted'] for row in records for event in row['event'] if event['kind'] == 'action')
    paths = set(static_closure({'bot_research.experiments.validation.check_relevant_turret_guard'}))
    paths.add(Path('td_game/balanced.json'))
    output = {'time_utc': now(), 'checks': checks, 'all_passed': all(checks.values()), 'cases': cases,
              'source_sha256': {str(path): hashlib.sha256(path.read_bytes()).hexdigest() for path in paths},
              'scope': 'Component checks on legal public observations; not strength measurements.'}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({'all_passed': output['all_passed'], 'checks': len(checks)}))
    if not output['all_passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
