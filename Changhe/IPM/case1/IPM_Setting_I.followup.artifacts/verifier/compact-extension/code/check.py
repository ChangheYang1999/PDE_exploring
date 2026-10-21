from pathlib import Path
from datetime import datetime,timezone
import json,math,time
import numpy as np
from scipy.special import roots_legendre
from field import Field
root=Path(__file__).resolve().parents[1]
f=Field();rows=[]
out={'date':datetime.now(timezone.utc).isoformat(),'parameters':{'A':f.A,'cl':f.cl,'X0':f.X,'Y0':f.Y,'cutoff_m':f.m,'I':f.I},'scope':'floating manufactured checks; full proof in PROOF.md','checks':rows}
def save(row):
 rows.append(row);out['date']=datetime.now(timezone.utc).isoformat();(root/'verification/checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(row),flush=True)
# Local identities and independent high-order finite differences.
weights=[4/5,-1/5,4/105,-1/280]
def diff(fun,x,y,axis,h):
 return sum(w*(fun(x+j*h*(axis==0),y+j*h*(axis==1))-fun(x-j*h*(axis==0),y-j*h*(axis==1)))/h for j,w in enumerate(weights,1))
pts=[(1.,.5),(np.pi/f.k,.1),(4.8,1.),(7.,2.5),(12.,1.),(16.,1.)]
for x,y in pts:
 rv=float(f.rho(x,y));g=np.array([f.rho_x(x,y),f.rho_y(x,y)]);u=f.U(x,y);R=float((f.cl*np.array([x,y])+u)@g-rv)
 gx=np.array([diff(f.rho,x,y,i,1e-3) for i in range(2)]);du=np.stack([diff(f.U,x,y,i,1e-3) for i in range(2)],axis=1)
 save({'type':'local_and_fd','point':[x,y],'rho':rv,'U':u.tolist(),'R':R,'rho_gradient_fd_error':float(np.max(np.abs(gx-g))),'elliptic_fd_error':float(-du[1,0]+du[0,1]-g[0]),'divU_fd':float(np.trace(du))})
# Outside support the full-plane inverse is a nonsingular tensor integral and is zero.
for order in [32,64,96]:
 z,w=roots_legendre(order)
 def grid(edges):
  coords=[];weights=[]
  for a,b in zip(edges[:-1],edges[1:]):coords.extend((a+b)/2+(b-a)/2*z);weights.extend((b-a)/2*w)
  return np.array(coords),np.array(weights)
 xs,xw=grid([-15,-10,-5,0,5,10,15]);ys,yw=grid([-4,-2,0,2,4]);xx=xs[:,None];yy=ys[None,:]
 charge=f.rho(xx,yy)*xw[:,None]*yw[None,:]
 for x,y in [(20.,8.),(0.,8.),(20.,0.)]:
  dx=x-xx;dy=y-yy;rr=dx*dx+dy*dy
  u=np.array([np.sum(-dx*dy/(np.pi*rr**2)*charge),np.sum((dx*dx-dy*dy)/(2*np.pi*rr**2)*charge)])
  save({'type':'outside_inverse','order':order,'point':[x,y],'U_integral':u.tolist(),'error':float(np.linalg.norm(u))})
# Independent polar principal value centered at each observation point. The
# integration disk covers the compact support. Angular kernel has zero mean;
# subtracting rho(X) does not change the exact integral and regularizes r=0.
for nang,order,width in [(256,12,.25),(512,16,.125),(1024,20,.1)]:
 zz,ww=roots_legendre(order);theta=(np.arange(nang)+.371)*2*np.pi/nang;ct,st=np.cos(theta),np.sin(theta)
 ka=np.stack([-ct*st/np.pi,(ct*ct-st*st)/(2*np.pi)])
 for point in [(1.,.5),(np.pi/f.k,.1)]:
  start=time.monotonic();px,py=point;rv=float(f.rho(px,py));total=np.zeros(2);Rmax=np.hypot(15+abs(px),4+abs(py))
  edges=np.linspace(0,Rmax,int(np.ceil(Rmax/width))+1)
  for a,b in zip(edges[:-1],edges[1:]):
   rad=(a+b)/2+(b-a)/2*zz;rw=(b-a)/2*ww
   values=f.rho(px+rad[:,None]*ct[None,:],py+rad[:,None]*st[None,:])-rv
   total+=np.einsum('ij,kj,i->k',values,ka,rw/rad)*(2*np.pi/nang)
  total[1]-=rv/2
  actual=f.U(px,py)
  save({'type':'interior_inverse','angles':nang,'radial_order':order,'panel_width':width,'point':list(point),'U_integral':total.tolist(),'U_exact':actual.tolist(),'error':float(np.linalg.norm(total-actual)),'seconds':time.monotonic()-start})
# Sample extrema only locate a failure; the proof guarantees an exact extremum.
xs=np.linspace(0,15,401);ys=np.linspace(0,4,201);vals=f.rho(xs[:,None],ys[None,:]);ind=np.unravel_index(np.argmax(abs(vals)),vals.shape);x,y=xs[ind[0]],ys[ind[1]]
rv=float(f.rho(x,y));g=np.array([f.rho_x(x,y),f.rho_y(x,y)]);u=f.U(x,y);wv=f.cl*np.array([x,y])+u;R=float(wv@g-rv)
save({'type':'sampled_exterior_failure','point':[x,y],'rho':rv,'R':R,'R_report_Nf':abs(R)/(abs(rv)+sum(abs(wv*g)))})
