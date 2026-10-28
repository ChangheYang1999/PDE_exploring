"""Exploratory exact-boundary formula for the axis polygon clamp. NOT a certificate."""
import math, cmath, json
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from scipy.integrate import quad
A=.5

def primitive_line(x,m,d):
    if math.isinf(x): return 0.
    z=complex(x,m*x+d)
    return -np.log1p(-2*A/(z+A)).imag/(2*math.pi) if m==0 else -(np.log1p(-2*A/(z+A))/complex(1,m)).imag/(2*math.pi)

def line(m,d,lo,hi=math.inf):
    if hi<=lo:return 0.
    return primitive_line(hi,m,d)-primitive_line(lo,m,d)

def arc_primitive(x,b,s):
    c=complex(A+b,b);z=complex(x,b+math.sqrt(max(0.,s*s-(x-A-b)**2)))
    aa=np.log1p(-2*A/(z+A))/(2*A)
    bb=-1/((c*c-A*A)*(z-c))-2*c/(c*c-A*A)**2*cmath.log(z-c)+cmath.log(z-A)/(2*A*(A-c)**2)-cmath.log(z+A)/(2*A*(A+c)**2)
    return -A/math.pi*(.5*(aa-s*s*bb)).imag

def positive_mass(u,s,b):
    rt2=math.sqrt(2);rt3=math.sqrt(3)
    ans=0.;lo=max(u,s);hi=A-rt2*s
    if lo<hi: ans+=line(-1,hi,lo,hi)
    d1=-A-rt2*s;d2=((rt3-1)*b-A-2*s)/rt3
    cross=(d2-d1)/(1-1/rt3)
    lo=max(u,A+rt2*s,A-(rt3-1)*b+2*s)
    if lo<cross:ans+=line(1,d1,lo,cross)
    ans+=line(1/rt3,d2,max(lo,cross))
    return 2*ans

def negative_mass_magnitude(u,s,b):
    assert u+1e-10>=A+s
    rt2=math.sqrt(2);rt3=math.sqrt(3)
    left=A+b-s/rt2;right=A+b-s/2
    ans=0.
    if u<left:ans+=line(1,-A+rt2*s,u,left)
    low=max(u,left)
    if low<right:ans+=arc_primitive(right,b,s)-arc_primitive(low,b,s)
    ans+=line(1/rt3,((rt3-1)*b-A+2*s)/rt3,max(u,right))
    return 2*ans

def evaluate(alpha,b):
    c=2**(alpha-1)
    def pu(t):return (t/c)**(1/alpha)
    def first(t):return positive_mass(pu(t),pu(t+.5),b)
    def middle(t):return positive_mass(pu(t),pu(.5-t),b)
    def last(t):return negative_mass_magnitude(pu(t+.5),pu(t),b)
    opts=dict(epsabs=2e-8,epsrel=2e-8,limit=250)
    f1,e1=quad(first,0,1,**opts);f2,e2=quad(lambda u:first(1/u)/u**2,0,1,**opts)
    mid,em=quad(middle,0,.5,**opts)
    n1,en1=quad(last,0,1,**opts);n2,en2=quad(lambda u:last(1/u)/u**2,0,1,**opts)
    return dict(alpha=alpha,b=b,value=1+2*(f1+f2+mid+n1+n2),parts=dict(positive=f1+f2,middle=mid,negative=n1+n2),estimated_quad_error=2*(e1+e2+em+en1+en2))
if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--alpha',type=float,default=.75);p.add_argument('--b',type=float,default=.75);a=p.parse_args();v=evaluate(a.alpha,a.b);v['time_utc']=datetime.now(timezone.utc).isoformat();v['status']='Exploratory quadrature, not a certified lower bound';print(json.dumps(v,indent=2))
