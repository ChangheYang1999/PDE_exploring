#!/usr/bin/env python3
"""Independent homogeneous equations and symbolic source-maximum factors."""
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
    s,z,c,K,h=S.symbols('s z c K h');eps=c-S.Rational(1,2);delta=1+c
    # Exact rational inputs keep full polynomial substitution independent of
    # the coefficient recurrence without a huge symbolic denominator expansion.
    for c0 in [S.Rational(14,25),S.Rational(3,5),S.Rational(2,3),S.Rational(37,50)]:
        for K0 in [S.Rational(1,2),S.Integer(2)]:
            e0=c0-S.Rational(1,2);d0=1+c0
            for m in range(1,7):
                pp=[S.Rational(7,13)]
                for j in range(m):
                    n=2*m+1-2*j;d=e0*j+d0*(m-j)
                    pp.append(-S.Rational(n*(n-1),4*(j+1)*(j+2))*(1+K0*K0/d**2)*pp[-1])
                aa=[K0*(2*m+1-2*j)*pp[j]/(e0*j+d0*(m-j)) for j in range(m+1)]
                P=sum(pp[j]*s**j*z**(2*m+1-2*j) for j in range(m+1));Q=sum(aa[j]*s**j*z**(2*m-2*j) for j in range(m+1))
                E=-4*s*S.diff(P,s,2)-8*S.diff(P,s)-S.diff(P,z,2)
                L=lambda F:2*e0*s*S.diff(F,s)+d0*z*S.diff(F,z)
                check(f'm{m} c{c0} K{K0} q',L(Q)-2*K0*S.diff(P,z))
                check(f'm{m} c{c0} K{K0} eta',d0*E+L(E)-2*K0*S.diff(Q,z))
    H=1+K*K/(4*delta**2);d1=eps+delta
    p1=-S.Rational(5,2)*H*h;p2=-S.Rational(1,4)*(1+K*K/d1**2)*p1
    A=5*K*h/(2*delta);B=3*K*p1/d1;C=K*p2/(2*eps)
    expected=-25*K*K*h*h*(K*K+4*delta**2)*((13-14*c)*K*K-delta*(56*c*c+28*c-37))/(16*delta**4*(2*c-1)*(4*c+1)**2)
    check('symbolic quartic discriminant',B*B-4*A*C-expected)
    orbit=(S.Rational(25,2)*H*h*h*(S.Rational(7,2)+K*K*(S.Rational(9,8)/delta**2-1/d1**2)))
    check('symbolic orbit monotonicity discriminant',9*p1**2-20*h*p2-orbit)
    critical=(9*S.sqrt(7)-7)/28
    check('critical root',56*critical**2+28*critical-37)
    check('upper endpoint K2',(delta*(56*c*c+28*c-37)/(13-14*c)).subs(c,S.Rational(3,4))-S.Rational(217,20))
    atomic_json(ROOT/'results/t1_source_maximum_tests.json',dict(all_passed=True,case_count=len(rows),rows=rows,elapsed_seconds=time.perf_counter()-start))
    print('PASS',len(rows),time.perf_counter()-start)
if __name__=='__main__':main()
