"""Independent full-half-plane test of temperature quotient fluxes.

Uses the explicit transport-only beta2 manufacture of packet20, not a
numerics-lane source. Both Cartesian infinite tails are included. The
vorticity transport fails and no B2 candidate is claimed.
"""
import os
os.environ['OMP_NUM_THREADS']='1'
os.environ['OPENBLAS_NUM_THREADS']='1'
from pathlib import Path
from datetime import datetime,timezone
import numpy as np,json,time
from numpy.polynomial.legendre import leggauss
start=time.monotonic()
ng,wg=leggauss(160)
snodes=1.5+.5*ng
raw=lambda s: np.exp(-1/((s-1)*(2-s)))
Z=np.sum(.5*wg*raw(snodes))
bweights=.5*wg*raw(snodes)/Z
m1=np.sum(bweights*snodes);m2=np.sum(bweights*snodes**2)
mlog=np.sum(bweights*np.log(snodes));M=np.sum(bweights*(.75*snodes-.5)**2)

def lowmom(stop):
 stop=np.asarray(stop)
 length=np.clip(stop-1,0,1)
 pts=1+length[...,None]*(ng+1)/2
 den=(pts-1)*(2-pts)
 val=np.zeros_like(den)
 np.exp(np.divide(-1,den,out=np.full_like(den,-np.inf),where=den>0),out=val)
 ww=length[...,None]*wg/2*val/Z
 return [np.sum(ww*f(pts),axis=-1) for f in [lambda s:np.ones_like(s),lambda s:s,lambda s:s*s,np.log,lambda s:(.75*s-.5)**2]]

def yfields(y):
 y=np.asarray(y);inside=(y>1)&(y<2)
 h=np.where(y<=1,m1,y);H=np.where(y<=1,m1*y,.5*(y*y+m2));hp=np.where(y<=1,0.,1.)
 if np.any(inside):
  c,z1,z2,_,_=lowmom(y[inside]);v=y[inside]
  h[inside]=v*c+m1-z1;H[inside]=.5*(v*v*c+z2)+v*(m1-z1);hp[inside]=c
 g=m1/h;gp=-m1*hp/h**2;f=4*H/h-2*y;fp=2-4*H*hp/h**2
 return g,gp,f,fp

def ifields(I):
 I=np.asarray(I)
 chi=np.ones_like(I);eta=np.zeros_like(I)
 big=I>=2;mid=(I>1)&(I<2)
 chi[big]=np.exp(2*mlog)/I[big]**2;eta[big]=1.
 if np.any(mid):
  c,_,_,l,_=lowmom(I[mid]);eta[mid]=c;chi[mid]=np.exp(-2*(np.log(I[mid])*c-l))
 ichi=-2*chi*eta
 F=np.where(I<=.25,I*I,M);Fm=(I>.25)&(I<1)
 if np.any(Fm):
  c,_,_,_,t2=lowmom((I[Fm]+.5)/.75);F[Fm]=t2+I[Fm]**2*(1-c)
 ratio=np.divide(F,I*I,out=np.ones_like(I),where=I!=0)
 return chi,ichi,ratio,F

def nodes(n,a,b=None):
 z,w=leggauss(n);t=(z+1)/2;w=w/2
 if b is None:return a+t/(1-t),w/(1-t)**2
 return a+(b-a)*t,w*(b-a)

rows=[]
for n in (24,48,96):
 Is=[];Iws=[]
 for a,b in [(0.,.25),(.25,1.),(1.,2.),(2.,None)]:
  x,w=nodes(n,a,b);Is.extend(x);Iws.extend(w)
 ys=[];yws=[]
 for a,b in [(0.,1.),(1.,2.),(2.,None)]:
  x,w=nodes(n,a,b);ys.extend(x);yws.extend(w)
 I=np.array(Is);wi=np.array(Iws);y=np.array(ys);wy=np.array(yws)
 g,gp,f,fp=yfields(y);chi,ichi,ratio,F=ifields(I)
 P=ratio[:,None]*g[None,:]**2
 v=-chi[:,None]*fp[None,:]-ichi[:,None]*(f*gp/g)[None,:]
 measure=2*wi[:,None]*wy[None,:]/g[None,:]
 powers=[]
 for p in (1.5,2.,3.):
  un=float(np.sum(measure*P**p));vn=float(np.sum(measure*v*P**p));target=(2/p-2)*un
  powers.append({'p':p,'integral_Pp':un,'integral_vPp':vn,'identity_rhs':target,'signed_error':vn-target,'relative_error':abs(vn-target)/max(abs(vn),abs(target))})
 vp1=float(np.sum(measure*v*P))
 theta=[];wt=[]
 bounds=sorted([0.,np.arctan(m1/1.),np.arctan(m1/.25),np.pi/2])
 for a,b in zip(bounds[:-1],bounds[1:]):
  x,w=nodes(n,a,b);theta.extend(x);wt.extend(w)
 theta=np.array(theta);wt=np.array(wt)
 Iang=m1/np.tan(theta)
 _,_,_,Fang=ifields(Iang)
 h=Fang
 integral_p0=float(2*np.sum(wt*h/np.cos(theta)**2))
 rows.append({'order':n,'powers':powers,'critical_integral_vP':vp1,'critical_angular_p0':integral_p0,'critical_lhs_2int_p0':2*integral_p0,'critical_rhs_minus2int_vP':-2*vp1,'critical_signed_error':2*integral_p0+2*vp1})
result={'status':'COMPLETE','claim':'transport-only manufacture, not a B2 profile','moments':{'m1':float(m1),'m2':float(m2),'M':float(M),'mlog':float(mlog)},'rows':rows,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start}
Path('research/50_axis_quotients_full_class/verification/manufacture.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
