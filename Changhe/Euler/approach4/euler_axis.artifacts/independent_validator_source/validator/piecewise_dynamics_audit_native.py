#!/usr/bin/env python3
"""Swirl, maxima, stagnation and segmented circulation checks of saved exports."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,time,json
from fast_native_field import FastNativeField
load_piecewise=FastNativeField.load
from piecewise_dynamics import core_swirl_fraction,far_swirl_fraction,vorticity_maximum_identity,root_inventory,axis_branches
from piecewise_characteristics import characteristic
from independent_global_diagnostics import swirl_maximum
from independent_artifacts import atomic_json,sha256,verify_source_identity
ROOT=Path(__file__).resolve().parent

def main():
    ap=argparse.ArgumentParser();ap.add_argument('candidate',type=Path);ap.add_argument('--geometry',required=True,type=Path);ap.add_argument('--output',required=True,type=Path)
    a=ap.parse_args();a.output=a.output.resolve()
    if not a.output.is_relative_to(ROOT.parent):raise ValueError('output outside lane')
    if a.output.exists():raise FileExistsError('retain previous audit')
    start=time.perf_counter();cpu=time.process_time();working=load_piecewise(a.candidate);field,gauge=working.reporting_gauge()
    geometry=json.loads(a.geometry.read_text());aeff=float(geometry['core']['a_eff'])
    if abs(gauge['dilation_L']/geometry['gauge']['dilation_L']-1)>1e-12:raise ValueError('geometry uses a different gauge')
    paths=[Path(__file__),ROOT/'fast_native_field.py',ROOT/'src/piecewise_precision.py',ROOT.parent/'research/native_derivative_operators/PROOF.md',*sorted((ROOT/'src').glob('piecewise_*.py')),*sorted((ROOT/'src').glob('independent_*.py'))]
    hashes={str(p.relative_to(ROOT.parent)):sha256(p) for p in paths}
    out=dict(created_utc=datetime.now(timezone.utc).isoformat(),candidate_sha256=sha256(a.candidate),geometry_sha256=sha256(a.geometry),
             source_sha256=hashes,source_identity_root='verifier lane',c_l=field.c_l,gauge=gauge,a_eff=aeff,accepted_as_A=False,
             scope='Independent finite-search diagnostics of a piecewise approximation in reporting coordinates; no exact-profile or complete-basin claim.')
    def save(phase):
        verify_source_identity(ROOT.parent,hashes)
        if sha256(a.candidate)!=out['candidate_sha256'] or sha256(a.geometry)!=out['geometry_sha256']:raise RuntimeError('input changed')
        out.update(phase=phase,updated_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.perf_counter()-start,cpu_seconds=time.process_time()-cpu)
        atomic_json(a.output,out);print(phase,out['elapsed_seconds'],flush=True)
    out['swirl_fractions']=[core_swirl_fraction(field,4*aeff,nradial=nr,nangle=na) for nr,na in [(24,64),(48,96)]]
    out['far_swirl_fraction']=far_swirl_fraction(field);save('swirl_fractions')
    out['vorticity_maximum']=vorticity_maximum_identity(field,geometry['core']['maximum_point_r_z']);save('vorticity_maximum')
    out['swirl_maximum']=swirl_maximum(field);save('swirl_maximum')
    out['stagnation_inventory']=root_inventory(field,aeff);save('stagnation_inventory')
    out['axis_branches']=axis_branches(field,out['stagnation_inventory'],aeff);save('axis_branches')
    paths=[];out['characteristics']=paths
    for i,(r,z) in enumerate([(0.3,0.2),(1.0,-0.5),(3.0,1.0)]):
        for tolerance in [1e-8,1e-10]:
            for endpoint in [-3.,3.]:
                row=characteristic(field,[r*aeff,z*aeff],endpoint,rtol=tolerance,atol=tolerance*.01)
                row['trajectory_index']=i;paths.append(row);save(f'characteristic_{i}_{tolerance}_{endpoint}')
    save('complete')
if __name__=='__main__':main()
