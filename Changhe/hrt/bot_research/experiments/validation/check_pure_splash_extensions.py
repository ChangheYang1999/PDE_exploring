"""Independently check every listed pure-splash map and original combat."""
from copy import deepcopy
from dataclasses import asdict
from datetime import datetime,timezone
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
    p=argparse.ArgumentParser();p.add_argument('--data',required=True);p.add_argument('--output',required=True);a=p.parse_args()
    start=time.perf_counter();file=Path(a.data);assert not file.is_absolute() and '..' not in file.parts
    digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    data=json.loads(file.read_text());hashes=dict(data['input_sha256']);hashes[str(file)]=digest(file)
    for source in static_closure({'bot_research.experiments.validation.check_pure_splash_extensions'}):
        if str(source) in hashes:assert hashes[str(source)]==digest(source)
        hashes[str(source)]=digest(source)
    assert all(digest(p)==h for p,h in hashes.items())
    cfg=balanced_config();g=cfg.globals
    base=PlayerState('independent fixture',g.initial_hp,data['funded_initial_gold'])
    assert all(apply_action(base,act,data['round'],cfg)['accepted'] for act in data['original_constructions'])
    available={(x,y) for x in range(g.width) for y in range(g.height)}-{g.spawn,g.base}-{(b.x,b.y) for b in base.buildings}
    assert available=={tuple(c) for c in data['available_cells']}
    expected=set().union(*(set(combinations(sorted(available),k)) for k in range(3)))
    seen=set();maxima={k:-1 for k in range(3)};counts={k:[0,0] for k in range(3)}
    attacker=PlayerState('one tier3',g.initial_hp,0)
    attacker.roster=[RosterEntry(0,'tier3',data['round'],data['round']+g.roster_lifespan-1)]
    legal=rejected=0
    def check(row):
        state=deepcopy(base);accepted=True
        for x,y in reversed(row['cells']):
            accepted=bool(apply_action(state,dict(op='build_turret',type='splash',x=x,y=y),data['round'],cfg)['accepted'])
            if not accepted:break
        assert accepted==row['accepted']
        if not accepted:return None
        path=shortest_path(g.width,g.height,{(b.x,b.y) for b in state.buildings},g.spawn,g.base)
        assert [list(c) for c in path]==row['path']
        exposure=sum(cfg.turrets[b.type].damage*sum(
            abs(x-b.x)<=1 and abs(y-b.y)<=1 and (x,y)!=(b.x,b.y) for x,y in path[:-1])
            for b in state.buildings)
        assert exposure==row['exposure']
        totals=asdict(simulate_map(attacker,deepcopy(state),path,data['round'],cfg))
        assert totals['spawned']==1 and totals['cleared']==0
        assert totals['hits']==int(exposure<cfg.minions['tier3'].hp)
        assert totals['damage']==totals['hits']*cfg.minions['tier3'].damage
        return exposure
    for row in data['rows']:
        key=tuple(sorted(tuple(c) for c in row['cells']));assert key in expected and key not in seen
        seen.add(key);counts[len(key)][0]+=1
        value=check(row)
        if value is None:rejected+=1
        else:
            legal+=1;counts[len(key)][1]+=1;maxima[len(key)]=max(maxima[len(key)],value)
    assert seen==expected
    for k in range(3):
        assert maxima[k]==data['maximum_by_count'][str(k)]['exposure']
        assert counts[k]==[data['maximum_by_count'][str(k)]['proposed'],data['maximum_by_count'][str(k)]['accepted']]
    witness=check(data['three_splash_witness']);assert witness is not None
    smallest=next((k for k in range(3) if maxima[k]>=cfg.minions['tier3'].hp),None)
    if smallest is None and witness>=cfg.minions['tier3'].hp:smallest=3
    assert smallest==data['minimum_additions'] and data['minimum_cost']==smallest*cfg.turrets['splash'].cost
    assert all(digest(p)==h for p,h in hashes.items())
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,
        input_sha256=hashes,all_passed=True,listed_candidates=len(seen),legal=legal,rejected=rejected,
        original_combat_checks=legal+1,maximum_by_count=maxima,three_splash_exposure=witness,
        minimum_additions=smallest,minimum_cost=data['minimum_cost'],
        scope='All listed maps independently reconstructed in reverse construction order. Coverage checked against every size-zero-to-two subset. Original one-tier3 combat checks the exposure criterion on every accepted map and the size-three witness.')
    atomic_json(a.output,out,exclusive=True)
    print(json.dumps({k:v for k,v in out.items() if k!='input_sha256'}))

if __name__=='__main__':main()
