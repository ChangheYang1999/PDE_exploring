"""Independent replay of cheap-search witnesses and exhaustive single splashes."""
from copy import deepcopy
from dataclasses import asdict
from datetime import datetime,timezone
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
    parser=argparse.ArgumentParser();parser.add_argument('--data',required=True);parser.add_argument('--output',required=True)
    args=parser.parse_args();start=time.perf_counter();file=Path(args.data)
    assert not file.is_absolute() and '..' not in file.parts
    digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    data=json.loads(file.read_text());hashes=dict(data['input_sha256']);hashes[str(file)]=digest(file)
    for p in static_closure({'bot_research.experiments.validation.check_cheap_guard'}):
        if str(p) in hashes:assert hashes[str(p)]==digest(p)
        hashes[str(p)]=digest(p)
    cfg=balanced_config();base=PlayerState('checker fixture',800,data['funded_initial_gold'])
    assert all(apply_action(base,a,data['round'],cfg)['accepted'] for a in data['original_constructions'])
    checked=[]
    for name,w in data['winners'].items():
        assert w is not None
        state=deepcopy(base)
        assert all(apply_action(state,a,data['round'],cfg)['accepted'] for a in w['actions'])
        assert base.gold-state.gold==w['cost']
        route=shortest_path(cfg.globals.width,cfg.globals.height,((b.x,b.y) for b in state.buildings),cfg.globals.spawn,cfg.globals.base)
        assert [list(x) for x in route]==w['path']
        attacker=PlayerState('checker attacker',800,0)
        attacker.roster=[RosterEntry(i,t,data['round'],data['round']+cfg.globals.roster_lifespan-1) for i,t in enumerate(data['threats'][name])]
        actual=asdict(simulate_map(attacker,state,route,data['round'],cfg))
        assert actual==w['outcome'] and actual['damage']==0
        checked.append(dict(roster=name,cost=w['cost'],actions=w['actions'],outcome=actual))
    singles=[]
    for x in range(cfg.globals.width):
        for y in range(cfg.globals.height):
            action=dict(op='build_turret',type='splash',x=x,y=y);state=deepcopy(base)
            if not apply_action(state,action,data['round'],cfg)['accepted']:continue
            route=shortest_path(cfg.globals.width,cfg.globals.height,((b.x,b.y) for b in state.buildings),cfg.globals.spawn,cfg.globals.base)
            exposure=0
            for cell in route[:-1]:
                for b in state.buildings:
                    if b.type=='splash' and abs(cell[0]-b.x)<=1 and abs(cell[1]-b.y)<=1 and cell!=(b.x,b.y):
                        exposure+=cfg.turrets['splash'].damage
            singles.append(dict(actions=[action],splash_exposure=exposure,path_length=len(route)))
    assert singles==data['single_splash_additions']
    assert max(x['splash_exposure'] for x in singles)==data['maximum_single_splash_exposure']
    assert all(digest(p)==h for p,h in hashes.items())
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,
        input_sha256=hashes,all_passed=True,winning_witnesses=checked,single_splashes_checked=len(singles),
        maximum_single_splash_exposure=data['maximum_single_splash_exposure'],
        scope='Independent original-engine feasibility of retained witnesses and exhaustive one-splash exposure check. '
              'Minimal costs additionally rely on the separately reviewed full enumerator, not on these witnesses alone.')
    atomic_json(args.output,out,exclusive=True)
    print(json.dumps({k:out[k] for k in ('time_utc','runtime_seconds','all_passed','single_splashes_checked','maximum_single_splash_exposure')}))

if __name__=='__main__':main()
