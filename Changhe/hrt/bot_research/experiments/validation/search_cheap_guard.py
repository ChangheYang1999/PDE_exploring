"""Exhaustive one-turret, one-wall extensions of the two-splash fixture."""
from copy import deepcopy
from dataclasses import asdict
from datetime import datetime, timezone
from itertools import product
from pathlib import Path
import argparse
import hashlib
import json
import time
from td_game.actions import apply_action
from td_game.combat import simulate_map
from td_game.config import balanced_config
from td_game.pathfinding import shortest_path
from td_game.state import PlayerState, RosterEntry
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    started=time.perf_counter()
    paths=set(static_closure({'bot_research.experiments.validation.search_cheap_guard'})) | {Path('configs/balanced.json'),Path('td_game/balanced.json'),Path('bot_research/experiments/validation/analysis/cheap_guard_search/PROOF.md')}
    hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)}
    cfg=balanced_config()
    base_actions=[dict(op='build_turret',type='splash',x=10,y=1),
                  dict(op='build_turret',type='splash',x=1,y=0)]
    base=PlayerState('funded fixture',800,10000)
    assert all(apply_action(base,a,6,cfg)['accepted'] for a in base_actions)
    cells=[(x,y) for x in range(12) for y in range(12)
           if (x,y) not in ((10,1),(1,0),(0,0),(11,11))]
    turrets=[None]+[dict(op='build_turret',type=t,x=x,y=y)
                   for t in ('gun1','gun2','gun3','splash') for x,y in cells]
    walls=[None]+[dict(op='build_wall',x=x,y=y) for x,y in cells]
    threats={'t3x3':['tier1']*3+['tier3']*3,
             't3x6':['tier1']*3+['tier3']*6,
             't4x1':['tier1']*3+['tier4']}
    attackers={}
    for name,roster in threats.items():
        p=PlayerState('attacker',800,0)
        p.roster=[RosterEntry(i,t,6,17) for i,t in enumerate(roster)]
        attackers[name]=p
    best={name:None for name in threats}
    proposed=accepted=duplicate=0
    single_splashes=[]
    for turret,wall in product(turrets,walls):
        if turret and wall and (turret['x'],turret['y'])==(wall['x'],wall['y']):
            duplicate+=1
            continue
        acts=[a for a in (turret,wall) if a is not None]
        proposed+=1
        state=deepcopy(base)
        if not all(apply_action(state,a,6,cfg)['accepted'] for a in acts):continue
        accepted+=1
        path=shortest_path(12,12,((b.x,b.y) for b in state.buildings),(0,0),(11,11))
        assert path
        cost=base.gold-state.gold
        exposure=10*sum(b.type=='splash' and max(abs(x-b.x),abs(y-b.y))==1
                        for x,y in path[:-1] for b in state.buildings)
        key=json.dumps(acts,sort_keys=True,separators=(',',':'))
        if turret and turret['type']=='splash' and wall is None:
            single_splashes.append(dict(actions=acts,splash_exposure=exposure,path_length=len(path)))
        for name,attacker in attackers.items():
            old=best[name]
            if old is not None and (cost,key)>=(old['cost'],old['tie_key']):continue
            outcome=asdict(simulate_map(attacker,deepcopy(state),path,6,cfg))
            if outcome['damage']==0:
                best[name]=dict(actions=acts,cost=cost,tie_key=key,path=[list(c) for c in path],
                                splash_exposure=exposure,outcome=outcome)
    assert proposed+duplicate==len(turrets)*len(walls)
    assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==h for p,h in hashes.items())
    result=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-started,
        input_sha256=hashes,
        original_constructions=base_actions,funded_initial_gold=10000,round=6,threats=threats,
        candidate_counts=dict(cells=len(cells),turret_options=len(turrets),wall_options=len(walls),
                              duplicate_cells_excluded=duplicate,proposed=proposed,accepted=accepted),
        tie_break='Minimum (total cost, JSON action list with sorted keys and compact separators).',
        winners=best,single_splash_additions=single_splashes,
        maximum_single_splash_exposure=max(x['splash_exposure'] for x in single_splashes),
        scope='Exhaustive funded fixture search with at most one turret and one wall. No full-game strength or general minimum claim.')
    atomic_json(args.output,result,exclusive=True)
    print(json.dumps({k:result[k] for k in ('time_utc','runtime_seconds','candidate_counts','maximum_single_splash_exposure')}))
    print(json.dumps({k:None if v is None else dict(cost=v['cost'],actions=v['actions']) for k,v in best.items()}))

if __name__=='__main__':main()
