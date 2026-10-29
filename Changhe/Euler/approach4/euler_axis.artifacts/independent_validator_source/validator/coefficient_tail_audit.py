#!/usr/bin/env python3
"""Direct asymptotic coefficient compatibility for a saved finite field."""
from pathlib import Path
import argparse,datetime,json,time
import numpy as np
from scipy.special import roots_legendre
from independent_fields import PotentialField
from eta_green_basis import EtaGreenField
from piecewise_loading import load_piecewise
from independent_geometry import reporting_gauge
from coefficient_tail import coefficient_audit
from independent_artifacts import atomic_json,sha256,source_identity,verify_source_identity
ROOT=Path(__file__).resolve().parent

def main():
    ap=argparse.ArgumentParser();ap.add_argument('input',type=Path);ap.add_argument('--output',required=True,type=Path);ap.add_argument('--nangle',type=int,default=64);ap.add_argument('--nradii',type=int,default=12);a=ap.parse_args()
    out=a.output.resolve()
    if not out.is_relative_to(ROOT.parent):raise ValueError('output outside lane')
    if out.exists():raise FileExistsError('preserve completed audit')
    start=time.perf_counter();cpu=time.process_time();digest=sha256(a.input);identity=source_identity(ROOT,__file__)
    for name in ['src/coefficient_tail.py','src/eta_green_basis.py','src/piecewise_loading.py','src/piecewise_jacobi.py','src/piecewise_adapter.py']:identity[name]=sha256(ROOT/name)
    if a.input.suffix=='.npz':field,gauge=load_piecewise(a.input).reporting_gauge()
    elif json.loads(a.input.read_text()).get('format')=='verifier-eta-green-v1':field,gauge=EtaGreenField.load(a.input).reporting_gauge()
    else:field,gauge=reporting_gauge(PotentialField.load(a.input))
    scale=float(field.interfaces[-1])*1.25 if hasattr(field,'interfaces') else field.phi.length
    radii=scale*2.**np.arange(a.nradii);mu,w=roots_legendre(a.nangle)
    result=coefficient_audit(field,radii,mu,w)
    result.update(completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),input_path=str(a.input.resolve()),input_sha256=digest,source_sha256=identity,gauge=gauge,radial_scale=scale,nangle=a.nangle,nradii=a.nradii,elapsed_seconds=time.perf_counter()-start,process_cpu_seconds=time.process_time()-cpu)
    if sha256(a.input)!=digest:raise RuntimeError('input changed')
    verify_source_identity(ROOT,identity);atomic_json(out,result)
    print(json.dumps({k:result[k] for k in ['input_path','correction_mismatch_sphere_norm','correction_relative_to_Euler','intervening_powers','elapsed_seconds']}),flush=True)
if __name__=='__main__':main()
