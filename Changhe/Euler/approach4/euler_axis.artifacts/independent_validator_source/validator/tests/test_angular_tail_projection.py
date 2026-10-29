#!/usr/bin/env python3
from pathlib import Path
import datetime,json,time
import numpy as np
from scipy.special import roots_legendre
from angular_tail_projection import columns,project
from independent_artifacts import atomic_json,sha256
ROOT=Path(__file__).resolve().parents[1]

def main():
    start=time.perf_counter();mu,w=roots_legendre(80);checks=[]
    def check(name,error,tol):
        e=float(np.max(abs(error)))
        if e>tol or not np.isfinite(e):raise AssertionError((name,e,tol))
        checks.append(dict(name=name,error=e,tolerance=tol))
    for p in [1.7,2.,2.8]:
        va,vb,da,db=columns(p,mu,8)
        check(f'stream Gram {p}',2*np.pi*np.einsum('i,jik,lik->jl',w,va,va)-np.diag(da),2e-8)
        check(f'swirl Gram {p}',2*np.pi*np.einsum('i,jik,lik->jl',w,vb,vb)-np.diag(db),2e-10)
        check(f'mixed Gram {p}',np.einsum('i,jik,lik->jl',w,va,vb),0)
        G=.3*va[1]-.2*va[7]+.7*vb[0]+.4*vb[6];H=.4*va[1]+.8*vb[0]
        d=project(p,mu,w,G,3,2,H)
        check(f'missing norm {p}',d['omitted_norm']**2-(.04*da[7]+.16*db[6]),2e-9)
        check(f'represented norm {p}',d['represented_mismatch_norm']**2-(.01*da[1]+.01*db[0]),2e-10)
        check(f'Pythagoras {p}',d['pythagoras_defect'],2e-9)
        d2=project(p,mu,w,G,8,8,G)
        check(f'full recovery {p}',d2['omitted_norm'],2e-10)
    record=dict(completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),all_passed=True,case_count=len(checks),rows=checks,elapsed_seconds=time.perf_counter()-start,
        source_sha256={str(p.relative_to(ROOT)):sha256(p) for p in [Path(__file__),ROOT/'src/angular_tail_projection.py']})
    atomic_json(ROOT/'results/angular_tail_projection_tests.json',record);print(json.dumps(record))
if __name__=='__main__':main()
