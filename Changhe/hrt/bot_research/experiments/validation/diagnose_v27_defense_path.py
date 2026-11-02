"""Observe original planner calls on a fixed, replayed v27 public history."""
from collections import Counter
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs
import argparse
import hashlib
import json
import time

from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.experiments.lead.v27 import Insurer, _cost_of, _with_buildings, _worst_leak
from bot_research.harness import gamekit as gk
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.replay_audit import normalized
from bot_research.experiments.validation.source_closure import static_closure


class TracedInsurer(Insurer):
    def __init__(self, **params):
        super().__init__(**params)
        self.calls = []

    def _plan(self, observation, budget, **kwargs):
        result = super()._plan(observation, budget, **kwargs)
        if observation['round'] <= 12:
            rules = gk.Rules.from_observation(observation)
            comps = kwargs.get('threat_types') or []
            after = _with_buildings(observation, result, budget - _cost_of(result, rules))
            row = dict(round=observation['round'], player=observation['player'], budget=budget,
                       partial=kwargs.get('partial'), allow_guns_requested=kwargs.get('allow_guns', True),
                       gun_cap=self.p['gun_cap'], roster_counts=[dict(Counter(c)) for c in comps],
                       actions=result, cost=_cost_of(result, rules),
                       worst_leak_before=_worst_leak(observation, rules, comps) if comps else None,
                       worst_leak_after=_worst_leak(after, rules, comps) if comps else None)
            self.calls.append(row)
        return result


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--result', required=True)
    p.add_argument('--output', required=True)
    a = p.parse_args()
    start = time.perf_counter()
    digest = lambda f: hashlib.sha256(Path(f).read_bytes()).hexdigest()
    hashes = {str(f): digest(f) for f in static_closure({'bot_research.experiments.validation.diagnose_v27_defense_path'})}
    hashes['td_game/balanced.json'] = digest('td_game/balanced.json')
    checked_row(a.result, hashes)
    row = json.loads(Path(a.result).read_text())
    c = row['condition']; side = c['candidate_side']
    assert c['candidate_spec'].split(':')[0] == 'bot_research.experiments.lead.v27'
    params = {k: json.loads(v[0]) for k, v in parse_qs(c['candidate_spec'].partition('?')[2]).items()}
    policy = TracedInsurer(**params)
    records = [json.loads(s) for s in Path(row['replay_path']).read_text().splitlines()]
    engine = Engine(balanced_config(), tuple(row['bot_specs']))
    assert normalized(engine.initial_records(tuple(row['bot_specs']))) == records[:2]
    rounds = []
    for rnd in range(1, row['rounds'] + 1):
        obs = engine.observation(side); saved = deepcopy(obs)
        proposed = policy(obs); assert obs == saved
        pair = records[2*rnd:2*rnd+2]
        actions = [[e['action'] for e in r['event'] if e['kind'] == 'action'] for r in pair]
        assert proposed == actions[side]
        if rnd <= 12:
            rules = gk.Rules.from_observation(obs)
            rounds.append(dict(round=rnd, fortress_after=policy.fortress,
                               passive=policy._passive(obs, rules),
                               own_start_gold=obs['players'][side]['gold'],
                               opponent_start_gold=obs['players'][1-side]['gold'],
                               own_actions=proposed))
        assert normalized(engine.play_round(actions)) == pair
    assert engine.result == row['result']
    assert all(digest(f) == h for f, h in hashes.items())
    out = dict(time_utc=datetime.now(timezone.utc).isoformat(), runtime_seconds=time.perf_counter()-start,
               all_passed=True, condition=c, input_sha256=hashes, calls=policy.calls, rounds=rounds,
               scope='Planner instrumentation on an existing public history; exact action and original-engine replay check. Extra leak calculations are diagnostics only.')
    atomic_json(a.output, out, exclusive=True)
    print(json.dumps({k: out[k] for k in ('time_utc', 'runtime_seconds', 'all_passed')}))

if __name__ == '__main__':
    main()
