"""Independent direct two-dimensional witness integration; diagnostic only."""
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad
from pathlib import Path
from datetime import datetime,timezone
import json

def witness(X,Y,alpha=.5,a=.5):
    d=np.abs(Y).copy()
    for x0 in [-.5,.5]:
        for sy in [-1,1]:
            dist=np.hypot(X-x0,Y-np.clip(Y,min(0,sy*a),max(0,sy*a)))
            d=np.minimum(d,dist)
            dx=np.sign(x0)/2;dy=sy*np.sqrt(3)/2
            t=np.maximum(0,(X-x0)*dx+(Y-sy*a)*dy)
            d=np.minimum(d,np.hypot(X-x0-t*dx,Y-sy*a-t*dy))
    boundary=.5+np.maximum(np.abs(Y)-a,0)/np.sqrt(3)
    sg=np.where(np.abs(X)>boundary,1,-1)*np.sign(Y)
    return 2**(alpha-1)*sg*d**alpha

def density(X,Y):
    def K(x,y):return x*y/(np.pi*(x*x+y*y)**2)
    return K(X-.5,Y)-K(X+.5,Y)

def main():
    alpha=.5;a=.5;nt=4096
    th=(np.arange(nt)+.5)*2*np.pi/nt;ct=np.cos(th);st=np.sin(th)
    circles=[]
    for r in [1,1.25,1.5,2,3,5,10]:
        x=r*ct;y=r*st
        val=float(np.mean(density(x,y)*witness(x,y,alpha,a))*2*np.pi*r)
        circles.append(dict(r=r,witness=val))
    gl,gw=leggauss(80)
    def radial(lo,hi,cx):
        lr=lo+(gl+1)/2*(hi-lo);r=np.exp(lr[:,None]);x=cx+r*ct;y=r*st
        v=np.mean(density(x,y)*witness(x,y,alpha,a),axis=1)*2*np.pi*np.exp(2*lr)
        return float(np.sum(v*gw)*(hi-lo)/2)
    near=sum(radial(lo,hi,.5) for lo,hi in zip([-28,-20,-12,-6,-3,-1,np.log(.5)],[-20,-12,-6,-3,-1,np.log(.5)]))
    far=sum(radial(lo,hi,0) for lo,hi in zip([0,1,2,4,8,12,20],[1,2,4,8,12,20]))
    a2=2**(1+alpha/2)/(np.pi*(alpha+2));a3=3/np.pi*quad(lambda t:np.sin(3*t)*(2*np.sin(t))**alpha,0,np.pi/6)[0]
    near+=a2/alpha*np.exp(-28*alpha)
    far+=2*a3/(1-alpha)*np.exp(-(1-alpha)*20)
    v=(gl+1)*np.pi/4;r=np.sin(v[:,None]);tt=np.pi/2-v[:,None]+v[:,None]*(gl[None,:]+1)/2
    x=r*np.cos(tt);y=r*np.sin(tt)
    jac=r*np.cos(v[:,None])*v[:,None]
    mid=float(np.sum(density(x,y)*witness(x,y,alpha,a)*jac*gw[:,None]*gw[None,:])*np.pi/2)
    result=dict(time_utc=datetime.now(timezone.utc).isoformat(),circles=circles,near_both=2*near,far=far,middle=mid,total=2*near+far+mid,status='Direct floating diagnostic, not a certificate')
    Path('data/witness_regions_diagnostic.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
