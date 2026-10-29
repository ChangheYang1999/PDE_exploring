#!/usr/bin/env python3
"""Re-evaluate four registered shells with value-only Chebyshev derivatives."""
import argparse,datetime,json,time
from pathlib import Path
import numpy as np
from independent_fields import PotentialField
from independent_geometry import core_scale,reporting_gauge,shell_quadrature,random_shell
from independent_pressure import GreenPoisson
from independent_projection import project_shell
from independent_registered_metrics import evaluate_set,annotate_and_aggregate
from independent_artifacts import sha256,source_identity,verify_source_identity,atomic_json,atomic_npz
ROOT=Path(__file__).resolve().parent

def main():
    p=argparse.ArgumentParser();p.add_argument('candidate',type=Path);p.add_argument('--output',required=True,type=Path)
    p.add_argument('--shells',type=int,nargs='+',default=[-3,0,5,10]);p.add_argument('--degrees',type=int,nargs='+',default=[16,24,36])
    p.add_argument('--seed',type=int,default=497286);p.add_argument('--trim-relative',type=float,default=2e-18)
    p.add_argument('--pressure-lmax',type=int,default=20);p.add_argument('--pressure-angle',type=int,default=48)
    p.add_argument('--pressure-radial',type=int,default=28);a=p.parse_args();out=a.output.resolve()
    if not out.is_relative_to(ROOT.parent):raise ValueError('output outside verifier lane')
    if out.exists() and any(out.iterdir()):raise FileExistsError('choose a fresh projection output directory')
    if len(set(a.shells))<4:raise ValueError('four distinct shells required for this route')
    if len(a.degrees)<3 or any(n<8 for n in a.degrees):raise ValueError('three projection degrees of at least eight required')
    out.mkdir(parents=True,exist_ok=True);start=time.perf_counter();identity=source_identity(ROOT,__file__);before=sha256(a.candidate)
    metadata={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'candidate_sha256':before,
              'candidate_path':str(a.candidate.resolve()),'source_sha256':identity,'projection_degrees':a.degrees,
              'shell_indices':a.shells,'seed':a.seed,'trim_relative':a.trim_relative}
    atomic_json(out/'metadata.json',metadata)
    field,gauge=reporting_gauge(PotentialField.load(a.candidate));core=core_scale(field)
    if core['a_eff'] is None:raise ValueError('core scale unresolved')
    pressure=GreenPoisson(field.source,decay_power=2*field.alpha,lmax=a.pressure_lmax,nangle=a.pressure_angle,
                         nradial=a.pressure_radial,scale=field.phi.length)
    rng=np.random.default_rng(a.seed);reference=[];histories=[];arrays={};levels={str(n):[] for n in a.degrees}
    for k in a.shells:
        lo=core['a_eff']*2.**k;hi=2*lo;sets=[]
        for collar in [False,True]:
            grid=shell_quadrature(lo,hi,nradial=8,nangle=64,collar=collar)
            P,G=pressure.on_spheres(grid['radii'],grid['mu'])
            sets.append(('collar_gauss' if collar else 'shell_gauss',grid,P,G))
        grid=random_shell(lo,hi,rng,256);grid['measure']='Independent uniform physical volume samples'
        P,G=pressure.evaluate(grid['r'],grid['z']);sets.append(('shell_random',grid,P,G))
        ref_arrays={}
        for name,grid,P,G in sets:
            metrics,values=evaluate_set(field,grid['r'],grid['z'],grid['weights'],P,G)
            reference.append({'shell_index':k,'set':name,'lower':lo,'upper':hi,'measure':grid['measure'],'metrics':metrics})
            ref_arrays[name]=values
            for key,value in values.items():arrays[f'reference_{k}_{name}_{key}']=value
        shell_history=[]
        for n in a.degrees:
            projected=project_shell(field,lo,hi,radial_degree=n,angular_degree=n,trim_relative=a.trim_relative,extended=True)
            differences={}
            for name,grid,P,G in sets:
                metrics,values=evaluate_set(projected,grid['r'],grid['z'],grid['weights'],P,G)
                levels[str(n)].append({'shell_index':k,'set':name,'lower':lo,'upper':hi,'measure':grid['measure'],'metrics':metrics})
                differences[name]={}
                for key in ['U','M','q_residual','eta_residual']:
                    absolute=float(np.max(np.abs(values[key]-ref_arrays[name][key])))
                    scale=float(np.max(np.abs(ref_arrays[name][key])))
                    differences[name][key]={'maximum_difference':absolute,'relative_to_reference_maximum':absolute/scale if scale else None}
                for key,value in values.items():arrays[f'degree{n}_{k}_{name}_{key}']=value
            shell_history.append({'degree':n,'phi_projection':projected.phi.metadata,'q_projection':projected.q.metadata,'differences':differences})
        histories.append({'shell_index':k,'lower':lo,'upper':hi,'history':shell_history})
        verify_source_identity(ROOT,identity)
        if before!=sha256(a.candidate):raise RuntimeError('candidate changed during projection')
        atomic_json(out/'progress.json',{'completed_shell':k,'projection_histories':histories})
        print(json.dumps({'completed_shell':k,'elapsed_seconds':time.perf_counter()-start}),flush=True)
    aggregate={key:annotate_and_aggregate(rows) for key,rows in levels.items()}
    summary={**metadata,'gauge':gauge,'core':core,'reference_rows':reference,'reference_aggregate':annotate_and_aggregate(reference),
             'projection_rows':levels,'projection_aggregates':aggregate,'projection_histories':histories,
             'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.perf_counter()-start,
             'pressure_parameters':{'lmax':a.pressure_lmax,'nangle':a.pressure_angle,'nradial':a.pressure_radial},
             'pressure_scope':'The independent full-space pressure reconstructed from original coefficients is held fixed across projection levels. Pressure convergence is checked separately.',
             'scope':'Four-shell A10 differentiation/representation check. This is not the full required A1 shell set and is not an A or B verdict.'}
    verify_source_identity(ROOT,identity)
    if before!=sha256(a.candidate):raise RuntimeError('candidate changed during projection')
    atomic_npz(out/'arrays.npz',arrays);atomic_json(out/'summary.json',summary)
    print(json.dumps({'output':str(out),'elapsed_seconds':summary['elapsed_seconds'],'projection_aggregates':aggregate}),flush=True)
if __name__=='__main__':main()
