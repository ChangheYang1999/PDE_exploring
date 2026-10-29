#!/usr/bin/env python3
"""Evaluate a saved field's q and eta on all frozen shell and collar grids."""
import argparse,datetime,json,time
from pathlib import Path
import numpy as np
from independent_fields import PotentialField
from eta_green_basis import EtaGreenField
from independent_geometry import core_scale,reporting_gauge
from piecewise_loading import load_piecewise
from reduced_screen import reduced_shells
from independent_artifacts import atomic_json,atomic_npz,sha256,source_identity,verify_source_identity
ROOT=Path(__file__).resolve().parent

def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()

def main():
    ap=argparse.ArgumentParser();ap.add_argument('candidate',type=Path);ap.add_argument('--output',required=True,type=Path)
    ap.add_argument('--nradial',type=int,default=8);ap.add_argument('--nangle',type=int,default=64);ap.add_argument('--nrandom',type=int,default=256)
    ap.add_argument('--seed',type=int,default=295174);a=ap.parse_args();out=a.output.resolve()
    if not out.is_relative_to(ROOT.parent):raise ValueError('output outside verifier lane')
    if out.exists():raise FileExistsError('preserve previous screen')
    out.mkdir(parents=True);start=time.perf_counter();cpu=time.process_time();identity=source_identity(ROOT,__file__)
    for name in ['src/reduced_screen.py','src/eta_green_basis.py','src/piecewise_loading.py','src/piecewise_jacobi.py','src/piecewise_adapter.py']:identity[name]=sha256(ROOT/name)
    before=sha256(a.candidate);metadata={'created_utc':utc(),'candidate_path':str(a.candidate.resolve()),'candidate_sha256':before,'source_sha256':identity,
       'parameters':{'nradial':a.nradial,'nangle':a.nangle,'nrandom':a.nrandom,'seed':a.seed}}
    atomic_json(out/'metadata.json',metadata)
    if a.candidate.suffix=='.npz':field,gauge=load_piecewise(a.candidate).reporting_gauge()
    elif json.loads(a.candidate.read_text()).get('format')=='verifier-eta-green-v1':field,gauge=EtaGreenField.load(a.candidate).reporting_gauge()
    else:field,gauge=reporting_gauge(PotentialField.load(a.candidate))
    core=core_scale(field);atomic_json(out/'geometry.json',{'gauge':gauge,'core':core})
    print(json.dumps({'core_done':utc(),'a_eff':core['a_eff'],'wall_seconds':time.perf_counter()-start}),flush=True)
    if core['a_eff'] is None:raise ValueError('unresolved outer half-vorticity radius')
    def checkpoint(rows,arrays,status):
        verify_source_identity(ROOT,identity)
        if sha256(a.candidate)!=before:raise RuntimeError('input changed')
        name=f'arrays_{len(rows):03d}.npz';atomic_npz(out/name,arrays)
        atomic_json(out/'progress.json',{'updated_utc':utc(),'rows':rows,'arrays_file':name,'arrays_sha256':sha256(out/name),
                                       'wall_seconds':time.perf_counter()-start,'status':status})
        print(json.dumps(dict(status,wall_seconds=time.perf_counter()-start)),flush=True)
    result,arrays=reduced_shells(field,core['a_eff'],nradial=a.nradial,nangle=a.nangle,nrandom=a.nrandom,seed=a.seed,callback=checkpoint)
    verify_source_identity(ROOT,identity)
    if sha256(a.candidate)!=before:raise RuntimeError('input changed')
    result.update(metadata,completed_utc=utc(),gauge=gauge,core=core,c_l=field.c_l,alpha=field.alpha,
                  wall_seconds=time.perf_counter()-start,process_cpu_seconds=time.process_time()-cpu,complete_required_shell_set=True,
                  equations_evaluated=['q','eta'])
    atomic_npz(out/'arrays.npz',arrays);atomic_json(out/'summary.json',result)
    print(json.dumps({'output':str(out),'aggregate':result['aggregate'],'wall_seconds':result['wall_seconds']}),flush=True)
if __name__=='__main__':main()
