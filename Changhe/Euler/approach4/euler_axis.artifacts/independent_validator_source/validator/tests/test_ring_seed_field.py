#!/usr/bin/env python3
"""Symbolically differentiated seed functions vs independent Taylor algebra."""
import time
from pathlib import Path
import numpy as np
import sympy as sp
from ring_seed_certificate import load_exact
from ring_seed_field import RingSeedField
from independent_artifacts import atomic_json
ROOT=Path(__file__).resolve().parents[1]

def main():
    start=time.perf_counter();rows=[];s,z=sp.symbols('s z',real=True);rho=s+z*z
    data=load_exact(ROOT.parent/'research/decaying_ring_seed/data/lead_ring_t2_params.json')
    rng=np.random.default_rng(208105);ss=np.r_[0.,0.,1.,rng.uniform(0.,8.,12)];zz=np.r_[0.,.7,0.,rng.uniform(-3.,3.,12)]
    for index in [0,14,23]:
        p=data[index];r=lambda key:sp.Rational(str(p[key])).evalf(20);c=r('c');A=r('Finf');B=c+(1+c)/2-A
        F=A*(1+(rho/r('b'))**3)**(-1/(6*c))+B/(1+(rho/r('rho1'))**int(p['n']))
        exprs={'phi':z*F,'q':r('K')*s*z*((1+rho)/2)**(-(3+1/c)/2)}
        field=RingSeedField(p);jets=field.jets(ss,zz,3)
        for name,expr in exprs.items():
            for ds in range(4):
                for dz in range(4-ds):
                    ref=np.asarray(sp.lambdify((s,z),sp.diff(expr,s,ds,z,dz).evalf(18),'numpy')(ss,zz),dtype=float)
                    got=jets[name][ds,dz];error=float(np.max(abs(got-ref)/(1+abs(ref))))
                    if not np.isfinite(error) or error>3e-11:raise AssertionError((index,name,ds,dz,error))
                    rows.append(dict(index=index,field=name,ds=ds,dz=dz,max_scaled_error=error))
    atomic_json(ROOT/'results/ring_seed_field_tests.json',dict(all_passed=True,case_count=len(rows),rows=rows,elapsed_seconds=time.perf_counter()-start))
    print('PASS',len(rows),time.perf_counter()-start)
if __name__=='__main__':main()
