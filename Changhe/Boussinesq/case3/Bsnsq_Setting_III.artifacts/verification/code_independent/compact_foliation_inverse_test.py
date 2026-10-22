"""P220 direct full-plane physical-space velocity quadrature for manufactured data.
Independent analytic Cartesian field derivatives and source-centered polar cubature.
No NUM code, modal inverse, finite box, boundary condition or fitted velocity.
"""
from pathlib import Path
from datetime import datetime,timezone
import time,json,hashlib,resource
import numpy as np
from scipy.special import expit,roots_legendre

def cutoff(s):
 c=np.zeros_like(s);cp=np.zeros_like(s);cpp=np.zeros_like(s);c[s<=4]=1;mask=(s>4)&(s<9)
 u=9-s[mask];v=s[mask]-4;z=1/v-1/u;h=expit(z);hc=expit(-z);zp=-1/v**2-1/u**2;zpp=2/v**3-2/u**3
 c[mask]=h;cp[mask]=h*hc*zp;cpp[mask]=h*hc*((hc-h)*zp*zp+zpp)
 return c,cp,cpp

def fields(x,y):
 x,y=np.broadcast_arrays(np.asarray(x,dtype=float),np.asarray(y,dtype=float));d=1+y*y;a=np.sqrt(d);s=x*x/d;c,cp,cpp=cutoff(s);ay=np.arcsinh(y)
 q=2*ay/a;qp=2/d-2*y*ay/(d*a);qpp=-6*y/(d*d)+(4*y*y-2)*ay/(d*d*a)
 p=x*q-x**3/(3*d*a);px=q-x*x/(d*a);py=x*qp+x**3*y/(d*d*a);lap=-2*x/(d*a)+x*qpp+x**3*(d-5*y*y)/(d*d*d*a)
 sx=2*x/d;sy=-2*y*x*x/(d*d);laps=2/d+x*x*(-2/(d*d)+8*y*y/(d*d*d));sgrad=sx*sx+sy*sy
 omega=-(c*lap+2*cp*(sx*px+sy*py)+p*(cpp*sgrad+cp*laps))
 velocity=np.stack((-c*py-cp*sy*p,c*px+cp*sx*p),axis=-1)
 return velocity,omega

def direct(point,nr,na):
 t,w=roots_legendre(nr);t=(t+1)/2;w=w/2;r=t/(1-t);wr=w/(1-t)**2
 angle=2*np.pi*(np.arange(na)+.371)/na;cs=np.cos(angle);sn=np.sin(angle)
 _,om=fields(point[0]+r[:,None]*cs,point[1]+r[:,None]*sn)
 rad=wr@om
 # K(-r e)r=(-sin theta,cos theta)/(2pi), with angular weight2pi/na.
 return np.array([-np.dot(rad,sn),np.dot(rad,cs)])/na

if __name__=='__main__':
 v=Path('research/220_compact_foliation_manufactured/verification');now=datetime.now(timezone.utc).isoformat();start=time.monotonic();points=np.array([[0,0],[0,.7],[.8,.3],[-.8,.3],[2.5,-1.],[4.,0.]])
 target,_=fields(*points.T);out={'started_utc':now,'method':'Full-plane polar integral centered at each target, r=t/(1-t), Gauss-Legendre in t and periodic angular rule with offset. Independent analytic Cartesian Omega includes cutoff derivatives.','points':points.tolist(),'exact_velocity_float':target.tolist(),'levels':[],'scope':'Manufactured inverse consistency test; quadrature differences are not rigorous bounds; vorticity equation fails exactly.'}
 for nr,na in [(96,128),(192,256),(384,512),(768,1024)]:
  tick=time.monotonic();values=np.array([direct(pt,nr,na) for pt in points]);err=values-target;row={'radial_nodes':nr,'angular_nodes':na,'velocity':values.tolist(),'error_vs_analytic':err.tolist(),'max_abs_error':float(abs(err).max()),'seconds':time.monotonic()-tick};out['levels'].append(row)
  (v/'direct_inverse.json').write_text(json.dumps(out,indent=2)+'\n');print(nr,na,row['max_abs_error'],row['seconds'],flush=True)
 out.update(ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest());(v/'direct_inverse.json').write_text(json.dumps(out,indent=2)+'\n')
