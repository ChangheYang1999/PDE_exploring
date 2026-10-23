from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,math
import mpmath as mp
import numpy as np
from q_exact_jets import jets,axis_gradient,beta_integral,pack
from q_checkpoint_reader import QCheckpoint

out=Path('research/finite_q_exact_jets/verification');out.mkdir(parents=True,exist_ok=True)
checks=[]
# Closed forms for independent constant-mode densities, including noninteger kappa.
for kap in [F(3,2),F(5,2),F(3),F(9,2),F(7)]:
 for a,b,d in [(F(3,4),F(1,8),F(-1,16)),(F(-2),F(3,5),F(4,7))]:
  j=jets([[a],[b],[d]],kap,F(3,2))
  assert j['c']==-a/4+b*(1+2*kap)/8-d*(1+4*kap)/24
  assert j['H_core']==-b/4+d*(4*kap+1)/((2*kap+1)*(2*kap+2))
  assert j['poisson']==0
  checks.append(dict(kind='closed_constant_modes',kappa=str(kap),a=str(a)))

# Independently differentiated parametric physical density, plus the old
# separately implemented adaptive full-plane harmonic integral.
mp.mp.dps=80
for case in range(1,9):
 M=1+case%4;N=M+3;kap=F(case+3,2);ell=F(7,4)
 coeff=[[F(((case+1)*(j+2)*(k+1))%13-6,32) for k in range(N+1-j)] for j in range(M)]
 je=jets(coeff,kap,ell)
 metadata=dict(N=N,M=M,L=1.,p=float(kap),cl=float(ell),gamma=1-1/float(kap),Lf=1.,gK=1.,mu=0.)
 path=out/f'manufactured_{case}.npz';np.savez(path,u=np.array([float(v) for row in coeff for v in row]),**metadata)
 old=QCheckpoint(path);raw=old.center_and_tail();core2=2.**(-2*float(kap))
 errs={key:abs(float(je[key])-reference) for key,reference in
       [('a',raw['a0']),('c',raw['quadrature'][-1]['c']),('b_core',raw['b']*core2),
        ('e_core',raw['e']*core2),('H_core',raw['quadrature'][-1]['H']*core2)]}
 assert max(errs.values())<5e-10,(case,errs)
 def mpf(v):return mp.mpf(v.numerator)/v.denominator
 def radius(s):return mp.power(2,-mpf(kap))*mp.sqrt(s)*(1-s)**(-mpf(kap))
 def density(s,sign):
  pol=sum(sign**j*s**j*sum(mpf(v)*mp.chebyt(k,2*s-1) for k,v in enumerate(row)) for j,row in enumerate(coeff))
  return radius(s)*(1-s)*pol
 max_derivative=0.
 for s in [F(1,64),F(1,7),F(2,3)]:
  yaxis,xaxis=axis_gradient(je,s);ss=mpf(s)
  independent_y=mp.diff(lambda u:density(u,-1),ss)/mp.diff(radius,ss)
  independent_x=density(ss,1)/radius(ss)
  err=max(abs(independent_y-mpf(yaxis)),abs(independent_x-mpf(xaxis)))
  assert err<mp.mpf('1e-65'),(case,s,err)
  max_derivative=max(max_derivative,float(err))
 checks.append(dict(kind='adaptive_canonical_and_MP80_parametric_derivatives',case=case,errors=errs,max_axis_error=max_derivative))
result=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS',checks=checks,
 scope='10 closed constant-mode identities and eight independent adaptive-inverse/MP80 axis tests. Rational jets are exact for binary saved coefficients. No profile or numerical existence assertion.')
(out/'checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2),flush=True)
