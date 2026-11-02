"""Small reproductions for evaluation-harness review, not strength tests."""
from __future__ import annotations
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

from td_bots.protocol import collect_actions
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.harness.match import TimedBot
from bot_research.harness.scenarios import make_overrides
from bot_research.harness.baselines import random_legal


def main():
    engine = Engine(balanced_config(), ('A', 'B'))
    override = make_overrides('eco:1')[0]
    def untouched(obs):
        return []
    def mutating(obs):
        obs['players'][obs['player']]['gold'] = 0
        return []
    def raising(obs):
        raise RuntimeError('intentional audit error')
    outputs = {}
    for name, fn in [('untouched', untouched), ('mutating', mutating), ('raising', raising)]:
        actions, errors = collect_actions([TimedBot(fn, override), TimedBot(untouched)],
                                         [engine.observation(p) for p in (0, 1)])
        outputs[name] = {'scripted_actions': actions[0], 'errors': errors}
    assert len(outputs['untouched']['scripted_actions']) == 5
    # Report facts without prescribing semantics: scripted starts currently depend
    # on the discarded policy invocation's mutations and exceptions.
    expansion = []
    gold, factories = 100, 0
    for round_number in range(1, 51):
        purchases = gold // 20
        factories += purchases
        gold = gold % 20 + 22 + factories * 15
        if round_number in (10, 15, 20, 25, 30, 40, 50):
            expansion.append({'round': round_number, 'factory_actions_this_round': purchases,
                              'factories_after_round': factories, 'gold_after_round': gold})
    random_failures = []
    for seed in range(100):
        obs = engine.observation(0)
        obs['players'][0]['gold'] = 1
        actions = random_legal(seed)(obs)
        if any(a['op'] == 'buy_factory' for a in actions):
            random_failures.append({'seed': seed, 'gold': 1, 'actions': actions})
            if len(random_failures) == 3:
                break
    paths = ('bot_research/harness/match.py', 'bot_research/harness/tournament.py',
             'bot_research/harness/scenarios.py', 'bot_research/harness/baselines.py',
             'bot_research/harness/gamekit.py')
    result = {'time_utc': datetime.now(timezone.utc).isoformat(),
              'sources': {p: hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in paths},
              'override_interaction': outputs, 'factory_action_expansion': expansion,
              'random_legal_unaffordable_factory': random_failures}
    with Path('bot_research/runs/validation/harness-audit-001.json').open('x') as stream:
        json.dump(result, stream, sort_keys=True, indent=2)
        stream.write('\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
