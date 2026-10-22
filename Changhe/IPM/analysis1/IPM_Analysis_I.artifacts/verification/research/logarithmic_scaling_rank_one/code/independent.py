from pathlib import Path
from fractions import Fraction as F
from math import comb
import sys,json
sys.dont_write_bytecode=True
from flint import fmpq
R=Path(__file__).resolve().parents[3];D=R/'research/logarithmic_scaling_rank_one';E=D/'evidence';sys.path.insert(0,str(R/'research/full_derivative_norm_bound_v2/code'));import protocol as p
start=p.now();A=p.load(E/'check.json');p.rehash(A['parent_files']);assert p.sha(D/'PROOF.md')==A['proof_sha256']=='99cbccd132ab68569fdfdcd438b36fca0ceaa82740f3ff822c84ac13121813a1'
raw=R/'data_exact/modal_v2.json';assert p.sha(raw)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6';raw=p.load(raw)
def hx(t):
 sign=-1 if t.startswith('-') else 1;t=t.lstrip('+-');m,e=t.split('p');whole,frac=m[2:].split('.');return fmpq(sign*int(whole+frac,16))*fmpq(2)**(int(e)-4*len(frac))
k,bi,bo=[hx(raw['scalars_hex'][n]) for n in ['k','bi','bo']];arr=raw['arrays']['Aout'];assert arr['shape']==A['Aout_shape']==[260,10];C=[hx(arr['hex'][10*m]) for m in range(260)];assert list(map(str,C))==A['all_260_leading_cosines'] and C[1]!=0 and k*C[1]!=0
actual={'k':k,'bi':bi,'bo':bo,'leading_cosine_m1':C[1],'Euler_leading_cosine_m1':fmpq(k.p*C[1].p,k.q*C[1].q),'membership_lower':fmpq(k.p+k.q,k.q),'axis_limit':fmpq(5,2),'strain_limit':fmpq(2),'s':fmpq(153,50),'center_margin_at_upper':fmpq(11,25),'weight3over2_far_margin':fmpq(k.q-2*k.p,2*k.q),'weight3over2_residual_margin':fmpq(3*k.q-4*k.p,2*k.q),'outer_log_gap':fmpq(bo.p*k.q+k.p*bo.q-3*bo.q*k.q,bo.q*k.q),'nonlocal_to_rank_gap':fmpq(4)};assert {n:str(v) for n,v in actual.items()}==A['actual'] and 0<k<fmpq(1,2)
exponents=[];gaps=[]
for j,l in raw['outer_jl']:
 ex=k-3
 for _ in range(j):ex+=k-1
 for _ in range(l):ex-=2
 exponents.append(ex);gaps.append(j*(1-k)+2*l)
assert list(map(str,exponents))==A['outer_exponents'] and list(map(str,gaps))==A['exterior_gaps'] and gaps[0]==0 and all(t>0 for t in gaps[1:])
# Differential ring adapted from205, now includes sigma as an independent formal scalar.
# Monomial: powers of x,y,beta,sigma followed by sorted formal Cartesian jets.
def mon(x=0,y=0,b=0,s=0,jets=(),c=1):return {(x,y,b,s,tuple(sorted(jets))):F(c)} if c else {}
def jet(name,dx=0,dy=0):return mon(jets=((name,dx,dy),))
def add(*terms):
 out={}
 for f in terms:
  for t,c in f.items():out[t]=out.get(t,F())+c
 return {t:c for t,c in out.items() if c}
def scale(f,c):return {t:c*v for t,v in f.items() if c*v}
def mul(f,g):
 out={}
 for (x,y,b,s,j),c in f.items():
  for (xx,yy,bb,ss,jj),cc in g.items():
   t=(x+xx,y+yy,b+bb,s+ss,tuple(sorted(j+jj)));out[t]=out.get(t,F())+c*cc
 return {t:c for t,c in out.items() if c}
def deriv(f,axis):
 out={}
 for (x,y,b,s,jets),c in f.items():
  powers=[x,y]
  if powers[axis]:
   v=powers.copy();v[axis]-=1;out=add(out,mon(*v,b,s,jets,c*powers[axis]))
  for i,(name,dx,dy) in enumerate(jets):
   d=[dx,dy];d[axis]+=1;jj=list(jets);jj[i]=(name,*d);out=add(out,mon(x,y,b,s,jj,c))
 return out
def power(f,n):
 out=mon()
 for _ in range(n):out=mul(out,f)
 return out
x,y,beta,sigma=mon(x=1),mon(y=1),mon(b=1),mon(s=1);aa,v1,v2,Q=[jet(n) for n in ['a','v1','v2','Q']];rho=mul(mon(2,1),aa)
G=add(mul(x,deriv(rho,0)),mul(y,deriv(rho,1)));expectedG=mul(mon(2,1),add(scale(aa,3),mul(x,deriv(aa,0)),mul(y,deriv(aa,1))));assert G==expectedG
U1=mul(x,add(scale(sigma,-1),v1));U2=mul(y,add(sigma,v2));coupling=add(mul(U1,deriv(rho,0)),mul(U2,deriv(rho,1)),scale(mul(sigma,G),F(1,3)))
B=add(scale(mul(sigma,add(scale(mul(x,deriv(aa,0)),-2),scale(mul(y,deriv(aa,1)),4))),F(1,3)),mul(v1,add(scale(aa,2),mul(x,deriv(aa,0)))),mul(v2,add(aa,mul(y,deriv(aa,1)))))
assert coupling==mul(mon(2,1),B)
# No zero-order a*sigma term survives after cancellation.
assert all(not (sigpow and jets==(('a',0,0),)) for (xp,yp,bp,sigpow,jets) in coupling)
St={(0,0):1}
for n in range(1,5):
 for j in range(n+1):St[n,j]=j*St.get((n-1,j),0)+St.get((n-1,j-1),0)
identities=3
for pp in range(5):
 for qq in range(5-pp):
  f=mul(mon(x=2),Q)
  for _ in range(qq):f=deriv(f,1)
  for _ in range(pp):f=add(mul(x,deriv(f,0)),mul(beta,f))
  closed={}
  for ell in range(pp+1):
   bp=power(add(beta,mon(c=2)),pp-ell)
   for j in range(ell+1):closed=add(closed,scale(mul(bp,mul(mon(x=2+j),jet('Q',j,qq))),comb(pp,ell)*St.get((ell,j),0)))
  assert f==closed,(pp,qq);identities+=1
out={'start_utc':start,'utc':p.now(),'status':'PASS_INDEPENDENT_INTEGER_HEX_FMPQ_NONZERO_AND_DIFFERENTIAL_RING','proof_sha256':p.sha(D/'PROOF.md'),'code_sha256':p.sha(Path(__file__)),'check_sha256':p.sha(E/'check.json'),'parent_pin_count':len(A['parent_files']),'exact_parameters_compared':len(actual),'leading_cosines_compared':len(C),'outer_exponents_compared':len(exponents),'exterior_gaps_compared':len(gaps),'nonzero_coefficient':str(C[1]),'nonzero_Euler_coefficient':str(k*C[1]),'differential_ring_checks':identities,'source_reuse':'Differential ring adapted from205 with independent sigma variable. No NPZ, Sympy or primary evaluator import.','scope':'Independent exact coefficient decoding and finite formal algebra only. Parent canonical matches, complete Sobolev arguments and boundedness/compactness proofs are analytic dependencies.'};p.write(E/'independent.json',out);print(json.dumps(out))
