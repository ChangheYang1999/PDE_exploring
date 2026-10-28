from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import ctx,arb
from sympy import symbols,chebyshevt,Poly,expand
import json,hashlib
import angular as A
ctx.threads=1
p=Path(__file__).resolve().parents[1]
mm=A.moments(1044)
obj={'normalization':'probability Beta(1/4,3/2), z=2u-1','beta_parameters':['1/4','3/2'],'recurrence':'(4n+7)m[n+1]=-10m[n]+(4n-7)m[n-1]','moments':[[v.numerator,v.denominator] for v in mm]}
data=p/'evidence/angular_moments.json'
data.write_text(json.dumps(obj,separators=(',',':'))+'\n')
u,z=symbols('u z')
def integrate(poly):
 po=Poly(expand(poly),u)
 total=F(0)
 for (j,),c in po.terms():
  rat=F(1)
  for k in range(j):rat*=F(4*k+1,4*k+7)
  total+=F(int(c.p),int(c.q))*rat
 return total
for j in range(25):assert integrate(chebyshevt(j,2*u-1))==mm[j]
b=[F((-1)**j*(j*j+3),j+2) for j in range(11)]
q=A.quotient(b)
B=sum(v*chebyshevt(j,z) for j,v in enumerate(b))
Q=sum(v*chebyshevt(j,z) for j,v in enumerate(q))
assert expand((1+z)*Q-2*(B-A.axis(b)))==0
exact=integrate(Q.subs(z,2*u-1)**2)
runs=[]
for bits in (256,384):
 ctx.prec=bits
 got=A.normalized_square(q,mm)
 assert got.contains(A.aa(exact))
 assert got>0
 mass=A.beta_mass()
 assert mass>0
 runs.append({'bits':bits,'normalized_square':str(got),'exact_square':str(exact),'full_angular_mass':str(mass),'target_integrand':str(A.target_integrand(b,mm))})
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','tests':['25 moments versus exact independent monomial beta integration','degree10 polynomial quotient identity','Arb convolution norm versus exact rational beta integral at256/384 bits'],'runs':runs,'proof_sha256':hashlib.sha256((p/'PROOF.md').read_bytes()).hexdigest(),'module_sha256':hashlib.sha256((p/'code/angular.py').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'moments_sha256':hashlib.sha256(data.read_bytes()).hexdigest()}
(p/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['date'],out['status'])
