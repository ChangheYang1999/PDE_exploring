"""Exact radial integrals with the optimal spatial Cauchy-Schwarz scale."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as s
from flint import arb,ctx
import json
ctx.prec=384
r,t=s.symbols('r t',positive=True)
p=1-126*t**5+420*t**6-540*t**7+315*t**8-70*t**9

def aa(x):return arb(int(s.numer(x)))/arb(int(s.denom(x)))
def integral(expr,lower,upper):
    poly=s.Poly(s.expand(expr*r),r)
    rational=s.Rational(0);logcoeff=s.Rational(0)
    for (degree,),coef in poly.terms():
        power=degree-1
        if power==-1:logcoeff+=coef
        else:rational+=coef*(upper**(power+1)-lower**(power+1))/(power+1)
    return rational,logcoeff

def radial_integrals(q):
    ans=[[s.Rational(0),s.Rational(0)] for _ in range(3)]
    low=s.expand(1-p.subs(t,(q*r-1)/(q-1)))
    high=s.expand(p.subs(t,(r-1)/(q-1)))
    for f,lo,hi in [(low,1/q,s.Integer(1)),(high,s.Integer(1),q)]:
        exprs=[r*f*f,r*s.diff(f,r)**2,r*(s.diff(f,r,2)+s.diff(f,r)/r)**2]
        for k,expr in enumerate(exprs):
            ra,lc=integral(expr,lo,hi)
            ans[k][0]+=ra;ans[k][1]+=lc
    vals=[aa(ra)+aa(lc)*aa(q).log() for ra,lc in ans]
    return ans,vals
base=Path(__file__).resolve().parents[2]
params={state:json.loads((base/f'source_audit/state{state:03d}_exact.json').read_text())['exact_parameters'] for state in [88,131]}
records=[]
for q in [s.Rational(21,20),s.Rational(11,10),s.Rational(23,20),s.Rational(6,5),s.Rational(5,4),s.Rational(4,3),s.Rational(3,2),s.Rational(2)]:
    exact,(A,B,C)=radial_integrals(q)
    cq=(B+(A*C).sqrt()).sqrt()
    scale=(A/C).sqrt()
    rec={'q':str(q),'radial_integrals':{name:{'rational':str(ra),'log_coefficient':str(lc)} for name,(ra,lc) in zip(['A','B','C'],exact)},'scale_t':scale.str(70),'kernel_L1_upper_bound':cq.str(70),'inverse_bounds':{}}
    for state in [88,131]:
        sigma=s.Rational(params[state]['sigma']);alpha=s.Rational(1,2);beta=aa(alpha-sigma)
        inv=cq*aa(q)**(-2*beta)/(1-aa(q)**beta)/(1-aa(alpha))
        safe=int(float(inv))+1
        assert inv < arb(safe)
        rec['inverse_bounds'][str(state)]={'sigma_exact':str(sigma),'alpha':'1/2','bound':inv.str(70),'safe_integer':safe}
    records.append(rec)
    print(q,cq.str(12),rec['inverse_bounds']['131']['bound'][:55],flush=True)
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'formula':'C_q <= sqrt(B+sqrt(A*C)), optimized in spatial Cauchy-Schwarz scale t=sqrt(A/C)','records':records,'scope':'The inverse constants refer to q-dependent norm N_(alpha,sigma,q), not the ordinary Holder seminorm.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
