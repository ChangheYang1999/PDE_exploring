"""Paired, wider-pool confirmation of screened profiles. Still development data."""
from __future__ import annotations
import argparse
from dataclasses import asdict
from datetime import datetime, timezone
import json
from pathlib import Path
import time

from bot_research.bots.counters.archetypes import Archetype, Profile, PROFILES, make
from bot_research.bots.counters import pool
from bot_research.experiments.validation.evaluate import evaluate, source_hashes
from bot_research.experiments.validation.isolated_match import CallableBot


def opponents():
    factories = {name: (lambda name=name: make(name)) for name in sorted(PROFILES)}
    factories.update({
        'turtle_splash': lambda: CallableBot(pool.turtle()),
        'turtle_gun2': lambda: CallableBot(pool.turtle(kind='gun2')),
        'spending_mirror': lambda: CallableBot(pool.mirror()),
        'random_130': lambda: CallableBot(pool.random_legal(seed=130)),
        'stacker8_t1': lambda: CallableBot(pool.stacker()),
        'rush_t5': lambda: CallableBot(pool.rush_t5()),
    })
    return factories


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--profiles', default='bot_research/runs/validation/profile-finalists-001.json')
    parser.add_argument('--shard', type=int, required=True)
    parser.add_argument('--shards', type=int, default=2)
    parser.add_argument('--output', required=True)
    parser.add_argument('--max-seconds', type=float, default=480)
    parser.add_argument('--skip-files', nargs='*', default=[])
    args = parser.parse_args()
    skip = set()
    for file in args.skip_files:
        for line in Path(file).read_text().splitlines():
            c = json.loads(line)['condition']
            skip.add((c['profile_index'], c['opponent'], c['candidate_side']))
    selection = json.loads(Path(args.profiles).read_text())
    start = time.perf_counter()
    factories = opponents()
    meta = {'started_utc': datetime.now(timezone.utc).isoformat(), 'selection': selection,
            'sources': source_hashes(), 'opponents': list(factories), 'shard': args.shard,
            'shards': args.shards, 'purpose': 'development confirmation, not holdout validation'}
    Path(args.output).with_suffix('.meta.json').write_text(json.dumps(meta, sort_keys=True, indent=2) + '\n')
    with Path(args.output).open('x') as stream:
        for selected_index, selected in enumerate(selection['selected']):
            if selected_index % args.shards != args.shard:
                continue
            values = selected['profile']
            profile = Profile(**dict(values, roster=tuple(values['roster'])))
            name = f"profile_{selected['index']:04d}"
            for other, factory in factories.items():
                for side in (0, 1):
                    key = (selected['index'], other, side)
                    if key in skip:
                        continue
                    if time.perf_counter() - start >= args.max_seconds:
                        print('Bounded batch ended.', flush=True)
                        return
                    bots = [Archetype(profile), factory()]
                    names = (name, other)
                    if side:
                        bots.reverse()
                        names = tuple(reversed(names))
                    condition = {'initial_state': 'standard', 'engine_seed': None, 'candidate_side': side,
                                 'profile_index': selected['index'], 'profile': asdict(profile), 'opponent': other,
                                 'purpose': 'development confirmation'}
                    row = evaluate(names, bots=bots, condition=condition)
                    winner = row['result']['winner']
                    row['candidate_outcome'] = 'D' if winner is None else ('W' if winner == side else 'L')
                    stream.write(json.dumps(row, sort_keys=True) + '\n')
                    stream.flush()
                    print(json.dumps({'profile': name, 'opponent': other, 'side': side, 'outcome': row['candidate_outcome'],
                                      'hp': row['hp'], 'rounds': row['rounds'], 'elapsed': time.perf_counter() - start}), flush=True)


if __name__ == '__main__':
    main()
