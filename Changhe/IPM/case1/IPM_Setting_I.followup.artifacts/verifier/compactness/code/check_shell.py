"""Independent nonsingular annular kernel check for the compactness examples."""
from pathlib import Path
from datetime import datetime,timezone
import json
import numpy as np
from scipy.integrate import quad
from scipy.special import roots_legendre

def raw(r):
 r=np.asarray(r);out=np.zeros_like(r)
 mask=(r>1)&(r<2)
 out[mask]=np.exp(-1/(r[mask]-1)-1/(2-r[mask]))
 return out

Z=quad(lambda r:r*float(raw(r))/4,1,2,epsabs=1e-15,epsrel=1e-13)[0]
rows=[]
for order in [48,96,192]:
 q,w=roots_legendre(order);r=(q+3)/2;wr=w/2
 theta=(np.arange(512)+.371)*2*np.pi/512
 xx=r[:,None]*np.cos(theta);yy=r[:,None]*np.sin(theta)
 rho=xx*xx*yy*raw(r)[:,None]/Z
 weights=wr[:,None]*r[:,None]*(2*np.pi/512)
 moment=float(np.sum(wr*r*raw(r)/(4*Z)))
 for x,y in [(0.,0.),(.2,.3),(.6,.1),(-.4,.2)]:
  dx=x-xx;dy=y-yy;r2=dx*dx+dy*dy
  u=np.array([np.sum(weights*(-dx*dy/(np.pi*r2*r2))*rho),np.sum(weights*((dx*dx-dy*dy)/(2*np.pi*r2*r2))*rho)])
  exact=np.array([-x,y]);error=float(np.max(np.abs(u-exact)))
  rows.append({'radial_order':order,'angles':512,'point':[x,y],'U':u.tolist(),'exact':exact.tolist(),'max_error':error,'strain_moment':moment})
rec={'date':datetime.now(timezone.utc).isoformat(),'shell_normalization_float':Z,
 'status':'floating manufactured check, proof uses the exact defining integral',
 'max_error':max(r['max_error'] for r in rows),'rows':rows}
Path('verifier/compactness/verification/shell.json').write_text(json.dumps(rec,indent=2)+'\n')
print(json.dumps(rec,indent=2))
