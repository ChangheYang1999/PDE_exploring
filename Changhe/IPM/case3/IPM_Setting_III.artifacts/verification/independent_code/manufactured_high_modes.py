"""High-angular-frequency manufactured inverse tests.

G=Im((x+i*y)^k)*(1+r^2)^a/k^2,
a=(p+2-k)/2, rho=Delta G, psi=-G_x,
U=(G_xy,-G_xx). This defines an exact canonical pair for odd k>=3.
The formulas below use bounded angular functions and log radial powers.
"""
import json,time
from pathlib import Path
from dataclasses import asdict
from datetime import datetime,timezone
import numpy as np
from direct_inverse import DirectInverse,Quadrature

class HighMode:
 def __init__(self,k,p):self.k=k;self.p=p;self.a=(p+2-k)/2
 def components(self,x,y):
  x,y=np.broadcast_arrays(np.asarray(x,float),np.asarray(y,float));r=np.hypot(x,y);theta=np.arctan2(y,x)
  log1=np.log(np.hypot(1.,r))*2
  safe=np.maximum(r,np.finfo(float).tiny)
  factor=np.exp((self.k-2)*np.log(safe)+self.a*log1)/(self.k*self.k)
  t=-np.expm1(-log1);c=np.cos(theta);ss=np.sin(theta);k=self.k;a=self.a
  sn=np.sin(k*theta);sn1=np.sin((k-1)*theta);sn2=np.sin((k-2)*theta)
  cs1=np.cos((k-1)*theta);cs2=np.cos((k-2)*theta)
  rho=4*a*factor*t*((k+1)+(a-1)*t)*sn
  gxx=factor*(k*(k-1)*sn2+4*a*k*c*t*sn1+2*a*t*sn+4*a*(a-1)*c*c*t*t*sn)
  gxy=factor*(k*(k-1)*cs2+2*a*k*t*(ss*sn1+c*cs1)+4*a*(a-1)*c*ss*t*t*sn)
  return np.where(r>0,rho,0.),np.stack((np.where(r>0,gxy,0.),np.where(r>0,-gxx,0.)),axis=-1)
 def rho(self,x,y):return self.components(x,y)[0]

if __name__=='__main__':
 points=np.array([[.3,.7],[3.,-2.],[100.,40.],[5.,.003]])
 cases=[]
 for k,p in [(9,.5),(31,.5),(63,.5),(31,.96)]:
  manufactured=HighMode(k,p);exact=manufactured.components(*points.T)[1]
  for n,nt,ne in [(24,128,64),(40,256,96),(64,512,144),(80,1024,192)]:
   conf=Quadrature(n,nt,ne,4.,1.,p,16.)
   start=time.time();got=DirectInverse(manufactured.rho,conf).velocities(points)
   row={'utc':datetime.now(timezone.utc).isoformat(),'mode':k,'exponent':p,'config':asdict(conf),'points':points.tolist(),'max_absolute_error':float(np.max(abs(got-exact))),'errors':abs(got-exact).tolist(),'seconds':time.time()-start}
   cases.append(row);print(json.dumps(row),flush=True)
   Path('research/inverse/verification/manufactured_high_modes.json').write_text(json.dumps(cases,indent=2)+'\n')
