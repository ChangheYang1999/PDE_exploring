"""FLOAT scan of the signed principal bound. Not a whole-plane certificate.

The copied N4 evaluator is used only within this lane. Exact input and copied
code hashes are recorded separately. Arb evaluates radial coefficients; angular
sampling and the reported grid supremum use binary64. A selected point is then
reevaluated using Arb. No server, remote compute or multiple workers are used.
"""
from pathlib import Path
from fractions import Fraction
from datetime import datetime, timezone
import json, math, time
import numpy as np
from flint import arb, ctx
from n4_radial_copy import Radial, ar, q

root=Path(__file__).resolve().parents[1]
ctx.prec=256
start=time.monotonic()
model=Radial(root/'data/state131_independent.json')
angles=np.linspace(0,math.pi/2,257)
radii=np.exp2(np.linspace(-12,16,225))
records=[]
best=None
for rf in radii:
    r=ar(q(Fraction(float(rf))))
    R=1+r*r;t=r*r/R;u=1/R
    pref={j:R**ar(p)/r**4 for j,p in model.p.items()}
    vals={}
    for name in ('rho_x','rho_y'):
        A,d,kind=model.fields[name]
        coeff={}
        for (j,n),P in A.items():
            coeff[n]=coeff.get(n,arb(0))+pref[j]*model.poly_arb(P,t,u)
        vals[name]=sum(float(v)*(np.sin(n*angles) if kind=='s' else np.cos(n*angles)) for n,v in coeff.items())
    a=vals['rho_x'];b=vals['rho_y']
    # Stable evaluation avoids subtraction when b is positive.
    denom=np.hypot(a,b)+b
    theta=np.where(b>=0,np.divide(a*a,2*denom,out=np.zeros_like(a),where=denom>0),(np.hypot(a,b)-b)/2)
    idx=int(theta.argmax())
    item={'r':float(rf),'angle':float(angles[idx]),'theta_grid':float(theta[idx]),'rho_x':float(a[idx]),'rho_y':float(b[idx])}
    records.append(item)
    if best is None or item['theta_grid']>best['theta_grid']:best=item.copy()
x=Fraction.from_float(best['r']*math.cos(best['angle']))
y=Fraction.from_float(best['r']*math.sin(best['angle']))
pt=model.evaluate(x,y);a=pt['rho_x'];b=pt['rho_y'];z=((a*a+b*b).sqrt()-b)/2
out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':'C1-BASE-S131','label':'FLOAT','scope':'225 radii x 257 angles; no continuum or exterior upper bound',
     'radii_log2_range':[-12,16],'best_grid':best,'selected_point_exact_xy':[str(x),str(y)],'selected_point_arb_theta':z.str(60),
     'selected_point_status':'individual point enclosure, PENDING-N4; not a global upper bound','radial_maxima':records,'elapsed_seconds':time.monotonic()-start}
(root/'verification/principal_scan.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='radial_maxima'},indent=2))
