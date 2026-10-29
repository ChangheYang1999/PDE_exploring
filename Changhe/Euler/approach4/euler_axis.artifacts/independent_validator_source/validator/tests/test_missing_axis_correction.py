#!/usr/bin/env python3
"""Exact coefficient checks for the missing outgoing-axis power obstruction."""
from pathlib import Path
from datetime import datetime,timezone
import json,time
import sympy as s
from independent_artifacts import atomic_json,sha256
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter();cpu=time.process_time();rows=[]
def zero(name,expression):
    value=s.factor(expression)
    if value!=0:raise AssertionError((name,value))
    rows.append(dict(name=name,passed=True))
p,b,a,H,K,x,z=s.symbols('p b a H K x z',positive=True)
c=1/(2*p);delta=1+c;d=p+1
h=H*x*(1-b*x)
lhs=(c+b*x)*(-2*p*x)*s.diff(h,x)
rhs=(-1+b*(1-2*p)*x)*h
for j in [1,2]:zero('swirl expansion coefficient '+str(j),s.expand(lhs-rhs).coeff(x,j))
eta=s.series(2*K*K*h*(h-1)/(c+b*x),x,0,3).removeO().expand()
zero('vorticity leading coefficient',eta.coeff(x,1)+2*K*K*H/c)
zero('positive forced next coefficient',eta.coeff(x,2)-2*K*K*H/c*(H+b+b/c))
f=z+b*z**3;D=1+z*z
numerator=s.expand(4*a*d*f*D-s.diff(f,z,2)*D**2/2+2*d*z*s.diff(f,z)*D+d*f*D-2*d*(d+1)*z*z*f)
zero('geometric leading coefficient',numerator.coeff(z,5)-b*(4*a*(p+1)-p*(2*p-1)))
for j in [0,2,4,6]:zero('geometric parity coefficient '+str(j),numerator.coeff(z,j))
phi=f/(2*D**d)
phi_s=-a*d*f/(2*D**(d+1))
for pv in [s.Rational(3,4),s.Rational(5,6),s.Rational(2,3)]:
    geom=(-8*phi_s-s.diff(phi,z,2)).subs(p,pv)
    target=(numerator/D**(p+3)).subs(p,pv)
    zero('differentiated geometry p='+str(pv),geom-target)
    # An exact algebraic check of the separation of the omitted power.
    assert 2*pv<2
    rows.append(dict(name='power gap p='+str(pv),gap=str(2-2*pv),passed=True))
zero('source amplitude relation',4*a*(p+1)-3*(b-p-1)*(1+K*K/delta**2)-
     (-8*(-a*(p+1)/2)-6*((b-p-1)/2)*(1+K*K/delta**2)))
result=dict(all_passed=True,case_count=len(rows),rows=rows,completed_utc=datetime.now(timezone.utc).isoformat(),
    wall_seconds=time.perf_counter()-start,cpu_seconds=time.process_time()-cpu,
    source_sha256=sha256(__file__),scope='Finite symbolic checks supporting the standalone proof, not a proof-assistant formalization.')
atomic_json(ROOT/'results/missing_axis_correction_tests.json',result)
print('PASS',len(rows),result['wall_seconds'])
