"""Float checks of the exactly admissible pole-constraint witness."""
from pathlib import Path
from datetime import datetime,timezone
import numpy as np,json
from numpy.polynomial.legendre import leggauss

def base(X,Y,alpha,a):
    dx=X-.5;dy=Y-a
    segment=np.hypot(dx,np.maximum(dy,0))
    projection=.5*dx+np.sqrt(3)/2*dy
    ray=np.where(projection>0,abs(np.sqrt(3)/2*dx-.5*dy),np.hypot(dx,dy))
    dist=np.minimum(np.minimum(segment,ray),Y)
    sign=np.sign(dx-np.maximum(dy,0)/np.sqrt(3))
    return 2**(alpha-1)*sign*dist**alpha

def evaluate(alpha=.5,a=.465,c=.5,n=256,delta=1e-8,R=1e7):
    gx,gw=leggauss(n);parts=[]
    for left,right in [(delta,.5),(.5,2.),(2.,R)]:
        ul,ur=np.log(left),np.log(right)
        r=np.exp((ul+ur)/2+(ur-ul)/2*gx)[:,None]
        angle=np.where(r<=.5,np.pi,np.arccos(np.clip(-.5/r,-1,1)))
        th=angle*(gx+1)[None,:]/2
        X=np.maximum(.5+r*np.cos(th),0);Y=np.maximum(r*np.sin(th),0)
        other=np.hypot(X+.5,Y);F=base(X,Y,alpha,a)
        lower=np.maximum(-c-r**alpha,c-other**alpha)
        upper=np.minimum(-c+r**alpha,c+other**alpha)
        plus=np.clip(F,lower,upper);minus=np.clip(-F,lower,upper)
        nu=(X-.5)*Y/(np.pi*r**4)-(X+.5)*Y/(np.pi*other**4)
        val=(ur-ul)/2*np.sum(nu*(plus-minus)*r*r*angle*gw[:,None]*gw[None,:])
        parts.append(float(val))
    return dict(alpha=alpha,a=a,c=c,order=n,parts=parts,D_diagnostic=sum(parts)+c)

if __name__=='__main__':
    rows=[]
    for a in [.3,.465,.6,1.,1.5]:
        for c in [0.,.1,.2,.3,.4,.5]:
            row=evaluate(a=a,c=c,n=160);rows.append(row);print(row,flush=True)
    Path('data/lattice_pole_diagnostic.json').write_text(json.dumps(dict(time_utc=datetime.now(timezone.utc).isoformat(),status='Floating quadrature only; no numerical lower bound certified',rows=rows),indent=2)+'\n')
