"""Check exact forecast, adapter semantics and legal fallback proposals."""
from copy import deepcopy
from datetime import datetime, timezone
import argparse
import hashlib
import json
from pathlib import Path
import time
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.harness.match import TimedBot
from bot_research.harness.scenarios import make_overrides
from bot_research.bots.counters.snapshots.lead_fifteen_001 import Lead15
from bot_research.bots.counters.prefixed_v4 import PARAMETERS, lead15
from bot_research.bots.counters.prefixed_free_v4 import timing
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    cases = []
    for scenario in ('mirror:1:2', 'asym:3:2', 'mirror:22:3', 'asym:23:2'):
        for side in (0, 1):
            counter = timing(scenario=scenario, attack_round=5, tier='tier3', attack_share=1.0)
            target = lead15(scenario=scenario)
            original = TimedBot(Lead15(**PARAMETERS), make_overrides(scenario)[1-side])
            engine = Engine(balanced_config(), ('component0', 'component1'))
            checked = []
            for rnd in range(1, 9):
                if engine.result is not None:
                    break
                actions = [None, None]
                actions[side] = counter(engine.observation(side))
                obs = engine.observation(1-side)
                actions[1-side] = target(deepcopy(obs))
                assert original.decide(deepcopy(obs)) == actions[1-side]
                assert not original.scenario_errors
                owner = counter.__self__
                assert owner.calls == target.calls == owner.policy.model.last_round == rnd
                assert owner.policy.model.policy.calls == rnd
                trace = owner.trace[-1]
                assert trace['predicted_actions'] == actions[1-side]
                alternatives = trace['defense']['alternatives']
                picked = next(c for c in alternatives if c['label'] == trace['defense']['selected'])
                assert (picked['residual'], picked['cost']) == min((c['residual'], c['cost']) for c in alternatives)
                records = engine.play_round(actions)
                assert all(e['accepted'] for r in records for e in r['event'] if e['kind'] == 'action')
                checked.append(dict(round=rnd, defense=trace['defense']))
            cases.append(dict(scenario=scenario, side=side, rounds=checked, all_passed=True))
            print(json.dumps(dict(scenario=scenario, side=side, rounds=len(checked), all_passed=True)), flush=True)
    sources = set(static_closure({'bot_research.experiments.validation.check_free_forecast'}))
    sources.add(Path('td_game/balanced.json'))
    result = dict(time_utc=datetime.now(timezone.utc).isoformat(), runtime_seconds=time.perf_counter()-started,
        all_passed=True, cases=cases, source_sha256={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
        scope='Eight component prefixes through round eight: exact public forecasts, legal proposals, adapter agreement, and choice by measured residual/cost. Not full-game strength.')
    atomic_json(args.output, result, exclusive=True)
    print(json.dumps({k:result[k] for k in ('time_utc','runtime_seconds','all_passed')}))


if __name__ == '__main__':
    main()
