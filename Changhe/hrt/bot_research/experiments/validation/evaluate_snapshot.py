"""Development challenge of archived lead Planner v1; never a final holdout run."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import time
from bot_research.bots.counters.archetypes import PROFILES, Archetype, Profile
from bot_research.bots.counters.posterior_response import PosteriorResponse
from bot_research.bots.counters.snapshots.lead_planner_001 import Planner
from bot_research.experiments.validation.confirm_profiles import opponents
from bot_research.experiments.validation.evaluate import evaluate
from bot_research.experiments.validation.isolated_match import CallableBot


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    cases = opponents()
    selected = json.loads(Path('bot_research/runs/validation/profile-finalists-001.json').read_text())['selected']
    for item in selected:
        p = Profile(**dict(item['profile'], roster=tuple(item['profile']['roster'])))
        cases[f"profile_{item['index']:04d}"] = lambda p=p: Archetype(p)
    cases['posterior_growth'] = PosteriorResponse
    started = time.perf_counter()
    with Path(args.output).open('x') as stream:
        for name, factory in cases.items():
            for side in (0, 1):
                bots = [CallableBot(Planner()), factory()]
                names = ('lead_planner_v1', name)
                if side:
                    bots.reverse()
                    names = tuple(reversed(names))
                row = evaluate(names, bots=bots, condition={'candidate_side': side,
                    'initial_state': 'standard', 'engine_seed': None,
                    'candidate_snapshot': 'bots/counters/snapshots/lead_planner_001.py',
                    'purpose': 'development challenge of the first lead candidate'})
                winner = row['result']['winner']
                row['candidate_outcome'] = 'D' if winner is None else ('W' if winner==side else 'L')
                stream.write(json.dumps(row, sort_keys=True)+'\n')
                stream.flush()
                print(json.dumps({'opponent': name, 'side': side, 'outcome': row['candidate_outcome'],
                    'hp': row['hp'], 'rounds': row['rounds'], 'elapsed_seconds': time.perf_counter()-started}), flush=True)
                if time.perf_counter()-started >= 480:
                    print('Bounded batch incomplete; check coverage.', flush=True)
                    return


if __name__ == '__main__':
    main()
