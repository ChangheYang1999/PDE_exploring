"""Check wall preparation against original snapshots and route geometry."""
from copy import deepcopy
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json,time
from td_game.actions import apply_action
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.walled_handoff import snapshot_after_builds
from bot_research.bots.defense.frozen.v7.plan import plan_walls
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure

def main():
    start=time.perf_counter();A=Path('bot_research/experiments/validation/analysis/handoff_wall_intervention')
    paths=set(static_closure({'bot_research.experiments.validation.check_handoff_wall_component'}))|{A/'PROOF.md'}
    digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();hashes={str(p):digest(p) for p in paths};cases=[]
    for mode,stage in [('stage_a',0),('full',None)]:
        cfg=balanced_config();e=Engine(cfg,('prepared','idle'));state=e.players[0];state.gold=10000
        assert apply_action(state,dict(op='build_turret',type='gun1',x=10,y=1),1,cfg)['accepted']
        obs=e.observation(0);original=deepcopy(obs);walls=plan_walls(obs,state.gold,stage=stage)
        assert obs==original
        for action in walls:assert apply_action(state,action,1,cfg)['accepted']
        rebuilt=snapshot_after_builds(obs['players'][0],state,cfg)
        assert rebuilt==e.snapshot(0)
        route=e.path(0);blocked={(b.x,b.y) for b in state.buildings};cells=[]
        for x in range(12):
            for y in range(12):
                if (x,y) in blocked or (x,y) in route:continue
                adj=sum(max(abs(x-u),abs(y-v))==1 for u,v in route[:-1])
                if adj:cells.append(dict(x=x,y=y,adjacency=adj))
        cases.append(dict(mode=mode,walls=walls,cost=len(walls)*cfg.wall_cost,route=route,route_length=len(route)-1,
            additional_splash_cells=cells,off_route_splash_ceiling=sum(c['adjacency'] for c in cells)*cfg.turrets['splash'].damage,
            original_snapshot_equal=True))
    assert all(digest(p)==h for p,h in hashes.items());now=datetime.now(timezone.utc).isoformat()
    atomic_json(A/'verification/component.json',dict(time_utc=now,runtime_seconds=time.perf_counter()-start,input_sha256=hashes,cases=cases,all_passed=True,scope='Wall legality, original-snapshot equality and fixed-route exposure only; not a strength test.'),exclusive=True)
    print(json.dumps(dict(time_utc=now,all_passed=True,cases=[{k:v for k,v in c.items() if k in ('mode','cost','route_length','off_route_splash_ceiling')} for c in cases])))
if __name__=='__main__':main()
