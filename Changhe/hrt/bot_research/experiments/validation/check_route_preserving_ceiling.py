"""Check the exact splash ceiling for the fixed corner-gun route."""
from copy import deepcopy
from dataclasses import asdict
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json,time
from td_game.actions import apply_action
from td_game.config import balanced_config
from td_game.engine import Engine
from td_game.combat import simulate_map
from td_game.state import PlayerState,RosterEntry
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure

def main():
    start=time.perf_counter();A=Path('bot_research/experiments/validation/analysis/route_preserving_defense')
    paths=set(static_closure({'bot_research.experiments.validation.check_route_preserving_ceiling','bot_research.bots.economy.frozen.v17.freeplan'}))|{A/'PROOF.md'}
    digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();hashes={str(p):digest(p) for p in paths}
    cfg=balanced_config();e=Engine(cfg,('ceiling','attacker'));state=e.players[0];state.gold=10000
    assert apply_action(state,dict(op='build_turret',type='gun1',x=10,y=1),1,cfg)['accepted']
    original=e.path(0);assert len(original)-1==22
    cells=[]
    for x in range(12):
        for y in range(12):
            if (x,y) in original or (x,y)==(10,1):continue
            exposure=sum(max(abs(x-u),abs(y-v))==1 for u,v in original[:-1])
            if exposure:cells.append(dict(x=x,y=y,adjacency=exposure))
    assert len(cells)==20 and sum(c['adjacency'] for c in cells)==56
    for c in cells:
        assert apply_action(state,dict(op='build_turret',type='splash',x=c['x'],y=c['y']),1,cfg)['accepted']
        assert e.path(0)==original
    reverse=sum(sum(max(abs(b.x-u),abs(b.y-v))==1 for b in state.buildings if b.type=='splash') for u,v in original[:-1])
    assert reverse==56
    cases=[]
    for tier,n in [('tier4',1)]+[('tier5',n) for n in (1,2,3,227,228,229)]:
        attacker=PlayerState('attacker',800,0,roster=[RosterEntry(i,tier,1,12) for i in range(n)])
        result=simulate_map(attacker,deepcopy(state),original,1,cfg)
        expect=0 if tier=='tier4' else min(n,228)*cfg.minions[tier].damage
        assert result.damage==expect
        if tier=='tier5':assert result.killed==0 and result.hits==min(n,228)
        cases.append(dict(tier=tier,n=n,combat=asdict(result)))
    assert all(digest(p)==h for p,h in hashes.items())
    now=datetime.now(timezone.utc).isoformat();receipt=A/'verification/ceiling.json'
    atomic_json(receipt,dict(time_utc=now,runtime_seconds=time.perf_counter()-start,all_passed=True,input_sha256=hashes,route=original,cells=cells,adjacency=56,splash_ceiling=560,cases=cases,scope='Exact fixed-gun, route-preserving splash bound. Other gun layouts and full-game outcomes are not bounded.'),exclusive=True)
    with (A/'RESULTS.md').open('x') as f:f.write(f'''# A route-preserving splash ceiling\n\nChecked {now}.\n\nCONFIRMED: with the fixed gun1 at (10,1), adding turrets only off the current route keeps the route at22 steps and caps splash exposure at560. The bound is attained by twenty splashes; every addition is legal on the unchanged engine. The proof covers all such placements, and the checker counts the56 contributing adjacencies in two orders.\n\nOn the maximizing splash map, tier4 is stopped, while a tier5 takes at most616 total damage and survives. Original combat confirms all incoming tier5 copies arrive for n=1,2,3,227,228, and the229th copy is cleared at the tick cutoff. No additional guns beyond the fixed corner gun are included in that combat statement.\n\nThe current budget defender never builds walls or blocks its current route, so this restriction explains why its splash coverage cannot reach tier5 immunity. It is not a proof that every defensive gun mixture loses. Evidence and exact input hashes: verification/ceiling.json.\n''')
    with Path('bot_research/notes/validation.md').open('a') as f:f.write(f'\n## {now}: Route-preserving defense has a 560-HP splash ceiling\n\nClaim and verdict: CONFIRMED under the fixed corner-gun and off-current-route construction hypotheses. The unchanged free_plan never builds walls or blocks its current route. From the round4 corner gun alone, route22 remains fixed; the twenty eligible splash cells contribute56 adjacencies, so exposure cannot exceed560. Original-engine placement checks and independent counting pass. On the all-splash maximizing map, tier5 copies survive, as proved and checked for seven combat cases. This does not bound other added-gun layouts or prove a full-game loss. Proof and receipt: experiments/validation/analysis/route_preserving_defense/.\n')
    print(json.dumps(dict(time_utc=now,all_passed=True,runtime=time.perf_counter()-start)))
if __name__=='__main__':main()
