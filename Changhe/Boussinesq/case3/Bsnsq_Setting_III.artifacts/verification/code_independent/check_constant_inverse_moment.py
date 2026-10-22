"""Ordinary full-plane moment checks, reduced analytically to a radial integral."""
from pathlib import Path
from datetime import datetime, timezone
import json, math, time
from scipy.integrate import quad
start=time.monotonic()

def source(r,sigma):
    a=(1-sigma)/2
    return -r*(8*a*(1+r*r)**(a-1)+4*r*r*a*(a-1)*(1+r*r)**(a-2))
def difference(r,sigma):
    a=(1-sigma)/2
    lead=-(1-sigma)*(3-sigma)*r**(-sigma)
    if r<=1:
        return source(r,sigma)-lead
    u=1/(r*r);p=(a-2)*math.log1p(u)
    return lead*(math.expm1(p)+2*u*math.exp(p)/(a+1))

rows=[]
for beta in [7/3,2.5,8/3]:
    moments=[]
    for j in [1,2,3]:
        sigma=j/beta
        f=(lambda r,s=sigma:difference(r,s)) if j<3 else (lambda r,s=sigma:source(r,s))
        a,ea=quad(f,0,1,epsabs=2e-11,epsrel=2e-11,limit=250)
        b,eb=quad(f,1,math.inf,epsabs=2e-11,epsrel=2e-11,limit=250)
        moments.append({'j':j,'sigma':sigma,'integral':a+b,'absolute_error_vs_exact_2':abs(a+b-2),'quadrature_error_estimate':ea+eb})
    weights=[1,2/7,-3/11]
    estimated=-sum(w*d['integral']/2 for w,d in zip(weights,moments))
    exact=-78/77
    rows.append({'beta':beta,'moments':moments,'estimated_C2':estimated,'exact_C2':exact,'absolute_C_error':abs(estimated-exact)})
result={'timestamp_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'rows':rows,'maximum_moment_error':max(v['absolute_error_vs_exact_2'] for row in rows for v in row['moments']),'scope':'Manufactured inverse only. Quadrature estimates are not interval bounds. Exact integral proof is in PROOF.md section 8.'}
Path('research/90_third_terms_and_constant_velocity/verification/ordinary_moment_manufactures.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
