"""Extend the pinned empty-map guard prefix until the next HP threshold."""
from datetime import datetime,timezone
from pathlib import Path
import argparse,hashlib,json,time
from td_game.config import balanced_config
from td_game.pathfinding import shortest_path
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();start=time.perf_counter()
    src=Path('bot_research/bots/counters/data/staged_guards_001.json');cfg=balanced_config();g=cfg.globals;digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    files=set(static_closure({'bot_research.experiments.validation.design_guard_ladder'}))|{src,Path('configs/balanced.json'),Path('td_game/balanced.json')};hashes={str(p):digest(p) for p in files}
    base=[r for r in json.loads(src.read_text())['layouts'] if r['layout']=='empty'];assert len(base)==1
    guards=[tuple(c) for c in base[0]['guards']];stages=list(base[0]['stages'])
    while stages[-1]['splash_exposure']<180:
        choices=[]
        for x in range(g.width):
            for y in range(g.height):
                cell=(x,y)
                if cell in guards or cell in (tuple(g.spawn),tuple(g.base)):continue
                route=shortest_path(g.width,g.height,set(guards)|{cell},g.spawn,g.base)
                if route is None:continue
                score=cfg.turrets['splash'].damage*sum(max(abs(a-u),abs(b-v))==1 for a,b in route[:-1] for u,v in guards+[cell])
                choices.append(dict(cell=[x,y],splash_exposure=score,path=[list(c) for c in route],length=len(route)-1))
        best=max(choices,key=lambda r:(r['splash_exposure'],r['length'],-r['cell'][0],-r['cell'][1]));assert best['splash_exposure']>stages[-1]['splash_exposure']
        guards.append(tuple(best['cell']));stages.append(dict(stage=len(guards),legal_choices=len(choices),**best));assert len(guards)<=20
    assert all(digest(p)==h for p,h in hashes.items())
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,input_sha256=hashes,layout='empty',guards=guards,stages=stages,scope='Existing first three guard cells retained. Further choices maximize one-step exposure, then route length, then lexicographic cell order. Not a globally optimal sequence.')
    atomic_json(a.output,out,exclusive=True);print(json.dumps(dict(guards=guards,exposures=[r['splash_exposure'] for r in stages],sha256=digest(a.output))))
if __name__=='__main__':main()
