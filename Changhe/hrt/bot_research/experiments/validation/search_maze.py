"""Screen cheap fixed mazes as an economic and offensive counter family."""
from __future__ import annotations
import argparse
import itertools
import json
from datetime import datetime, timezone
from pathlib import Path
import time

from bot_research.bots.counters.archetypes import make
from bot_research.bots.counters.maze_pressure import MazePressure
from bot_research.experiments.validation.evaluate import evaluate, source_hashes


def conditions():
    for index, (lines, growth, tier, defense) in enumerate(itertools.product(
            (2, 4), range(0, 9), ('tier1', 'tier2', 'tier3', 'tier4', 'tier5'),
            ('', 'splash', 'gun2', 'gun3'))):
        yield index, {'n_lines': lines, 'growth_rounds': growth, 'tier': tier,
                      'defense': defense, 'defense_count': int(bool(defense))}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--shard', type=int, default=0)
    parser.add_argument('--shards', type=int, default=1)
    parser.add_argument('--skip-files', nargs='*', default=[])
    parser.add_argument('--max-seconds', type=float, default=480)
    args = parser.parse_args()
    assert 0 < args.max_seconds <= 540
    opponents = ['splash_t2', 'rush_t1', 'eco5_t3', 'splash3_t4']
    skip = {json.loads(line)['index'] for file in args.skip_files for line in Path(file).read_text().splitlines()}
    started = time.perf_counter()
    metadata = {'time_utc': datetime.now(timezone.utc).isoformat(), 'sources': source_hashes(),
                'opponents': opponents, 'total_conditions': sum(1 for _ in conditions()),
                'shard': args.shard, 'shards': args.shards, 'skip_files': args.skip_files,
                'purpose': 'development screen; candidate player 0; no reserved holdouts'}
    with Path(args.output).with_suffix('.meta.json').open('x') as stream:
        json.dump(metadata, stream, sort_keys=True, indent=2)
        stream.write('\n')
    with Path(args.output).open('x') as stream:
        for index, parameters in conditions():
            if index in skip or index % args.shards != args.shard:
                continue
            if time.perf_counter()-started >= args.max_seconds:
                break
            matches = []
            for opponent in opponents:
                row = evaluate((f'maze_{index:03d}', opponent),
                               bots=[MazePressure(**parameters), make(opponent)],
                               condition={'parameters': parameters, 'candidate_side': 0,
                                          'engine_seed': None, 'initial_state': 'standard'})
                # The batch metadata saves source versions. Keep round summaries
                # for finalist inspection, but omit repeated rule dictionaries.
                for key in ('source_sha256', 'rules'):
                    row.pop(key)
                matches.append(row)
            scores = [.5 if r['result']['winner'] is None else int(r['result']['winner']==0) for r in matches]
            result = {'index': index, 'parameters': parameters, 'matches': matches,
                      'score': scores, 'worst': min(scores), 'mean': sum(scores)/len(scores)}
            stream.write(json.dumps(result, sort_keys=True)+'\n')
            stream.flush()
            if index % 20 < args.shards or min(scores) >= .5:
                print(json.dumps({'index': index, 'parameters': parameters, 'scores': scores,
                                  'elapsed_seconds': time.perf_counter()-started}), flush=True)
    print(json.dumps({'finished_utc': datetime.now(timezone.utc).isoformat(),
                      'elapsed_seconds': time.perf_counter()-started}), flush=True)


if __name__ == '__main__':
    main()
