"""Exact moment identities and quadrature illustrations for the scalar counterexample."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
import json, hashlib, math
import sympy as sp
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
A=sp.Integer(2);b=sp.Rational(1,2)
identities=[]
for n in range(21):
    log_exponent= -sp.Rational(1,2) + (-sp.Rational(1,2)-n)+1
    assert log_exponent==-n
    assert sp.sin(log_exponent*2*sp.pi/2)==0
    identities.append({'n':n,'log_exponent':str(log_exponent),'sine_factor':'0'})
lam=sp.Rational(-1,2)
assert sp.sin(lam*sp.pi)==-1
assert lam**2/4==sp.Rational(1,16)
x=sp.symbols('x',positive=True)
assert sp.simplify((sp.sqrt(1+x)-sp.sqrt(x))*(sp.sqrt(1+x)+sp.sqrt(x))-1)==0
assert sp.simplify(sp.diff(2*(sp.sqrt(1+x)-1),x)-(1+x)**(-sp.Rational(1,2)))==0
# Composite Gauss quadrature uses the logarithmic variable and a stable cutoff formula.
def grid(order):
    z,w=np.polynomial.legendre.leggauss(order)
    edges=np.linspace(-16,16,65)
    pts=np.concatenate([.5*(r-l)*z+.5*(r+l) for l,r in zip(edges[:-1],edges[1:])])
    weights=np.concatenate([.5*(r-l)*w for l,r in zip(edges[:-1],edges[1:])])
    return pts,weights
const=math.sqrt(math.pi)*math.exp(1/16-math.pi**2)
cutoffs=[1,2,10,100,1e4,1e8]
quad=[]
for order in [24,40]:
    z,w=grid(order);u_dt=np.exp(-z*z+.5*z)*np.sin(2*math.pi*z)
    moments=[]
    for n in range(7):
        value=float(np.dot(w,np.exp(-z*z-n*z)*np.sin(2*math.pi*z)))
        bound=math.sqrt(math.pi)*math.exp(n*n/4)
        assert abs(value)<2e-13*bound
        moments.append(value)
    J=float(np.dot(w,u_dt*np.exp(-z)))
    assert abs(J+const)<2e-15
    cuts=[]
    for K in cutoffs:
        kt=K*np.exp(z);bracket=1/(np.sqrt(1+kt)+np.sqrt(kt))-1
        value=float(2*np.dot(w,u_dt*np.exp(-z)*bracket))
        # The analytic upper estimate on |integral_K^infinity f| derived from (7).
        bounds=[]
        a=Fraction(1)
        for N in range(1,41):
            a*=Fraction(2*N-1,2*N)
            log_bound=math.log(float(a))+.5*math.log(math.pi)+N*N/4-math.log(N-.5)+(.5-N)*math.log(K)
            bounds.append((log_bound,N))
        log_bound,N=min(bounds)
        cuts.append({'K':K,'integral_f_0_K':value,'difference_from_exact_limit':value-2*const,'analytic_tail_bound_evaluated_float':math.exp(log_bound),'bound_N':N,'scope':'Illustrative quadrature, not an interval enclosure; analytic bound concerns exact integrals.'})
    quad.append({'order':order,'moment_values_0_to_6':moments,'J':J,'cutoffs':cuts})
maxdiff=max(abs(a['integral_f_0_K']-b['integral_f_0_K']) for a,b in zip(quad[0]['cutoffs'],quad[1]['cutoffs']))
assert maxdiff<3e-15
result={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'PASS','exact_moment_identities':identities,'exact_rationalization_and_primitive':'PASS','Gaussian_constant_float':const,'Gprime0_float':-const/math.pi**2,'integral_f_exact_limit_float':2*const,'quadrature':quad,'maximum_quadrature_rule_difference':maxdiff,'proof_sha256':hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact symbolic identities and floating illustrative quadrature only. Smoothness and nonvanishing are proved in PROOF.md.'}
(ROOT/'verification/check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items()if k not in ('quadrature','exact_moment_identities')},indent=2))
