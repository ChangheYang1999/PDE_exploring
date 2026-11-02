"""Exercise stateful schedule and mixed wrappers on four-round engine prefixes.

A counting factory policy exposes accidental model recreation. Prefixes cover
rounds before, during and after the mixed attack, in both player assignments.
These are component fixtures, not strength evaluations or complete games.
"""
from datetime import datetime, timezone
import argparse
import hashlib
import json
from pathlib import Path
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.stateful_mixed import StatefulMixed
from bot_research.bots.counters.stateful_schedule import StatefulSchedule
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


class CountingFactory:
    def __init__(self):
        self.calls = 0

    def __call__(self, observation):
        self.calls += 1
        return [{'op': 'buy_factory'} for _ in range(self.calls)]


def fixture():
    return CountingFactory()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    model = 'bot_research.experiments.validation.check_stateful_wrappers:@fixture'
    checks = []
    for kind in ('mixed', 'schedule'):
        for side in (0, 1):
            policy = (StatefulMixed(model_spec=model, attack_round=3, evaluations=32,
                                   seed=17, count_cap=20) if kind == 'mixed' else
                      StatefulSchedule(model_spec=model, schedule=[(2, 'tier1', 1),
                                                                  (3, 'tier2', 1)]))
            target = CountingFactory()
            engine = Engine(balanced_config(), ('fixture0', 'fixture1'))
            for rnd in range(1, 5):
                actions = [None, None]
                actions[side] = policy.decide(engine.observation(side))
                actions[1-side] = target(engine.observation(1-side))
                assert policy.trace[-1]['predicted_actions'] == actions[1-side]
                assert policy.model.last_round == rnd
                assert policy.model.policy.calls == rnd
                records = engine.play_round(actions)
                assert all(e['accepted'] for r in records for e in r['event']
                           if e['kind'] == 'action')
                checks.append({'wrapper': kind, 'side': side, 'round': rnd,
                               'predicted_factory_count': rnd, 'all_accepted': True})
    sources = static_closure({'bot_research.experiments.validation.check_stateful_wrappers'})
    output = {'time_utc': datetime.now(timezone.utc).isoformat(), 'checks': checks,
              'all_passed': True, 'prefixes': 4, 'checked_rounds': len(checks),
              'source_sha256': {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
              'scope': 'Four standard-initial-state prefixes, each of four rounds. Tests state retention and legal wrapper integration, not full-game strength.'}
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({'prefixes': 4, 'checked_rounds': len(checks), 'all_passed': True}))


if __name__ == '__main__':
    main()
