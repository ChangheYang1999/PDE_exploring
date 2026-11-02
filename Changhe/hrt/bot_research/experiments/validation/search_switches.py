"""Target the observed-purchase classifier with abrupt but legal plan changes."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import itertools
import json
from pathlib import Path
import time

from bot_research.bots.counters.archetypes import PROFILES
from bot_research.bots.counters.posterior_response import PosteriorResponse
from bot_research.bots.counters.switching import SwitchingArchetype
from bot_research.experiments.validation.evaluate import evaluate, source_hashes


def conditions():
    index = 0
    for prefix, after, switch_round in itertools.product(
            ('eco5_t3', 'splash_t2', 'gun_t3', 'rush_t1', 'rush_t2'), sorted(PROFILES), range(2, 9)):
        if prefix == after:
            continue
        yield index, prefix, after, switch_round
        index += 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--shard', required=True, type=int)
    parser.add_argument('--shards', type=int, default=2)
    parser.add_argument('--output', required=True)
    parser.add_argument('--max-seconds', type=float, default=480)
    parser.add_argument('--skip-files', nargs='*', default=[])
    args = parser.parse_args()
    skip = set()
    for file in args.skip_files:
        skip.update(json.loads(line)['condition']['index'] for line in Path(file).read_text().splitlines())
    start = time.perf_counter()
    Path(args.output).with_suffix('.meta.json').write_text(json.dumps({
        'started_utc': datetime.now(timezone.utc).isoformat(), 'sources': source_hashes(),
        'target': 'PosteriorResponse(opening=growth, discount=0.9)', 'all_conditions': list(conditions()),
        'shard': args.shard, 'shards': args.shards,
        'purpose': 'adversarial development; none of the reserved holdouts used'}, sort_keys=True, indent=2) + '\n')
    with Path(args.output).open('x') as stream:
        for index, prefix, after, switch_round in conditions():
            if index in skip or index % args.shards != args.shard:
                continue
            if time.perf_counter() - start >= args.max_seconds:
                print('Bounded batch ended.', flush=True)
                break
            target = PosteriorResponse()
            attacker = SwitchingArchetype(prefix, after, switch_round)
            name = f'switch_{prefix}_to_{after}_r{switch_round}'
            condition = {'index': index, 'prefix': prefix, 'after': after, 'switch_round': switch_round,
                         'initial_state': 'standard', 'engine_seed': None, 'counter_side': 0,
                         'target': 'posterior_growth_discount0.9'}
            row = evaluate((name, 'posterior_growth'), bots=[attacker, target], condition=condition)
            row['target_trace'] = target.trace
            row['counter_outcome'] = 'D' if row['result']['winner'] is None else ('W' if row['result']['winner'] == 0 else 'L')
            stream.write(json.dumps(row, sort_keys=True) + '\n')
            stream.flush()
            if row['counter_outcome'] != 'L' or index % 20 < args.shards:
                print(json.dumps({'index': index, 'prefix': prefix, 'after': after, 'switch_round': switch_round,
                                  'counter_outcome': row['counter_outcome'], 'hp': row['hp'],
                                  'elapsed': time.perf_counter() - start}), flush=True)


if __name__ == '__main__':
    main()
