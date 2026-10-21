from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from math import isqrt,ceil
import json,hashlib
import numpy as np
import sympy as sp
root=Path(__file__).resolve().parents[1]
t=sp.symbols('t',real=True);hxx,hxy,hyy=sp.symbols('hxx hxy hyy',real=True)
ehe=hxx*sp.cos(t)**2+2*hxy*sp.cos(t)*sp.sin(t)+hyy*sp.sin(t)**2
averages=[sp.simplify(sp.integrate(z*ehe/2,(t,0,2*sp.pi))/(2*sp.pi)) for z in [-sp.sin(2*t),sp.cos(2*t)]]
assert averages==[-hxy/4,(hxx-hyy)/8],averages
leading=[sp.simplify(z/2) for z in averages]
assert leading==[-hxy/8,(hxx-hyy)/16]
files=['grid-states/data/dnB_n96m40S.npz','ritz-resolution/data/dnSB_n120m48.npz','domain-states/data/dnB_n96m40SL4.npz','fixed-cl-correction/data/n96m40S_radius0.05.npz','fixed-cl-correction/data/n120m48_S_radius0.05.npz']
rows=[];eps=F(1,10**7)
for name in files:
 p=root.parent/name
 with np.load(p) as d:
  N=int(d['N']);M=int(d['M']);L=F(float(d['L']));k=1/F(float(d['c_l']));b=d['b'];B0=ceil(float(np.max(abs(b))))
  assert np.all(b[0]==1) and 0<k<F(1,5) and L>=1
  H=isqrt(2*N*(2*M-1));H+=H*H<2*N*(2*M-1)
  D=(F(N*N*H*B0)+F(3,2))/L**2
  error=D*eps**4/4;lo=eps**2/8-error;hi=eps**2/8+error
  sourcebound=(1+D*eps**2)*eps**5/(5*(F(1,5)-eps)**2)
  rows.append(dict(source=str(p),md5=hashlib.md5(p.read_bytes()).hexdigest(),N=N,M=M,L=str(L),B0=B0,H=H,D=str(D),cutoff=str(eps),strain_leading=str(eps**2/8),strain_remainder_bound=str(error),strain_remainder_float=float(error),strain_interval=[str(lo),str(hi)],origin_disk_U_bound_at_distance_at_least_one_fifth=str(sourcebound),origin_disk_U_bound_float=float(sourcebound)))
  print(name,'strain leading',float(eps**2/8),'remainder bound',float(error),'origin disk velocity',float(sourcebound),flush=True)
result=dict(date=datetime.now(timezone.utc).isoformat(),angular_averages=list(map(str,averages)),local_inner_coefficient_per_epsilon_squared=list(map(str,leading)),rows=rows,scope='Exact rational center-strain and origin-disk bounds for ideal-node interpolants. No annular quadrature enclosure or local Hessian enclosure.')
(root/'verification/check.json').write_text(json.dumps(result,indent=2)+'\n')
print('ALL_EXACT_CHECKS_PASS')
