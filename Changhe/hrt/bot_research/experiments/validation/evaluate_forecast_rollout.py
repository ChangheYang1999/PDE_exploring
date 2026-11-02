"""One authoritative match for the complete-continuation counter."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from bot_research.bots.counters.forecast_rollout import ForecastRollout
from bot_research.bots.counters.snapshots.lead_planner_003 import Planner
from bot_research.experiments.validation.evaluate import evaluate
from bot_research.experiments.validation.isolated_match import CallableBot


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--output', required=True)
    p.add_argument('--lam', type=float, default=1.0)
    p.add_argument('--side', type=int, choices=(0, 1), default=0)
    p.add_argument('--max-candidates', type=int, default=12)
    args = p.parse_args()
    parameters = {'model_lam': args.lam, 'max_candidates': args.max_candidates}
    counter = ForecastRollout(**parameters)
    bots = [counter, CallableBot(Planner(lam=args.lam))]
    names = ('forecast_rollout', 'planner_v3')
    if args.side:
        bots.reverse()
        names = tuple(reversed(names))
    directory = Path(args.output).with_suffix('')
    directory.mkdir(exist_ok=False)
    replay = str(directory / 'replay.jsonl')
    row = evaluate(names, bots=bots, replay_path=replay,
        condition={'parameters': parameters, 'counter_side': args.side,
                   'initial_state': 'standard', 'engine_seed': None,
                   'purpose': 'known-policy continuation-search development'})
    winner = row['result']['winner']
    row['counter_outcome'] = 'D' if winner is None else ('W' if winner == args.side else 'L')
    row['forecast_trace'] = counter.trace
    records = [json.loads(line) for line in Path(replay).read_text().splitlines()]
    actual = {r['round']: [e['action'] for e in r['event'] if e['kind'] == 'action']
              for r in records if r['player'] == 1-args.side and r['round'] > 0}
    row['forecast_mismatch_rounds'] = [t['round'] for t in counter.trace
        if t['predicted_actions'] != actual[t['round']]]
    with Path(args.output).open('x') as stream:
        json.dump(row, stream, sort_keys=True)
        stream.write('\n')
    print(json.dumps({k: row[k] for k in ('counter_outcome', 'hp', 'rounds',
        'runtime_seconds', 'decision_seconds', 'forecast_mismatch_rounds',
        'rejected_actions', 'bot_errors', 'source_changed_during_match')}), flush=True)


if __name__ == '__main__':
    main()
