#!/usr/bin/env python3
"""Degree-limited projection of saved forced tails, with exact stated limits."""
from pathlib import Path
import argparse,datetime,json,time
import numpy as np
from scipy.special import roots_legendre
from numpy.polynomial import Polynomial as Poly
from independent_farfield import angular_data,evaluate_vector
from coefficient_tail import velocity_coefficients
from angular_tail_projection import project
from independent_artifacts import sha256,atomic_json
ROOT=Path(__file__).resolve().parent

def main():
    ap=argparse.ArgumentParser();ap.add_argument('directory',type=Path);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
    out=a.output.resolve()
    if not out.is_relative_to(ROOT.parent) or out.exists():raise ValueError('use fresh lane output')
    start=time.perf_counter();rows=[];inputs={}
    for path in sorted(a.directory.glob('*.json')):
        d=json.loads(path.read_text())
        if 'A1_saved' not in d:continue
        inputs[str(path.resolve())]=sha256(path);records=[]
        da=len(d['A1_saved'])-1;db=len(d['B1_saved'])-1
        for n in [64,96,128]:
            mu,w=roots_legendre(n);data=angular_data(d['alpha'],Poly(d['A']),Poly(d['B']))
            G=evaluate_vector(data,mu,'G');H=velocity_coefficients(d['correction_exponent'],Poly(d['A1_saved']),Poly(d['B1_saved']),mu)
            records.append(dict(nangle=n,**project(d['correction_exponent'],mu,w,G,da,db,H)))
        rows.append(dict(name=path.stem,c_l=d['c_l'],degree_A=da,degree_B=db,records=records))
    atomic_json(out,dict(completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),elapsed_seconds=time.perf_counter()-start,rows=rows,input_sha256=inputs,
        source_sha256={str(p.relative_to(ROOT)):sha256(p) for p in [Path(__file__),ROOT/'src/angular_tail_projection.py',ROOT/'src/coefficient_tail.py',ROOT/'src/independent_farfield.py']},
        scope='Projection limits are the degrees of the saved H polynomials. Lower bounds hold for fixed leading F in those explicit spaces; not after changing F or increasing the degrees.'))
    print(str(out))
if __name__=='__main__':main()
