"""Test heavier first-round purchases followed by forecast defense."""
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


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--output', required=True)
    args = p.parse_args()
    directory = Path(args.output).with_suffix('')
    directory.mkdir(exist_ok=False)
    started = time.perf_counter()
    with Path(args.output).open('x') as stream:
        for lam, tier, cap, side in itertools.product((1.0, 0.5, 0.2), ('tier1', 'tier2', 'tier3'), (1, 2), (0, 1)):
            parameters = {'model_lam': lam, 'attack_round': 1, 'tier': tier,
                          'attack_share': 1.0, 'count_cap': cap}
            counter = ForecastTiming(**parameters)
            bots = [counter, CallableBot(Planner(lam=lam))]
            names = ('forecast_first_wave', 'planner_v3')
            if side:
                bots.reverse()
                names = tuple(reversed(names))
            replay = str(directory / f'lam{lam}-{tier}-cap{cap}-side{side}.jsonl')
            row = evaluate(names, bots=bots, replay_path=replay, condition={
                'parameters': parameters, 'counter_side': side, 'initial_state': 'standard',
                'engine_seed': None, 'purpose': 'paired targeted first-wave development'})
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
            print(json.dumps({'parameters': parameters, 'side': side,
                'outcome': row['counter_outcome'], 'hp': row['hp'], 'rounds': row['rounds'],
                'mismatches': row['forecast_mismatch_rounds'],
                'elapsed_seconds': time.perf_counter() - started}), flush=True)
            if time.perf_counter() - started > 480:
                print('Bounded batch incomplete; inspect coverage.', flush=True)
                return


if __name__ == '__main__':
    main()
