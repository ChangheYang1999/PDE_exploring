"""Behavioral checks for a compiled library and its conflict criterion."""
from __future__ import annotations
import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path
from bot_research.bots.counters.compiled_library import CompiledLibrary
from bot_research.experiments.validation.compile_library import conflict_round, maximum_compatible
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation_strict import now


def observation(entry, side):
    data = deepcopy(entry['observation'])
    players = data.pop('players')
    if side:
        players.reverse()
    for i, player in enumerate(players):
        player['name'] = f'renamed_{i}'
    return dict(data, player=side, players=players)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    raw = Path(args.data).read_bytes()
    data = json.loads(raw)
    digest = hashlib.sha256(raw).hexdigest()
    checks = []
    for plan in data['plans']:
        for side in (0, 1):
            bot = CompiledLibrary(args.data, digest, fallback='idle')
            for entry in plan['rounds']:
                assert bot.decide(observation(entry, side)) == entry['actions']
                assert not bot.switched and plan['id'] in bot.active
                assert bot.trace[-1]['fallback'] is None
            checks.append({'plan': plan['id'], 'side': side, 'rounds': len(plan['rounds']), 'passed': True})
    first = data['plans'][0]['rounds']
    assert len(first) >= 2
    bot = CompiledLibrary(args.data, digest, fallback='idle')
    returned = bot.decide(observation(first[0], 0))
    returned.append({'op': 'invalid_deliberate_caller_mutation'})
    assert bot.plans[data['plans'][0]['id']][1]['actions'] == first[0]['actions']
    checks.append({'case': 'returned action isolation', 'passed': True})
    for field in ('hp', 'gold', 'n_factories'):
        bot = CompiledLibrary(args.data, digest, fallback='idle')
        changed = observation(first[0], 0)
        changed['players'][0][field] += 1
        assert bot.decide(changed) == [] and bot.switched
        assert bot.decide(observation(first[1], 0)) == [] and bot.switched
        checks.append({'case': field + ' mismatch and permanent fallback', 'passed': True})
    bot = CompiledLibrary(args.data, digest, fallback='idle')
    changed = observation(first[0], 0)
    changed['rules']['globals']['max_rounds'] += 1
    assert bot.decide(changed) == [] and bot.switched
    checks.append({'case': 'rules mismatch', 'passed': True})
    try:
        CompiledLibrary(args.data, '0' * 64)
    except ValueError:
        pass
    else:
        raise AssertionError('Wrong digest was accepted.')
    checks.append({'case': 'data digest mismatch', 'passed': True})
    def p(obs, acts):
        return {'rounds': [{'round': i + 1, 'observation': o, 'actions': a}
                           for i, (o, a) in enumerate(zip(obs, acts))]}
    a = p([0, 1, 2], [0, 1, 2])
    b = p([0, 1, 2], [0, 9, 2])
    c = p([0, 9, 2], [0, 9, 8])
    assert conflict_round(a, b) == 2
    assert conflict_round(a, c) is None
    assert conflict_round(b, c) is None
    selected, edges = maximum_compatible([a, b, c])
    assert selected == [0, 2] and edges == [{'left': 0, 'right': 1, 'round': 2}]
    checks.append({'case': 'conflict graph and exact maximum with reconverging observations', 'passed': True})
    output = {'time_utc': now(), 'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'data_file': args.data, 'data_sha256': digest, 'checks': checks, 'all_passed': True,
              'scope': 'Recorded-observation unit checks in both assignments, not fresh policy games.'}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({'checks': len(checks), 'all_passed': True}))


if __name__ == '__main__':
    main()
