"""Fresh-process development match with direct target-prediction diagnostics."""
import argparse
import json
from pathlib import Path
from bot_research.experiments.validation.isolated_match import resolve
from bot_research.experiments.validation.evaluate import evaluate
from bot_research.experiments.validation.artifact_io import atomic_json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--job', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    job = json.loads(Path(args.job).read_text())
    if job.get('prefixes'):
        raise ValueError('This diagnostic runner supports standard development games.')
    bots = [resolve(d) for d in job['bots']]
    side = job['condition']['candidate_side']
    owner = getattr(bots[side].decide, '__self__', None)
    result = evaluate(tuple(job['names']), bots=bots, replay_path=job['replay_path'], condition=job['condition'])
    winner = result['result']['winner']
    result['candidate_outcome'] = 'D' if winner is None else ('W' if winner == side else 'L')
    trace = getattr(owner, 'trace', None)
    if not isinstance(trace, list):
        raise ValueError('Candidate did not expose a prediction trace.')
    records = [json.loads(line) for line in Path(job['replay_path']).read_text().splitlines()]
    actions = {r['round']: [e['action'] for e in r['event'] if e['kind'] == 'action']
               for r in records if r['round'] > 0 and r['player'] == 1 - side}
    result['forecast_trace'] = trace
    result['forecast_mismatch_rounds'] = [t['round'] for t in trace if t['predicted_actions'] != actions[t['round']]]
    result['forecast_trace_missing_rounds'] = sorted(set(range(1, result['rounds'] + 1)) - {t['round'] for t in trace})
    atomic_json(args.output, result, exclusive=True)


if __name__ == '__main__':
    main()
