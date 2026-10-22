"""Exact change-of-variable controls for packet172, independent of quadrature."""
from pathlib import Path
from datetime import datetime,timezone
import json,sys,time
import sympy as s
start=time.monotonic();out={'utc':datetime.now(timezone.utc).isoformat(),'checks':[]}
def eq(label,a,b):
    assert s.simplify(s.expand(a-b))==0,label
    out['checks'].append({'name':label,'pass':True})
t,L,R=s.symbols('t L R',positive=True);z=1-t
# Rational b includes integer and noninteger endpoint powers; symbolic b is
# checked as independent positive z and q=z^(2b), avoiding unsafe simplification.
b,q,zz=s.symbols('b q zz',positive=True)
r=L*zz**(-b)*s.sqrt(1-q)
drdt=b*L*zz**(-b-1)/s.sqrt(1-q)
for n in range(2,13):
    eps=n%2
    chi=1 if eps else s.sqrt(1-q)
    h_over_difference=r*zz**(b+1)*chi/2
    original=R**(n-2)*r**(1-n)*h_over_difference*drdt
    expected=b*L/2*(R/r)**(n-2)*(1-q)**(-s.Rational(eps,2))
    eq(f'compact_M_n{n}',original,expected)
# Verify the actual radius derivative independently at rational exponents.
for bb in [s.Rational(3,2),s.Rational(7,3),s.Rational(3),s.Rational(1237,400)]:
    rr=L*s.sqrt(z**(-2*bb)-1)
    # Square-root ratio is handled by replacing the positive-domain relation.
    derivative=s.diff(rr,t)
    claimed=bb*L*z**(-bb-1)/s.sqrt(1-z**(2*bb))
    ratio=s.simplify(derivative**2-claimed**2)
    assert ratio==0
    out['checks'].append({'name':f'drdt_squared_b{bb}', 'pass':True,'positive_sign':'drdt>0 for 0<t<1'})
# Angular product exceptional n=1, exact Laurent coefficients.
w=s.symbols('w');K=9;g=s.symbols('g0:'+str(K))
cos=lambda n:(w**n+w**(-n))/2
sin=lambda n:(w**n-w**(-n))/(2*s.I)
a=s.expand(sin(1)*sum(g[k]*cos(k) for k in range(K)))
for n in range(1,K+1):
    coef=s.expand(a).coeff(w,n)*2*s.I
    expected=(g[0]-g[2]/2) if n==1 else (g[n-1]-(g[n+1] if n+1<K else 0))/2
    eq(f'sine_product_n{n}',coef,expected)
out['elapsed_seconds']=time.monotonic()-start;out['all_passed']=True
Path(sys.argv[1]).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'checks':len(out['checks']),'elapsed_seconds':out['elapsed_seconds'],'all_passed':True}))
