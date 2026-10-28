"""Floating search within the proved extended family; no certificate."""
from pathlib import Path
from datetime import datetime,timezone
from finite_projection_diagnostic import amplitude
from numpy.polynomial.legendre import leggauss
from scipy.special import gamma
import numpy as np,json

def evaluate(alpha,a,nr=256,nt=320):
    rho=min(1.,a/7);delta=min(rho/4,.25);R=4096.;gx,gw=leggauss(nr);tx,tw=leggauss(nt);total=0.
    for left,right in [(delta,.5),(.5,2.),(2.,R)]:
        ul,ur=np.log(left),np.log(right);r=np.exp((ul+ur)/2+(ur-ul)/2*gx)[:,None]
        limit=np.where(r<=.5,np.pi,np.arccos(np.clip(-.5/r,-1,1)))
        theta=limit*(tx+1)[None,:]/2;X=np.maximum(.5+r*np.cos(theta),0);Y=np.maximum(r*np.sin(theta),0)
        nu=(X-.5)*Y/(np.pi*r**4)-(X+.5)*Y/(np.pi*((X+.5)**2+Y**2)**2)
        total+=np.sum(2*nu*amplitude(X,Y,alpha,a,rho)*r*r*limit*gw[:,None]*tw[None,:])*(ur-ul)/4
    A=gamma((alpha+2)/2)/(2*np.sqrt(np.pi)*gamma((alpha+3)/2));local=2*A*delta**alpha/alpha
    loss=2*alpha*delta/(np.pi*(1-2*delta))+2*(1+delta)*delta**(alpha+3)/((1-delta)**4*(alpha+3))
    L=R-.5;tail=2**alpha*L**(alpha-1)/((1-alpha)*(1-1/(4*L*L))**2)
    return dict(alpha=alpha,a=a,rho=rho,delta=delta,regular=float(total),unnormalized_lower_expression=float(total+local-loss-tail+.5))
if __name__=='__main__':
    rows=[evaluate(alpha,a) for alpha in [.25,.3,.4,.5] for a in [.5,1.,1.5,2.]]
    Path('data/finite_projection_extended_diagnostic.json').write_text(json.dumps(dict(time_utc=datetime.now(timezone.utc).isoformat(),status='Floating diagnostic only',rows=rows),indent=2)+'\n')
    for row in rows:print(row,flush=True)
