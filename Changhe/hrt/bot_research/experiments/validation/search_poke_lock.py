"""Ablate known-policy forecasting and challenge two frozen development targets."""
from __future__ import annotations
import argparse
import itertools
import json
from datetime import datetime, timezone
from pathlib import Path
import time
from bot_research.bots.counters.poke_lock import PokeLock
from bot_research.bots.counters.snapshots.lead_planner_001 import Planner
from bot_research.bots.economy.frozen.v2.econ import make as economy
from bot_research.experiments.validation.evaluate import evaluate, source_hashes


class Bot:
    def __init__(self, function):
        self.decide = function


def conditions():
    for i, (n, reserve, phi, opponent) in enumerate(itertools.product(
            (0, 1, 2, 4, 6), (0, 180), (0.0, .25, 1.0), ('planner_v1', 'economy_v2_late6'))):
        yield i, {'opening_units': n, 'reserve': reserve, 'phi': phi, 'saturate_round': 20}, opponent


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--shard', type=int, default=0)
    parser.add_argument('--shards', type=int, default=1)
    args = parser.parse_args()
    start = time.perf_counter()
    with Path(args.output).with_suffix('.meta.json').open('x') as stream:
        json.dump({'time_utc': datetime.now(timezone.utc).isoformat(), 'sources': source_hashes(),
                   'all_conditions': list(conditions()), 'shard': args.shard, 'shards': args.shards,
                   'purpose': 'development ablation and counter search; counter player 0'}, stream, indent=2)
        stream.write('\n')
    with Path(args.output).open('x') as stream:
        for i, parameters, target in conditions():
            if i % args.shards != args.shard:
                continue
            bot = Bot(Planner()) if target == 'planner_v1' else Bot(economy(late_round=6, phi=0.0))
            row = evaluate(('poke_lock', target), bots=[PokeLock(**parameters), bot],
                condition={'index': i, 'parameters': parameters, 'target': target, 'counter_side': 0,
                           'initial_state': 'standard', 'engine_seed': None})
            winner = row['result']['winner']
            row['counter_outcome'] = 'D' if winner is None else ('W' if winner == 0 else 'L')
            stream.write(json.dumps(row, sort_keys=True)+'\n')
            stream.flush()
            print(json.dumps({'index': i, 'parameters': parameters, 'target': target,
                              'outcome': row['counter_outcome'], 'hp': row['hp'],
                              'rounds': row['rounds'], 'elapsed_seconds': time.perf_counter()-start}), flush=True)
            if time.perf_counter()-start > 480:
                print('Bounded batch incomplete; check coverage.', flush=True)
                return


if __name__ == '__main__':
    main()
