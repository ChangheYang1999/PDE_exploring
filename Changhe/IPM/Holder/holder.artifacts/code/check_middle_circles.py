"""Floating diagnostic only, with exact marginal checks on rounded masses."""
import numpy as np
from numpy.polynomial.legendre import leggauss
from middle_circle_plan import best_plan,cost_of
from pathlib import Path
from datetime import datetime,timezone
import json,time

def run(alpha=.5,n=192,nr=64,m=8):
    gx,gw=leggauss(nr);ts=(gx+1)*np.pi/4;weights=gw*np.pi/4
    ss=-1+(np.arange(n)+.5)*2/n;unit=2**44
    totals=np.zeros(m+1);old=np.zeros(m+1);counts={}
    for t,weight in zip(ts,weights):
        r=np.sin(t);theta=np.pi/2+t*ss;z=r*np.exp(1j*theta)
        G=z/(np.pi*(z*z-.25)**2);W=t*r*np.cos(t)
        index=np.arange(n);same=(2*r*np.sin(t*index/n))**alpha
        opposite=(2*r*np.cos(t*index/n))**alpha
        for j in range(m+1):
            phi=j*np.pi/(2*m)
            density=(np.exp(1j*phi)*G).real*W
            half=[int(round(x*2/n*unit)) for x in density];masses=half+[-x for x in half]
            plan,info=best_plan(masses,same,opposite)
            counts[info['kind']]=counts.get(info['kind'],0)+1
            totals[j]+=weight*cost_of(plan,same,opposite,n)/unit
            aa=abs(G.real)*np.cos(phi);bb=abs(G.imag)*np.sin(phi)
            # Half-plane sum of the four-orbit bound equals half its four-point cost.
            hc=(2*abs(z.real))**alpha;vc=(2*abs(z.imag))**alpha;dc=(2*r)**alpha
            old[j]+=weight*np.sum(np.maximum(aa*hc+bb*(dc-hc),aa*(dc-vc)+bb*vc))*W*2/n
    return dict(alpha=alpha,angles_per_half=n,radial_gauss=nr,phase_intervals=m,middle_cost=totals.tolist(),reflection_cost=old.tolist(),plan_counts=counts)
if __name__=='__main__':
    started=time.monotonic();rows=[run(a) for a in [.1,.5,.75,.9]]
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-started,status='Floating diagnostic only; no continuous mass enclosure',rows=rows)
    Path('data/middle_circle_diagnostic.json').write_text(json.dumps(out,indent=2)+'\n')
    for r in rows:print(r,flush=True)
