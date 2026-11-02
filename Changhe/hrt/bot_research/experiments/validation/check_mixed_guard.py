"""Check the selected porous guard through legal actions and original combat."""
from copy import deepcopy
from dataclasses import asdict
from datetime import datetime,timezone
from fractions import Fraction
from pathlib import Path
import argparse,hashlib,json,time
from td_game.actions import apply_action
from td_game.combat import simulate_map
from td_game.config import balanced_config
from td_game.engine import Engine
from td_game.pathfinding import shortest_path
from td_game.state import PlayerState,RosterEntry
from bot_research.bots.counters.mixed_guard_maze import MixedGuardMaze,DATA,DATA_SHA256
from bot_research.bots.counters.staged_guard_maze import DATA as GUARDS
from bot_research.bots.counters.maze_grower import DATA as WALLS
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();start=time.perf_counter()
 digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
 paths=set(static_closure({'bot_research.experiments.validation.check_mixed_guard'}))|{f.relative_to(Path.cwd()) for f in (DATA,GUARDS,WALLS)}|{Path('td_game/balanced.json'),Path('configs/balanced.json')}
 hashes={str(p):digest(p) for p in paths};assert digest(DATA)==DATA_SHA256;cfg=balanced_config();w=json.loads(DATA.read_text())['witnesses'][0]
 splashes=next(r for r in json.loads(GUARDS.read_text())['layouts'] if r['layout']=='empty')['guards'][:2]
 state=PlayerState('component defender',800,10000)
 actions=[dict(op='build_turret',type='splash',x=x,y=y) for x,y in splashes]+w['extra_actions']
 for action in actions:assert apply_action(state,action,1,cfg)['accepted']
 path=shortest_path(cfg.globals.width,cfg.globals.height,[(b.x,b.y) for b in state.buildings],cfg.globals.spawn,cfg.globals.base);assert path==[tuple(c) for c in w['path']]
 combats=[];by={}
 for n in (1,2,3,10,60,251):
  for kind in cfg.minions:
   attacker=PlayerState('component attacker',800,0,roster=[RosterEntry(k,kind,1,None) for k in range(n)])
   r=simulate_map(attacker,deepcopy(state),path,1,cfg);by[n,kind]=r;combats.append(dict(count=n,kind=kind,original=asdict(r)))
 assert by[1,'tier3'].hits==0 and by[60,'tier3'].hits>0
 for kind in ('tier3','tier4','tier5'):assert asdict(by[60,kind])==w['swarm'][kind]
 rank=sorted(('tier3','tier4','tier5'),key=lambda t:(Fraction(by[60,t].damage,60*cfg.minions[t].cost),t),reverse=True);assert rank==w['rank'] and 'tier3' in rank[:2]
 prefixes=[]
 for late in (9,10):
  for side in (0,1):
   policy=MixedGuardMaze(growth_rounds=12,upgrade_round=late);engine=Engine(cfg,('a','b'))
   for rnd in range(1,12):
    obs=engine.observation(side);copy=deepcopy(obs);acts=policy.decide(obs);assert obs==copy;pair=[[],[]];pair[side]=acts;records=engine.play_round(pair)
    assert all(e['accepted'] for r in records for e in r['event'] if e['kind']=='action')
    count=(rnd>=4)+(rnd>=6)+2*(rnd>=late);assert engine.snapshot(side)['n_turrets']==count
    if rnd>=late:assert engine.path(side)==path
   prefixes.append(dict(upgrade_round=late,side=side,rounds=11))
 assert all(digest(p)==h for p,h in hashes.items())
 out=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,all_passed=True,input_sha256=hashes,combats=combats,prefixes=prefixes,rank=rank,scope='Thirty original combats and four eleven-round construction prefixes. No full-game conclusion.')
 atomic_json(a.output,out,exclusive=True);print(json.dumps({k:out[k] for k in ('time_utc','runtime_seconds','all_passed')}))

if __name__=='__main__':main()
