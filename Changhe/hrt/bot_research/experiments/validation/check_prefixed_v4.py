"""Check model call-through, forecasts and original-adapter agreement."""
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
from bot_research.bots.counters.prefixed_v4 import PARAMETERS, lead15, timing, schedule
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
            for rnd in range(1, 6):
                actions = [None, None]
                actions[side] = counter(engine.observation(side))
                target_obs = engine.observation(1-side)
                actions[1-side] = target(deepcopy(target_obs))
                assert original.decide(deepcopy(target_obs)) == actions[1-side]
                assert not original.scenario_errors
                owner = counter.__self__
                assert owner.calls == target.calls == rnd
                assert owner.policy.model.last_round == rnd
                assert owner.policy.model.policy.calls == rnd
                assert owner.trace[-1]['predicted_actions'] == actions[1-side]
                records = engine.play_round(actions)
                assert all(e['accepted'] for r in records for e in r['event'] if e['kind'] == 'action')
            cases.append({'scenario': scenario, 'side': side, 'rounds': engine.round,
                          'opening_calls': target.opening_calls, 'all_passed': True})
            print(json.dumps(cases[-1]), flush=True)
    sources = set(static_closure({'bot_research.experiments.validation.check_prefixed_v4'}))
    sources.update((Path('td_game/balanced.json'), Path('bot_research/experiments/validation/analysis/prefixed_forecast/PROOF.md')))
    result = {'time_utc': datetime.now(timezone.utc).isoformat(),
              'runtime_seconds': time.perf_counter()-started, 'all_passed': True, 'cases': cases,
              'source_sha256': {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
              'scope': 'Eight five-round component prefixes through unchanged engine; exact public forecasts, call counts, legal actions and agreement with the existing TimedBot adapter. Not full-game strength.'}
    atomic_json(args.output, result, exclusive=True)
    print(json.dumps({k: result[k] for k in ('time_utc', 'runtime_seconds', 'all_passed')}))


if __name__ == '__main__':
    main()
