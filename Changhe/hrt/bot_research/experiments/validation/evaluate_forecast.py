"""Paired test of forecast-and-lock counters against the first lead policy."""
from __future__ import annotations
import argparse
import itertools
import json
from pathlib import Path
import time
from bot_research.bots.counters.forecast_lock import ForecastLock
from bot_research.bots.counters.snapshots.lead_planner_001 import Planner
from bot_research.experiments.validation.evaluate import evaluate
from bot_research.experiments.validation.isolated_match import CallableBot


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--replay-dir', required=True)
    args = parser.parse_args()
    Path(args.replay_dir).mkdir(parents=True, exist_ok=False)
    started = time.perf_counter()
    with Path(args.output).open('x') as stream:
        for n, reserve, sr, side in itertools.product((1, 2, 4, 6), (0, 180), (20, 45), (0, 1)):
            counter = ForecastLock(n, reserve, sr)
            bots = [counter, CallableBot(Planner())]
            names = ('forecast_lock', 'lead_planner_v1')
            if side:
                bots.reverse()
                names = tuple(reversed(names))
            condition = {'opening_units': n, 'reserve': reserve, 'saturate_round': sr,
                         'counter_side': side, 'initial_state': 'standard', 'engine_seed': None,
                         'purpose': 'targeted counter development with a private public-observation model'}
            replay = str(Path(args.replay_dir) / f'opening{n}-reserve{reserve}-sr{sr}-side{side}.jsonl')
            row = evaluate(names, bots=bots, condition=condition, replay_path=replay)
            winner = row['result']['winner']
            row['counter_outcome'] = 'D' if winner is None else ('W' if winner==side else 'L')
            row['forecast_trace'] = counter.trace
            # Check predictions against the authoritative opponent action records.
            records = [json.loads(line) for line in Path(replay).read_text().splitlines()]
            actual = {r['round']: [e['action'] for e in r['event'] if e['kind']=='action']
                      for r in records if r['player']==1-side and r['round']>0}
            row['forecast_mismatch_rounds'] = [t['round'] for t in counter.trace
                if t['predicted_actions'] != actual[t['round']]]
            stream.write(json.dumps(row, sort_keys=True)+'\n')
            stream.flush()
            print(json.dumps({'condition': condition, 'outcome': row['counter_outcome'],
                'hp': row['hp'], 'rounds': row['rounds'], 'prediction_mismatches': row['forecast_mismatch_rounds'],
                'elapsed_seconds': time.perf_counter()-started}), flush=True)
            if time.perf_counter()-started >= 480:
                print('Bounded batch incomplete; check coverage.', flush=True)
                return


if __name__ == '__main__':
    main()
