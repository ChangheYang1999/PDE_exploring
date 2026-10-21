"""Independent nonsingular full-plane effect of replacing dnSB's center.
No other lane code; no candidate solver. CPU, one thread, small compact arrays.
"""
from pathlib import Path
import sys,json,hashlib
from datetime import datetime,timezone
import numpy as np
from scipy.special import roots_legendre
from scipy.integrate import quad
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'inverse/code'))
from collocation import NodalDensity
from density import gradient_fd
root=Path(__file__).resolve().parents[1]
source=Path('numerics/data/dnSB_n120m48.npz')
f=NodalDensity(source)

def transition(t):
 t=np.asarray(t);u=np.clip(t,1e-12,1-1e-12)
 aa=np.exp(-1/u);bb=np.exp(-1/(1-u));v=aa/(aa+bb)
 return np.where(t<=0,0,np.where(t>=1,1,v))
def shell_raw(r):
 r=np.asarray(r);u=np.clip(r-1,1e-12,1-1e-12)
 return np.where((r>1)&(r<2),np.exp(-1/u-1/(1-u)),0.)
Z=quad(lambda r:r*float(shell_raw(r))/4,1,2,epsabs=1e-15,epsrel=1e-13)[0]
points=[[5.403023058681398,8.414709848078965],[.20794827803092428,9.99783764189357]]

def invert_compact(x,y,xx,yy,charge):
 dx=x-xx;dy=y-yy;rr=dx*dx+dy*dy
 return np.array([np.sum(-dx*dy/(np.pi*rr**2)*charge),np.sum((dx*dx-dy*dy)/(2*np.pi*rr**2)*charge)])
rows=[]
for order,nang in [(48,512),(96,1024)]:
 zz,ww=roots_legendre(order);th=(np.arange(nang)+.371)*2*np.pi/nang
 ct,st=np.cos(th)[None,:],np.sin(th)[None,:]
 # Fixed shell, source support1<r<2; both observation points have radius10.
 rs=(zz+3)/2;sw=ww/2
 sx=rs[:,None]*ct;sy=rs[:,None]*st
 scharge=(sx*sx*sy*shell_raw(rs)[:,None]/Z)*(sw*rs)[:,None]*(2*np.pi/nang)
 su=[invert_compact(*pt,sx,sy,scharge) for pt in points]
 # Separate integration panels at chi's two transition radii.
 rhat=np.r_[.5*(zz+1),1+.5*(zz+1)];rw=np.r_[ww/2,ww/2]
 for eps in [1/8,1/16,1/32,1/64,1/128]:
  rr=eps*rhat;wr=eps*rw
  xx=rr[:,None]*ct;yy=rr[:,None]*st
  delta=(1-transition(rhat-1))[:,None]*(xx*xx*yy-f(xx,yy))
  rho3=(delta*np.sin(3*th)[None,:]).sum(1)*(2/nang)
  dc=float(np.sum(wr*rho3/rr**2))
  charge=delta*(wr*rr)[:,None]*(2*np.pi/nang)
  values=[]
  for pt,usp in zip(points,su):
   uc=invert_compact(*pt,xx,yy,charge);du=uc-dc*usp;gr=gradient_fd(f,*pt,relative_step=.0005)
   values.append({'point':pt,'core_velocity':uc.tolist(),'core_velocity_over_epsilon8':(uc/eps**8).tolist(),
    'shell_velocity':usp.tolist(),'total_velocity_change':du.tolist(),'transport_change':float(du@gr)})
  rows.append({'radial_order_per_panel':order,'angles':nang,'epsilon':eps,'strain_correction':dc,'strain_over_epsilon4':dc/eps**4,
   'density_difference_max_over_epsilon5':float(np.max(np.abs(delta))/eps**5),'points':values})
  (root/'verification/core.json').write_text(json.dumps({'date':datetime.now(timezone.utc).isoformat(),'source_md5':f.md5,'scope':'floating compact-source checks; exact strain preservation follows from the proof, not rounded quadrature','rows':rows},indent=2)+'\n')
  print(json.dumps(rows[-1]),flush=True)
