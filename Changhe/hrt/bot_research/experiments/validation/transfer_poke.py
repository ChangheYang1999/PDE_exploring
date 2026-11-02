"""Development transfer of the small-opening defensive counter."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import time
from bot_research.bots.counters.poke_lock import PokeLock
from bot_research.experiments.validation.confirm_profiles import opponents
from bot_research.experiments.validation.evaluate import evaluate


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--opening-units', type=int, default=1)
    parser.add_argument('--reserve', type=int, default=0)
    parser.add_argument('--output', required=True)
    parser.add_argument('--skip-files', nargs='*', default=[])
    args = parser.parse_args()
    skip = set()
    for name in args.skip_files:
        for line in Path(name).read_text().splitlines():
            c = json.loads(line)['condition']
            skip.add((c['opponent'], c['candidate_side']))
    parameters = {'opening_units': args.opening_units, 'reserve': args.reserve, 'phi': 1.0,
                  'saturate_round': 20}
    started = time.perf_counter()
    with Path(args.output).open('x') as stream:
        for opponent, factory in opponents().items():
            for side in (0, 1):
                if (opponent, side) in skip:
                    continue
                if time.perf_counter()-started > 480:
                    print('Bounded batch ended; inspect coverage and resume with --skip-files.', flush=True)
                    return
                bots = [PokeLock(**parameters), factory()]
                names = ('poke_lock', opponent)
                if side:
                    bots.reverse()
                    names = tuple(reversed(names))
                row = evaluate(names, bots=bots, condition={'candidate_side': side,
                    'parameters': parameters, 'opponent': opponent, 'initial_state': 'standard',
                    'engine_seed': None, 'purpose': 'development transfer; no reserved holdout'})
                winner = row['result']['winner']
                row['candidate_outcome'] = 'D' if winner is None else ('W' if winner == side else 'L')
                stream.write(json.dumps(row, sort_keys=True)+'\n')
                stream.flush()
                print(json.dumps({'opponent': opponent, 'side': side, 'outcome': row['candidate_outcome'],
                    'hp': row['hp'], 'rounds': row['rounds'], 'elapsed_seconds': time.perf_counter()-started}), flush=True)


if __name__ == '__main__':
    main()
