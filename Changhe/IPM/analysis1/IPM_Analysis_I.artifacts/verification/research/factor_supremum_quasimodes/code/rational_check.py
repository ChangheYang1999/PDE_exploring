"""Independent exact sparse differential-ring checks; no sympy import or outputs."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
from flint import fmpq as Q
ROOT=Path(__file__).resolve().parents[1]
# Laurent monomials in r,I5,I7,J,chi,Dchi,D2chi.
ZERO=(0,)*7
def mono(coef=1,**kw):
 e=list(ZERO)
 for k,v in kw.items():e[int(k[1:])]=v
 return {tuple(e):Q(coef)}
def add(*ps):
 z={}
 for p in ps:
  for e,c in p.items():z[e]=z.get(e,Q(0))+c
 return {e:c for e,c in z.items() if c}
def scale(p,c):return {e:a*Q(c) for e,a in p.items() if a*Q(c)}
def mul(p,q):
 z={}
 for a,c in p.items():
  for b,d in q.items():
   e=tuple(u+v for u,v in zip(a,b));z[e]=z.get(e,Q(0))+c*d
 return {e:c for e,c in z.items() if c}
# Derivative rules for each generator, created separately from the symbolic source.
derivs=[mono(e0=1),mono(e0=6,e4=1),mono(e0=8,e4=1),mono(-1,e0=2,e4=1),mono(e5=1),mono(e6=1),{}]
def D(p):
 ans={}
 for e,c in p.items():
  for i,n in enumerate(e):
   if n:
    v=list(e);v[i]-=1
    ans=add(ans,mul({tuple(v):c*n},derivs[i]))
 return ans
psi2=scale(add(mono(e0=2,e3=1),mono(-1,e0=-2,e1=1)),Q(1,8))
psi4=mono(Q(-1,8),e0=-4,e2=1)
f2=add(mono(e0=4,e4=1),mono(Q(1,4),e0=4,e5=1));f4=mono(Q(1,8),e0=4,e5=1)
checks={};norms=[]
for m,p,f in [(2,psi2,f2),(4,psi4,f4)]:
 checks[f'poisson_{m}']=not add(scale(D(D(p)),-1),scale(p,m*m),scale(f,-1))
 vals=[mul(v,mono(e0=-2)) for v in [p,D(p),D(D(p))]]
 norms.append([{','.join(map(str,e)):str(c) for e,c in sorted(v.items())} for v in vals])
# Independent Green integration-by-parts expressions.
a2=add(mono(Q(1,4),e0=6,e4=1),mono(Q(-1,2),e1=1));b2=add(mono(Q(1,2),e3=1),mono(Q(-1,4),e0=2,e4=1))
a4=add(mono(Q(1,8),e0=8,e4=1),mono(-1,e2=1));b4=mono(Q(-1,8),e4=1)
for m,a,b,p in [(2,a2,b2,psi2),(4,a4,b4,psi4)]:checks[f'green_ibp_{m}']=not add(scale(add(mul(mono(e0=-m),a),mul(mono(e0=m),b)),Q(1,2*m)),scale(p,-1))
# Triangle bounds from differentiated coefficients; constant+B1 coefficient.
primitive={(0,0,0,1,0,0,0):(Q(1,2),Q(0)),(-4,1,0,0,0,0,0):(Q(1,6),Q(0)),(-6,0,1,0,0,0,0):(Q(1,8),Q(0)),(2,0,0,0,1,0,0):(Q(1),Q(0)),(2,0,0,0,0,1,0):(Q(0),Q(1))}
bounds=[]
for p in [psi2,psi4]:
 row=[]
 for v in [p,D(p),D(D(p))]:
  norm=mul(v,mono(e0=-2));a=b=Q(0)
  for e,c in norm.items():u,w=primitive[e];a+=abs(c)*u;b+=abs(c)*w
  row.append((a,b))
 bounds.append(row)
total=[Q(0),Q(0)]
for m,row in zip([2,4],bounds):
 for k in range(2):total[k]+=row[2][k]+(2+2*m)*row[1][k]+(m*m+2*m)*row[0][k]
checks['hessian_constant']=total==[Q(7),Q(3,8)]
# Coefficients (constant,ell) of 3ell-c-1 after c=3ell-1.
checks['cubic_normalization']=[Q(0)-Q(-1)-1,Q(3)-Q(3)]==[Q(0),Q(0)]
checks['strain_rankone']=Q(1,8)*Q(1,3)==Q(1,24)
# Axis multipole decay degrees are -3 velocity, -4 component quotient for mode2;
# mode4 is two orders smaller. The symbolic source checks exact Cartesian parity.
if not all(checks.values()):raise RuntimeError(checks)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INDEPENDENT_RATIONAL_DIFFERENTIAL_RING','checks':checks,'normalized_derivatives':norms,'bounds':[[[str(a),str(b)] for a,b in row] for row in bounds],'hessian_bound':[str(v) for v in total],'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest(),'scope':'Finite identities only; weak convergence and Fredholm consequence require the informal proof.'}
(ROOT/'evidence/rational_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
