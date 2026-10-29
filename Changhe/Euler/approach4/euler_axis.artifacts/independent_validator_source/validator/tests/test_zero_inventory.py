#!/usr/bin/env python3
import json,time
from pathlib import Path
import numpy as np
from independent_fields import ScalarExpansion,PotentialField
from ring_seed_certificate import load_exact
from ring_seed_field import RingSeedField
from zero_inventory import inventory
from independent_artifacts import atomic_json
ROOT=Path(__file__).resolve().parents[1]
def main():
    start=time.perf_counter();rows=[]
    def run(name,f,want,R):
        out=inventory(f,radius=R,nradial=65,nangle=81,max_starts=32)
        for key,value in want.items():
            if out['counts'][key]!=value:raise AssertionError((name,key,out['counts'],want))
        if abs(out['boundary_winding']-out['reflected_index_sum'])>1e-8:raise AssertionError((name,'degree mismatch'))
        rows.append(dict(name=name,result=out))
    def field(c,p,q=()):return PotentialField(ScalarExpansion(p),ScalarExpansion(q),c)
    run('linear P',field(.6,[(.5,0,1,0)],[(1,0,0,0)]),dict(P=1,A=0,B=0,O=0,D=0),3.)
    run('linear B',field(.6,[(1.4,0,1,0)]),dict(P=0,A=0,B=1,O=0,D=0),3.)
    run('three axis zeros',field(.74,[(-.87,0,1,0),(.5,0,3,0)],[(1,0,2,0)]),dict(P=2,A=1,B=0,O=0,D=0),3.)
    c=.6;nu=(1+c)/2
    run('local ring polynomial has extra zeros',field(c,[(c+nu,0,1,0),(-nu,1,1,0),(4*nu/3,0,3,0)],[(1,1,1,0)]),dict(P=0,A=0,B=1,O=1,D=2),3.)
    data=load_exact(ROOT.parent/'research/decaying_ring_seed/data/lead_ring_t2_params.json')
    for i in [0,6,14,23]:
        run(f'decaying certified seed {i}',RingSeedField(data[i]),dict(P=0,A=0,B=1,O=1,D=0),16.)
    result=dict(all_passed=True,case_count=len(rows),rows=rows,elapsed_seconds=time.perf_counter()-start)
    atomic_json(ROOT/'results/zero_inventory_tests.json',result);print('PASS',len(rows),result['elapsed_seconds'])
if __name__=='__main__':main()
