#!/usr/bin/env python3
"""Exact resonance enumeration and equatorial transport coefficient check."""
from pathlib import Path
from fractions import Fraction
import time
import sympy as S
from independent_artifacts import atomic_json
ROOT=Path(__file__).resolve().parents[1]
def main():
    start=time.perf_counter();rows=[]
    def check(name,condition):
        if not condition:raise AssertionError(name)
        rows.append(dict(name=name,passed=True))
    def modes(even,limit):
        out=[]
        for j in range(1,limit//2):
            for k in range(3,limit-2*j+1):
                if even and k%2:continue
                den=4*j-k+2
                if not den:continue
                c=Fraction(k-2-j,den)
                if Fraction(1,2)<c<Fraction(3,4):out.append((2*j+k,j,k,c))
        return sorted(out)
    even=modes(True,50);all_modes=modes(False,30)
    check('first even mode',even[0]==(36,8,20,Fraction(5,7)))
    check('second even mode',even[1]==(40,9,22,Fraction(11,16)))
    check('third even mode',even[2]==(44,10,24,Fraction(2,3)))
    check('first unrestricted mode',all_modes[0]==(19,4,11,Fraction(5,7)))
    for degree,j,k,c in even+all_modes:
        check(f'divisor {j},{k},{c}',j*(1+4*c)+(1+c)*(2-k)==0)
    r,z,a=S.symbols('r z a');f=S.Function('f')(r);b=S.Function('b')(r);g=S.Function('g')(r)
    residual=S.expand((f+S.Function('f2')(r)*z*z)*S.diff(g*z*z,r)+(b*z+S.Function('b3')(r)*z**3)*S.diff(g*z*z,z)-a*g*z*z)
    check('equatorial z2 transport',S.expand(residual.coeff(z,2)-(f*S.diff(g,r)+(2*b-a)*g))==0)
    delta,K,Q=S.symbols('delta K Q',nonzero=True)
    eta=S.cancel(2*(Q*z*z)*(Q*z*z-K)/(-delta*z))
    check('axis eta slope',S.expand(eta).coeff(z,1)==2*K*Q/delta)
    atomic_json(ROOT/'results/t3_equatorial_zero_tests.json',dict(all_passed=True,case_count=len(rows),rows=rows,elapsed_seconds=time.perf_counter()-start,
        even_modes=[dict(degree=d,j=j,k=k,c_l=str(c)) for d,j,k,c in even]))
    print('PASS',len(rows),time.perf_counter()-start)
if __name__=='__main__':main()
