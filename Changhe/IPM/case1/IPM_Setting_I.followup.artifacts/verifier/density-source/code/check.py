"""Independent symbolic elliptic identities and smooth quadrupole counterexample."""
import json
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
import sympy as s
from scipy.integrate import quad
x,y=s.symbols('x y',real=True)
a=s.Function('a')(x,y);b=s.Function('b')(x,y);f=s.Function('f')(x,y)
D=s.diff(a,x)+s.diff(b,y);C=s.diff(b,x)-s.diff(a,y)+s.diff(f,x)
checks={
 'laplace_a':s.simplify(s.diff(D,x)-s.diff(C,y)+s.diff(f,x,y)-s.diff(a,x,2)-s.diff(a,y,2)),
 'laplace_b':s.simplify(s.diff(D,y)+s.diff(C,x)-s.diff(f,x,2)-s.diff(b,x,2)-s.diff(b,y,2)),
}
r,q,r0=s.symbols('r q r0',positive=True)
Lambda=1+s.log(r0/r)
primitive=r**(q-3)*(Lambda/(q-3)+1/(q-3)**2)
checks['endpoint_integral']=s.simplify(s.diff(primitive,r)-r**(q-4)*Lambda)
t=s.symbols('t',real=True)
checks['angular_square']=s.integrate(s.cos(2*t)**2,(t,0,2*s.pi))-s.pi
assert all(v==0 for v in checks.values()),checks

def smooth(u):
 if u<=0:return 0.
 if u>=1:return 1.
 aa=np.exp(-1/u);bb=np.exp(-1/(1-u));return aa/(aa+bb)
rows=[]
for eps in [1e-2,1e-3,1e-4,1e-6,1e-8]:
 def chi(r):return smooth((r-eps)/eps)*smooth((.5-r)/.25)
 bounds=[eps,2*eps,.25,.5]
 I=sum(quad(lambda t:chi(np.exp(t)),np.log(lo),np.log(hi),epsabs=1e-11,epsrel=1e-11)[0] for lo,hi in zip(bounds[:-1],bounds[1:]))
 # Direct angular convolution, independent of the modal identity's angular simplification.
 th=(np.arange(4096)+.37)*2*np.pi/4096
 direct=I*np.mean((1-2*np.cos(th)**2)*(-np.cos(2*th)))
 row={'epsilon':eps,'d11_origin_modal':I/2,'d11_origin_angular':direct,'proved_lower_bound':np.log(1/(8*eps))/2,'quadrature_gap':direct-I/2}
 assert direct>=row['proved_lower_bound']-1e-12
 rows.append(row)
result={'date':datetime.now(timezone.utc).isoformat(),'symbolic':{k:str(v) for k,v in checks.items()},'quadrupoles':rows,'status':'checks passed; numerical quadrature illustrates the separate exact argument'}
out=Path(__file__).resolve().parents[1]/'verification/checks.json'
out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
