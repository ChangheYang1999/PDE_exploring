"""Independent exact obstruction search for finite turret-range forests."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import time


def members(mask):
    while mask:
        bit=mask & -mask
        yield bit.bit_length()-1
        mask^=bit


def graph(cells):
    index={cell:i for i,cell in enumerate(cells)}
    return [sum(1<<index[p] for p in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)) if p in index)
            for x,y in cells]


def obstruction(mask,neighbors):
    degrees={v:(neighbors[v]&mask).bit_count() for v in members(mask)}
    high=[v for v,d in degrees.items() if d>=3]
    if high:
        v=max(high,key=lambda x:(degrees[x],sum(degrees[y] for y in members(neighbors[x]&mask))))
        chosen=sorted(members(neighbors[v]&mask),key=lambda x:degrees[x],reverse=True)[:3]
        return sorted([v,*chosen],key=lambda x:degrees[x],reverse=True)
    unseen=mask
    while unseen:
        first=(unseen & -unseen).bit_length()-1
        component=[]
        pending=[first]
        unseen^=1<<first
        while pending:
            v=pending.pop()
            component.append(v)
            fresh=neighbors[v]&unseen
            unseen^=fresh
            pending.extend(members(fresh))
        if len(component)>=3 and all(degrees[v]==2 for v in component):
            return component
    return None


def verify_forest(mask,neighbors):
    # Independent witness check via degrees and edge counts per component.
    if any((neighbors[v]&mask).bit_count()>2 for v in members(mask)):
        return False
    unseen=set(members(mask))
    while unseen:
        root=unseen.pop()
        pending=[root]
        vertices=0
        degrees=0
        while pending:
            v=pending.pop()
            vertices+=1
            adjacent=set(members(neighbors[v]&mask))
            degrees+=len(adjacent)
            fresh=adjacent&unseen
            unseen-=fresh
            pending.extend(fresh)
        if degrees!=2*(vertices-1):
            return False
    return True


def solve(cells,seconds):
    neighbors=graph(cells)
    full=(1<<len(cells))-1
    greedy=full
    while (bad:=obstruction(greedy,neighbors)) is not None:
        greedy^=1<<bad[0]
    best=greedy
    visited=set()
    nodes=0
    pruned=0
    started=time.perf_counter()
    def search(mask):
        nonlocal best,nodes,pruned
        nodes+=1
        if nodes%1024==0 and time.perf_counter()-started>seconds:
            raise TimeoutError('Exact search time budget exhausted.')
        if mask.bit_count()<=best.bit_count() or mask in visited:
            pruned+=1
            return
        visited.add(mask)
        bad=obstruction(mask,neighbors)
        if bad is None:
            best=mask
            return
        for v in bad:
            search(mask^(1<<v))
    complete=True
    try:
        search(full)
    except TimeoutError:
        complete=False
    assert verify_forest(best,neighbors)
    return {'complete':complete,'maximum' if complete else 'lower_bound':best.bit_count(),
            'cells':[list(p) for p in cells],
            'witness':[list(cells[v]) for v in members(best)],
            'witness_checked':True,'nodes':nodes,'memoized_subsets':len(visited),
            'pruned':pruned,'runtime_seconds':time.perf_counter()-started}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--radius-squared-times-four',nargs='+',type=int,default=[25,36,49])
    parser.add_argument('--seconds-per-case',type=float,default=100)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    result={'started_utc':datetime.now(timezone.utc).isoformat(),
            'method':'Exact degree/cycle obstruction deletion search, integer arithmetic.',
            'implementation_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'cases':[]}
    for radius in args.radius_squared_times_four:
        extent=0
        while 4*extent*extent<radius:
            extent+=1
        cells=sorted((x,y) for x in range(-extent,extent+1) for y in range(-extent,extent+1)
                     if 0<4*(x*x+y*y)<=radius)
        row=solve(cells,args.seconds_per_case)
        row['radius_squared_times_four']=radius
        result['cases'].append(row)
        print(json.dumps({k:v for k,v in row.items() if k not in ('cells','witness')}),flush=True)
    result['finished_utc']=datetime.now(timezone.utc).isoformat()
    with Path(args.output).open('x') as output:
        json.dump(result,output,sort_keys=True,indent=2)
        output.write('\n')
    assert all(row['complete'] for row in result['cases'])


if __name__=='__main__':
    main()
