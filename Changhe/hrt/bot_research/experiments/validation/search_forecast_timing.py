"""Screen a finite grid of timed attacks against frozen Planner parameter variants."""
from __future__ import annotations
import argparse
import itertools
import json
from pathlib import Path
import time
from bot_research.bots.counters.forecast_timing import ForecastTiming
from bot_research.bots.counters.snapshots.lead_planner_003 import Planner
from bot_research.experiments.validation.evaluate import evaluate
from bot_research.experiments.validation.isolated_match import CallableBot


def conditions():
    for i, values in enumerate(itertools.product((1.0, 0.5, 0.2), range(2, 11),
                                                 ('tier2', 'tier3', 'tier4', 'tier5'),
                                                 (0.25, 0.5, 1.0))):
        lam, rnd, tier, share = values
        yield i, {'model_lam': lam, 'attack_round': rnd, 'tier': tier, 'attack_share': share}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--output', required=True)
    p.add_argument('--shard', type=int, default=0)
    p.add_argument('--shards', type=int, default=1)
    p.add_argument('--skip-files', nargs='*', default=[])
    args = p.parse_args()
    skip = {json.loads(line)['condition']['index'] for name in args.skip_files
            for line in Path(name).read_text().splitlines()}
    started = time.perf_counter()
    directory = Path(args.output).with_suffix('')
    directory.mkdir(exist_ok=False)
    with Path(args.output).open('x') as stream:
        for index, parameters in conditions():
            if index % args.shards != args.shard or index in skip:
                continue
            if time.perf_counter() - started > 480:
                print('Bounded batch ended; resume with --skip-files.', flush=True)
                return
            candidate = ForecastTiming(**parameters)
            replay = str(directory / f'case-{index:03d}.jsonl')
            row = evaluate(('forecast_timing', 'planner_v3'),
                bots=[candidate, CallableBot(Planner(lam=parameters['model_lam']))],
                replay_path=replay, condition={'index': index, 'parameters': parameters,
                    'counter_side': 0, 'initial_state': 'standard', 'engine_seed': None,
                    'purpose': 'timed-purchase development screen; no reserved holdout'})
            winner = row['result']['winner']
            row['counter_outcome'] = 'D' if winner is None else ('W' if winner == 0 else 'L')
            row['forecast_trace'] = candidate.trace
            records = [json.loads(line) for line in Path(replay).read_text().splitlines()]
            actual = {r['round']: [e['action'] for e in r['event'] if e['kind'] == 'action']
                      for r in records if r['player'] == 1 and r['round'] > 0}
            row['forecast_mismatch_rounds'] = [t['round'] for t in candidate.trace
                if t['predicted_actions'] != actual[t['round']]]
            stream.write(json.dumps(row, sort_keys=True) + '\n')
            stream.flush()
            print(json.dumps({'index': index, 'parameters': parameters,
                'outcome': row['counter_outcome'], 'hp': row['hp'], 'rounds': row['rounds'],
                'mismatches': row['forecast_mismatch_rounds'],
                'elapsed_seconds': time.perf_counter() - started}), flush=True)


if __name__ == '__main__':
    main()
