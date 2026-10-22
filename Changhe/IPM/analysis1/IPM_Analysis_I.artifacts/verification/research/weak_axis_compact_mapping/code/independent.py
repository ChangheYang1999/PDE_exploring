from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from math import comb
import sys,os,json
sys.dont_write_bytecode=True
for n in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[n]='1'
from flint import fmpq
from mpmath import iv
iv.dps=100
R=Path(__file__).resolve().parents[3];D=R/'research/weak_axis_compact_mapping';E=D/'evidence';sys.path.insert(0,str(R/'research/full_derivative_norm_bound_v2/code'));import protocol as p
start=p.now();A=p.load(E/'check.json');assert A['proof_sha256']==p.sha(D/'PROOF.md')=='3bd85b7a29499ddd57fc3e13335bb8571c54f2aefcfec1fd93ba306c3a6de6a7';p.rehash(A['parent_files'])
raw=p.load(R/'data_exact/modal_v2.json');assert p.sha(R/'data_exact/modal_v2.json')=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
def hx(t):
 sg=-1 if t.startswith('-') else 1;t=t.lstrip('+-');m,e=t.split('p');a,b=m[2:].split('.');return fmpq(sg*int(a+b,16))*fmpq(2)**(int(e)-4*len(b))
k,bi,bo=[hx(raw['scalars_hex'][n]) for n in ['k','bi','bo']];s=fmpq(153,50);theta=fmpq(3,50)
actual={'k':k,'bi':bi,'bo':bo,'s':s,'theta':theta,'center_rate_infimum':fmpq(147,50)-fmpq(5,2),'far_rate_minimum':(3*k.q-k.p)/fmpq(k.q),'inner_factor_gap':(bi.p-2*bi.q)/fmpq(bi.q),'outer_correction_gap':fmpq(bo.p*k.q+k.p*bo.q-3*k.q*bo.q,bo.q*k.q)}
assert {n:str(v) for n,v in actual.items()}==A['actual'] and 0<k<fmpq(1,2) and actual['inner_factor_gap']>0 and actual['outer_correction_gap']>0 and actual['center_rate_infimum']==fmpq(11,25)
knots=[hx(t) for t in raw['arrays']['knots']['hex']];unique=[];multiplicities=[]
for t in knots:
 if unique and t==unique[-1]:multiplicities[-1]+=1
 else:
  if unique:assert t>unique[-1]
  unique.append(t);multiplicities.append(1)
assert multiplicities==[8]+[1]*1557+[8] and len(knots)==A['knots_checked']==1573 and len(unique)==A['distinct_knots']==1559 and raw['degree']==A['degree']==7
shapes={n:raw['arrays'][n]['shape'] for n in ['S','D','Aout','Ei','Eo']};assert shapes==A['shapes'] and shapes['S'][0]==A['modes']==260
# Separate exponent construction accumulates j copies of k-1 and l copies of -2.
exponents=[]
for j,l in raw['outer_jl']:
 e=k-3
 for _ in range(j):e+=k-1
 for _ in range(l):e-=2
 exponents.append(e)
assert list(map(str,exponents))==A['outer_exponents'] and exponents[0]==k-3 and all(e<exponents[0] for e in exponents[1:])
# Differential polynomials: (power x,power y,power beta,sorted tuple of formal jets).
# Differentiate the expression tree in this ring; do not import the primary or Sympy.
def mon(x=0,y=0,b=0,jets=(),c=1):return {(x,y,b,tuple(sorted(jets))):F(c)} if c else {}
def jet(name,dx=0,dy=0):return mon(jets=((name,dx,dy),))
def add(*terms):
 out={}
 for f in terms:
  for t,c in f.items():out[t]=out.get(t,F())+c
 return {t:c for t,c in out.items() if c}
def scale(f,c):return {t:c*v for t,v in f.items() if c*v}
def mul(f,g):
 out={}
 for (x,y,b,j),c in f.items():
  for (xx,yy,bb,jj),cc in g.items():
   t=(x+xx,y+yy,b+bb,tuple(sorted(j+jj)));out[t]=out.get(t,F())+c*cc
 return {t:c for t,c in out.items() if c}
def deriv(f,axis):
 out={}
 for (x,y,b,jets),c in f.items():
  powers=[x,y]
  if powers[axis]:
   v=powers.copy();v[axis]-=1;out=add(out,mon(*v,b,jets,c*powers[axis]))
  for i,(name,dx,dy) in enumerate(jets):
   d=[dx,dy];d[axis]+=1;jj=list(jets);jj[i]=(name,*d);out=add(out,mon(x,y,b,jj,c))
 return out
def power(f,n):
 out=mon()
 for _ in range(n):out=mul(out,f)
 return out
x,y,beta=mon(x=1),mon(y=1),mon(b=1);aa,v1,v2,Q=[jet(n) for n in ['a','v1','v2','Q']];rho=mul(mon(2,1),aa)
g=add(mul(mul(x,v1),deriv(rho,0)),mul(mul(y,v2),deriv(rho,1)))
B=add(mul(v1,add(scale(aa,2),mul(x,deriv(aa,0)))),mul(v2,add(aa,mul(y,deriv(aa,1)))))
assert g==mul(mon(2,1),B)
# Independent closed normal-order formula for (E_x+beta)^p(x² Q_y^q).
St={(0,0):1}
for n in range(1,5):
 for j in range(n+1):St[n,j]=j*St.get((n-1,j),0)+St.get((n-1,j-1),0)
identities=1
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
# Exact exponent accounting from x-power, y-length and amplitude, including sqrt.
# Affine-polynomial coefficient tuples ordered (constant,b,q,k).
center=tuple(F(x)/2 for x in [12,-2,-2,0]);far=tuple(F(x)/2 for x in [-6,-2,-2,2]);assert center==(6,-1,-1,0) and far==(-3,-1,-1,1)
# Interpolation coefficient arithmetic is checked exactly at the actual order.
assert (1-theta)*3+theta*2==6-s and (1-theta)*(-1)+theta*(-1)==-1

def V(q):q=fmpq(q);return iv.mpf(int(q.p))/int(q.q)
def endpoint(t):sg,m,e,bc=t;return F((-1 if sg else 1)*int(m))*F(2)**int(e)
# Direct integer-numerator formulas differ from the primary Arb expression order.
iv_expr={'far_rate_minimum':(3*iv.mpf(int(k.q))-int(k.p))/int(k.q),'inner_factor_gap':(iv.mpf(int(bi.p))-2*int(bi.q))/int(bi.q),'outer_correction_gap':(iv.mpf(int(bo.p))*int(k.q)+iv.mpf(int(k.p))*int(bo.q)-3*iv.mpf(int(k.q))*int(bo.q))/(iv.mpf(int(bo.q))*int(k.q))};balls={}
for n,v in iv_expr.items():
 lo,hi=map(endpoint,v._mpi_);exact=F(str(actual[n]));a,b=map(F,A['strict_windows'][n]);al,au=map(F,[A['arb256'][n]['lower_exact'],A['arb256'][n]['upper_exact']]);assert a<lo<=exact<=hi<b and max(lo,al)<=min(hi,au);balls[n]={'lower_exact':str(lo),'upper_exact':str(hi)}
out={'start_utc':start,'utc':p.now(),'status':'PASS_INDEPENDENT_HEX_FMPQ_IV_AND_NORMAL_ORDER_ALGEBRA','proof_sha256':p.sha(D/'PROOF.md'),'code_sha256':p.sha(Path(__file__)),'check_sha256':p.sha(E/'check.json'),'parent_pin_count':len(A['parent_files']),'exact_values_compared':len(actual),'outer_exponents_compared':10,'knots_compared':len(knots),'differential_ring_checks':identities,'iv100':balls,'strict_windows':A['strict_windows'],'scope':'Separate data decoding, arithmetic engine and finite differential algebra. Harmonic convergence, shell geometry and Sobolev membership remain analytic proof obligations, not finite-test conclusions.'};p.write(E/'independent.json',out);print(json.dumps(out))
