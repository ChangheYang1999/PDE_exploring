"""Factorial development test of purchase-based opponent identification."""
from __future__ import annotations
from datetime import datetime, timezone
import json
from pathlib import Path
import time

from bot_research.bots.counters.archetypes import PROFILES, make
from bot_research.bots.counters.posterior_response import PosteriorResponse
from bot_research.experiments.validation.evaluate import evaluate


def main():
    path = Path('bot_research/runs/validation/posterior-response-001.jsonl')
    started = time.perf_counter()
    with path.open('x') as stream:
        for opening in ('growth', 'splash'):
            for fixed in (None, 'splash_t2'):
                for opponent in sorted(PROFILES):
                    for side in (0, 1):
                        candidate = PosteriorResponse(opening=opening, fixed=fixed)
                        name = f'posterior_{opening}_{fixed or "adaptive"}'
                        bots = [candidate, make(opponent)]
                        names = (name, opponent)
                        if side:
                            bots.reverse()
                            names = tuple(reversed(names))
                        condition = {'initial_state': 'standard', 'engine_seed': None,
                                     'candidate_side': side, 'opening': opening,
                                     'fixed_response': fixed, 'purpose': 'development factorial ablation'}
                        result = evaluate(names, bots=bots, condition=condition)
                        result['posterior_trace'] = candidate.trace
                        winner = result['result']['winner']
                        result['candidate_outcome'] = 'D' if winner is None else ('W' if winner == side else 'L')
                        stream.write(json.dumps(result, sort_keys=True) + '\n')
                        stream.flush()
                        print(json.dumps({'opening': opening, 'fixed': fixed, 'opponent': opponent, 'side': side,
                                          'outcome': result['candidate_outcome'], 'hp': result['hp'],
                                          'seconds': time.perf_counter() - started}), flush=True)
                        if time.perf_counter() - started > 480:
                            print('Bounded batch ended; remaining conditions must be resumed separately.', flush=True)
                            return
    print(datetime.now(timezone.utc).isoformat(), flush=True)


if __name__ == '__main__':
    main()
