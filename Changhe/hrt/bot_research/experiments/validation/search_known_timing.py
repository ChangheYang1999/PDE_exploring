"""Bounded deterministic timing screens against explicit frozen public policies."""
from __future__ import annotations
import argparse
import itertools
import json
from pathlib import Path
import time
from bot_research.bots.counters.known_policy import KnownTiming, policy_factory
from bot_research.experiments.validation.evaluate import evaluate
from bot_research.experiments.validation.isolated_match import CallableBot


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--model', required=True)
    p.add_argument('--model-parameters', type=json.loads, default={})
    p.add_argument('--rounds', nargs='+', type=int, default=[1])
    p.add_argument('--tiers', nargs='+', default=['tier1', 'tier2', 'tier3'])
    p.add_argument('--shares', nargs='+', type=float, default=[1.0])
    p.add_argument('--caps', nargs='+', type=int, default=[1, 2, 200])
    p.add_argument('--defense-first', action='store_true')
    p.add_argument('--sides', nargs='+', type=int, choices=(0, 1), default=[0])
    p.add_argument('--shard', type=int, default=0)
    p.add_argument('--shards', type=int, default=1)
    p.add_argument('--start', type=int, default=0)
    p.add_argument('--output', required=True)
    a = p.parse_args()
    root = Path(a.output).with_suffix('')
    root.mkdir(exist_ok=False)
    start = time.perf_counter()
    cases = itertools.product(a.rounds, a.tiers, a.shares, a.caps, a.sides)
    with Path(a.output).open('x') as f:
        for index, (rnd, tier, share, cap, side) in enumerate(cases):
            if index < a.start or index % a.shards != a.shard:
                continue
            if time.perf_counter()-start > 480:
                print(json.dumps({'stopped_before_index': index, 'reason': '480 second batch bound'}), flush=True)
                return
            parameters = {'attack_round': rnd, 'tier': tier, 'attack_share': share,
                          'count_cap': cap, 'defense_first': a.defense_first}
            counter = KnownTiming(model=a.model, model_parameters=a.model_parameters, **parameters)
            target = CallableBot(policy_factory(a.model, a.model_parameters))
            bots, names = [counter, target], ('known_timing', a.model)
            if side:
                bots.reverse()
                names = tuple(reversed(names))
            replay = str(root / f'case{index:04d}.jsonl')
            row = evaluate(names, bots=bots, replay_path=replay, condition={
                'index': index, 'counter_side': side, 'parameters': parameters,
                'model': a.model, 'model_parameters': a.model_parameters,
                'initial_state': 'standard', 'engine_seed': None,
                'purpose': 'known-policy development grid; no reserved holdout'})
            winner = row['result']['winner']
            row['counter_outcome'] = 'D' if winner is None else ('W' if winner == side else 'L')
            row['forecast_trace'] = counter.trace
            records = [json.loads(line) for line in Path(replay).read_text().splitlines()]
            actual = {r['round']: [e['action'] for e in r['event'] if e['kind'] == 'action']
                      for r in records if r['player'] == 1-side and r['round'] > 0}
            row['forecast_mismatch_rounds'] = [t['round'] for t in counter.trace
                                             if t['predicted_actions'] != actual[t['round']]]
            f.write(json.dumps(row, sort_keys=True)+'\n')
            f.flush()
            print(json.dumps({k: row[k] for k in ('condition', 'counter_outcome', 'hp',
                'rounds', 'runtime_seconds', 'bot_errors', 'rejected_actions',
                'source_changed_during_match', 'forecast_mismatch_rounds')}), flush=True)


if __name__ == '__main__':
    main()
