"""Ablate opponent forecasting for the stronger single-tier2 opening."""
from __future__ import annotations
import argparse
import itertools
import json
from pathlib import Path
import time
from bot_research.bots.counters.opening_lock import OpeningLock
from bot_research.bots.counters.snapshots.lead_planner_003 import Planner
from bot_research.bots.economy.frozen.v2.econ import make as economy
from bot_research.experiments.validation.evaluate import evaluate
from bot_research.experiments.validation.isolated_match import CallableBot


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--output', required=True)
    p.add_argument('--shard', type=int, default=0)
    p.add_argument('--shards', type=int, default=1)
    p.add_argument('--skip-files', nargs='*', default=[])
    args = p.parse_args()
    directory = Path(args.output).with_suffix('')
    directory.mkdir(exist_ok=False)
    skipped = {json.loads(s)['condition']['index'] for name in args.skip_files for s in Path(name).read_text().splitlines()}
    started = time.perf_counter()
    targets = [('planner_lam1', lambda: Planner(lam=1.0)),
               ('planner_lam.5', lambda: Planner(lam=0.5)),
               ('planner_lam.2', lambda: Planner(lam=0.2)),
               ('econ_v2_late6', lambda: economy(late_round=6, phi=0.0))]
    with Path(args.output).open('x') as stream:
        settings = itertools.product((0.0, 0.25, 1.0), (1, 6), targets, (0, 1))
        for index, (phi, late, (name, factory), side) in enumerate(settings):
            if index % args.shards != args.shard or index in skipped:
                continue
            if time.perf_counter() - started > 480:
                print('Bounded batch ended; resume with --skip-files.', flush=True)
                return
            parameters = {'opening_tier': 'tier2', 'opening_units': 1,
                          'phi': phi, 'late_round': late, 'reserve': 0, 'saturate_round': 20}
            bots = [OpeningLock(**parameters), CallableBot(factory())]
            names = ('opening_lock', name)
            if side:
                bots.reverse()
                names = tuple(reversed(names))
            replay = str(directory / f'case-{index:03d}.jsonl')
            row = evaluate(names, bots=bots, replay_path=replay,
                condition={'index': index, 'parameters': parameters, 'target': name,
                           'counter_side': side, 'initial_state': 'standard', 'engine_seed': None,
                           'purpose': 'forecast-free opening development ablation'})
            winner = row['result']['winner']
            row['counter_outcome'] = 'D' if winner is None else ('W' if winner == side else 'L')
            stream.write(json.dumps(row, sort_keys=True) + '\n')
            stream.flush()
            print(json.dumps({'index': index, 'parameters': parameters, 'target': name,
                              'side': side, 'outcome': row['counter_outcome'], 'hp': row['hp'],
                              'rounds': row['rounds'], 'elapsed_seconds': time.perf_counter()-started}), flush=True)


if __name__ == '__main__':
    main()
