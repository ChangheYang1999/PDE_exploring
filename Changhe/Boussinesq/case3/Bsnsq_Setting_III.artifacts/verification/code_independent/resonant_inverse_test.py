"""Manufactured whole-plane logarithmic dipole resonance, no solver code.
Omega=x/(1+r^2). Psi=x H(r^2) with H(0)=0 gives the exact relative inverse.
This is a Poisson/inverse test, not a Boussinesq profile candidate.
"""
from pathlib import Path
from datetime import datetime,timezone
import time,json,hashlib
import numpy as np
from cartesian_inverse import CartesianInverse,InverseSettings

def h_values(s):
 s=np.asarray(s,dtype=float);h=np.empty_like(s);hp=np.empty_like(s);small=s<1e-3
 z=s[small]
 # H=sum_{k>=1} (-1)^k s^k/[4 k(k+1)].
 hs=np.zeros_like(z);dhs=np.zeros_like(z)
 for k in range(8,0,-1):
  hs=hs*z+(-1)**k/(4*k*(k+1));dhs=dhs*z+(-1)**k/(4*(k+1))
 h[small]=z*hs;hp[small]=dhs
 z=s[~small];log=np.log1p(z)
 h[~small]=(1-(1+1/z)*log)/4;hp[~small]=-(z-log)/(4*z*z)
 return h,hp

def omega(x,y):return np.asarray(x)/(1+np.asarray(x)**2+np.asarray(y)**2)
def velocity(points):
 x,y=np.asarray(points).T;s=x*x+y*y;h,hp=h_values(s)
 return np.column_stack((-2*x*y*hp,h+2*x*x*hp))

points=np.array([[0,0],[.001,.002],[.17,.41],[1.13,-.73],[0,2.1],[6.3,3.7]])
start=time.monotonic();out={'started_utc':datetime.now(timezone.utc).isoformat(),'scope':'Manufactured logarithmic-resonance full-plane inverse only; not a B2 profile.',
 'field':'Omega=x/(1+r^2); Psi=x/4*[1-(1+1/r^2)log(1+r^2)], analytically continued at r=0; relative velocity at0 is0.',
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'points':points.tolist(),'exact_relative_velocity':velocity(points).tolist(),'runs':[]}
for radius in (8.,16.,32.):
 for order in (12,24,48):
  v=CartesianInverse(omega,InverseSettings(radius=radius,core_radial_order=order,core_angular_order=order,exterior_radial_order=order,exterior_angular_order=order,decay_power=1.))
  full=v.relative(points);cut=v.relative(points,include_exterior=False)
  row={'radius':radius,'order':order,'full_error':float(np.max(abs(full-velocity(points)))),'without_exterior_error':float(np.max(abs(cut-velocity(points)))),'computed':full.tolist()};out['runs'].append(row);print(row['radius'],row['order'],row['full_error'],row['without_exterior_error'],flush=True)
out['truncated_center_drift']=[{'R':r,'U2_at0_circular':float(np.log1p(r*r)/4)} for r in [1.,10.,100.,1000.,1e6]]
out['ended_utc']=datetime.now(timezone.utc).isoformat();out['elapsed_seconds']=time.monotonic()-start
Path('verification/resonant_inverse.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['elapsed_seconds'],flush=True)
