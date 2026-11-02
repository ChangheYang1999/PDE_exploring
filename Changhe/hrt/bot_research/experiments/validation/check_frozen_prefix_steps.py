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
from bot_research.experiments.lead.frozen import best_v9b as best
from bot_research.bots.counters.prefixed_frozen_best_v9b import target as target_factory
from bot_research.bots.counters.prefixed_frozen_best_v9b import timing
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    expected = 'dc96ac422078fd2cadafcc72fce10bb1d22bbb50b9c19a4bbe7937a2fba85ee7'
    assert hashlib.sha256(Path('bot_research/experiments/lead/frozen/best_v9b.py').read_bytes()).hexdigest() == expected
    sources = set(static_closure({'bot_research.experiments.validation.check_frozen_prefix_steps'}))
    sources.add(Path('td_game/balanced.json'))
    frozen = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    started = time.perf_counter()
    cases = []
    for free_steps in (15, 30):
        scenario = 'asym:3:2'
        for side in (0, 1):
            counter = timing(scenario=scenario, attack_round=5, tier='tier3', attack_share=1.0, free_steps=free_steps)
            target = target_factory(scenario=scenario)
            original = TimedBot(best.make(), make_overrides(scenario)[1-side])
            engine = Engine(balanced_config(), ('component0', 'component1'))
            checked = []
            for rnd in range(1, 9):
                if engine.result is not None:
                    break
                actions = [None, None]
                own_obs = engine.observation(side)
                own_before = deepcopy(own_obs)
                actions[side] = counter(own_obs)
                assert own_obs == own_before, 'Counter changed its observation.'
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
            cases.append(dict(scenario=scenario, free_steps=free_steps, side=side, rounds=checked, all_passed=True))
            print(json.dumps(dict(scenario=scenario, free_steps=free_steps, side=side, rounds=len(checked), all_passed=True)), flush=True)
    sources = set(static_closure({'bot_research.experiments.validation.check_frozen_prefix_steps'}))
    sources.add(Path('td_game/balanced.json'))
    assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest() == h for p, h in frozen.items())
    result = dict(time_utc=datetime.now(timezone.utc).isoformat(), runtime_seconds=time.perf_counter()-started,
        all_passed=True, cases=cases, source_sha256=frozen,
        scope='Four component prefixes through round eight on asym:3:2, with steps15/30: exact public forecasts, legal proposals, adapter agreement, and choice by measured residual/cost. Not full-game strength.')
    atomic_json(args.output, result, exclusive=True)
    print(json.dumps({k:result[k] for k in ('time_utc','runtime_seconds','all_passed')}))


if __name__ == '__main__':
    main()
