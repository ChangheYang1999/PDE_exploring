from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,math
import numpy as np
import sympy as s
from numpy.polynomial.legendre import leggauss
D=Path(__file__).resolve().parents[1]
n=s.symbols('n',integer=True,nonnegative=True)
scale=s.simplify(2**(3*n)*2**(-4*n)*2**(-n)*2**(2*n))
assert scale==1
z,nu,lam=s.symbols('z nu lam',positive=True)
identity=s.simplify((1+lam**2*z**2/nu**2)-(lam**2*(lam**-2+z**2/nu**2)))
assert identity==0
# Coordinates zeta=t nu^2 have positive Jacobian nu^2.
t=s.symbols('t',positive=True)
jac=s.det(s.Matrix([t*nu**2,nu]).jacobian([t,nu]));assert jac==nu**2
assert s.simplify(nu**-4*(t**2*nu**2)**s.Rational(-1,2)*jac - nu**-3/t)==0
# In log(t) coordinates dt=t dz; u(e^z)/t*dt=u(e^z)dz.
records=[]
for order in (32,64,96):
 x,w=leggauss(order);v=1+.1*x;z=.25+.05*x
 vw=.1*w;zw=.05*w
 tt=np.exp(z);u=tt**-.5*np.exp(-z*z)*np.sin(2*np.pi*z)
 theta=np.exp(-1/(1-x*x))
 tensor=vw[:,None]*zw[None,:]*theta[:,None]*theta[None,:]
 vals=[]
 for nval in (0,1,2,4,8,12,20):
  amp=v[:,None]**-2/(2.**(-2*nval)+(tt[None,:]*v[:,None])**2)**.5
  val=float(np.sum(tensor*amp*u[None,:]*tt[None,:])/(2*np.pi)**2)
  assert val>0
  vals.append({'n':nval,'scaled_projection':val})
 limit=float(np.sum(tensor*v[:,None]**-3*u[None,:])/(2*np.pi)**2)
 assert 0<vals[-1]['scaled_projection']<=limit*(1+1e-14)
 assert all(a['scaled_projection']<b['scaled_projection']for a,b in zip(vals,vals[1:]))
 records.append({'order':order,'scaled_values':vals,'positive_limit':limit})
err=max(abs(a['scaled_projection']-b['scaled_projection'])for a,b in zip(records[-1]['scaled_values'],records[-2]['scaled_values']))
ans={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'PASS','exact_scaling_exponent':str(scale),'exact_angular_factor_identity':str(identity),'coordinate_jacobian':str(jac),'limiting_integrand_identity':'PASS','quadratures':records,'order64_to96_max_difference':err,'proof_sha256':hashlib.sha256((D/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact finite algebra and illustrative quadrature. Analytic positivity and non-C1 proof are in PROOF.md; no interval enclosure or profile computation.'}
(D/'verification/check.json').write_text(json.dumps(ans,indent=2)+'\n');print(json.dumps(ans,indent=2))
