"""Exact radial polynomial integration and Arb evaluation for selected LP bases."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import sympy as s
from flint import arb,ctx
import json
r,t=s.symbols('r t',positive=True)
p=1-126*t**5+420*t**6-540*t**7+315*t**8-70*t**9
ctx.prec=384

def aa(x):return arb(int(s.numer(x)))/arb(int(s.denom(x)))
def integrate_laurent(expr,lower,upper):
    # The only negative power is r^-1, yielding log(upper/lower).
    poly=s.Poly(s.expand(expr*r),r)
    rational=s.Rational(0);logcoeff=s.Rational(0)
    for (degree,),coef in poly.terms():
        power=degree-1
        if power==-1:logcoeff+=coef
        else:rational+=coef*(upper**(power+1)-lower**(power+1))/(power+1)
    return rational,logcoeff

base=Path(__file__).resolve().parents[2]
d=json.loads((base/'source_audit/state131_exact.json').read_text())
sigma=s.Rational(d['exact_parameters']['sigma']);alpha=s.Rational(1,2);beta=aa(alpha-sigma)
records=[]
for q in [s.Rational(11,10),s.Rational(23,20),s.Rational(6,5),s.Rational(5,4),s.Rational(4,3),s.Rational(3,2),s.Rational(2)]:
    low=s.expand(1-p.subs(t,(q*r-1)/(q-1)))
    high=s.expand(p.subs(t,(r-1)/(q-1)))
    rational=s.Rational(0);logcoef=s.Rational(0)
    for f,lower,upper in [(low,1/q,s.Integer(1)),(high,s.Integer(1),q)]:
        ra,lc=integrate_laurent(r*(f-s.diff(f,r,2)-s.diff(f,r)/r)**2,lower,upper)
        rational+=ra;logcoef+=lc
    J=aa(rational)+aa(logcoef)*aa(q).log()
    cq=(J/2).sqrt()
    inv=cq*aa(q)**(-2*beta)/(1-aa(q)**beta)/(1-aa(alpha))
    safe_integer=int(float(inv))+1
    assert inv < arb(safe_integer), 'upper integer failed Arb certification'
    records.append({'q':str(q),'J_rational':str(rational),'J_log_coefficient':str(logcoef),
        'kernel_L1_upper_bound':cq.str(50),'inverse_upper_bound':inv.str(50),
        'inverse_upper_integer':safe_integer})
    print(q,cq.str(12),inv.str(12),flush=True)
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),
     'state':131,'alpha':str(alpha),'sigma_exact':str(sigma),'records':records,
     'scope':'Arb enclosures of sufficient constants in the q-dependent norm. This is a finite candidate comparison, not a globally optimal constant.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
