"""Enumerate legal single-gun openings against three tier1 copies.

Every legal gun1 coordinate is checked with the unchanged Engine in both
assignments. The chosen (10,1) point follows the seven-cell corner-coverage
argument; this search checks that argument and measures its alternatives.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import time
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.economy.frozen.v2.fastsim import MapModel, simulate
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    start = time.perf_counter()
    cases = []
    config = balanced_config()
    for y in range(12):
        for x in range(12):
            if (x, y) in ((0, 0), (11, 11)):
                continue
            outcomes = []
            for side in (0, 1):
                engine = Engine(config, ('check0', 'check1'))
                rules = engine.observation(side)['rules']
                actions = [[], []]
                actions[side] = [{'op':'build_turret', 'type':'gun1', 'x':x, 'y':y}]
                actions[1-side] = [{'op':'buy_minion', 'type':'tier1'}]*3
                rows = engine.play_round(actions)
                assert all(e['accepted'] for r in rows for e in r['event'] if e['kind']=='action')
                model = MapModel([(x, y, 'gun1')], rules)
                damage = 800-engine.players[side].hp
                assert simulate(model, ['tier1']*3, rules)[1] == damage
                outcomes.append(dict(damage=damage, gold=engine.players[side].gold,
                                     path=model.path, coverage=model.guns[0][1] if model.guns else []))
            assert outcomes[0] == outcomes[1]
            cases.append(dict(x=x, y=y, **outcomes[0]))
    selected = next(c for c in cases if (c['x'],c['y'])==(10,1))
    original = next(c for c in cases if (c['x'],c['y'])==(3,1))
    assert selected['damage']==0
    assert selected['coverage']==list(range(8,15))
    assert original['damage']==5
    paths = set(static_closure({'bot_research.experiments.validation.search_guard_geometry'}))
    paths.add(Path('td_game/balanced.json'))
    result = dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,
                  source_sha256={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
                  all_passed=True, original_engine_rounds=2*len(cases), cases=cases,
                  selected=selected, original=original,
                  zero_damage_coordinates=[[c['x'],c['y']] for c in cases if c['damage']==0],
                  scope='One gun1, three tier1, standard empty opening, both assignments. No universal roster or full-game strength claim.')
    atomic_json(args.output,result,exclusive=True)
    print(json.dumps({k:result[k] for k in ('time_utc','runtime_seconds','all_passed','original_engine_rounds','zero_damage_coordinates')}))


if __name__=='__main__':
    main()
