#!/usr/bin/env python3
"""Selected-point higher-precision checks of the saved piecewise expressions."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,time
import mpmath as mp
import numpy as np
from fast_native_field import FastNativeField
load_piecewise=FastNativeField.load
from piecewise_precision import PrecisionField
from independent_artifacts import atomic_json,sha256,verify_source_identity
ROOT=Path(__file__).resolve().parent


def convert(x,dps):
    if isinstance(x,dict):return {k:convert(v,dps) for k,v in x.items()}
    if isinstance(x,list):return [convert(v,dps) for v in x]
    if isinstance(x,int):return x
    return mp.nstr(x,dps)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('candidate',type=Path);ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args();out=a.output.resolve()
    if not out.is_relative_to(ROOT.parent) or out.exists():raise ValueError('fresh output in this lane required')
    start=time.perf_counter();cpu=time.process_time();f64=load_piecewise(a.candidate);high=PrecisionField.load(a.candidate)
    paths=[Path(__file__),ROOT/'fast_native_field.py',ROOT/'src/piecewise_precision.py',ROOT.parent/'research/native_derivative_operators/PROOF.md',ROOT/'src/piecewise_precision.py',ROOT/'src/piecewise_adapter.py',ROOT/'src/piecewise_jacobi.py',ROOT/'src/piecewise_loading.py',ROOT/'src/independent_fields.py']
    hashes={str(p.relative_to(ROOT.parent)):sha256(p) for p in paths}
    result=dict(created_utc=datetime.now(timezone.utc).isoformat(),candidate_sha256=sha256(a.candidate),source_sha256=hashes,source_identity_root='verifier lane',
        coordinates='Saved working coordinates; exact stored binary inputs, with fixed one-sided element choice.',rows=[],
        scope='Numerical stability and selected-point differentiation checks, not an interval enclosure. Pressure is excluded.')
    def save(phase):
        verify_source_identity(ROOT.parent,hashes)
        if sha256(a.candidate)!=result['candidate_sha256']:raise RuntimeError('input changed')
        result.update(phase=phase,updated_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.perf_counter()-start,cpu_seconds=time.process_time()-cpu)
        atomic_json(out,result);print(phase,result['elapsed_seconds'],flush=True)
    # Includes origin, axis, core, near each interface, exterior and a distant axis.
    points=[(0.,0.),(0.,-.753),(0.31,-.417),(1.7,.2),(0.,1.999),(0.,2.001),(3.3,-4.1),(3.,3.999),(3.,4.001),(0.,4.999),(0.,5.001),(17.1,-2.3),(0.,128.)]
    save('expanded_ball')
    for i,(r,z) in enumerate(points):
        row=dict(point_r_z=[r,z],precisions=[]);result['rows'].append(row)
        previous=None
        for dps in [70,100]:
            with mp.workdps(dps):
                reference=high.point(r,z);text=convert(reference,dps)
            xyz=np.array([r,0.,z]);U,J=f64.cartesian(xyz,True);red=f64.reduced(r,z)
            actual={'velocity':U,'jacobian':J,'primitive_without_pressure':f64.primitive_cartesian(xyz),'source':f64.source(r,z),'q_residual':red['q'],'eta_residual':red['eta']}
            errors={}
            for key,v in actual.items():
                ref=np.asarray(text[key],dtype=float);error=float(np.max(abs(ref-np.asarray(v))));scale=float(np.max(abs(ref)))
                errors[key]=dict(max_abs_error=error,reference_scale=scale,relative_error=error/scale if scale else None)
            precision_changes={}
            if previous:
                with mp.workdps(110):
                    for key in actual:
                        before=np.asarray(previous[key],dtype=object).ravel();after=np.asarray(text[key],dtype=object).ravel()
                        precision_changes[key]=mp.nstr(max(abs(mp.mpf(x)-mp.mpf(y)) for x,y in zip(before,after)),20)
            row['precisions'].append(dict(dps=dps,reference=text,float64_errors=errors,changes_from_previous_precision=precision_changes));previous=text
            save(f'point_{i}_dps_{dps}')
    save('complete')
if __name__=='__main__':main()
