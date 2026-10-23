"""Direct-kernel manufactured check of an exact interior affine pair."""
from pathlib import Path
from datetime import datetime,timezone
import json
import numpy as np
from scipy.integrate import quad
from direct_inverse import DirectInverse,Quadrature,cartesian_gradient

def smooth_step(t):
 t=np.asarray(t);ans=np.zeros_like(t,dtype=float);ans[t>=1]=1;mask=(t>0)&(t<1);z=t[mask]
 aa=np.exp(-1/z);bb=np.exp(-1/(1-z));ans[mask]=aa/(aa+bb);return ans

def bump(t):
 t=np.asarray(t);ans=np.zeros_like(t,dtype=float);mask=(t>2)&(t<3);z=t[mask];ans[mask]=np.exp(-1/((z-2)*(3-z)));return ans
J=quad(lambda t:float(bump(t))/t,2,3,epsabs=1e-15,epsrel=1e-13)[0];rows=[]
for a,D in [(1.,.5),(-1.,1.)]:
 b=(a/4-D)/J
 for L in [2.,8.]:
  def rho(x,y):
   x,y=np.broadcast_arrays(x,y);r=np.hypot(x,y);angle=np.divide(y*(3*x*x-y*y),r*r,out=np.zeros_like(r,dtype=float),where=r!=0)
   return a*y*(1-smooth_step(r/L-1))+b*angle*bump(r/L)
  errors=[]
  for level,(nr,nt,ne,of) in enumerate([(24,128,96,2.),(40,256,144,4.),(64,512,224,8.)]):
   inv=DirectInverse(rho,Quadrature(nr,nt,ne,of,L,.5,0.,2.));err=[]
   for x,y in [(0.,.003),(.71,.33),(.2,1.3)]:
    exact=D*np.array([x,-y]);u=inv.velocity(x,y);g=np.array(cartesian_gradient(rho,x,y,.0015,0.));rv=float(rho(x,y));R=((1+D)*np.array([x,y])+u)@g-rv
    row={'a':a,'D':D,'L':L,'level':level,'x':x,'y':y,'velocity':u.tolist(),'exact_velocity':exact.tolist(),'abs_velocity_error':float(max(abs(u-exact))),'R':float(R),'rho':rv,'gradient':g.tolist()};rows.append(row);err.append(row['abs_velocity_error'])
   errors.append(max(err));print(json.dumps({'a':a,'D':D,'L':L,'level':level,'max_error':max(err)}),flush=True)
  assert errors[-1]<5e-7,(a,D,L,errors)
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','J':J,'rows':rows,'scope':'Independently implemented cancellation-kernel inverse and Cartesian FD8 for smooth compact remote strain fields. Exact interior transport and failure of global transport proved in PROOF.md.'}
out=Path('research/near_one_noncompact_limits/verification');(out/'checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':'PASS','utc':result['utc']}),flush=True)
