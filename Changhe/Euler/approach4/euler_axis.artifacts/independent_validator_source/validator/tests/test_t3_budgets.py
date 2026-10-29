#!/usr/bin/env python3
"""Exact equatorial coefficients and radial-shape incompatibility for T3."""
from pathlib import Path
import time
import sympy as S
from independent_artifacts import atomic_json
ROOT=Path(__file__).resolve().parents[1]
def main():
    start=time.perf_counter();rows=[]
    def check(name,value):
        value=S.factor(value)
        if value!=0:raise AssertionError((name,value))
        rows.append(dict(name=name,passed=True))
    s,z,c,K,Q,F1,G1=S.symbols('s z c K Q F1 G1');delta=1+c;gamma=1+4*c
    f=S.Function('f')(s);A=S.Function('A')(s);E=S.Function('E')(s)
    h=2*s*(c-f);b=c+2*f+2*s*S.diff(f,s)
    rq=h*S.diff(A*z*z,s)+b*z*S.diff(A*z*z,z)+(1-2*f)*A*z*z
    re=h*S.diff(E*z,s)+b*z*S.diff(E*z,z)+delta*E*z-S.diff((A*z*z)**2,z)
    check('equatorial q',S.expand(rq).coeff(z,2)-h*S.diff(A,s)-(1+2*c+2*f+4*s*S.diff(f,s))*A)
    check('equatorial eta',S.expand(re).coeff(z,1)-h*S.diff(E,s)-(1+2*c+2*f+2*s*S.diff(f,s))*E)
    ratio=K*gamma/(delta*(c-f))
    check('ratio derivative',S.diff(ratio,s)-S.diff(f,s)*ratio/(c-f))
    check('ratio at origin',ratio.subs(f,-(1+2*c)/2)-2*K/delta)
    phi=z*(-(1+2*c)/2+F1*(s+z*z));q=z*z*(Q+G1*(s+z*z))
    ws=2*s*(c-S.diff(phi,z));wz=c*z+2*phi+2*s*S.diff(phi,s)
    rq=S.Poly(S.expand((1-2*S.diff(phi,z))*q+ws*S.diff(q,s)+wz*S.diff(q,z)),s,z)
    check('radial seed sz2',rq.coeff_monomial(s*z*z)-gamma*G1-6*Q*F1)
    check('radial seed z4',rq.coeff_monomial(z**4)+2*delta*G1+2*Q*F1)
    eta=-4*s*S.diff(phi,s,2)-8*S.diff(phi,s)-S.diff(phi,z,2)
    check('radial seed eta linear',S.expand(eta).coeff(z,1)+14*F1)
    check('positive determinant',6*delta-gamma-(5+2*c))
    atomic_json(ROOT/'results/t3_budgets_tests.json',dict(all_passed=True,case_count=len(rows),rows=rows,elapsed_seconds=time.perf_counter()-start))
    print('PASS',len(rows),time.perf_counter()-start)
if __name__=='__main__':main()
