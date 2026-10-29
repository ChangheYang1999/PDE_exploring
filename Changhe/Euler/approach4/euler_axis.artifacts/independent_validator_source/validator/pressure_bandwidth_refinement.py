#!/usr/bin/env python3
"""Refine bulk pressure above the proved angular bandwidth of a frozen field."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,time
import numpy as np
from fast_native_field import FastNativeField
from piecewise_pressure import InterfaceGreenPoisson
from independent_artifacts import atomic_json,sha256,verify_source_identity
ROOT=Path(__file__).resolve().parent.parent;BASE=ROOT/'axisymmetric_euler_24h'
ap=argparse.ArgumentParser();ap.add_argument('candidate',type=Path);ap.add_argument('--reference',type=Path,required=True);ap.add_argument('--samples',type=Path);ap.add_argument('--output',type=Path,required=True)
a=ap.parse_args();out=a.output.resolve()
if not out.is_relative_to(ROOT) or out.exists():raise ValueError('Output must be fresh inside the lane')
start=time.perf_counter();cpu=time.process_time();field=FastNativeField.load(a.candidate)
reference=json.loads(a.reference.read_text())
if reference['phase']!='complete' or reference['candidate_sha256']!=sha256(a.candidate):raise ValueError('Reference is incomplete or belongs to another field')
for name,h in reference['source_sha256'].items():
    p=Path(name)
    if not p.is_absolute():p=ROOT/p if name.startswith(('research/','axisymmetric_euler_24h/')) else BASE/p
    if sha256(p)!=h:raise ValueError('Reference source changed: '+name)
paths=[Path(__file__),BASE/'fast_native_field.py',BASE/'src/piecewise_adapter.py',BASE/'src/piecewise_jacobi.py',BASE/'src/piecewise_loading.py',BASE/'src/piecewise_pressure.py',BASE/'src/piecewise_precision.py',ROOT/'research/angular_pressure_bandwidth/PROOF.md',ROOT/'research/angular_pressure_bandwidth/verification/check.py',ROOT/'research/angular_pressure_bandwidth/verification/output.json',*sorted((BASE/'src').glob('independent_*.py'))]
hashes={str(p.relative_to(ROOT)):sha256(p)for p in paths}
points=np.asarray(reference['points_r_z'],dtype=float)
N=max(int(e['nmax'])for e in field.elements);D=2*N+2;L=16*((D+15)//16)
# All three angular rules meet polynomial exactness in exact arithmetic.
levels=[(L,max(96,L+32),64),(L,max(128,L+64),96),(L+16,max(160,L+96),128)]
rec=dict(created_utc=datetime.now(timezone.utc).isoformat(),candidate_sha256=sha256(a.candidate),reference_sha256=sha256(a.reference),source_sha256=hashes,coordinate_convention='Original working coordinates, same twenty points as the reference.',points_r_z=points.tolist(),angular_bound={'maximum_saved_element_nmax':N,'bulk_source_maximum_degree':D,'hypothesis':'All radial pieces use finite Legendre angular expansions; radial derivatives preserve angular degree.'},levels=[],scope='Finite-point pressure convergence, not a uniform A7 bound or Euler acceptance. Bulk source only; no stress-interface distribution or fitted pressure.')

def save(phase):
    verify_source_identity(ROOT,hashes)
    if sha256(a.candidate)!=rec['candidate_sha256'] or sha256(a.reference)!=rec['reference_sha256']:raise RuntimeError('Inputs changed')
    rec.update(phase=phase,updated_utc=datetime.now(timezone.utc).isoformat(),wall_seconds=time.perf_counter()-start,cpu_seconds=time.process_time()-cpu)
    atomic_json(out,rec);print(json.dumps({'phase':phase,'wall_seconds':rec['wall_seconds']}),flush=True)
save('started')
previous_p=np.asarray(reference['green_refinements'][-1]['pressure']);previous_g=np.asarray(reference['green_refinements'][-1]['gradient'])
for lmax,na,nr in levels:
    if 2*na-1<D+lmax:raise ValueError('Angular projection below exact polynomial requirement')
    obj=InterfaceGreenPoisson(field.source,interfaces=field.interfaces,decay_power=2*field.alpha,scale=field.phi.length,lmax=lmax,nangle=na,nradial=nr)
    p,g=obj.evaluate(points[:,0],points[:,1])
    if not (np.isfinite(p).all() and np.isfinite(g).all()):raise ValueError('Nonfinite pressure')
    direct=np.asarray(reference['direct_newton_values'][-1]['pressure'])
    row=dict(lmax=lmax,nangle=na,nradial=nr,pressure=p.tolist(),gradient=g.tolist(),change_from_previous={'pressure':float(np.max(abs(p-previous_p))),'gradient':float(np.max(abs(g-previous_g)))},difference_from_fine_direct={'pressure':float(np.max(abs(p-direct)))},direct_gradient_comparisons=[])
    for item in reference['direct_gradient_checks']:
        index=item['point_index'];best=item['steps'][-1]
        row['direct_gradient_comparisons'].append({'point_index':index,'h':best['h'],'max_abs_error':float(np.max(abs(g[index]-np.asarray(best['gradient']))))})
    radii=np.array([.173,.713,1.713,2.713,9.713,17.13,71.3]);coefficients=obj.source_coefficients(radii)
    row['source_mode_probe']={'radii':radii.tolist(),'maximum_abs_above_degree_bound':float(np.max(abs(coefficients[:,D+1:]),initial=0.)),'maximum_abs_retained':float(np.max(abs(coefficients)))}
    rec['levels'].append(row);previous_p=p;previous_g=g;save('green_'+str(lmax)+'_'+str(na)+'_'+str(nr))
if a.samples:
    rec['samples_sha256']=sha256(a.samples)
    with np.load(a.samples,allow_pickle=False)as samples:
        rp=np.empty_like(samples['P']);rg=np.empty(rp.shape+(2,))
        for radius in np.unique(samples['R']):
            mask=samples['R']==radius;pp,gg=obj.on_spheres([float(radius)],samples['mu'][mask]);rp[mask]=pp[0];rg[mask]=gg[0]
        err=rp-samples['P'];i=int(np.argmax(abs(err)))
        rec['saved_sample_comparison']={'count':int(rp.size),'max_abs_error':float(np.max(abs(err))),'rms_error':float(np.sqrt(np.mean(err**2))),'worst_index':i,'worst_r_z':[float(samples['r'][i]),float(samples['z'][i])],'reconstructed_pressure':rp.tolist(),'reconstructed_gradient':rg.tolist(),'exported_pressure':samples['P'].tolist(),'R':samples['R'].tolist(),'mu':samples['mu'].tolist()}
    if sha256(a.samples)!=rec['samples_sha256']:raise RuntimeError('Samples changed')
save('complete')
