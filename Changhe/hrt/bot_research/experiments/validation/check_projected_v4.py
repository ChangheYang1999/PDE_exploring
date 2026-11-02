"""Verify public-model projections against actual submissions through the engine."""
import argparse
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import time
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.projected_forecast import ProjectedTiming
from bot_research.bots.counters.prefixed_v4 import PARAMETERS
from bot_research.bots.counters.snapshots.lead_fifteen_001 import Lead15
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    cases = []
    for projection in ('minions', 'nonminions', 'opening'):
        for side in (0, 1):
            counter = ProjectedTiming(projection=projection,
                model_spec='bot_research.bots.counters.snapshots.lead_fifteen_001:@make',
                model_parameters=PARAMETERS, attack_round=3, tier='tier3', attack_share=1.0, count_cap=1000)
            target = Lead15(**PARAMETERS)
            engine = Engine(balanced_config(), ('component0','component1'))
            checked = 0
            for rnd in range(1, 13):
                actions = [None, None]
                obs = engine.observation(side)
                before = deepcopy(obs)
                actions[side] = counter.decide(obs)
                assert obs == before, 'Counter mutated the public observation.'
                actions[1-side] = target(engine.observation(1-side))
                trace = counter.trace[-1]
                assert trace['round'] == rnd
                if projection != 'opening':
                    assert trace['full_predicted_actions'] == actions[1-side]
                    wanted = projection == 'minions'
                    expected = [a for a in actions[1-side] if (a['op']=='buy_minion') == wanted]
                    assert trace['predicted_actions'] == expected
                    assert counter.model.model.last_round == rnd
                else:
                    expected = [{'op':'buy_minion','type':'tier1'} for _ in range(3)] if rnd==1 else []
                    assert trace['predicted_actions'] == expected
                    assert trace['full_predicted_actions'] is None
                    assert counter.model.last_round == rnd
                records = engine.play_round(actions)
                assert all(e['accepted'] for r in records for e in r['event'] if e['kind']=='action')
                checked += 1
                if engine.result is not None:
                    break
            cases.append(dict(projection=projection, side=side, checked_rounds=checked, all_passed=True))
            print(json.dumps(cases[-1]), flush=True)
    paths = set(static_closure({'bot_research.experiments.validation.check_projected_v4'}))
    paths.add(Path('td_game/balanced.json'))
    result = dict(time_utc=datetime.now(timezone.utc).isoformat(), runtime_seconds=time.perf_counter()-started,
                  source_sha256={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
                  cases=cases, all_passed=True, scope='Component prefixes through the unchanged engine: observation immutability, complete model predictions, selected projections, call counts and accepted actions. Not strength evidence.')
    atomic_json(args.output, result, exclusive=True)
    print(json.dumps({k:result[k] for k in ('time_utc','runtime_seconds','all_passed')}))


if __name__ == '__main__':
    main()
