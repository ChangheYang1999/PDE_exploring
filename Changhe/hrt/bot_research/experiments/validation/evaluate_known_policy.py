"""Authoritative paired checks of a frozen public-policy forecast counter."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from bot_research.bots.counters.known_policy import KnownTiming, KnownSchedule, KnownRollout, policy_factory
from bot_research.experiments.validation.evaluate import evaluate
from bot_research.experiments.validation.isolated_match import CallableBot


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--mode', choices=('timing', 'schedule', 'rollout'), default='timing')
    parser.add_argument('--model', choices=('planner003', 'econ_v4', 'fortress_v4', 'fortress_v6'), required=True)
    parser.add_argument('--model-parameters', type=json.loads, default={})
    parser.add_argument('--parameters', type=json.loads, default={})
    parser.add_argument('--sides', type=int, nargs='+', choices=(0, 1), default=[0, 1])
    args = parser.parse_args()
    counter_class = {'timing': KnownTiming, 'schedule': KnownSchedule, 'rollout': KnownRollout}[args.mode]
    directory = Path(args.output).with_suffix('')
    directory.mkdir(exist_ok=False)
    with Path(args.output).open('x') as stream:
        for side in args.sides:
            counter = counter_class(model=args.model, model_parameters=args.model_parameters, **args.parameters)
            target = CallableBot(policy_factory(args.model, args.model_parameters))
            bots, names = [counter, target], ('known_'+args.mode, args.model)
            if side:
                bots.reverse()
                names = tuple(reversed(names))
            replay = str(directory / f'side{side}.jsonl')
            row = evaluate(names, bots=bots, replay_path=replay, condition={
                'counter_side': side, 'counter_mode': args.mode, 'model': args.model,
                'model_parameters': args.model_parameters, 'parameters': args.parameters,
                'initial_state': 'standard', 'engine_seed': None,
                'purpose': 'known frozen-policy development counter; no reserved holdout'})
            winner = row['result']['winner']
            row['counter_outcome'] = 'D' if winner is None else ('W' if winner == side else 'L')
            row['forecast_trace'] = counter.trace
            records = [json.loads(s) for s in Path(replay).read_text().splitlines()]
            actual = {r['round']: [e['action'] for e in r['event'] if e['kind'] == 'action']
                      for r in records if r['player'] == 1-side and r['round'] > 0}
            row['forecast_mismatch_rounds'] = [t['round'] for t in counter.trace
                if t['predicted_actions'] != actual[t['round']]]
            stream.write(json.dumps(row, sort_keys=True) + '\n')
            stream.flush()
            print(json.dumps({k: row[k] for k in ('condition', 'counter_outcome', 'hp',
                'rounds', 'runtime_seconds', 'forecast_mismatch_rounds', 'rejected_actions',
                'bot_errors', 'source_changed_during_match')}), flush=True)


if __name__ == '__main__':
    main()
