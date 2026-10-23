"""Exact algebra supporting the separate full third-derivative energy proof."""
from pathlib import Path
from datetime import datetime,timezone
from itertools import product
import json
import sympy as s
x,y,ell=s.symbols('x y ell',real=True);xs=[x,y]
rho=x**4*y+3*x*x*y**3+y**5+x*x*y+2*y
psi=x*y*(x**4+2*x*x*y*y+3*y**4+5*x*x+7*y*y+11)
U=[-s.diff(psi,y),s.diff(psi,x)];W=[ell*x+U[0],ell*y+U[1]]
adv=lambda f:sum(W[l]*s.diff(f,xs[l]) for l in range(2))
transport=adv(rho)-rho;checks=[]
for ids in product(range(2),repeat=3):
 i,j,k=ids;ds=[xs[i],xs[j],xs[k]];f=s.diff(rho,*ds)
 g1=sum(s.diff(U[l],xs[a])*s.diff(rho,xs[l],xs[b],xs[c]) for a,b,c in [(i,j,k),(j,i,k),(k,i,j)] for l in range(2))
 g2=sum(s.diff(U[l],xs[a],xs[b])*s.diff(rho,xs[l],xs[c]) for a,b,c in [(i,j,k),(i,k,j),(j,k,i)] for l in range(2))
 g3=sum(s.diff(U[l],*ds)*s.diff(rho,xs[l]) for l in range(2))
 assert s.expand(s.diff(transport,*ds)-(adv(f)+(3*ell-1)*f+g1+g2+g3))==0
 checks.append('third commutator '+str(ids))
for order in [2,4]:
 for ids in product(range(2),repeat=order):
  ds=[xs[i] for i in ids];f=s.diff(rho,*ds)
  # The nonlinear commutator is defined directly, independently of its binomial form.
  comm=sum(s.diff(U[l]*s.diff(rho,xs[l]),*ds)-U[l]*s.diff(f,xs[l]) for l in range(2))
  assert s.expand(s.diff(transport,*ds)-(adv(f)+(order*ell-1)*f+comm))==0
  checks.append('ordered commutator '+str(ids))
for i,j in product(range(2),repeat=2):
 ds=[xs[i],xs[j]]
 direct=sum(s.diff(U[l]*s.diff(rho,xs[l]),*ds)-U[l]*s.diff(rho,xs[l],*ds) for l in range(2))
 split=sum(s.diff(U[l],xs[i])*s.diff(rho,xs[l],xs[j])+s.diff(U[l],xs[j])*s.diff(rho,xs[l],xs[i])+s.diff(U[l],xs[i],xs[j])*s.diff(rho,xs[l]) for l in range(2))
 assert s.expand(direct-split)==0
 checks.append('second split '+str((i,j)))
assert s.expand(sum(s.diff(W[i],xs[i]) for i in range(2))-2*ell)==0
checks.append('constant divergence')
# Independent local divergence identity underlying the interpolation bound.
v=[x*x+2*x*y+y**3,3*x**3-y*y,x*y+4*y]
A=sum(s.diff(z,q)**2 for z in v for q in xs)
flux=[sum(z*s.diff(z,q) for z in v)*A for q in xs]
first=sum(z*sum(s.diff(z,q,2) for q in xs)*A for z in v)
second=2*sum(z*s.diff(z,xs[i])*s.diff(w,xs[j])*s.diff(w,xs[i],xs[j]) for z in v for w in v for i in range(2) for j in range(2))
assert s.expand(sum(s.diff(flux[i],xs[i]) for i in range(2))-A*A-first-second)==0
checks.append('interpolation divergence identity')
a,b=s.symbols('a b',positive=True)
assert s.factor((a*b/(a*a+b*b))**2+(-a*a/(a*a+b*b))**2-a*a/(a*a+b*b))==0
checks.append('velocity multiplier contraction')
lam=s.symbols('lam',positive=True)
scaled=lam*rho.subs({x:x/lam,y:y/lam})
for q in xs:
 assert s.expand(s.diff(scaled,q)-s.diff(rho,q).subs({x:x/lam,y:y/lam}))==0
checks.append('scaling invariance of gradient')
root=Path('research/small_gradient_exclusion/verification');root.mkdir(parents=True,exist_ok=True)
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','count':len(checks),'checks':checks,'C_star':str(6+3*s.sqrt(2)/2),'scope':'Algebra only; exterior integrability, canonical multiplier domain and integration by parts are proved separately in PROOF.md.'}
(root/'checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
