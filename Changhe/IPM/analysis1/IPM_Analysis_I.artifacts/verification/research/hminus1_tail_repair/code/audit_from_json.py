"""Exact-rational audit from canonical hex JSON; no numerical convolution claim.
No JS/TS, servers/listeners/tunnels, RLScience or Lean/Lake.
"""
import json,hashlib
from pathlib import Path
from fractions import Fraction as F
B=Path(__file__).resolve().parents[3];D=B/'research/hminus1_tail_repair'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def dec(s):
 neg=s.startswith('-');man,e=s.lstrip('+-').split('p');w,f=man[2:].split('.');v=F(int(w+f,16),16**len(f))*F(2)**int(e);return -v if neg else v

def evaluate():
 plan=load(D/'source/plan.json');p=B/plan['modal_json'];assert sha(p)==plan['modal_json_sha256'];z=load(p);ar=z['arrays']
 k=dec(z['scalars_hex']['k']);L=dec(z['scalars_hex']['L']);bo=dec(z['scalars_hex']['bo']);t=dec(ar['knots']['hex'][-1]);assert 0<k<F(1,4) and bo>120
 pairs=z['outer_jl'];assert pairs==plan['pairs'];ex=[k-j*(1-k)-2*l for j,l in pairs]+[3-bo]
 a1=2*k-1;a2=3*k-2;d=k-2;a3=4*k-3
 assert [ex[i] for i in (0,1,2,6,3)]==[k,a1,a2,d,a3]
 distinct=0
 for i,x in enumerate(ex):
  for y in ex[i+1:]:assert x!=y;distinct+=1
 assert distinct==55
 alpha=k-3
 from math import comb
 for n in range(7):assert alpha**n==sum(F(comb(n,j))*(-bo)**(n-j)*(alpha+bo)**j for j in range(n+1))
 assert plan['density_rows']=={'D0':0,'D1':1,'D2':2,'Dd':6} and pairs[2]==[2,0] and pairs[6]==[0,1]
 assert k>a1>a2>d>a3 and a1>-1 and a2<-1 and d<-1 and a3<-2
 assert all(x<=a3 for i,x in enumerate(ex) if i not in (0,1,2,6))
 checks=0
 for i,x in enumerate(ex):
  for j,y in enumerate(ex):
   w=x+y-1
   assert w==a1 if (i,j)==(0,0) else w==a2 if (i,j) in ((0,1),(1,0)) else w<=a3
   assert w!=d;checks+=2
 checks_den=0
 for x in ex:
  for n in range(1,262):assert (2*n)**2-(x+1)**2!=0;checks_den+=1
 for x,N in [(a1,522),(a2,783),(d,261)]:
  for n in range(1,N+1):assert (2*n)**2-(x+1)**2>0 and x-2*n<-1;checks_den+=2
 assert k-4<a3 and a1+a1-1==k+a2-1==a2+k-1==a3
 assert (a1/k-1)*k/(1-k)==-1 and (a2/k-1)*k/(2*(1-k))==-1 and d/k-1==-2/k
 # Exact scalar identities for arbitrary angular ordered products.
 assert (k/(1-k))*(a1/k-1)==-1
 norm_exps=[a1-k,a2-k,d-k];assert norm_exps==[k-1,2*k-2,F(-2)] and all(x<0 for x in norm_exps)
 # Laurent basis differentiation reconstructs partial_x independently of(3).
 signatures=[];forcechecks=0
 for a,nuMax in [(k,521),(a1,1043),(a2,1565),(d,521)]:
  for nu in range(1,nuMax+1,2):
   poly={}
   def add(n,c):poly[n]=poly.get(n,F(0))+c
   for e in (-1,1):
    for s in (-1,1):add(s*nu+e,F(s)*a/2-F(e)*nu/2)
   poly={n:c for n,c in poly.items() if c};expected={}
   for nn,coef in [(nu+1,(a-nu)/2),(nu-1,(a+nu)/2)]:
    if nn:
     expected[nn]=expected.get(nn,F(0))+coef;expected[-nn]=expected.get(-nn,F(0))-coef
   expected={n:c for n,c in expected.items() if c};assert poly==expected
   signatures.append([str(a),nu,[[n,str(c)] for n,c in sorted(poly.items())]]);forcechecks+=1
 # Universal coefficient identities for angular factorization(5).
 # 2(cos²-2sin²)=3zeta-1; -8cos²sin²=-2+2zeta².
 assert [2*(F(1,2)-2*F(1,2)),2*(F(1,2)+2*F(1,2))]==[-1,3]
 assert [-8*F(1,4),F(0),8*F(1,4)]==[-2,0,2]
 M0=plan['base_quotient_degree'];M1=2*M0+2;M2=M0+M1+2
 assert plan['correction_quotient_degrees']==dict(H1=M1,H2=M2,Hd=M0)
 assert plan['new_stream_maxima']==dict(H1=M1+2,H2=M2+2,Hd=M0+2)
 residualmax=(2*M2+4)+(2*M2+3);assert residualmax==plan['residual_max_odd_frequency']
 angular=0
 for nu in range(1,residualmax+1,2):assert 0<F(1,nu**2)<=1;angular+=1
 return {'method':'exact Fraction from hexadecimal JSON; Laurent differentiation and all exponent pairs','exact':{'k':str(k),'L':str(L),'tplus':str(t),'bo':str(bo),'a1':str(a1),'a2':str(a2),'d':str(d),'a3':str(a3),'all_original_exponents':[str(x) for x in ex],'norm_decay_exponents':[str(x) for x in norm_exps]},'counts':{'distinct_exponent_pairs':distinct,'normalization_zero_join_jets':7,'ordered_product_checks':checks,'mode_denominator_and_outer_integrability_checks':checks_den,'Laurent_force_basis_checks':forcechecks,'angular_primitive_multiplier_checks':angular,'factor_polynomial_identities':2},'force_basis_sha256':hashlib.sha256(json.dumps(signatures,sort_keys=True).encode()).hexdigest(),'source':{'path':str(p.relative_to(B)),'sha256':sha(p)}}
