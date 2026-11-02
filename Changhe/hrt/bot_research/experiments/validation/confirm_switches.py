"""Paired confirmation and forgetting-rate ablation of discovered switch counters."""
from __future__ import annotations
import argparse
import itertools
import json
from pathlib import Path
import time

from bot_research.bots.counters.posterior_response import PosteriorResponse
from bot_research.bots.counters.switching import SwitchingArchetype
from bot_research.experiments.validation.evaluate import evaluate


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--discounts', type=float, nargs='+', default=[0, .25, .5, .9, 1])
    parser.add_argument('--replay-dir')
    args = parser.parse_args()
    conditions = json.loads(Path('bot_research/runs/validation/switch-finalists-001.json').read_text())['conditions']
    if args.replay_dir:
        Path(args.replay_dir).mkdir(parents=True, exist_ok=False)
    start = time.perf_counter()
    with Path(args.output).open('x') as stream:
        for c, discount, side in itertools.product(conditions, args.discounts, (0, 1)):
            target = PosteriorResponse(discount=discount)
            counter = SwitchingArchetype(c['prefix'], c['after'], c['switch_round'])
            counter_name = f"switch_{c['index']:03d}"
            target_name = f"posterior_discount{discount}"
            bots = [target, counter]
            names = (target_name, counter_name)
            if side:
                bots.reverse()
                names = tuple(reversed(names))
            condition = dict(c, candidate_side=side, counter_side=1-side, discount=discount,
                             purpose='paired counter confirmation and adaptation-rate ablation')
            replay = None
            if args.replay_dir and discount in (.9, 0) and c['index'] in (92, 22):
                replay = str(Path(args.replay_dir) / f"switch{c['index']}-discount{discount}-side{side}.jsonl")
            row = evaluate(names, bots=bots, condition=condition, replay_path=replay)
            row['posterior_trace'] = target.trace
            winner = row['result']['winner']
            row['candidate_outcome'] = 'D' if winner is None else ('W' if winner == side else 'L')
            stream.write(json.dumps(row, sort_keys=True) + '\n')
            stream.flush()
            print(json.dumps({'switch_index': c['index'], 'discount': discount, 'side': side,
                              'outcome': row['candidate_outcome'], 'hp': row['hp'],
                              'elapsed_seconds': time.perf_counter()-start}), flush=True)
            if time.perf_counter()-start >= 480:
                print('Bounded batch ended before all conditions; do not report complete.', flush=True)
                return


if __name__ == '__main__':
    main()
