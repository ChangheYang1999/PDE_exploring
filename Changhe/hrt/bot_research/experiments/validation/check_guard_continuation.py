"""Original-engine component checks of unchanged guard opening and control."""
from copy import deepcopy
from datetime import datetime, timezone
import argparse
import hashlib
import json
from pathlib import Path
import time
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.guard_geometry import GuardGeometry
from bot_research.bots.counters.guard_continuation import GuardContinuation
from bot_research.experiments.lead.frozen.best_v9b import make as target
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    paths = set(static_closure({'bot_research.experiments.validation.check_guard_continuation'}))
    paths.add(Path('td_game/balanced.json'))
    sources = {str(p): digest(p) for p in paths}
    cases = []
    for roster in [('tier1',), ('tier2',)]:
        for hold in (None, 11):
            for side in (0, 1):
                kw = dict(roster=roster, x=9, y=1, parameters=dict(foreign_attack_from=hold))
                old = GuardGeometry(**kw)
                control = GuardContinuation(version='econ17', **kw)
                revised = GuardContinuation(version='econ19', **kw)
                opponent = target()
                engine = Engine(balanced_config(), ('guard-check-0', 'guard-check-1'))
                rounds = []
                for rnd in range(1, 9):
                    if engine.result is not None:
                        break
                    observation = engine.observation(side)
                    before = deepcopy(observation)
                    original = old.decide(observation)
                    assert observation == before
                    replacement = control.decide(observation)
                    assert observation == before
                    assert original == replacement
                    if rnd == 1:
                        assert revised.decide(observation) == original
                        assert observation == before
                    pair = [None, None]
                    pair[side] = original
                    pair[1-side] = opponent(engine.observation(1-side))
                    records = engine.play_round(pair)
                    assert all(e['accepted'] for record in records for e in record['event'] if e['kind'] == 'action')
                    rounds.append(dict(round=rnd, actions=original))
                cases.append(dict(roster=roster, hold=hold, side=side, rounds=rounds))
                print(json.dumps(dict(roster=roster, hold=hold, side=side, checked_rounds=len(rounds))), flush=True)
    changed = [p for p, h in sources.items() if digest(p) != h]
    assert not changed
    result = dict(time_utc=datetime.now(timezone.utc).isoformat(), runtime_seconds=time.perf_counter()-started,
                  source_sha256=sources, source_changed_during_run=changed, all_passed=True, cases=cases,
                  scope='Eight original-engine prefixes through round eight: legacy-control action equality, observation immutability, legality, and identical first-round actions for economy19. No full-game strength claim.')
    atomic_json(args.output, result, exclusive=True)
    print(json.dumps(dict(all_passed=True, runtime_seconds=result['runtime_seconds'])), flush=True)


if __name__ == '__main__':
    main()
