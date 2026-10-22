from pathlib import Path
from fractions import Fraction as F
from math import comb
import sys,json
sys.dont_write_bytecode=True
from flint import fmpq
R=Path(__file__).resolve().parents[3];D=R/'research/weak_axis_compact_higher_orders';E=D/'evidence';sys.path.insert(0,str(R/'research/full_derivative_norm_bound_v2/code'));import protocol as p
start=p.now();A=p.load(E/'check.json');p.rehash(A['parent_files']);assert p.sha(D/'PROOF.md')==A['proof_sha256']=='0dcddf0f8356c434242ffc63986a74079e578d70acb7c32acc76975018730f4f'
raw=R/'data_exact/modal_v2.json';assert p.sha(raw)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6';raw=p.load(raw)
def hx(t):
 sign=-1 if t.startswith('-') else 1;t=t.lstrip('+-');m,e=t.split('p');whole,frac=m[2:].split('.');return fmpq(sign*int(whole+frac,16))*fmpq(2)**(int(e)-4*len(frac))
k,bi,bo=[hx(raw['scalars_hex'][n]) for n in ['k','bi','bo']];actual={'k':k,'bi':bi,'bo':bo,'spline_degree':fmpq(raw['degree']),'matched_derivative_order':fmpq(raw['degree']-1),'weak_a_order':fmpq(7),'weak_g_order':fmpq(6),'max_uniform_s':fmpq(7,2),'axis_limit':fmpq(5,2),'center_base':fmpq(6),'far_margin_at_b0':(3*k.q-k.p)/fmpq(k.q),'inner_gap':(bi.p-2*bi.q)/fmpq(bi.q),'outer_log_gap':fmpq(bo.p*k.q+k.p*bo.q-3*k.q*bo.q,bo.q*k.q)}
assert {n:str(v) for n,v in actual.items()}==A['actual'] and 0<k<fmpq(1,2) and bi>50 and bo>120
knots=[hx(t) for t in raw['arrays']['knots']['hex']];unique=[];mult=[]
for t in knots:
 if unique and t==unique[-1]:mult[-1]+=1
 else:
  if unique:assert t>unique[-1]
  unique.append(t);mult.append(1)
assert mult==[8]+[1]*1557+[8] and len(knots)==A['knots_checked']==1573 and len(unique)==A['distinct_knots']==1559
shapes={n:raw['arrays'][n]['shape'] for n in ['S','D','Aout','Ei','Eo']};assert shapes==A['shapes'] and shapes['S'][0]==A['modes']==260
exponents=[]
for j,l in raw['outer_jl']:
 e=k-3
 for _ in range(j):e+=k-1
 for _ in range(l):e-=2
 exponents.append(e)
assert list(map(str,exponents))==A['outer_exponents'] and exponents[0]==k-3 and all(t<k-3 for t in exponents[1:])
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
for n in range(1,7):
 for j in range(n+1):St[n,j]=j*St.get((n-1,j),0)+St.get((n-1,j-1),0)
identities=1
for pp in range(7):
 for qq in range(7-pp):
  f=mul(mon(x=2),Q)
  for _ in range(qq):f=deriv(f,1)
  for _ in range(pp):f=add(mul(x,deriv(f,0)),mul(beta,f))
  closed={}
  for ell in range(pp+1):
   bp=power(add(beta,mon(c=2)),pp-ell)
   for j in range(ell+1):closed=add(closed,scale(mul(bp,mul(mon(x=2+j),jet('Q',j,qq))),comb(pp,ell)*St.get((ell,j),0)))
  assert f==closed,(pp,qq);identities+=1
# Independent affine coefficient arithmetic. Ordered coordinates:constant,b,q,k.
center=tuple(fmpq(t,2) for t in [12,-2,-2,0]);far=tuple(fmpq(t,2) for t in [-6,-2,-2,2]);assert center==(6,-1,-1,0) and far==(-3,-1,-1,1)
# Bilinear interpolation coefficients in 1,b,n,theta,btheta,ntheta.
left=[6,-1,-1,-1,0,0];right=[6,-1,-1,-1,0,0];assert left==right
assert actual['max_uniform_s']+actual['axis_limit']==actual['center_base'] and actual['weak_g_order']==actual['weak_a_order']-1
out={'start_utc':start,'utc':p.now(),'status':'PASS_INDEPENDENT_HEX_FMPQ_NORMAL_ORDER_HIGHER_DERIVATIVES','proof_sha256':p.sha(D/'PROOF.md'),'code_sha256':p.sha(Path(__file__)),'check_sha256':p.sha(E/'check.json'),'parent_pin_count':len(A['parent_files']),'exact_parameters_compared':len(actual),'knots_compared':len(knots),'outer_exponents_compared':len(exponents),'differential_ring_checks':identities,'maximum_total_derivative':6,'source_reuse':'Formal differential ring adapted from independently checked result202, now extended through6. No primary evaluator or Sympy import.','scope':'Exact data and finite algebra checks only. The explicit equal coefficient arrays for interpolation are tautological diagnostics, not independent analytical evidence. The annular weak derivative and Sobolev proof remain analytic; no new interval enclosure or physical norm.'};p.write(E/'independent.json',out);print(json.dumps(out))
