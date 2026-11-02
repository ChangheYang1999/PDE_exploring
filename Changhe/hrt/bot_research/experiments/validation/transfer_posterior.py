"""Test purchase-based adaptation on additional, unmodeled development policies."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import time

from bot_research.bots.counters.archetypes import Archetype, Profile, PROFILES
from bot_research.bots.counters.posterior_response import PosteriorResponse
from bot_research.bots.counters.visible_search import VisibleSearch
from bot_research.experiments.validation.confirm_profiles import opponents
from bot_research.experiments.validation.evaluate import evaluate


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--discount', type=float, default=0.9)
    parser.add_argument('--opening', default='growth')
    args = parser.parse_args()
    cases = {k: v for k, v in opponents().items() if k not in PROFILES}
    selected = json.loads(Path('bot_research/runs/validation/profile-finalists-001.json').read_text())['selected']
    for item in selected:
        values = item['profile']
        p = Profile(**dict(values, roster=tuple(values['roster'])))
        cases[f"profile_{item['index']:04d}"] = lambda p=p: Archetype(p)
    cases['visible_search'] = VisibleSearch
    start = time.perf_counter()
    with Path(args.output).open('x') as stream:
        for name, factory in cases.items():
            for side in (0, 1):
                candidate = PosteriorResponse(opening=args.opening, discount=args.discount)
                bots = [candidate, factory()]
                names = ('posterior', name)
                if side:
                    bots.reverse()
                    names = tuple(reversed(names))
                condition = {'initial_state': 'standard', 'engine_seed': None, 'candidate_side': side,
                             'opening': args.opening, 'discount': args.discount,
                             'purpose': 'development transfer to policies absent from the classifier model set'}
                row = evaluate(names, bots=bots, condition=condition)
                row['posterior_trace'] = candidate.trace
                winner = row['result']['winner']
                row['candidate_outcome'] = 'D' if winner is None else ('W' if winner == side else 'L')
                stream.write(json.dumps(row, sort_keys=True) + '\n')
                stream.flush()
                print(json.dumps({'opponent': name, 'side': side, 'outcome': row['candidate_outcome'],
                                  'hp': row['hp'], 'rounds': row['rounds'], 'elapsed': time.perf_counter() - start}), flush=True)
                if time.perf_counter() - start >= 480:
                    print('Bounded batch ended; inspect coverage before claiming completion.', flush=True)
                    return


if __name__ == '__main__':
    main()
