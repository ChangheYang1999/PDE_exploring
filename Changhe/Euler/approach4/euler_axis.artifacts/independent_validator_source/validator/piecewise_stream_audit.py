#!/usr/bin/env python3
"""Reconstruct a saved potential from its bulk eta and interface distributions."""
import argparse,datetime,time
from pathlib import Path
import numpy as np
from piecewise_loading import load_piecewise
from piecewise_stream import ReconstructedStream
from independent_artifacts import atomic_json,sha256,verify_source_identity
ROOT=Path(__file__).resolve().parent
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('candidate',type=Path);ap.add_argument('--output',required=True,type=Path)
    a=ap.parse_args();out=a.output.resolve()
    if not out.is_relative_to(ROOT.parent):raise ValueError('outside lane')
    if out.exists():raise FileExistsError('retain previous audit')
    start=time.perf_counter();cpu=time.process_time();field=load_piecewise(a.candidate)
    paths=[Path(__file__),ROOT/'src/piecewise_adapter.py',ROOT/'src/piecewise_jacobi.py',ROOT/'src/piecewise_loading.py',ROOT/'src/piecewise_pressure.py',ROOT/'src/piecewise_stream.py',*sorted((ROOT/'src').glob('independent_*.py'))]
    hashes={str(p.relative_to(ROOT)):sha256(p) for p in paths}
    result=dict(created_utc=utc(),candidate_sha256=sha256(a.candidate),source_sha256=hashes,
                scope='Five-dimensional full-space bulk inversion plus diagnostic surface distributions. A successful reconstruction does not establish smoothness or Euler momentum.')
    def checkpoint(phase):
        verify_source_identity(ROOT,hashes)
        if sha256(a.candidate)!=result['candidate_sha256']:raise RuntimeError('input changed')
        result.update(phase=phase,updated_utc=utc(),elapsed_seconds=time.perf_counter()-start,cpu_seconds=time.process_time()-cpu)
        atomic_json(out,result);print(phase,result['elapsed_seconds'],flush=True)
    points=np.array([[0,0],[0,.731],[0,-.827],[.317,-.419],[.81,.57],[1.2,-.6],[1.77,.2],[0,1.9],
                     [1.8,1.2],[0,-2.2],[3.1,.7],[2.9,-4.2],[0,6.3],[8.9,1.1],[0,10.7],
                     [8.4,8.3],[17.1,-2.3],[0,-37],[76,31],[241,-179]],dtype=float)
    result['points_r_z']=points.tolist();r,z=points.T;p=field.jets(r*r,z,1)['phi']
    exact=p[0,0];gradient=np.stack([2*r*p[1,0],p[0,1]],axis=-1)
    result['coefficient_potential']=exact.tolist();result['coefficient_gradient']=gradient.tolist();rows=[]
    for name,lmax,na,nr in [('medium',24,48,32),('fine',36,80,56)]:
        inverse=ReconstructedStream(field,lmax=lmax,nangle=na,nradial=nr)
        bulk,bg=inverse.bulk.evaluate(r,z);surface,sg=inverse.surface.evaluate(r,z)
        got=bulk+surface;gg=bg+sg
        rows.append(dict(name=name,lmax=lmax,nangle=na,nradial=nr,potential=got.tolist(),gradient=gg.tolist(),
            max_abs_potential_error=float(np.max(abs(got-exact))),max_abs_gradient_error=float(np.max(abs(gg-gradient))),
            max_abs_bulk_potential_error=float(np.max(abs(bulk-exact))),max_abs_bulk_gradient_error=float(np.max(abs(bg-gradient))),
            surface_potential=surface.tolist(),surface_gradient=sg.tolist()))
        result['refinements']=rows;checkpoint(name)
    result['refinement_change']=dict(potential=float(np.max(abs(np.array(rows[0]['potential'])-got))),gradient=float(np.max(abs(np.array(rows[0]['gradient'])-gg))))
    checkpoint('complete')
if __name__=='__main__':main()
