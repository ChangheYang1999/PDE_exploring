"""Unchanged-engine smoke and legality checks for the expanded tuning pool."""
from __future__ import annotations
import json
from pathlib import Path
from bot_research.bots.counters import pool
from bot_research.bots.counters.archetypes import make
from bot_research.experiments.validation.evaluate import evaluate


class CallableBot:
    def __init__(self, decide):
        self.decide = decide


def main():
    factories = {'turtle_splash': lambda: pool.turtle(), 'turtle_gun': lambda: pool.turtle(kind='gun2'),
        'mirror': pool.mirror, 'random_130': lambda: pool.random_legal(seed=130),
        'stacker': pool.stacker, 'rush_t5': pool.rush_t5}
    with Path('bot_research/runs/validation/expanded-pool-smoke-001.jsonl').open('x') as stream:
        for name, factory in factories.items():
            for side in (0, 1):
                names = (name, 'rush_t1') if side == 0 else ('rush_t1', name)
                bots = [CallableBot(factory()), make('rush_t1')] if side == 0 else [make('rush_t1'), CallableBot(factory())]
                result = evaluate(names, bots=bots)
                assert not any(result['bot_errors']), name
                assert not any(result['rejected_actions']), name
                stream.write(json.dumps(result, sort_keys=True) + '\n')
                stream.flush()
                print(name, side, result['hp'], result['rounds'], result['runtime_seconds'], flush=True)


if __name__ == '__main__':
    main()
