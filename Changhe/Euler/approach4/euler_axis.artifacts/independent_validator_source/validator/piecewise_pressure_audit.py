#!/usr/bin/env python3
"""Independent full-space pressure checks on a saved piecewise export.

The saved sample pressure is compared only after reconstruction, never used
as data for the solve. Surface stress corrections are reported separately.
"""
import argparse, datetime, json, time
from pathlib import Path
import numpy as np
from piecewise_loading import load_piecewise
from piecewise_adapter import PiecewiseField
from piecewise_pressure import InterfaceGreenPoisson, InterfaceStressPressure, DirectInterfaceNewton
from independent_artifacts import atomic_json, sha256, verify_source_identity

ROOT=Path(__file__).resolve().parent

def utc(): return datetime.datetime.now(datetime.timezone.utc).isoformat()

def main():
    ap=argparse.ArgumentParser();ap.add_argument('candidate',type=Path)
    ap.add_argument('--samples',type=Path);ap.add_argument('--output',required=True,type=Path)
    args=ap.parse_args();out=args.output.resolve()
    if not out.is_relative_to(ROOT.parent):raise ValueError('output outside verifier lane')
    if out.exists():raise FileExistsError('preserve completed or interrupted audit')
    started=time.perf_counter();cpu=time.process_time();field=load_piecewise(args.candidate)
    paths=[Path(__file__),ROOT/'src/piecewise_adapter.py',ROOT/'src/piecewise_jacobi.py',ROOT/'src/piecewise_loading.py',ROOT/'src/piecewise_pressure.py',*sorted((ROOT/'src').glob('independent_*.py'))]
    hashes={str(p.relative_to(ROOT)):sha256(p) for p in paths}
    result=dict(created_utc=utc(),candidate_sha256=sha256(args.candidate),source_sha256=hashes,
                coordinate_convention='Original exported working coordinates; no reporting dilation.',
                scope='Pressure of a piecewise approximation. Bulk tr(DU^2) and distributional div div(U tensor U) are separate. Neither establishes an Euler solution.')
    def checkpoint(phase):
        verify_source_identity(ROOT,hashes)
        if sha256(args.candidate)!=result['candidate_sha256']:raise RuntimeError('candidate changed')
        result.update(phase=phase,updated_utc=utc(),elapsed_seconds=time.perf_counter()-started,cpu_seconds=time.process_time()-cpu)
        atomic_json(out,result);print(json.dumps({'phase':phase,'elapsed_seconds':result['elapsed_seconds']}),flush=True)
    checkpoint('started')
    points=np.array([[0,0],[0,.731],[0,-.827],[.317,-.419],[.81,.57],[1.2,-.6],[1.77,.2],[0,1.9],
                     [1.8,1.2],[0,-2.2],[3.1,.7],[2.9,-4.2],[0,6.3],[8.9,1.1],[0,10.7],
                     [8.4,8.3],[17.1,-2.3],[0,-37],[76,31],[241,-179]],dtype=float)
    result['points_r_z']=points.tolist();resolutions=[('medium',32,64,48),('fine',40,96,64)]
    pressures=[];references=[]
    for label,lmax,na,nr in resolutions:
        obj=InterfaceGreenPoisson(field.source,interfaces=field.interfaces,decay_power=2*field.alpha,
                                  scale=field.phi.length,lmax=lmax,nangle=na,nradial=nr)
        p,g=obj.evaluate(points[:,0],points[:,1]);pressures.append(obj)
        references.append(dict(label=label,lmax=lmax,nangle=na,nradial=nr,pressure=p.tolist(),gradient=g.tolist()))
        result['green_refinements']=references;checkpoint('green_'+label)
    p=np.asarray(references[-1]['pressure']);g=np.asarray(references[-1]['gradient'])
    result['green_refinement_max_abs']=dict(pressure=float(np.max(np.abs(p-np.asarray(references[0]['pressure'])))),
                                           gradient=float(np.max(np.abs(g-np.asarray(references[0]['gradient'])))))
    stress=InterfaceStressPressure(field,decay_power=2*field.alpha,scale=field.phi.length,lmax=40,nangle=96,nradial=64)
    sp,sg=stress.evaluate(points[:,0],points[:,1])
    result['stress_surface_correction']=dict(pressure=(sp-p).tolist(),gradient=(sg-g).tolist(),
                                             max_abs_pressure=float(np.max(np.abs(sp-p))),max_abs_gradient=float(np.max(np.abs(sg-g))))
    checkpoint('stress_correction')
    if args.samples:
        result['samples_sha256']=sha256(args.samples)
        with np.load(args.samples,allow_pickle=False) as samples:
            rp=np.empty_like(samples['P']);rg=np.empty(rp.shape+(2,))
            # Use the stored spherical grid to avoid converting identical
            # sphere radii into roundoff-distinct cache keys.
            for radius in np.unique(samples['R']):
                mask=samples['R']==radius
                vv,gg=pressures[-1].on_spheres([float(radius)],samples['mu'][mask])
                rp[mask]=vv[0];rg[mask]=gg[0]
            err=rp-samples['P'];idx=int(np.argmax(np.abs(err)))
            result['saved_sample_pressure_comparison']=dict(count=int(rp.size),max_abs_error=float(np.max(np.abs(err))),
                rms_error=float(np.sqrt(np.mean(err**2))),max_reference_scale=float(np.max(np.abs(rp))),
                worst_index=idx,worst_point_r_z=[float(samples['r'][idx]),float(samples['z'][idx])],
                reconstructed_worst=float(rp[idx]),exported_worst=float(samples['P'][idx]))
        checkpoint('sample_pressure_comparison')
    direct_rows=[]
    for nr,na in [(40,64),(64,96)]:
        obj=DirectInterfaceNewton(field.source,interfaces=field.interfaces,decay_power=2*field.alpha,
                                  scale=field.phi.length,nradial=nr,nangle=na,cutoff=64)
        vals=[]
        for i,(r,z) in enumerate(points):
            vals.append(obj.evaluate(r,z))
            result['direct_newton_values']=direct_rows+[dict(nradial=nr,nangle=na,pressure=vals)]
            checkpoint(f'direct_{nr}_point_{i}')
        values=np.array(vals)
        direct_rows.append(dict(nradial=nr,nangle=na,pressure=vals,max_abs_error_against_fine_green=float(np.max(np.abs(values-p)))))
    result['direct_newton_values']=direct_rows
    obj=DirectInterfaceNewton(field.source,interfaces=field.interfaces,decay_power=2*field.alpha,
                              scale=field.phi.length,nradial=64,nangle=96,cutoff=64)
    gradient_rows=[]
    for index in [0,1,3,8,16]:
        r,z=points[index];steps=[]
        for h in [.01,.003,.001]:
            columns=[]
            for axis in [0,1]:
                if axis==0 and r==0:columns.append(0.);continue
                values=[]
                for delta in [-2,-1,1,2]:
                    rr,zz=r,z
                    if axis==0:rr+=delta*h
                    else:zz+=delta*h
                    values.append(obj.evaluate(rr,zz))
                columns.append((values[0]-8*values[1]+8*values[2]-values[3])/(12*h))
            steps.append(dict(h=h,gradient=columns,max_abs_error=float(np.max(np.abs(np.array(columns)-g[index])))))
            result['direct_gradient_checks']=gradient_rows+[dict(point_index=index,steps=steps)]
            checkpoint(f'direct_gradient_point_{index}_step_{h}')
        gradient_rows.append(dict(point_index=index,steps=steps))
    result['direct_gradient_checks']=gradient_rows
    result['interpretation']='These comparisons test pressure evaluation, not the Euler residual or exact interface regularity. No pressure correction was fitted to reduce momentum defects.'
    checkpoint('complete')
if __name__=='__main__':main()
