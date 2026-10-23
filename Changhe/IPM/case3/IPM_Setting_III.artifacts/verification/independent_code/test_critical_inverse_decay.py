"""Manufactured critical/logarithmic and finite-moment inverse tails."""
from pathlib import Path
from datetime import datetime,timezone
import json,math
import numpy as np
import mpmath as mp
from direct_inverse import DirectInverse,Quadrature
mp.mp.dps=55

def expected(x,y,m):
    xx,yy=mp.mpf(x),mp.mpf(y);ss=xx*xx+yy*yy
    if not ss:return np.zeros(2)
    if m==2:I=(mp.log1p(ss)+1/(1+ss)-1)/2
    else:I=ss*ss/(4*(1+ss)**2)
    H=I/ss**2;f=(1+ss)**(-m);J=f-4*H
    return np.array([float(xx*(H+yy*yy*J/ss)),float(-yy*(H+xx*xx*J/ss))])
rows=[]
for m in [2,3]:
    def rho(x,y):return np.asarray(y)/(1+np.asarray(x)**2+np.asarray(y)**2)**m
    errors=[]
    for level,(nr,nt,ne,of) in enumerate([(24,128,96,2.),(40,256,144,4.),(64,512,224,8.)]):
        inv=DirectInverse(rho,Quadrature(nr,nt,ne,of,1.,.5,0.,2.));err=[]
        for r in [.003,.23,1.3,7.,71.,1e4]:
            for th in [.037,.71,math.pi/2]:
                x,y=r*math.cos(th),r*math.sin(th);u=inv.velocity(x,y);v=expected(x,y,m)
                relative=float(np.linalg.norm(u-v)/max(np.linalg.norm(v),1e-300));err.append(relative)
                rows.append({'m':m,'level':level,'r':r,'theta':th,'velocity':u.tolist(),'analytic_velocity':v.tolist(),'relative_error':relative})
        errors.append(max(err));print(json.dumps({'m':m,'level':level,'maximum_relative_error':max(err)}),flush=True)
    assert errors[-1]<3e-7,(m,errors)
# Algebraically separate tests of the logarithmic coefficient and finite moment.
far=[]
for r in [mp.mpf('1e3'),mp.mpf('1e6'),mp.mpf('1e12')]:
    ss=r*r;I2=(mp.log1p(ss)+1/(1+ss)-1)/2;I3=ss*ss/(4*(1+ss)**2)
    assert abs(I2-(mp.log(r)-mp.mpf('.5')))<2/r**2
    assert abs(I3-mp.mpf('.25'))<1/r**2
    far.append({'r':str(r),'critical_scaled_radial_coefficient':str(I2),'predicted_log_coefficient':str(mp.log(r)-mp.mpf('.5')),'finite_moment_scaled_radial_coefficient':str(I3)})
# Direct positive radial integral, independent of the closed stream formula.
mu=mp.pi*mp.quad(lambda r:r**3/(1+r*r)**3,[0,1,mp.inf]);assert abs(mu-mp.pi/4)<mp.mpf('1e-50')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','rows':rows,'far_coefficients':far,'moment':str(mu),'method':'Independent full-plane cancellation-kernel quadrature at three resolutions versus 55-digit explicit canonical streams; no producer code or modal inverse.','scope':'Finite numerical checks of independently proved inverse-tail formulas, without interval enclosures or any transport-profile claim.'}
p=Path('research/critical_inverse_decay/verification/manufactured.json');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':'PASS','rows':len(rows),'utc':out['utc']}),flush=True)
