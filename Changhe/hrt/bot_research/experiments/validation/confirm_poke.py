"""Paired confirmation of forecast-free opening counters on frozen targets."""
from __future__ import annotations
import argparse
import itertools
import json
from pathlib import Path
import time
from bot_research.bots.counters.poke_lock import PokeLock
from bot_research.bots.counters.snapshots.lead_planner_001 import Planner
from bot_research.bots.economy.frozen.v2.econ import make as economy
from bot_research.experiments.validation.evaluate import evaluate
from bot_research.experiments.validation.isolated_match import CallableBot


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    directory = Path(args.output).with_suffix('')
    directory.mkdir(exist_ok=False)
    started = time.perf_counter()
    with Path(args.output).open('x') as stream:
        for n, reserve, target, side in itertools.product((1, 2), (0, 180), ('planner_v1', 'economy_v2_late6'), (0, 1)):
            parameters = {'opening_units': n, 'reserve': reserve, 'phi': 1.0, 'saturate_round': 20}
            counter = PokeLock(**parameters)
            opponent = CallableBot(Planner()) if target == 'planner_v1' else CallableBot(economy(late_round=6, phi=0.0))
            bots = [counter, opponent]
            names = ('poke_lock', target)
            if side:
                bots.reverse()
                names = tuple(reversed(names))
            replay = directory / f'n{n}-reserve{reserve}-{target}-side{side}.jsonl'
            row = evaluate(names, bots=bots, replay_path=str(replay), condition={'counter_side': side,
                'parameters': parameters, 'target': target, 'initial_state': 'standard', 'engine_seed': None,
                'purpose': 'paired development counter confirmation'})
            winner = row['result']['winner']
            row['counter_outcome'] = 'D' if winner is None else ('W' if winner == side else 'L')
            stream.write(json.dumps(row, sort_keys=True)+'\n')
            stream.flush()
            print(json.dumps({'parameters': parameters, 'target': target, 'side': side,
                'outcome': row['counter_outcome'], 'hp': row['hp'], 'rounds': row['rounds'],
                'elapsed_seconds': time.perf_counter()-started}), flush=True)
            if time.perf_counter()-started > 480:
                print('Bounded batch incomplete; inspect coverage.', flush=True)
                return


if __name__ == '__main__':
    main()
