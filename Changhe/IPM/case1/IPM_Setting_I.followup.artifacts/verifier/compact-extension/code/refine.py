from pathlib import Path
from datetime import datetime,timezone
import json,time
import numpy as np
from scipy.special import roots_legendre
from field import Field
f=Field();root=Path(__file__).resolve().parents[1];rows=[]
for nang,order,width in [(2048,24,.08),(4096,24,.08)]:
 zz,ww=roots_legendre(order);theta=(np.arange(nang)+.371)*2*np.pi/nang;ct,st=np.cos(theta),np.sin(theta)
 ka=np.stack([-ct*st/np.pi,(ct*ct-st*st)/(2*np.pi)])
 for point in [(1.,.5),(np.pi/f.k,.1),(0.,0.)]:
  start=time.monotonic();px,py=point;rv=float(f.rho(px,py));total=np.zeros(2);cs=0.;Rmax=np.hypot(15+abs(px),4+abs(py))
  edges=np.linspace(0,Rmax,int(np.ceil(Rmax/width))+1)
  for a,b in zip(edges[:-1],edges[1:]):
   rad=(a+b)/2+(b-a)/2*zz;rw=(b-a)/2*ww
   values=f.rho(px+rad[:,None]*ct[None,:],py+rad[:,None]*st[None,:])-rv
   total+=np.einsum('ij,kj,i->k',values,ka,rw/rad)*(2*np.pi/nang)
   if point==(0.,0.):cs+=np.einsum('ij,j,i->',values,np.sin(3*theta),rw/rad**2)*(2/nang)
  total[1]-=rv/2;actual=f.U(px,py)
  row={'angles':nang,'radial_order':order,'panel_width':width,'point':list(point),'U_integral':total.tolist(),'U_exact':actual.tolist(),'error':float(np.linalg.norm(total-actual)),'seconds':time.monotonic()-start}
  if point==(0.,0.):row.update(strain=cs,strain_exact=f.H0,strain_error=abs(cs-f.H0))
  rows.append(row);(root/'verification/refine.json').write_text(json.dumps({'date':datetime.now(timezone.utc).isoformat(),'rows':rows},indent=2)+'\n');print(json.dumps(row),flush=True)
