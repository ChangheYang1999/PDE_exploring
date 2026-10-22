"""Whole-plane physical inverse on a fixed foliation rectangle with Duffy singularities.
No numerics code imports. The Cartesian analytic source comes from our separate initial
polar implementation; the discretization and singular integration here are different.
"""
from pathlib import Path
from datetime import datetime,timezone
import time,json,hashlib,resource
import numpy as np
from scipy.special import roots_legendre
from scipy.optimize import brentq
from compact_foliation_inverse_test import fields

def ymap(v):return v/(1-v*v)**4

def vmap(y):return 0. if y==0 else brentq(lambda v:ymap(v)-y,-1+1e-8,1-1e-8,xtol=2e-15)

def integrand(k,v,point):
 y=ymap(v);yp=(1+7*v*v)/(1-v*v)**5;a=np.sqrt(1+y*y);x=k*a;om=fields(x,y)[1];dx=point[0]-x;dy=point[1]-y;den=dx*dx+dy*dy
 factor=om*a*yp/(2*np.pi*den)
 return np.stack((dy*factor,-dx*factor),axis=-1)

def direct(point,n):
 pts,w=roots_legendre(n);t=(pts+1)/2;w=w/2;tt=t[:,None];zz=t[None,:];ww=w[:,None]*w[None,:]
 v0=vmap(point[1]);k0=point[0]/np.sqrt(1+point[1]**2)
 sgrid=np.array([0,1,4,4.1,4.3,4.7,5.5,6.5,7.5,8.3,8.7,8.9,9]);kb=np.unique(np.concatenate((-np.sqrt(sgrid),np.sqrt(sgrid),[k0] if abs(k0)<3 else [])))
 vb=np.unique(np.array([-1,1,v0]+[vmap(y)for y in [-100,-10,-3,-1,-.3,0,.3,1,3,10,100]]));val=np.zeros(2);duffy=0
 for kl,kr in zip(kb[:-1],kb[1:]):
  for vl,vr in zip(vb[:-1],vb[1:]):
   if (k0==kl or k0==kr) and (v0==vl or v0==vr):
    ak=(kr if k0==kl else kl)-k0;av=(vr if v0==vl else vl)-v0
    for k,zv in [(k0+ak*tt+np.zeros_like(zz),v0+av*tt*zz),(k0+ak*tt*zz,v0+av*tt+np.zeros_like(zz))]:
     val+=np.sum(integrand(k,zv,point)*(ww*abs(ak*av)*tt)[...,None],axis=(0,1))
    duffy+=1
   else:
    k=kl+(kr-kl)*tt+np.zeros_like(zz);zv=vl+(vr-vl)*zz+np.zeros_like(tt)
    val+=np.sum(integrand(k,zv,point)*(ww*(kr-kl)*(vr-vl))[...,None],axis=(0,1))
 return val,{'panels':(len(kb)-1)*(len(vb)-1),'duffy_panels':duffy,'v0':v0,'k0':k0}

if __name__=='__main__':
 v=Path('research/220_compact_foliation_manufactured/verification');start=time.monotonic();now=datetime.now(timezone.utc).isoformat();points=np.array([[0,0],[0,.7],[.8,.3],[-.8,.3],[2.5,-1.],[4.,0.]])
 target,_=fields(*points.T);out={'started_utc':now,'method':'Full-plane physical-space k=x/sqrt(1+y²), y=v/(1-v²)^4; cutoff panels, Gauss-Legendre and Duffy triangles; no box or exterior omission.','points':points.tolist(),'analytic_velocity':target.tolist(),'levels':[],'scope':'Manufactured consistency only; differences are not rigorous enclosures.'}
 for n in [12,20,32,48,72]:
  tick=time.monotonic();rows=[direct(pt,n)for pt in points];values=np.array([r[0]for r in rows]);err=values-target;row={'order':n,'velocity':values.tolist(),'errors':err.tolist(),'max_abs_error':float(np.max(abs(err))),'seconds':time.monotonic()-tick,'geometry':[r[1]for r in rows]};out['levels'].append(row);(v/'duffy_inverse.json').write_text(json.dumps(out,indent=2)+'\n');print(n,row['max_abs_error'],row['seconds'],flush=True)
 out.update(ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest());(v/'duffy_inverse.json').write_text(json.dumps(out,indent=2)+'\n')
