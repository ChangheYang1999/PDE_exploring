#!/usr/bin/env python3
"""Fixed-leading-tail replacement, explicitly separate from global acceptance."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,time
import numpy as np
from scipy.special import roots_legendre
from independent_artifacts import atomic_json,atomic_npz,sha256
from piecewise_loading import load_piecewise
from coefficient_tail import coefficient_audit
from tail_replacement import replace_first_correction
from piecewise_adapter import spherical_jets
ROOT=Path(__file__).resolve().parent

def main():
    ap=argparse.ArgumentParser();ap.add_argument('input',type=Path);ap.add_argument('--output',required=True,type=Path);args=ap.parse_args()
    out=args.output.resolve()
    if not out.is_relative_to(ROOT.parent):raise ValueError('output outside lane')
    out.mkdir(parents=True,exist_ok=False);start=time.perf_counter();cpu=time.process_time();digest=sha256(args.input)
    files=[Path(__file__),ROOT/'src/tail_replacement.py',ROOT/'src/coefficient_tail.py',ROOT/'src/angular_tail_projection.py',ROOT/'src/independent_farfield.py',ROOT/'src/independent_fields.py',ROOT/'src/piecewise_loading.py',ROOT/'src/piecewise_adapter.py',ROOT/'src/piecewise_jacobi.py']
    sources={str(p.relative_to(ROOT)):sha256(p) for p in files}
    old=load_piecewise(args.input);mu,w=roots_legendre(96);results={}
    variants=[('original',old,{})]+[(label,*replace_first_correction(old,degree)) for label,degree in [('degree12',12),('full',None)]]
    for label,field,info in variants:
        gauged,gauge=field.reporting_gauge();scale=float(gauged.interfaces[-1]);radii=scale*2.**np.arange(1,15)
        d=coefficient_audit(gauged,radii,mu,w);d.update(gauge=gauge,replacement=info)
        interface=[]
        for R in gauged.interfaces:
            inside=spherical_jets(gauged,np.full(mu.shape,R),mu,3,element=int(R==gauged.interfaces[-1]))
            outside=spherical_jets(gauged,np.full(mu.shape,R),mu,3,element=int(R==gauged.interfaces[-1])+1)
            row=dict(radius=float(R),jumps={})
            for key,maxorder in [('phi',3),('q',2)]:
                for n in range(maxorder+1):row['jumps'][f'{key}_dR{n}']=float(np.max(abs(inside[key][n,0]-outside[key][n,0])))
            interface.append(row)
        d['interfaces_absolute_jumps']=interface
        atomic_json(out/(label+'.json'),d)
        if label!='original':
            payload=dict(field.coefficients);payload['meta_json']=np.array(json.dumps(field.metadata))
            atomic_npz(out/(label+'_coeffs.npz'),payload)
        results[label]={k:d[k] for k in ['correction_mismatch_sphere_norm','correction_relative_to_Euler','rows','interfaces_absolute_jumps']}
    if sha256(args.input)!=digest:raise RuntimeError('input changed')
    if any(sha256(ROOT/name)!=value for name,value in sources.items()):raise RuntimeError('source changed')
    summary=dict(completed_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.perf_counter()-start,process_cpu_seconds=time.process_time()-cpu,
        input_path=str(args.input.resolve()),input_sha256=digest,source_sha256=sources,results=results,
        scope='Exterior operator experiment. Only first correction changed. Interior coefficients retained, interface and global pressure consistency not repaired. No candidate.')
    atomic_json(out/'summary.json',summary)
    print(json.dumps(dict(output=str(out),elapsed_seconds=summary['elapsed_seconds'])),flush=True)
if __name__=='__main__':main()
