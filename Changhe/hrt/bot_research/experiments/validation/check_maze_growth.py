"""Verify every pinned wall map and exact recurrence on the original engine."""
from copy import deepcopy
from datetime import datetime,timezone
from pathlib import Path
import argparse,hashlib,json,time
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.maze_grower import MazeGrower,DATA,DATA_SHA256
from bot_research.experiments.validation.source_closure import static_closure
from bot_research.experiments.validation.artifact_io import atomic_json


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);args=p.parse_args();start=time.perf_counter()
    paths=set(static_closure({'bot_research.experiments.validation.check_maze_growth'}))|{DATA.relative_to(Path.cwd()),Path('td_game/balanced.json'),Path('configs/balanced.json')}
    digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    inputs={str(p):digest(p) for p in paths};assert digest(DATA)==DATA_SHA256
    data=json.loads(DATA.read_text());cases=[]
    for row in data['layouts']:
        assert row['cost']==len(row['walls'])==len({tuple(c) for c in row['walls']})
        assert all(len(c)==2 and all(type(x)==int for x in c) for c in row['walls'])
        for side in (0,1):
            bot=MazeGrower(layout=row['id'],growth_rounds=9);engine=Engine(balanced_config(),('a','b'))
            observed=[]
            for rnd in range(1,10):
                obs=engine.observation(side);saved=deepcopy(obs);actions=bot.decide(obs);assert obs==saved
                submissions=[[],[]];submissions[side]=actions;records=engine.play_round(submissions)
                assert all(e['accepted'] for r in records for e in r['event'] if e['kind']=='action')
                snap=engine.snapshot(side);expected=row['no_hit_growth'][rnd-1]
                assert snap['gold']==expected['gold'] and snap['n_factories']==expected['factories']
                assert snap['length_path']==row['length'] and snap['n_walls']==row['cost']
                assert snap['n_turrets']==0 and snap['hp']==800
                own=next(r for r in records if r['player']==side)
                income=next(e for e in own['event'] if e['kind']=='income')
                assert income['hits']==0 and income['path']==row['length'] and income['factories']==15*snap['n_factories']
                observed.append(dict(round=rnd,factories=snap['n_factories'],gold=snap['gold']))
            cases.append(dict(layout=row['id'],side=side,observed=observed))
    assert all(digest(p)==h for p,h in inputs.items())
    result=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,all_passed=True,input_sha256=inputs,cases=cases,scope='Every imported layout, both assignments, nine original-engine no-hit rounds. Exact wall legality, route length, affordability, income and input immutability. Full-game strength not tested here.')
    atomic_json(args.output,result,exclusive=True);print(json.dumps({k:result[k] for k in ('time_utc','runtime_seconds','all_passed')}))

if __name__=='__main__':main()
