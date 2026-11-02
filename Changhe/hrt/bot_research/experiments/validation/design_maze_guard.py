"""Select one legal non-wall splash cell for each declared wall layout."""
from datetime import datetime,timezone
from pathlib import Path
import argparse,hashlib,json,time
from td_game.pathfinding import shortest_path
from bot_research.experiments.validation.artifact_io import atomic_json


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);args=p.parse_args();start=time.perf_counter()
    source=Path('bot_research/bots/counters/data/maze_layouts_001.json');maps=json.loads(source.read_text())
    rows=[]
    for layout in maps['layouts']:
        if layout['id'] not in ('empty','lead_opening','cash_rank_1'):continue
        walls={tuple(c) for c in layout['walls']};choices=[]
        for x in range(12):
            for y in range(12):
                cell=(x,y)
                if cell in walls or cell in ((0,0),(11,11)):continue
                path=shortest_path(12,12,walls|{cell},(0,0),(11,11))
                if path is None:continue
                exposure=10*sum(max(abs(x-a),abs(y-b))==1 for a,b in path[:-1])
                choices.append(dict(cell=list(cell),splash_exposure=exposure,path=[list(c) for c in path],length=len(path)-1))
        best=max(choices,key=lambda r:(r['splash_exposure'],r['length'],-r['cell'][0],-r['cell'][1]))
        assert best['splash_exposure']>=20
        rows.append(dict(layout=layout['id'],legal_cells=len(choices),selected=best))
    result=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,layouts=rows,
        input_sha256={str(source):hashlib.sha256(source.read_bytes()).hexdigest(),str(Path(__file__).relative_to(Path.cwd())):hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
        scope='Exhaustive single-cell exposure search on three fixed wall maps. No full-game optimization.')
    atomic_json(args.output,result,exclusive=True)
    print(json.dumps([{k:v for k,v in row.items() if k!='selected'}|{k:v for k,v in row['selected'].items() if k!='path'} for row in rows]))

if __name__=='__main__':main()
