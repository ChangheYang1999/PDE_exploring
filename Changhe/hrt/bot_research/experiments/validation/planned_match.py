"""Fresh standard game, retaining optional contingent-plan traces."""
from __future__ import annotations
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
        raise ValueError('This development runner requires the standard initial state.')
    bots = [resolve(description) for description in job['bots']]
    side = job['condition']['candidate_side']
    owner = getattr(bots[side].decide, '__self__', None)
    result = evaluate(tuple(job['names']), bots=bots, replay_path=job['replay_path'], condition=job['condition'])
    winner = result['result']['winner']
    result['candidate_outcome'] = 'D' if winner is None else ('W' if winner == side else 'L')
    result['compiled_trace'] = getattr(owner, 'trace', None)
    atomic_json(args.output, result, exclusive=True)


if __name__ == '__main__':
    main()
