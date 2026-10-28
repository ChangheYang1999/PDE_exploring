"""Floating quadrature of the finite projection witness. Not a certificate."""
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import gamma
import json

def amplitude(X,Y,alpha,a,rho):
    dx=X-.5;dy=Y-a
    segment=np.hypot(dx,np.maximum(dy,0))
    projection=.5*dx+np.sqrt(3)/2*dy
    ray=np.where(projection>0,abs(np.sqrt(3)/2*dx-.5*dy),np.hypot(dx,dy))
    dist=np.minimum(segment,ray)
    sign=np.sign(dx-np.maximum(dy,0)/np.sqrt(3))
    v=np.hypot(dist,Y)
    pi=np.divide(2*dist*Y,v,out=np.zeros_like(v),where=v>0)
    P=pi**alpha;H=np.maximum(2*X,0)**alpha;B=np.minimum(v,rho)**alpha
    M=np.maximum(0,np.minimum(np.minimum(P,H),.5*(P+H+B-1)))
    return sign*M

def evaluate(alpha,a=.6,nr=320,nt=400):
    rho=a/6;delta=rho/4;R=4096.;gx,gw=leggauss(nr);tx,tw=leggauss(nt)
    total=0.
    for left,right in [(delta,.5),(.5,2.),(2.,R)]:
        ul,ur=np.log(left),np.log(right);uu=(ul+ur)/2+(ur-ul)/2*gx
        r=np.exp(uu)[:,None];limit=np.where(r<=.5,np.pi,np.arccos(np.clip(-.5/r,-1,1)))
        theta=limit*(tx+1)[None,:]/2
        X=np.maximum(.5+r*np.cos(theta),0);Y=np.maximum(r*np.sin(theta),0)
        nu=(X-.5)*Y/(np.pi*r**4)-(X+.5)*Y/(np.pi*((X+.5)**2+Y**2)**2)
        values=2*nu*amplitude(X,Y,alpha,a,rho)*r*r*limit
        total+=np.sum(values*gw[:,None]*tw[None,:])*(ur-ul)/4
    A=gamma((alpha+2)/2)/(2*np.sqrt(np.pi)*gamma((alpha+3)/2))
    local=2*A*delta**alpha/alpha
    localloss=2*alpha*delta/(np.pi*(1-2*delta))+2*(1+delta)*delta**(alpha+3)/((1-delta)**4*(alpha+3))
    L=R-.5;tail=2**alpha*L**(alpha-1)/((1-alpha)*(1-1/(4*L*L))**2)
    lowerlike=(total+local-localloss-tail+.5)/(1+2*alpha*alpha)
    return dict(alpha=alpha,a=a,rho=rho,delta=delta,R=R,regular=total,local_leading=local,local_loss=localloss,tail_error=tail,diagnostic_lower_expression=lowerlike)
if __name__=='__main__':
    rows=[evaluate(alpha,a) for alpha in [.05,.1,.2,.25] for a in [.3,.6,1.]]
    Path('data/finite_projection_diagnostic.json').write_text(json.dumps(dict(time_utc=datetime.now(timezone.utc).isoformat(),status='Floating diagnostic only. Regular integral is not enclosed.',rows=rows),indent=2)+'\n')
    for row in rows:print(row,flush=True)
