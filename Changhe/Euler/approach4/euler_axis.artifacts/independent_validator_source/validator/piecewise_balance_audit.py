#!/usr/bin/env python3
"""Retain finite-ball balances, their residual work, and interface fluxes."""
import argparse,datetime,json,time
from pathlib import Path
import numpy as np
from piecewise_loading import load_piecewise
from piecewise_pressure import InterfaceGreenPoisson
from piecewise_balances import piecewise_ball_balance
from independent_artifacts import atomic_json,sha256,verify_source_identity
ROOT=Path(__file__).resolve().parent
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('candidate',type=Path);ap.add_argument('--geometry',required=True,type=Path);ap.add_argument('--output',required=True,type=Path)
    a=ap.parse_args();out=a.output.resolve()
    if not out.is_relative_to(ROOT.parent):raise ValueError('output outside lane')
    if out.exists():raise FileExistsError('retain previous audit')
    start=time.perf_counter();cpu=time.process_time();field=load_piecewise(a.candidate)
    geometry=json.loads(a.geometry.read_text());aeff=geometry['core']['a_eff']/geometry['gauge']['dilation_L']
    paths=[Path(__file__),ROOT/'src/piecewise_adapter.py',ROOT/'src/piecewise_jacobi.py',ROOT/'src/piecewise_loading.py',ROOT/'src/piecewise_pressure.py',ROOT/'src/piecewise_balances.py',*sorted((ROOT/'src').glob('independent_*.py'))]
    hashes={str(p.relative_to(ROOT)):sha256(p) for p in paths}
    result=dict(created_utc=utc(),candidate_sha256=sha256(a.candidate),geometry_sha256=sha256(a.geometry),source_sha256=hashes,
        coordinate_convention='Original exported working coordinates; a_eff converted from reporting coordinates.',working_a_eff=aeff,
        scope='Piecewise classical energy and helicity. Continuous bulk pressure from full-space Green reconstruction. The residual-source identity is an implementation check; raw defects remain acceptance diagnostics. No distributional helicity is defined.')
    def checkpoint(phase):
        verify_source_identity(ROOT,hashes)
        if sha256(a.candidate)!=result['candidate_sha256'] or sha256(a.geometry)!=result['geometry_sha256']:raise RuntimeError('input changed')
        result.update(phase=phase,updated_utc=utc(),elapsed_seconds=time.perf_counter()-start,cpu_seconds=time.process_time()-cpu)
        atomic_json(out,result);print(phase,result['elapsed_seconds'],flush=True)
    pressure=InterfaceGreenPoisson(field.source,interfaces=field.interfaces,decay_power=2*field.alpha,scale=field.phi.length,lmax=32,nangle=64,nradial=48)
    result['pressure_parameters']=dict(lmax=32,nangle=64,nradial=48);rows=[]
    for label,nr,na in [('medium',12,32),('fine',24,64)]:
        for factor in [1,4,16]:
            row=piecewise_ball_balance(field,pressure,aeff*factor,nangle=na,nradial=nr)
            row.update(label=label,nradial=nr,nangle=na,radius_over_a_eff=factor)
            rows.append(row);result['rows']=rows;checkpoint(f'{label}_{factor}')
    result['refinement_changes']=[dict(radius_over_a_eff=factor,**{key:float(rows[j+3][key]-rows[j][key]) for key in ['energy','helicity','energy_defect','helicity_defect','energy_corrected_error','helicity_corrected_error']}) for j,factor in enumerate([1,4,16])]
    checkpoint('complete')
if __name__=='__main__':main()
