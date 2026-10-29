#!/usr/bin/env python3
"""Exact checks of the axis-only construction and its off-axis obstruction."""
from pathlib import Path
import time
import sympy as S
from independent_artifacts import atomic_json
ROOT=Path(__file__).resolve().parents[1]
def main():
    started=time.perf_counter();rows=[]
    def check(name,value):
        value=S.factor(value)
        if value!=0:raise AssertionError((name,value))
        rows.append(dict(name=name,passed=True))
    s,z,c,K,Q,I=S.symbols('s z c K Q I');delta=1+c;ell=-1/(I-2)
    check('inner finite-part cancellation',1+ell*(I-2))
    k=1/c
    check('outer finite-part factor',c/delta-1/(k+1))
    q=S.Function('q')(z);w=S.Function('w')(z)
    eta=2*q*(q-K)/w
    derivative=(S.diff(w,z)-delta)*q/w
    check('axis eta equation from q equation',(w*S.diff(eta,z)+delta*eta-S.diff(q*q,z)).subs(S.diff(q,z),derivative))
    u=s+z*z;f=S.Function('f');b=S.Function('b')
    phi=z*f(u)+s*z*b(u)
    lap=4*s*S.diff(phi,s,2)+8*S.diff(phi,s)+S.diff(phi,z,2)
    check('axis lift trace',phi.subs(s,0)-z*f(z*z))
    check('axis lift source',(-lap).subs(s,0)+z*(14*S.Subs(S.Derivative(f(S.Symbol('u')),S.Symbol('u')),S.Symbol('u'),z*z)+4*z*z*S.Subs(S.Derivative(f(S.Symbol('u')),S.Symbol('u'),2),S.Symbol('u'),z*z)+8*b(z*z)))
    e=2*K*Q/delta;p=-e/8
    phi=-(1+2*c)*z/2+p*s*z+Q**2*s*z*(s+z*z)/(4*delta)
    q=Q*z*z
    rq=(1-2*S.diff(phi,z))*q+2*s*(c-S.diff(phi,z))*S.diff(q,s)+(c*z+2*phi+2*s*S.diff(phi,s))*S.diff(q,z)
    eta=-4*s*S.diff(phi,s,2)-8*S.diff(phi,s)-S.diff(phi,z,2)
    check('central axis eta',eta.subs(s,0)-2*q*(q-K)/(-delta*z))
    check('first off-axis defect',S.Poly(S.expand(rq),s,z).coeff_monomial(s*z*z)+3*Q*e/4)
    check('axis residual vanishes',rq.subs(s,0))
    atomic_json(ROOT/'results/t3_axis_model_tests.json',dict(all_passed=True,case_count=len(rows),rows=rows,elapsed_seconds=time.perf_counter()-started))
    print('PASS',len(rows),time.perf_counter()-started)
if __name__=='__main__':main()
