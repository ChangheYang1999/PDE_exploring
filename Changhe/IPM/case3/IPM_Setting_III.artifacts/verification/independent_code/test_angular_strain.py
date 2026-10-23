from pathlib import Path
from datetime import datetime,timezone
import json,numpy as np
from angular_log_inverse import GaussianAngular,AngularLogInverse
r=np.array([.001,.01,.1,.3,1.,2.,3.]);theta=np.array([0.,.07,.37,.81,1.2,np.pi/2])
x=r[:,None]*np.cos(theta);y=r[:,None]*np.sin(theta);r2=x*x+y*y
out=[]
for q,e in [(.3,.04),(-.2,.07)]:
 model=GaussianAngular(q,e)
 P=-q*x*y+e*(x**3*y-x*y**3)
 Px=-q*y+e*(3*x*x*y-y**3);Py=-q*x+e*(x**3-3*x*y*y)
 Pxx=6*e*x*y;Pyy=-6*e*x*y;Pxy=-q+3*e*(x*x-y*y)
 psi_xx=np.exp(-r2)*(Pxx-4*x*Px+(4*x*x-2)*P)
 psi_yy=np.exp(-r2)*(Pyy-4*y*Py+(4*y*y-2)*P)
 psi_xy=np.exp(-r2)*(Pxy-2*x*Py-2*y*Px+4*x*y*P)
 s11=-psi_xy;s12=(psi_xx-psi_yy)/2
 srr=s11*np.cos(2*theta)+s12*np.sin(2*theta)
 srt=-s11*np.sin(2*theta)+s12*np.cos(2*theta)
 B=q*(4-2*r2)+e*(2*x**4-2*y**4-6*x*x+10*y*y-6)
 Bx=-4*q*x+e*(8*x**3-12*x);By=-4*q*y+e*(-8*y**3+20*y)
 gx=y*np.exp(-r2)*(Bx-2*x*B);gy=np.exp(-r2)*((1-2*y*y)*B+y*By)
 gr=gx*np.cos(theta)+gy*np.sin(theta);gt=-gx*np.sin(theta)+gy*np.cos(theta)
 for order in [32,64,128]:
  f=AngularLogInverse(model,order).fields(np.log(r),theta)
  errors={k:float(np.max(abs(f[k]-v))) for k,v in [('Srr',srr),('Srtheta',srt),('grad_radial',gr),('grad_angular',gt)]}
  if order==128:assert max(errors.values())<2e-10,errors
  out.append(dict(q=q,e=e,order=order,points=int(x.size),errors=errors))
result=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS',manufactured_cartesian_checks=out)
Path('research/angular_log_inverse/verification/strain_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
