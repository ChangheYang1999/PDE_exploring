"""Both player assignments for selected development-grid timing finalists."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import time
from bot_research.bots.counters.forecast_timing import ForecastTiming
from bot_research.bots.counters.snapshots.lead_planner_003 import Planner
from bot_research.experiments.validation.evaluate import evaluate
from bot_research.experiments.validation.isolated_match import CallableBot


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--manifest', required=True)
    p.add_argument('--output', required=True)
    p.add_argument('--shard', type=int, default=0)
    p.add_argument('--shards', type=int, default=1)
    args = p.parse_args()
    finalists = json.loads(Path(args.manifest).read_text())['paired_finalists']
    directory = Path(args.output).with_suffix('')
    directory.mkdir(exist_ok=False)
    started = time.perf_counter()
    with Path(args.output).open('x') as stream:
        for index, finalist in enumerate(finalists):
            if index % args.shards != args.shard:
                continue
            for side in (0, 1):
                if time.perf_counter() - started > 480:
                    raise RuntimeError('Batch limit reached; completed rows are preserved.')
                parameters = finalist['parameters']
                counter = ForecastTiming(**parameters)
                bots = [counter, CallableBot(Planner(lam=parameters['model_lam']))]
                names = ('forecast_timing_finalist', 'planner_v3')
                if side:
                    bots.reverse()
                    names = tuple(reversed(names))
                replay = str(directory / f"case-{finalist['screen_index']:03d}-side{side}.jsonl")
                row = evaluate(names, bots=bots, replay_path=replay, condition={
                    'screen_index': finalist['screen_index'], 'parameters': parameters,
                    'counter_side': side, 'initial_state': 'standard', 'engine_seed': None,
                    'purpose': 'paired development confirmation; player0 repeats its screen'})
                winner = row['result']['winner']
                row['counter_outcome'] = 'D' if winner is None else ('W' if winner == side else 'L')
                row['forecast_trace'] = counter.trace
                records = [json.loads(line) for line in Path(replay).read_text().splitlines()]
                actual = {r['round']: [e['action'] for e in r['event'] if e['kind'] == 'action']
                          for r in records if r['player'] == 1-side and r['round'] > 0}
                row['forecast_mismatch_rounds'] = [t['round'] for t in counter.trace
                    if t['predicted_actions'] != actual[t['round']]]
                stream.write(json.dumps(row, sort_keys=True) + '\n')
                stream.flush()
                print(json.dumps({'screen_index': finalist['screen_index'], 'side': side,
                    'parameters': parameters, 'outcome': row['counter_outcome'], 'hp': row['hp'],
                    'mismatches': row['forecast_mismatch_rounds'], 'elapsed_seconds': time.perf_counter()-started}), flush=True)


if __name__ == '__main__':
    main()
