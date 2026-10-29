#!/usr/bin/env python3
"""Registered independent shell evaluation with immutable, resumable inputs."""
import argparse,datetime,json,time
from pathlib import Path
import numpy as np
from eta_green_basis import EtaGreenField
from independent_geometry import core_scale
from independent_pressure import GreenPoisson
from independent_registered_metrics import registered_shells
from independent_artifacts import sha256,source_identity,verify_source_identity,atomic_json,atomic_npz

ROOT=Path(__file__).resolve().parent

def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()

def main():
    p=argparse.ArgumentParser();p.add_argument('candidate',type=Path);p.add_argument('--output',required=True,type=Path)
    p.add_argument('--seed',type=int,default=295174);p.add_argument('--nradial',type=int,default=8)
    p.add_argument('--nangle',type=int,default=64);p.add_argument('--nrandom',type=int,default=256)
    p.add_argument('--pressure-lmax',type=int,default=16);p.add_argument('--pressure-angle',type=int,default=40)
    p.add_argument('--pressure-radial',type=int,default=24);p.add_argument('--shells',type=int,nargs='*')
    p.add_argument('--no-origin',action='store_true');p.add_argument('--resume',action='store_true')
    a=p.parse_args();out=a.output.resolve();start=time.perf_counter()
    if not out.is_relative_to(ROOT.parent):raise ValueError('output outside verifier lane')
    if (out/'summary.json').exists():raise FileExistsError('preserve existing completed record')
    out.mkdir(parents=True,exist_ok=True)
    identity=source_identity(ROOT,__file__)
    for name in ['src/eta_green_basis.py','src/piecewise_adapter.py']:identity[name]=sha256(ROOT/name)
    before=sha256(a.candidate)
    parameters={'seed':a.seed,'nradial':a.nradial,'nangle':a.nangle,'nrandom':a.nrandom,
                'pressure_lmax':a.pressure_lmax,'pressure_angle':a.pressure_angle,'pressure_radial':a.pressure_radial,
                'shells':list(range(-6,12)) if a.shells is None else a.shells,'include_origin':not a.no_origin}
    if a.resume:
        metadata=json.loads((out/'metadata.json').read_text())
        if metadata['candidate_sha256']!=before:raise ValueError('resume candidate hash mismatch')
        if metadata['source_sha256']!=identity:raise ValueError('resume source hash mismatch')
        if metadata['parameters']!=parameters:raise ValueError('resume parameter mismatch')
    else:
        if (out/'metadata.json').exists():raise FileExistsError('unfinished validation exists; use --resume')
        metadata={'created_utc':utc(),'candidate_sha256':before,'candidate_path':str(a.candidate.resolve()),
                  'source_sha256':identity,'parameters':parameters}
        atomic_json(out/'metadata.json',metadata)
    field,gauge=EtaGreenField.load(a.candidate).reporting_gauge()
    if a.resume and (out/'geometry.json').exists():
        geometry=json.loads((out/'geometry.json').read_text())
        if geometry['gauge']!=gauge:raise ValueError('resume gauge mismatch')
        core=geometry['core']
    else:
        core=core_scale(field);atomic_json(out/'geometry.json',{'gauge':gauge,'core':core})
    if core['a_eff'] is None:raise ValueError('outer half-maximum radius unresolved')
    rows=[];arrays={};previous_wall=0.
    if a.resume and (out/'progress.json').exists():
        progress=json.loads((out/'progress.json').read_text());rows=progress['rows']
        saved=out/progress['arrays_file']
        if sha256(saved)!=progress['arrays_sha256']:raise ValueError('resume array checksum mismatch')
        with np.load(saved,allow_pickle=False) as data:arrays={k:data[k] for k in data.files}
        previous_wall=progress['checkpointed_process_wall_seconds']
    pressure=GreenPoisson(field.source,decay_power=2*field.alpha,lmax=a.pressure_lmax,nangle=a.pressure_angle,
                         nradial=a.pressure_radial,scale=field.phi.length)
    def checkpoint(rows,arrays,status):
        verify_source_identity(ROOT,identity)
        if sha256(a.candidate)!=before:raise RuntimeError('input changed during validation')
        # New names preserve the previous committed checkpoint if killed
        # between the array write and the progress-manifest replacement.
        name=f'checkpoint_arrays_{len(rows):03d}.npz';atomic_npz(out/name,arrays)
        data={'completed_utc':utc(),'status':status,'rows':rows,'arrays_file':name,'arrays_sha256':sha256(out/name),
              'checkpointed_process_wall_seconds':previous_wall+time.perf_counter()-start}
        atomic_json(out/'progress.json',data);print(json.dumps(status),flush=True)
    data,arrays=registered_shells(field,pressure,core['a_eff'],nradial=a.nradial,nangle=a.nangle,nrandom=a.nrandom,
                                seed=a.seed,shell_indices=parameters['shells'],include_origin=parameters['include_origin'],
                                callback=checkpoint,resume_rows=rows,resume_arrays=arrays)
    if before!=sha256(a.candidate):raise RuntimeError('input changed during validation')
    verify_source_identity(ROOT,identity)
    data.update(candidate_sha256=before,candidate_path=str(a.candidate.resolve()),gauge=gauge,core=core,
                completed_utc=utc(),created_utc=metadata['created_utc'],
                current_process_elapsed_seconds=time.perf_counter()-start,
                checkpointed_process_wall_seconds=previous_wall+time.perf_counter()-start,
                timing_scope='Checkpointed process wall time includes any in-process pauses and omits work lost after the last saved checkpoint. Created/completed timestamps include between-process interruption gaps.',
                pressure_parameters={'lmax':a.pressure_lmax,'nangle':a.pressure_angle,'nradial':a.pressure_radial},
                complete_required_shell_set=parameters['shells']==list(range(-6,12)) and parameters['include_origin'],
                source_sha256=identity,resumed=a.resume)
    atomic_npz(out/'arrays.npz',arrays);atomic_json(out/'summary.json',data)
    print(json.dumps({'output':str(out),'aggregate':data['aggregate'],'current_process_elapsed_seconds':data['current_process_elapsed_seconds']}),flush=True)
if __name__=='__main__':main()
