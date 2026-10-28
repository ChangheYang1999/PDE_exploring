"""Independent Laurent-Fourier reconstruction, Cartesian advection and tail constants."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
from hashlib import sha256
from datetime import datetime,timezone
import json,sys,time
from flint import fmpq,arb,ctx
here=Path(__file__).parent;root=here.parents[2];sys.set_int_max_str_digits(0)
def Q(v):
 q=F(v);return fmpq(q.numerator,q.denominator)
def A(v):
 q=F(str(v));return arb(q.numerator)/q.denominator
def add(p,n,v):
 p[n]=p.get(n,fmpq(0))+v
 if not p[n]:del p[n]
def lin(*terms):
 out={}
 for fac,p in terms:
  for n,v in p.items():add(out,n,fac*v)
 return out
def derivative(p,s,axis,imag):
 out={}
 for n,v in p.items():
  if axis=='x':
   add(out,n+1,v*(s-n)/2);add(out,n-1,v*(s+n)/2)
  else:
   sign=1 if imag else -1
   add(out,n+1,sign*v*(s-n)/2);add(out,n-1,-sign*v*(s+n)/2)
 return out,imag^(axis=='y')
def coefficient_norm(p,imag):
 assert all(p.get(-n,fmpq(0))==(-v if imag else v) for n,v in p.items())
 return abs(p.get(0,fmpq(0)))+sum((2*abs(v) for n,v in p.items() if n>0),fmpq(0))
def main():
 ctx.prec=640;start=time.monotonic();source=root/'research/source_audit/state131_exact.json';raw=json.loads(source.read_text());data=json.loads((here/'sectors.json').read_text());c=Q(raw['exact_parameters']['cl']);g=1/c;delta=1-g;assert str(delta)==data['delta'];R=data['R'];N=data['Q'];order=raw['canonical_order'];coeff=list(map(Q,raw['canonical_coefficients']));pp=[(3+g-j*delta)/2 for j in range(4)];fields={};caps={3:[],4:[]};checks=0
 for j in range(4):
  for q in range(N+1):
   p={};s=2*pp[j]-2*q
   for a,(jj,m,k) in zip(coeff,order):
    if jj!=j:continue
    b=fmpq(1)
    for l in range(q):b*= (pp[j]-k-l)/(l+1)
    if m:add(p,2*m,a*b/2);add(p,-2*m,a*b/2)
    else:add(p,0,a*b)
   D={(0,0):(p,False)}
   for d in range(1,5):
    for nx in range(d+1):
     ny=d-nx;prior=D[nx-1,ny] if nx else D[nx,ny-1]
     D[nx,ny]=derivative(prior[0],s-d+1,'x' if nx else 'y',prior[1]);assert D[nx,ny][1]==bool(ny%2)
    if d in caps:
     val=max(coefficient_norm(*D[nx,d-nx]) for nx in range(d+1));caps[d].append([j,q,str(val)])
   rho=lin((-1,D[2,1][0]),(-1,D[0,3][0]));rx=lin((-1,D[3,1][0]),(-1,D[1,3][0]));ry=lin((-1,D[2,2][0]),(-1,D[0,4][0]));u1=lin((-1,D[1,2][0]));u2=D[2,1][0]
   fields[j,q]=(rho,rx,ry,u1,u2,g-j*delta-2*q)
 for d in caps:assert caps[d]==data['potential_caps'][str(d)];checks+=len(caps[d])
 E={}
 for key,(rho,rx,ry,u1,u2,power) in fields.items():E[key]=lin((c*power-1,rho))
 for (i,qi),(_,_,_,u1,u2,_) in fields.items():
  for (j,qj),(_,rx,ry,_,_,_) in fields.items():
   row=E.setdefault((i+j+1,qi+qj),{})
   for u,dr in [(u1,rx),(u2,ry)]:
    for m,b in u.items():
     for n,a in dr.items():add(row,m+n,a*b)
 E={k:p for k,p in E.items() if p};old=json.loads((root/'research/05_tails/verification/state131_residual_truncated_sectors.json').read_text())['coefficients'];assert set(map(str,E))==set(old)
 bykey={(row['h'],row['q']):row for row in data['rows']};assert set(bykey)==set(E)
 # P1=1, P3=1+2z, P_(n+2)=2zP_n-P_(n-2), independently of explicit U formula.
 pol={1:{0:fmpq(1)},3:{0:fmpq(1),1:fmpq(2)}}
 for n in range(5,42,2):
  p={}
  for k,v in pol[n-2].items():add(p,k+1,2*v)
  for k,v in pol[n-4].items():add(p,k,-v)
  pol[n]=p
 for key,row in E.items():
  assert not row.get(0,0);assert all(row.get(-n,0)==-v for n,v in row.items());sins={n:-2*v for n,v in row.items() if n>0};assert {str(n):str(v) for n,v in sins.items()}==old[str(key)];checks+=len(sins)
  P={}
  for n,v in sins.items():
   assert n%2
   for k,w in pol[n].items():add(P,k,v*w)
  target=bykey[key];assert {str(k):str(v) for k,v in P.items()}==target['P'];assert Q(target['a'])==(key[0]-1)*delta+2*key[1]>=0;checks+=len(P)+1
 absj=[sum((abs(v) for v,(jj,m,k) in zip(coeff,order) if jj==j),fmpq(0)) for j in range(4)];assert list(map(str,absj))==data['absolute_branch_coefficients'];assert all(abs(pp[j]-k)<26 and 2*m<=18 and 0<2*pp[j]<4 for j,m,k in order);checks+=len(order)+4
 q0=N+1;M={};T={}
 for d in (3,4):
  ratio=A(F(q0+26,q0+1)*F(2*q0+34,2*q0+32)**d)/R**2;assert ratio<1
  M[d]=sum((A(v)*A(R)**A(-j*delta-2*q) for j,q,v in caps[d]),arb(0));T[d]=A(comb(q0+25,q0)*(2*q0+32)**d)*A(R)**(-2*q0)*sum((A(v)*A(R)**A(-j*delta) for j,v in enumerate(absj)),arb(0))/(1-ratio)
 eps=A(R)**A(delta)*(2*arb(2).sqrt()*A(c)*T[4]+2*T[3])+4*(T[3]*M[4]+M[3]*T[4]+T[3]*T[4]);assert eps<=A(data['epsilon_upper_rational']);checks+=3
 out={'utc':datetime.now(timezone.utc).isoformat(),'all_pass':True,'checks':checks,'method':'Independent Laurent coefficients; Cartesian velocity times density-gradient convolution; Chebyshev recurrence; directed omitted-tail evaluation','source_sha256':sha256(source.read_bytes()).hexdigest(),'sectors_sha256':sha256((here/'sectors.json').read_bytes()).hexdigest(),'epsilon':eps.str(100),'precision_bits':ctx.prec,'seconds':time.monotonic()-start};(here/'algebra_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(out,flush=True)
if __name__=='__main__':main()
