"""Summarize recorded deterministic conditions without inventing sample counts."""
from __future__ import annotations
import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path


def summarize(paths):
    rows = [json.loads(line) for path in paths for line in Path(path).read_text().splitlines() if line]
    scores = defaultdict(Counter)
    for row in rows:
        winner = row['result']['winner']
        for p, name in enumerate(row['bot_specs']):
            scores[name]['D' if winner is None else ('W' if p == winner else 'L')] += 1
            scores[name]['games'] += 1
            scores[name]['errors'] += len(row['bot_errors'][p])
            scores[name]['rejections'] += sum(row['rejected_actions'][p].values())
    return {'record_count': len(rows), 'trajectory_count': len({r['trajectory_sha256'] for r in rows}),
            'results_by_reason': dict(Counter(r['result']['reason'] for r in rows)),
            'scores': dict(scores), 'runtime_seconds': sum(r['runtime_seconds'] for r in rows),
            'max_decision_seconds': max((p['max'] for r in rows for p in r['decision_seconds']), default=0)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('paths', nargs='+')
    parser.add_argument('--output')
    args = parser.parse_args()
    result = summarize(args.paths)
    text = json.dumps(result, indent=2, sort_keys=True) + '\n'
    if args.output:
        with Path(args.output).open('x') as stream:
            stream.write(text)
    print(text)


if __name__ == '__main__':
    main()
