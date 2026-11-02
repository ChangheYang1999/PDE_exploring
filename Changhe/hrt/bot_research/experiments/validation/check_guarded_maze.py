"""Original-engine checks of delayed guard construction and dense tier1 attacks."""
from copy import deepcopy
from datetime import datetime,timezone
from pathlib import Path
import argparse,hashlib,json,time
from td_game.actions import apply_action
from td_game.config import balanced_config
from td_game.engine import Engine
from td_game.combat import simulate_map
from td_game.state import PlayerState,RosterEntry
from bot_research.bots.counters.guarded_maze import GuardedMaze,GUARD_DATA,GUARD_SHA256
from bot_research.bots.counters.maze_grower import DATA
from bot_research.experiments.validation.source_closure import static_closure
from bot_research.experiments.validation.artifact_io import atomic_json


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);args=p.parse_args();start=time.perf_counter()
    digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    paths=set(static_closure({'bot_research.experiments.validation.check_guarded_maze'}))|{DATA.relative_to(Path.cwd()),GUARD_DATA.relative_to(Path.cwd()),Path('td_game/balanced.json'),Path('configs/balanced.json')}
    inputs={str(p):digest(p) for p in paths};assert digest(GUARD_DATA)==GUARD_SHA256
    data=json.loads(GUARD_DATA.read_text());cases=[];config=balanced_config()
    for row in data['layouts']:
      for guard_round in (3,4):
       for side in (0,1):
        bot=GuardedMaze(layout=row['layout'],growth_rounds=6,guard_round=guard_round)
        engine=Engine(config,('a','b'))
        for rnd in range(1,7):
            obs=engine.observation(side);before=deepcopy(obs);actions=bot.decide(obs);assert obs==before
            pair=[[],[]];pair[side]=actions;records=engine.play_round(pair)
            assert all(e['accepted'] for r in records for e in r['event'] if e['kind']=='action')
            if rnd==guard_round:
                assert actions[0]==dict(op='build_turret',type='splash',x=row['selected']['cell'][0],y=row['selected']['cell'][1])
            if rnd>=guard_round:
                assert engine.snapshot(side)['n_turrets']==1
                assert engine.path(side)==[tuple(c) for c in row['selected']['path']]
        defender=deepcopy(engine.players[side]);path=engine.path(side)
        x,y=row['selected']['cell'];exposure=10*sum(max(abs(x-a),abs(y-b))==1 for a,b in path[:-1])
        assert exposure==row['selected']['splash_exposure'] and exposure>=20
        combats=[]
        for kind,count in [('tier1',1),('tier1',6),('tier1',249),('tier1',250),('tier1',251),('tier1',500),('tier2',1)]:
            attacker=PlayerState('attack',800,0,roster=[RosterEntry(i,kind,1,12) for i in range(count)])
            target=deepcopy(defender);result=simulate_map(attacker,target,path,6,config)
            if kind=='tier1':assert result.hits==result.damage==0 and target.hp==defender.hp
            combats.append(dict(kind=kind,count=count,hits=result.hits,damage=result.damage,killed=result.killed,cleared=result.cleared))
        cases.append(dict(layout=row['layout'],guard_round=guard_round,side=side,exposure=exposure,combats=combats))
    assert all(digest(p)==h for p,h in inputs.items())
    result=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,all_passed=True,cases=cases,input_sha256=inputs,scope='Twelve six-round original-engine prefixes and 84 original combats; tier1 counts through500 include the spawn-wrap boundary. Full-game strength remains separate.')
    atomic_json(args.output,result,exclusive=True);print(json.dumps({k:result[k] for k in ('time_utc','runtime_seconds','all_passed')}))

if __name__=='__main__':main()
