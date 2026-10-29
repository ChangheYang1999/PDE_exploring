#!/usr/bin/env python3
"""Jacobi adapter checked against saved values and symbolic polynomial derivatives."""
from pathlib import Path
import json,time
import numpy as np
import sympy as sp
from piecewise_jacobi import JacobiPiecewiseField
from independent_artifacts import atomic_json,sha256
ROOT=Path(__file__).resolve().parents[1]
EXPORT=ROOT/'external_exports/S1_pilot2_L0_20261028T2100Z'

def main():
    start=time.perf_counter();rows=[]
    def check(name,error,tol):
        e=float(np.max(abs(error)))
        rows.append(dict(name=name,error=e,tolerance=tol))
        if not np.isfinite(e) or e>tol:raise AssertionError((name,e,tol))
    field=JacobiPiecewiseField.load(EXPORT/'coeffs.npz')
    if field.elements[0].get('radial')!='jacobi':raise AssertionError('wrong metadata')
    with np.load(EXPORT/'samples.npz',allow_pickle=False) as data:
        got=field.cylindrical(data['r'],data['z'],3)
        for key,value in [('phi',got['phi'][0,0]),('q',got['q'][0,0]),('Ur',got['U'][:,0]),('Utheta',got['U'][:,1]),('Uz',got['U'][:,2]),('eta',got['eta'])]:
            check('exported '+key,(value-data[key])/(1+np.max(abs(data[key]))),2e-11)
    s,z=sp.symbols('s z',real=True);t=(s+z*z)/4
    for n,k in [(0,12),(3,5),(8,4),(12,6)]:
        # Isolate a single ball column. The other two elements are zero.
        coef={key:np.zeros_like(v) for key,v in field.coefficients.items()}
        labels=field.elements[0]['labels']
        at=[j for j,(nn,kk) in enumerate(labels) if nn==n and kk==k]
        if len(at)!=1:raise AssertionError((n,k,at))
        coef['phi_el0'][at[0]]=1.;isolated=JacobiPiecewiseField(field.metadata,coef)
        legendre=sp.Poly(sp.legendre(n,sp.Symbol('x')),sp.Symbol('x'))
        solid=sum(v*z**p[0]*(s+z*z)**((n-p[0])//2)/2**n for p,v in legendre.terms())
        expression=sp.expand(solid*sp.jacobi(k,0,sp.Rational(2*n+1,2),2*t-1))
        ss=np.array([0.,0.,.07,.2,.6]);zz=np.array([0.,.8,-.7,.3,.2]);got=isolated.jets(ss,zz,3,element=0)['phi']
        for (a,b),value in got.items():
            # Evaluate expanded exact polynomials at 45 digits, avoiding a float64 cancellation reference.
            derivative=sp.diff(expression,s,a,z,b)
            ref=np.array([float(derivative.subs({s:sp.Rational(str(x)),z:sp.Rational(str(y))}).evalf(45)) for x,y in zip(ss,zz)])
            check(f'symbolic n{n} k{k} {a},{b}',(value-ref)/(1+np.max(abs(ref))),5e-11)
    xyz=np.array([[0.,0.,0.],[.2,-.3,.7],[1.,.4,1.],[3.,.2,4.],[12.,0.,3.]])
    U,J=field.cartesian(xyz,True);hh=1e-4;fd=np.empty_like(J)
    for k in range(3):
        shift=np.zeros(3);shift[k]=hh
        fd[...,k]=(-field.cartesian(xyz+2*shift)+8*field.cartesian(xyz+shift)-8*field.cartesian(xyz-shift)+field.cartesian(xyz-2*shift))/(12*hh)
    check('Cartesian derivatives',(J-fd)/(1+np.max(abs(J))),3e-9)
    for L in [.1,2.3]:
        Ul,Jl=field.dilate(L).cartesian(L*xyz,True)
        check(f'dilation U {L}',(Ul-L*U)/(1+np.max(abs(L*U))),3e-12)
        check(f'dilation J {L}',(Jl-J)/(1+np.max(abs(J))),3e-12)
    atomic_json(ROOT/'results/piecewise_jacobi_tests.json',dict(all_passed=True,case_count=len(rows),rows=rows,elapsed_seconds=time.perf_counter()-start,
        coefficients_sha256=sha256(EXPORT/'coeffs.npz'),basis_sha256=sha256(EXPORT/'BASIS.md')))
    print('PASS',len(rows),time.perf_counter()-start)
if __name__=='__main__':main()
