#!/usr/bin/env python3
"""Separate core-radius and pressure-truncation effects on a saved approximation."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,time
import numpy as np
from fast_native_field import FastNativeField
load_piecewise = FastNativeField.load
from piecewise_pressure import InterfaceGreenPoisson
from independent_geometry import shell_quadrature
from independent_registered_metrics import evaluate_set
from independent_artifacts import sha256,atomic_json,verify_source_identity
ROOT=Path(__file__).resolve().parent


def main():
    ap=argparse.ArgumentParser();ap.add_argument('export',type=Path);ap.add_argument('--geometry',type=Path,required=True)
    ap.add_argument('--pressure-reference',type=Path,required=True);ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args();out=a.output.resolve()
    if not out.is_relative_to(ROOT.parent) or out.exists():raise ValueError('Fresh output inside verifier lane required')
    start=time.perf_counter();cpu=time.process_time()
    candidate=a.export/'coeffs.npz';meta_path=a.export/'candidate.json'
    meta=json.loads(meta_path.read_text());geometry=json.loads(a.geometry.read_text());reference=json.loads(a.pressure_reference.read_text())
    if reference['phase']!='complete':raise ValueError('Pressure reference incomplete')
    if reference['candidate_sha256']!=sha256(candidate):raise ValueError('Reference candidate mismatch')
    field=load_piecewise(candidate)
    radii={'primary_exported':float(meta['a_eff']),
           'independent_detected':float(geometry['core']['a_eff']/geometry['gauge']['dilation_L'])}
    paths=[Path(__file__),ROOT/'fast_native_field.py',ROOT/'src/piecewise_precision.py',ROOT.parent/'research/native_derivative_operators/PROOF.md',candidate,meta_path,a.geometry,a.pressure_reference]
    paths += [ROOT/'src'/name for name in ['piecewise_adapter.py','piecewise_jacobi.py','piecewise_loading.py','piecewise_pressure.py','independent_geometry.py','independent_registered_metrics.py','independent_pressure.py']]
    hashes={str(p.resolve()):sha256(p) for p in paths}
    record={'created_utc':datetime.now(timezone.utc).isoformat(),'source_hashes':hashes,'a_eff_working':radii,
            'c_l':field.c_l,'coordinates':'Original working coordinates; common positive dilation does not change ratios.',
            'scope':'Targeted comparison on shell 2 collar, not a replacement for the full registered test set.',
            'rows':[],'point_pressure_comparisons':[]}
    points=np.asarray(reference['points_r_z']);newton=np.asarray(reference['direct_newton_values'][-1]['pressure'])
    def checkpoint(phase):
        verify_source_identity(ROOT,hashes)
        record.update(phase=phase,updated_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.perf_counter()-start,cpu_seconds=time.process_time()-cpu)
        atomic_json(out,record);print(phase,record['elapsed_seconds'],flush=True)
    checkpoint('started')
    for label,lmax,na,nr in [('baseline',32,64,48),('resolved',64,112,80),('refined',80,128,96)]:
        pressure=InterfaceGreenPoisson(field.source,interfaces=field.interfaces,decay_power=2*field.alpha,scale=field.phi.length,lmax=lmax,nangle=na,nradial=nr)
        for radius_label,aeff in radii.items():
            grid=shell_quadrature(4*aeff,8*aeff,nradial=8,nangle=64,collar=True)
            p,g=pressure.on_spheres(grid['radii'],grid['mu'])
            metrics,arrays=evaluate_set(field,grid['r'],grid['z'],grid['weights'],p,g)
            record['rows'].append({'pressure_level':label,'lmax':lmax,'nangle':na,'nradial':nr,'radius_label':radius_label,
                                   'shell_index':2,'set':'collar_gauss','a_eff':aeff,'metrics':metrics})
            checkpoint(label+'_'+radius_label)
        p,g=pressure.evaluate(points[:,0],points[:,1])
        record['point_pressure_comparisons'].append({'pressure_level':label,'pressure':p.tolist(),'gradient':g.tolist(),
            'max_abs_error_against_direct_newton':float(np.max(abs(p-newton))),
            'max_abs_gradient_change_from_green40':float(np.max(abs(g-np.asarray(reference['green_refinements'][-1]['gradient']))))})
        checkpoint(label+'_points')
    record['interpretation']='Changing the detected core radius moves every registered shell. This test isolates that change and pressure truncation at one dominant set. Agreement there does not prove equality of complete validation procedures.'
    checkpoint('complete')

if __name__=='__main__':main()
