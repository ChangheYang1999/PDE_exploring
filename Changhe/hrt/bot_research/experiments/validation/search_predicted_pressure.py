"""Develop known-policy counters to archived Planner v3 parameter variants."""
from __future__ import annotations
import argparse
import itertools
import json
from pathlib import Path
import time
from bot_research.bots.counters.predicted_pressure import PredictedPressure
from bot_research.bots.counters.snapshots.lead_planner_003 import Planner
from bot_research.experiments.validation.evaluate import evaluate
from bot_research.experiments.validation.isolated_match import CallableBot


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--shard', type=int, default=0)
    parser.add_argument('--shards', type=int, default=1)
    parser.add_argument('--skip-files', nargs='*', default=[])
    args = parser.parse_args()
    skip = {json.loads(line)['condition']['index'] for name in args.skip_files
            for line in Path(name).read_text().splitlines()}
    started = time.perf_counter()
    directory = Path(args.output).with_suffix('')
    directory.mkdir(exist_ok=False)
    with Path(args.output).open('x') as stream:
        conditions = itertools.product((1.0, 0.5, 0.2), (2.0, 4.0, 12.0), (0.5, 1.0), (0, 1))
        for index, (lam, weight, defense_share, opening) in enumerate(conditions):
            if index % args.shards != args.shard or index in skip:
                continue
            if time.perf_counter()-started > 480:
                print('Bounded batch ended; resume with --skip-files.', flush=True)
                return
            model_params = {'lam': lam}
            parameters = {'model_params': model_params, 'attack_weight': weight,
                          'defense_share': defense_share, 'opening_units': opening}
            candidate = PredictedPressure(**parameters)
            replay = str(directory / f'case-{index:03d}.jsonl')
            row = evaluate(('predicted_pressure', 'planner_v3'),
                bots=[candidate, CallableBot(Planner(**model_params))], replay_path=replay,
                condition={'index': index, 'counter_side': 0, 'parameters': parameters,
                    'model_params': model_params, 'initial_state': 'standard', 'engine_seed': None,
                    'purpose': 'known-policy counter development, not reserved validation'})
            winner = row['result']['winner']
            row['counter_outcome'] = 'D' if winner is None else ('W' if winner == 0 else 'L')
            row['prediction_trace'] = candidate.trace
            records = [json.loads(s) for s in Path(replay).read_text().splitlines()]
            actual = {r['round']: [e['action'] for e in r['event'] if e['kind']=='action']
                      for r in records if r['player']==1 and r['round']>0}
            row['forecast_mismatch_rounds'] = [t['round'] for t in candidate.trace
                if t['predicted_actions'] != actual[t['round']]]
            stream.write(json.dumps(row, sort_keys=True)+'\n')
            stream.flush()
            print(json.dumps({'index': index, 'parameters': parameters, 'outcome': row['counter_outcome'],
                              'hp': row['hp'], 'rounds': row['rounds'],
                              'mismatches': row['forecast_mismatch_rounds'],
                              'elapsed_seconds': time.perf_counter()-started}), flush=True)


if __name__ == '__main__':
    main()
