"""Find a low-cost porous guard using exact original one- and sixty-copy combats."""
from copy import deepcopy
from dataclasses import asdict
from datetime import datetime,timezone
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import argparse,hashlib,json,time
from td_game.actions import apply_action
from td_game.combat import simulate_map
from td_game.config import balanced_config
from td_game.pathfinding import shortest_path
from td_game.state import PlayerState,RosterEntry
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();start=time.perf_counter()
    source=Path('bot_research/bots/counters/data/staged_guards_001.json');cfg=balanced_config();g=cfg.globals
    digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    files=set(static_closure({'bot_research.experiments.validation.search_mixed_guard'}))|{source,Path('configs/balanced.json'),Path('td_game/balanced.json')};hashes={str(p):digest(p) for p in files}
    guards=[tuple(c) for c in next(r for r in json.loads(source.read_text())['layouts'] if r['layout']=='empty')['guards']]
    attackers={}
    for n in (1,60):
        for tier in ('tier3','tier4','tier5'):
            attackers[(n,tier)]=PlayerState('component attacker',800,0,roster=[RosterEntry(k,tier,1,None) for k in range(n)])
    families=[]
    for prefix in (2,3):
        for kind in ('gun1','gun2','gun3'):
            families.append((60*(prefix-2)+cfg.turrets[kind].cost,prefix,kind,1))
        families.append((60*(prefix-2)+2*cfg.turrets['gun1'].cost,prefix,'gun1',2))
    tested=0;filtered=0;legal=0;witnesses=[];completed=[]
    for cost,prefix,kind,count in sorted(families):
        defender=PlayerState('component defender',800,100000)
        for x,y in guards[:prefix]:assert apply_action(defender,dict(op='build_turret',type='splash',x=x,y=y),1,cfg)['accepted']
        cells=[(x,y) for x in range(g.width) for y in range(g.height) if (x,y) not in guards[:prefix] and (x,y) not in (tuple(g.spawn),tuple(g.base))]
        family_count=0
        for points in combinations(cells,count):
            tested+=1;family_count+=1;state=deepcopy(defender)
            actions=[dict(op='build_turret',type=kind,x=x,y=y) for x,y in points]
            if not all(apply_action(state,action,1,cfg)['accepted'] for action in actions):continue
            legal+=1;path=shortest_path(g.width,g.height,[(b.x,b.y) for b in state.buildings],g.spawn,g.base)
            splash=10*sum(max(abs(x-u),abs(y-v))==1 for x,y in path[:-1] for u,v in guards[:prefix])
            lone_damage=splash+sum(cfg.turrets[kind].damage*sum((x-u)**2+(y-v)**2<=cfg.turrets[kind].range**2 for x,y in path[:-1]) for u,v in points)
            if splash>=180 or lone_damage<180:continue
            filtered+=1
            lone=simulate_map(attackers[(1,'tier3')],deepcopy(state),path,1,cfg)
            if lone.hits:continue
            swarm={tier:simulate_map(attackers[(60,tier)],deepcopy(state),path,1,cfg) for tier in ('tier3','tier4','tier5')}
            rank=sorted(swarm,key=lambda tier:(Fraction(swarm[tier].damage,60*cfg.minions[tier].cost),tier),reverse=True)
            if not swarm['tier3'].hits or 'tier3' not in rank[:2]:continue
            extra=([dict(op='build_turret',type='splash',x=guards[2][0],y=guards[2][1])] if prefix==3 else [])+actions
            witnesses.append(dict(additional_cost=cost,splash_prefix=prefix,extra_actions=extra,path=[list(c) for c in path],splash_exposure=splash,lone_potential_damage=lone_damage,lone_tier3=asdict(lone),swarm={t:asdict(r) for t,r in swarm.items()},rank=rank))
            print(json.dumps(dict(time_utc=datetime.now(timezone.utc).isoformat(),cost=cost,tested=tested,witness=witnesses[-1])),flush=True)
            break
        completed.append(dict(additional_cost=cost,splash_prefix=prefix,kind=kind,count=count,examined=family_count,exhausted=not witnesses))
        if witnesses:break
    assert all(digest(p)==h for p,h in hashes.items())
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,input_sha256=hashes,tested=tested,legal=legal,passed_analytic_filter=filtered,families=completed,witnesses=witnesses,scope='Original one-copy and homogeneous sixty-copy combat tests. Search stops at the first witness in the declared cost-ordered finite family. Not a full-game result or arbitrary-map optimum.')
    atomic_json(a.output,out,exclusive=True);print(json.dumps({k:out[k] for k in ('time_utc','runtime_seconds','tested')}),flush=True)

if __name__=='__main__':main()
