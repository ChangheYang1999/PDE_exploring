"""Greedy legal splash sequences on the three fixed development wall maps."""
from datetime import datetime,timezone
from pathlib import Path
import argparse,hashlib,json,time
from td_game.config import balanced_config
from td_game.pathfinding import shortest_path
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True);args=parser.parse_args()
    start=time.perf_counter();cfg=balanced_config();g=cfg.globals
    source=Path('bot_research/bots/counters/data/maze_layouts_001.json')
    paths=set(static_closure({'bot_research.experiments.validation.design_staged_guards'}))|{source,Path('td_game/balanced.json'),Path('configs/balanced.json')}
    digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();inputs={str(p):digest(p) for p in paths}
    rows=[]
    for layout in json.loads(source.read_text())['layouts']:
        if layout['id'] not in ('empty','lead_opening','cash_rank_1'):continue
        walls={tuple(c) for c in layout['walls']};guards=[];stages=[];previous=0
        for stage in range(1,4):
            blocked=walls|set(guards);choices=[]
            for x in range(g.width):
                for y in range(g.height):
                    cell=(x,y)
                    if cell in blocked or cell in (tuple(g.spawn),tuple(g.base)):continue
                    route=shortest_path(g.width,g.height,blocked|{cell},g.spawn,g.base)
                    if route is None:continue
                    splashes=guards+[cell]
                    score=cfg.turrets['splash'].damage*sum(max(abs(a-x0),abs(b-y0))==1 for a,b in route[:-1] for x0,y0 in splashes)
                    choices.append(dict(cell=[x,y],splash_exposure=score,path=[list(c) for c in route],length=len(route)-1))
            best=max(choices,key=lambda r:(r['splash_exposure'],r['length'],-r['cell'][0],-r['cell'][1]))
            assert best['splash_exposure']>=previous
            guards.append(tuple(best['cell']));previous=best['splash_exposure']
            stages.append(dict(stage=stage,legal_choices=len(choices),**best))
        rows.append(dict(layout=layout['id'],guards=[list(c) for c in guards],stages=stages))
    assert all(digest(p)==h for p,h in inputs.items())
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,input_sha256=inputs,layouts=rows,scope='Three greedy steps, exhaustive legal-cell choice at each fixed prefix. Not a globally optimal sequence.')
    atomic_json(args.output,out,exclusive=True)
    print(json.dumps([dict(layout=r['layout'],guards=r['guards'],scores=[s['splash_exposure'] for s in r['stages']]) for r in rows]))


if __name__=='__main__':main()
