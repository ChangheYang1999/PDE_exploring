"""Check legal guard prefixes, exact combat thresholds and scheduled policy actions."""
from copy import deepcopy
from dataclasses import asdict
from datetime import datetime,timezone
from pathlib import Path
import argparse,hashlib,json,time
from td_game.actions import apply_action
from td_game.combat import simulate_map
from td_game.config import balanced_config
from td_game.engine import Engine
from td_game.pathfinding import shortest_path
from td_game.state import PlayerState,RosterEntry
from bot_research.bots.counters.staged_guard_maze import StagedGuardMaze,DATA,DATA_SHA256
from bot_research.bots.counters.maze_grower import DATA as WALLS
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);args=p.parse_args();start=time.perf_counter()
    digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    paths=set(static_closure({'bot_research.experiments.validation.check_staged_guards'}))|{DATA.relative_to(Path.cwd()),WALLS.relative_to(Path.cwd()),Path('td_game/balanced.json'),Path('configs/balanced.json')}
    inputs={str(p):digest(p) for p in paths};assert digest(DATA)==DATA_SHA256
    cfg=balanced_config();rows=json.loads(DATA.read_text())['layouts'];walls={r['id']:r['walls'] for r in json.loads(WALLS.read_text())['layouts']};cases=[];prefixes=[]
    for row in rows:
        defender=PlayerState('component defender',800,100000)
        for x,y in walls[row['layout']]:assert apply_action(defender,dict(op='build_wall',x=x,y=y),1,cfg)['accepted']
        previous=0
        for i,stage in enumerate(row['stages']):
            x,y=stage['cell'];assert apply_action(defender,dict(op='build_turret',type='splash',x=x,y=y),1,cfg)['accepted']
            path=shortest_path(cfg.globals.width,cfg.globals.height,[(b.x,b.y) for b in defender.buildings],cfg.globals.spawn,cfg.globals.base)
            assert path==[tuple(c) for c in stage['path']]
            exposure=10*sum(max(abs(a-x),abs(b-y))==1 for a,b in path[:-1] for x,y in row['guards'][:i+1])
            assert exposure==stage['splash_exposure'] and exposure>=previous;previous=exposure
            for kind in cfg.minions:
                for n in (1,251):
                    attacker=PlayerState('component attacker',800,0,roster=[RosterEntry(k,kind,1,None) for k in range(n)])
                    expected=sum(k%250+len(path)-1<250 for k in range(n)) if cfg.minions[kind].hp>exposure else 0
                    result=simulate_map(attacker,deepcopy(defender),path,1,cfg)
                    assert result.hits==expected and result.damage==expected*cfg.minions[kind].damage
                    cases.append(dict(layout=row['layout'],stage=i+1,kind=kind,count=n,exposure=exposure,expected_hits=expected,original=asdict(result)))
        for schedule in ((4,6),(4,6,8),(3,5)):
            for side in (0,1):
                bot=StagedGuardMaze(layout=row['layout'],growth_rounds=12,guard_rounds=schedule);engine=Engine(cfg,('a','b'))
                rounds=[]
                for rnd in range(1,10):
                    obs=engine.observation(side);original=deepcopy(obs);actions=bot.decide(obs);assert obs==original
                    pair=[[],[]];pair[side]=actions;records=engine.play_round(pair)
                    assert all(e['accepted'] for record in records for e in record['event'] if e['kind']=='action')
                    count=sum(t<=rnd for t in schedule);assert engine.snapshot(side)['n_turrets']==count
                    if count:assert engine.path(side)==[tuple(c) for c in row['stages'][count-1]['path']]
                    rounds.append(dict(round=rnd,n_turrets=count,gold=engine.players[side].gold))
                prefixes.append(dict(layout=row['layout'],guard_rounds=schedule,side=side,rounds=rounds))
    assert len(cases)==90 and len(prefixes)==18 and all(digest(p)==h for p,h in inputs.items())
    output=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,all_passed=True,input_sha256=inputs,combats=cases,prefixes=prefixes,scope='Ninety original combats on nine legal guard prefixes, plus eighteen nine-round policy executions. Scheduled prefixes use growth12 to isolate construction. No full-game advantage is inferred.')
    atomic_json(args.output,output,exclusive=True);print(json.dumps({k:output[k] for k in ('time_utc','runtime_seconds','all_passed')}))

if __name__=='__main__':main()
