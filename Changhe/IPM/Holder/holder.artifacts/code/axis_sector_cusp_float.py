"""Exploratory one-dimensional formula for the distance-sector cusp."""
import math,json,argparse
from datetime import datetime,timezone
from scipy.integrate import quad
from axis_clamp_layercake_float import line,negative_mass_magnitude as old_negative,arc_primitive
A=.5;RT2=math.sqrt(2);RT3=math.sqrt(3)
def pos(u,s,p,b):
 v=max(u,s);w=A-RT2*max(s,p);ans=0.
 if v<w:ans+=line(-1,w,v,w)
 d1=-A-RT2*max(s,p);d2=((RT3-1)*b-A-2*s)/RT3;k=(d2-d1)/(1-1/RT3);z=max(u,A+RT2*max(s,p),A-(RT3-1)*b+2*s)
 if z<k:ans+=line(1,d1,z,k)
 return 2*(ans+line(1/RT3,d2,max(z,k)))
def mid(u,s,p,b):
 w=A-RT2*p;ans=0.
 if u<w:ans+=line(-1,w,u,w)
 d1=-A-RT2*p;d2=((RT3-1)*b-A+2*s)/RT3;k=(d2-d1)/(1-1/RT3);z=max(u,A+RT2*p)
 if z<k:ans+=line(1,d1,z,k)
 return 2*(ans+line(1/RT3,d2,max(z,k)))
def neg(u,s,b):
 assert u>=A-1e-10 and u>=s-1e-10
 l=A+b-s/RT2;r=A+b-s/2;ans=0.
 if u<l:ans+=line(1,-A+RT2*s,u,l)
 low=max(u,l)
 if low<r:ans+=arc_primitive(r,b,s)-arc_primitive(low,b,s)
 return 2*(ans+line(1/RT3,((RT3-1)*b-A+2*s)/RT3,max(u,r)))
def evaluate(alpha,b,t):
 assert -.5<=t<=0 and b>=.5
 c=2**(alpha-1);q0=t+.5;U=lambda w:(w/c)**(1/alpha)
 fp=lambda r:pos(U(abs(r+t)),U(r),(r+q0)**(1/alpha),b)
 fm=lambda q:mid(U(.5-q),U(q0-q),q**(1/alpha),b)
 fn=lambda r:neg(U(r+.5),U(r+q0),b)
 opts=dict(epsabs=1e-8,epsrel=1e-8,limit=400)
 vals=[];errs=[]
 for fun in [fp,fn]:
  x,e=quad(fun,0,1,**opts);y,f=quad(lambda u:fun(1/u)/u**2,0,1,**opts);vals.append(x+y);errs.append(e+f)
 m,e=quad(fm,0,q0,**opts) if q0>0 else (0.,0.)
 return dict(alpha=alpha,b=b,t=t,value=1+2*(sum(vals)+m),parts=dict(plus=vals[0],mid=m,low=vals[1]),estimated_error=2*(sum(errs)+e),status='Exploratory quadrature, not a certificate')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--alpha',type=float,default=.5);p.add_argument('--b',type=float,default=.5);p.add_argument('--shift',type=float,default=0);a=p.parse_args();v=evaluate(a.alpha,a.b,a.shift);v['time_utc']=datetime.now(timezone.utc).isoformat();print(json.dumps(v,indent=2))
