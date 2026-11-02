"""Run one exact improvement pass and retain its complete trace."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from bot_research.bots.counters.scheduled_rollout import ScheduledRollout
from bot_research.bots.counters.known_policy import policy_factory
from bot_research.experiments.validation.evaluate import evaluate
from bot_research.experiments.validation.isolated_match import CallableBot


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--model', default='planner003')
    parser.add_argument('--model-parameters', type=json.loads, default={})
    parser.add_argument('--baseline', type=json.loads, default=[])
    parser.add_argument('--candidate-mode', choices=('filtered', 'unit', 'unit_filtered'), default='filtered')
    parser.add_argument('--side', type=int, choices=(0, 1), default=0)
    parser.add_argument('--max-round', type=int, default=12)
    args = parser.parse_args()
    parameters = {'model': args.model, 'model_parameters': args.model_parameters,
                  'baseline_schedule': args.baseline, 'candidate_mode': args.candidate_mode,
                  'max_search_round': args.max_round}
    counter = ScheduledRollout(**parameters)
    target = CallableBot(policy_factory(args.model, args.model_parameters))
    bots, names = [counter, target], ('scheduled_rollout', args.model)
    if args.side:
        bots.reverse()
        names = tuple(reversed(names))
    directory = Path(args.output).with_suffix('')
    directory.mkdir(exist_ok=False)
    replay = str(directory / 'replay.jsonl')
    row = evaluate(names, bots=bots, replay_path=replay, condition={
        'counter_side': args.side, 'parameters': parameters, 'engine_seed': None,
        'initial_state': 'standard', 'purpose': 'complete rollout improvement development'})
    winner = row['result']['winner']
    row['counter_outcome'] = 'D' if winner is None else ('W' if winner == args.side else 'L')
    row['forecast_trace'] = counter.trace
    records = [json.loads(s) for s in Path(replay).read_text().splitlines()]
    actual = {r['round']: [e['action'] for e in r['event'] if e['kind'] == 'action']
              for r in records if r['player'] == 1-args.side and r['round'] > 0}
    row['forecast_mismatch_rounds'] = [t['round'] for t in counter.trace
                                    if t['predicted_actions'] != actual[t['round']]]
    selected_values = [max(tuple(c['score']) for c in t['candidates'])
                       for t in counter.trace if t['evaluated_continuations']]
    row['selected_values_nondecreasing'] = all(a <= b for a, b in zip(selected_values, selected_values[1:]))
    with Path(args.output).open('x') as stream:
        json.dump(row, stream, sort_keys=True)
        stream.write('\n')
    print(json.dumps({k: row[k] for k in ('hp', 'counter_outcome', 'rounds', 'runtime_seconds',
        'bot_errors', 'rejected_actions', 'source_changed_during_match',
        'forecast_mismatch_rounds', 'selected_values_nondecreasing')}), flush=True)


if __name__ == '__main__':
    main()
