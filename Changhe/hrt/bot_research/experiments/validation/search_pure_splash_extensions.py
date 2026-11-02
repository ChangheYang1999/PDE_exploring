"""Enumerate zero, one and two additional splashes on the guard fixture."""
from copy import deepcopy
from datetime import datetime,timezone
from itertools import combinations
from pathlib import Path
import argparse,hashlib,json,time
from td_game.actions import apply_action
from td_game.config import balanced_config
from td_game.pathfinding import shortest_path
from td_game.state import PlayerState
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True);args=parser.parse_args()
    start=time.perf_counter();cfg=balanced_config();g=cfg.globals
    inputs=set(static_closure({'bot_research.experiments.validation.search_pure_splash_extensions'}))
    inputs.update(map(Path,('td_game/balanced.json','configs/balanced.json',
        'bot_research/experiments/validation/analysis/pure_splash_extensions/PROOF.md',
        'bot_research/bots/counters/data/guard_ladder_001.json')))
    digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    hashes={str(p):digest(p) for p in sorted(inputs)}
    ladder=json.loads(Path('bot_research/bots/counters/data/guard_ladder_001.json').read_text())
    original=[dict(op='build_turret',type='splash',x=x,y=y) for x,y in ladder['guards'][:2]]
    base=PlayerState('funded splash fixture',g.initial_hp,10000)
    assert all(apply_action(base,a,6,cfg)['accepted'] for a in original)
    occupied={(b.x,b.y) for b in base.buildings}|{g.spawn,g.base}
    available=[(x,y) for x in range(g.width) for y in range(g.height) if (x,y) not in occupied]
    def evaluate(cells):
        state=deepcopy(base)
        actions=[dict(op='build_turret',type='splash',x=x,y=y) for x,y in cells]
        if not all(apply_action(state,a,6,cfg)['accepted'] for a in actions):
            return dict(cells=cells,accepted=False)
        path=shortest_path(g.width,g.height,((b.x,b.y) for b in state.buildings),g.spawn,g.base)
        damage=sum(cfg.turrets[b.type].damage for x,y in path[:-1] for b in state.buildings
                   if max(abs(x-b.x),abs(y-b.y))==1)
        return dict(cells=cells,accepted=True,exposure=damage,path=path)
    rows=[];maximum={}
    for k in range(3):
        group=[evaluate(cells) for cells in combinations(available,k)]
        rows.extend(group)
        legal=[r for r in group if r['accepted']]
        best=max(legal,key=lambda r:r['exposure'])
        maximum[str(k)]=dict(proposed=len(group),accepted=len(legal),exposure=best['exposure'],cells=best['cells'])
    witness=evaluate(ladder['guards'][2:]);assert len(witness['cells'])==3 and witness['accepted']
    threshold=cfg.minions['tier3'].hp
    minimum=next((int(k) for k,m in maximum.items() if m['exposure']>=threshold),None)
    if minimum is None and witness['exposure']>=threshold:minimum=3
    assert minimum is not None
    assert all(digest(p)==h for p,h in hashes.items())
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,
        input_sha256=hashes,round=6,funded_initial_gold=10000,original_constructions=original,
        available_cells=available,rows=rows,maximum_by_count=maximum,three_splash_witness=witness,
        tier3_hp=threshold,minimum_additions=minimum,minimum_cost=minimum*cfg.turrets['splash'].cost,
        scope='Fixed pure-splash fixture only. Exhaustive sizes zero through two, and a size-three witness.')
    atomic_json(args.output,out,exclusive=True)
    print(json.dumps({k:out[k] for k in ('time_utc','runtime_seconds','maximum_by_count','minimum_additions','minimum_cost')}))

if __name__=='__main__':main()
