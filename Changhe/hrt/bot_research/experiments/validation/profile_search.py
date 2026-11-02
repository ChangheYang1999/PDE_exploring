"""Finite development search over economic timing and defensive baselines.

Each shard is one process. Held-out profile definitions are never imported.
"""
from __future__ import annotations
import argparse
from dataclasses import asdict
import itertools
import json
import time
from datetime import datetime, timezone
from pathlib import Path

from bot_research.bots.counters.archetypes import Archetype, Profile, make
from bot_research.experiments.validation.evaluate import evaluate, source_hashes


def profiles():
    rosters = [('tier1',), ('tier2',), ('tier3',), ('tier4',), ('tier5',),
               ('tier3', 'tier1', 'tier1'), ('tier4', 'tier2', 'tier1'),
               ('tier1', 'tier1', 'tier3')]
    defenses = [('', 0), ('splash', 1), ('splash', 2), ('splash', 3),
                ('gun1', 2), ('gun2', 2), ('gun3', 1)]
    for growth, roster, (defense, count), invest in itertools.product(range(0, 9), rosters, defenses, (0.0, 0.2, 0.5)):
        yield Profile(growth_rounds=growth, roster=roster, defense=defense, defense_count=count, keep_investing=invest)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--shard', type=int, required=True)
    parser.add_argument('--shards', type=int, default=3)
    parser.add_argument('--output', required=True)
    parser.add_argument('--max-seconds', type=float, default=480)
    parser.add_argument('--skip-files', nargs='*', default=[])
    args = parser.parse_args()
    if not 0 < args.max_seconds <= 540:
        parser.error('Use a bounded batch of at most 540 seconds.')
    skip = set()
    for filename in args.skip_files:
        with Path(filename).open() as prior:
            skip.update(json.loads(line)['index'] for line in prior)
    started = time.perf_counter()
    opponents = ['splash_t2', 'rush_t1', 'eco5_t3', 'splash3_t4']
    metadata = {'started_utc': datetime.now(timezone.utc).isoformat(), 'script_sources': source_hashes(),
                'opponents': opponents, 'shard': args.shard, 'shards': args.shards,
                'objective': 'Maximize worst-opponent WDL, then mean score. This is tuning, not held-out validation.',
                'assignment': 'candidate player 0 in screening; both assignments required for finalists',
                'number_profiles_total': sum(1 for _ in profiles()),
                'skip_files': args.skip_files, 'skip_indices': sorted(skip)}
    meta_path = Path(args.output).with_suffix('.meta.json')
    with meta_path.open('x') as stream:
        json.dump(metadata, stream, indent=2)
        stream.write('\n')
    with Path(args.output).open('x') as stream:
        for index, profile in enumerate(profiles()):
            if index in skip or index % args.shards != args.shard:
                continue
            if time.perf_counter() - started > args.max_seconds:
                print('Reached runtime limit.', flush=True)
                break
            name = f'profile_{index:04d}'
            rows = []
            for opponent in opponents:
                result = evaluate((name, opponent), bots=[Archetype(profile), make(opponent)])
                for key in ('history', 'rules', 'source_sha256', 'condition'):
                    result.pop(key)
                rows.append(result)
            score = [0.5 if row['result']['winner'] is None else float(row['result']['winner'] == 0) for row in rows]
            record = {'index': index, 'profile': asdict(profile), 'score': score, 'worst': min(score),
                      'mean': sum(score) / len(score), 'matches': rows}
            stream.write(json.dumps(record, sort_keys=True) + '\n')
            stream.flush()
            if index % 30 < args.shards or min(score) >= 0.5:
                print(json.dumps({'index': index, 'profile': asdict(profile), 'score': score,
                                  'elapsed_seconds': time.perf_counter() - started}), flush=True)
    print(json.dumps({'completed_utc': datetime.now(timezone.utc).isoformat(),
                      'elapsed_seconds': time.perf_counter() - started}), flush=True)


if __name__ == '__main__':
    main()
