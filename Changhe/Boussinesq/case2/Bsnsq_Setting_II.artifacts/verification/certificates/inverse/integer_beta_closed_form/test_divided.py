#!/usr/bin/env python3
"""Check smooth quotient traces by differentiating the original PDE defects."""
from pathlib import Path
from datetime import datetime,timezone
import json,time
import mpmath as mp
import numpy as np
import exact_inverse as inv
from manufactured import original

start=time.monotonic();mp.mp.dps=85;rows=[]
for b in (2,3,4):
    ca=np.array([[1.,.25,-.125,.0625],[.5,-.25,.125,0],[-.25,.125,0,.0625]])
    cg=np.array([[14.,-2.,.25,.125],[1.,-.5,0,.25],[2.,0,-.125,.0625]])
    comp=inv.compiler(ca,cg,b)
    def psi(x,y):return inv.polar(comp,mp.sqrt(x*x+y*y),mp.atan2(y,x))[0]
    def defects(x,y):
        th,om=original(ca,cg,b,x,y)
        thx=mp.diff(lambda z:original(ca,cg,b,z,y)[0],x)
        thy=mp.diff(lambda z:original(ca,cg,b,x,z)[0],y)
        omx=mp.diff(lambda z:original(ca,cg,b,z,y)[1],x)
        omy=mp.diff(lambda z:original(ca,cg,b,x,z)[1],y)
        w1=b*x-mp.diff(lambda z:psi(x,z),y)
        w2=b*y+mp.diff(lambda z:psi(z,y),x)
        return w1*thx+w2*thy-(b-2)*th,w1*omx+w2*omy+om-thx
    for xs,ys in [('2','0'),('0','2'),('-2','0'),('0','-2'),('.7','.3')]:
        x,y=mp.mpf(xs),mp.mpf(ys);d=inv.divided(comp,x,y)
        if y==0:
            refs=[mp.diff(lambda z:defects(x,z)[0],0)/x**2,mp.diff(lambda z:defects(x,z)[1],0)/x]
        elif x==0:
            refs=[mp.diff(lambda z:defects(z,y)[0],0,2)/(2*y),mp.diff(lambda z:defects(z,y)[1],0)/y]
        else:
            raw=defects(x,y);refs=[raw[0]/(x*x*y),raw[1]/(x*y)]
        errors=[abs(d[k]-v) for k,v in zip(('R_Theta_div','R_Omega_div'),refs)]
        if x and y:
            cart=inv.cartesian(comp,x,y)
            errors.extend([abs(d['N_Theta_div']-cart['N_Theta']/abs(x*x*y)),abs(d['N_Omega_div']-cart['N_Omega']/abs(x*y))])
        assert max(errors)<mp.mpf('1e-62'),(b,xs,ys,errors)
        rows.append({'beta':b,'x':xs,'y':ys,'max_error':inv.dec(max(errors))})
    # Rational moment, direct row sums, and exact coefficient cancellation at the origin.
    mm=inv.moments(ca,cg,comp);at0=inv.divided(comp,0,0)
    def m(k):v=mm[k];return mp.mpf(v.numerator)/v.denominator
    assert abs(at0['R_Theta_div']+(m('c')-(2*b+2))*m('a0'))<mp.mpf('1e-80')
    assert abs(at0['R_Omega_div']-m('jet_defect'))<mp.mpf('1e-80')
record={'timestamp_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'status':'PASS','dps':85,'checks':rows,'code_sha256':inv.sha(inv.__file__),'test_sha256':inv.sha(__file__),'scope':'Manufactured tests by differentiation of original Cartesian PDE. No interval bound.'}
(inv.ROOT/'verification/divided_manufactured.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
