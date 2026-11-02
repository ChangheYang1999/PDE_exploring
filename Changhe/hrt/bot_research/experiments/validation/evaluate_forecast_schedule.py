"""Paired checks of the extracted cheap schedule and trajectory equivalence."""
from __future__ import annotations
import argparse
import itertools
import json
from pathlib import Path
import time
from bot_research.bots.counters.forecast_schedule import ForecastSchedule
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
        for lam, side in itertools.product((1.0, 0.5, 0.2), (0, 1)):
            counter = ForecastSchedule(model_lam=lam)
            bots = [counter, CallableBot(Planner(lam=lam))]
            names = ('forecast_schedule', 'planner_v3')
            if side:
                bots.reverse()
                names = tuple(reversed(names))
            replay = str(directory / f'lam{lam}-side{side}.jsonl')
            row = evaluate(names, bots=bots, replay_path=replay,
                condition={'model_lam': lam, 'schedule': counter.schedule, 'counter_side': side,
                           'initial_state': 'standard', 'engine_seed': None,
                           'purpose': 'extracted known-policy schedule development'})
            winner = row['result']['winner']
            row['counter_outcome'] = 'D' if winner is None else ('W' if winner == side else 'L')
            row['forecast_trace'] = counter.trace
            records = [json.loads(line) for line in Path(replay).read_text().splitlines()]
            actual = {r['round']: [e['action'] for e in r['event'] if e['kind'] == 'action']
                      for r in records if r['player'] == 1-side and r['round'] > 0}
            row['forecast_mismatch_rounds'] = [t['round'] for t in counter.trace
                if t['predicted_actions'] != actual[t['round']]]
            if lam == 1.0:
                reference = json.loads(Path(f'bot_research/runs/validation/forecast-rollout-001-lam1-side{side}.json').read_text())
                row['rollout_history_equal'] = reference['history'] == row['history']
                row['rollout_accepted_counts_equal'] = reference['accepted_actions'] == row['accepted_actions']
                def normalize(items):
                    items = json.loads(json.dumps(items))
                    for record in items:
                        record.pop('match', None)
                        record['snapshot']['name'] = str(record['player'])
                    return items
                old_records = [json.loads(line) for line in Path(reference['replay_path']).read_text().splitlines()]
                row['rollout_complete_trajectory_equal_up_to_names'] = normalize(old_records) == normalize(records)
                assert row['rollout_complete_trajectory_equal_up_to_names']
                assert row['rollout_history_equal'] and row['rollout_accepted_counts_equal']
            stream.write(json.dumps(row, sort_keys=True) + '\n')
            stream.flush()
            print(json.dumps({'lam': lam, 'side': side, 'outcome': row['counter_outcome'],
                              'hp': row['hp'], 'rounds': row['rounds'], 'runtime_seconds': row['runtime_seconds'],
                              'forecast_mismatches': row['forecast_mismatch_rounds'],
                              'rollout_history_equal': row.get('rollout_history_equal')}), flush=True)
            if time.perf_counter() - started > 480:
                print('Bounded batch incomplete.', flush=True)
                return


if __name__ == '__main__':
    main()
