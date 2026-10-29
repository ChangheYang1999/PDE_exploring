#!/usr/bin/env python3
"""Independent, finite zero search for saved fields. No completeness claim."""
import argparse,time,datetime
from pathlib import Path
from independent_fields import PotentialField
from piecewise_loading import load_piecewise
from independent_artifacts import atomic_json,sha256
from zero_inventory import inventory
ROOT=Path(__file__).resolve().parent

def main():
    p=argparse.ArgumentParser();p.add_argument('inputs',type=Path,nargs='+');p.add_argument('--output',type=Path,required=True)
    p.add_argument('--piecewise',action='store_true');p.add_argument('--radii',type=float,nargs='+',default=[8.,32.])
    p.add_argument('--nradial',type=int,default=97);p.add_argument('--nangle',type=int,default=129);p.add_argument('--max-starts',type=int,default=64)
    a=p.parse_args();out=a.output.resolve()
    if not out.is_relative_to(ROOT.parent):raise ValueError('output outside verifier lane')
    start=time.perf_counter();cpu=time.process_time();rows=[]
    hashes={str(f.relative_to(ROOT)):sha256(f) for f in [Path(__file__),ROOT/'src/zero_inventory.py',ROOT/'src/independent_fields.py',ROOT/'src/piecewise_adapter.py',ROOT/'src/piecewise_jacobi.py',ROOT/'src/piecewise_loading.py']}
    for path in a.inputs:
        h=sha256(path);field=load_piecewise(path) if a.piecewise else PotentialField.load(path)
        for radius in a.radii:
            t=time.perf_counter();result=inventory(field,radius=radius,nradial=a.nradial,nangle=a.nangle,max_starts=a.max_starts)
            if sha256(path)!=h:raise RuntimeError('input changed')
            row=dict(input=str(path.resolve()),sha256=h,c_l=field.c_l,elapsed_seconds=time.perf_counter()-t,result=result)
            rows.append(row);print(path.parent.name,radius,result['counts'],result['boundary_winding'],result['reflected_index_sum'],flush=True)
            atomic_json(out,dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),source_sha256=hashes,rows=rows,
                wall_seconds=time.perf_counter()-start,cpu_seconds=time.process_time()-cpu,scope='Finite numerical search only; no completeness certificate.'))
    for name,h in hashes.items():
        if sha256(ROOT/name)!=h:raise RuntimeError('source changed')
if __name__=='__main__':main()
