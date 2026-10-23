"""Exact independent monomial recurrence vs Fourier jet determinants."""
from pathlib import Path
from datetime import datetime,timezone
import json
import sympy as s
A,a=s.symbols('A a',real=True)
def poly(k):
    result=0
    for j in range(k+1):
        C=s.factorial(2*k+1)/(s.factorial(2*j+1)*s.factorial(2*k-2*j+1))
        result+=C*s.prod(1-a/(2*k+2*i*(A-1)) for i in range(j+1,k+1))
    return s.factor(result)
expected={1:a-4*A,2:3*a*a-(38*A+26)*a+128*A*(A+1),3:(a-8*A-4)*(a*a-(18*A+30)*a+96*A*A+192*A)}
rows=[]
for k in (1,2,3):
    p=poly(k);ratio=s.factor(p/expected[k]);assert not ratio.has(a)
    rows.append({'degree':2*k+1,'criterion':str(p),'ratio_to_independent_Fourier_determinant_polynomial':str(ratio)})
# Test sufficiency of the recurrence on exact rational examples. The harmonic
# coefficient can be nonzero: the two PDEs must still hold exactly.
x,y=s.symbols('x y');cases=[]
for k,AA,aa in [(1,s.Rational(2),s.Rational(8)),(2,s.Rational(3,2),s.Rational(11,3)),(3,s.Rational(11,4),s.Rational(-5)),(5,s.Rational(17,3),s.Rational(70,3))]:
    q=[s.S(0)]*(k+1);q[k]=1
    for j in range(k,0,-1):
        q[j-1]=s.Rational(2*j*(2*j+1),(2*k-2*j+3)*(2*k-2*j+2))*(aa/(2*k+2*j*(AA-1))-1)*q[j]
    h=sum(-aa*(2*j+1)*q[j]/(2*k+2*j*(AA-1))*x**(2*j)*y**(2*k+1-2*j) for j in range(k+1))
    chi=sum(q[j]*x**(2*j+1)*y**(2*k+1-2*j) for j in range(k+1))
    assert s.expand(AA*x*s.diff(h,x)+y*s.diff(h,y)-h+aa*s.diff(chi,x))==0
    assert s.expand(-s.diff(chi,x,2)-s.diff(chi,y,2)-s.diff(h,x))==0
    harmonic=sum((-1)**(k-j)*q[j] for j in range(k+1))
    assert s.factor(harmonic-poly(k).subs({A:AA,a:aa}))==0
    cases.append({'degree':2*k+1,'A':str(AA),'a':str(aa),'P':str(harmonic),'both_PDEs_exact':True})
result={'utc':datetime.now(timezone.utc).isoformat(),'low_degree_comparisons':rows,'exact_PDE_examples':cases,'scope':'All-degree positivity is proved in PROOF.md; finite exact tests are consistency checks.'}
Path('research/all_degree_resonances/verification/exact_checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
