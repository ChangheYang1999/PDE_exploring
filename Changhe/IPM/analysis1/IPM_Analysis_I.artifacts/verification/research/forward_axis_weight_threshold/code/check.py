from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
import sys,json,hashlib
sys.dont_write_bytecode=True
import numpy as np
R=Path(__file__).resolve().parents[3];D=R/'research/forward_axis_weight_threshold';E=D/'evidence'
def now():return datetime.now(timezone.utc).isoformat()
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
start=now();pf=load(E/'proof_first.json');assert pf['proof_sha256']==sha(D/'PROOF.md');pins={};parents={}
for label,rel,expected in [('residual','research/canonical_axis_residual/evidence/verdict.json','1cefbee28c5de00af4580231c5c7ca2fbc970e773bfa14faedff8227222fd001'),('quadrant','research/quadrant_euler_axis_obstruction/evidence/verdict.json','f39dd67370e62ed494d7a8bf711d574b9dbc55c30595ad0646bc9fa3b0d4678f')]:
 assert sha(R/rel)==expected;v=load(R/rel);parents[label]={'path':rel,'sha256':expected,'status':v['status']};pins[rel]=expected
 for n,h in v['files'].items():
  assert n not in pins or pins[n]==h;pins[n]=h
for n,h in pins.items():assert sha(R/n)==h,n
npz=R/'research/modal_exactification/evidence/trial_v2_h0.008.npz';assert sha(npz)=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
with np.load(npz,allow_pickle=False) as z:k=F.from_float(float(z['k'].item()))
A=2/k-1;Dval=2*A+1;b0=(A+3)/2;s=F(153,50);assert 0<k<F(1,2) and A>3
th=F(1,2)+(Dval*(s-F(1,2))-1)/A;phi=(F(307,100)*Dval-b0)/A
assert th-F(5,2)==Dval/A*(s-F(3,2)) and phi-F(5,2)==Dval/A*(F(307,100)-F(3,2))
# Exact polynomial dictionaries in independent indeterminates A,t,a. Equality proves all real parameter substitutions.
def add(*ps):
 d={}
 for p in ps:
  for i,c in p.items():d[i]=d.get(i,F(0))+c
 return {i:v for i,v in d.items() if v}
def mul(p,q):
 d={}
 for i,c in p.items():
  for j,b in q.items():key=tuple(x+y for x,y in zip(i,j));d[key]=d.get(key,F(0))+c*b
 return {i:v for i,v in d.items() if v}
def sc(p,b):return {i:b*c for i,c in p.items() if b*c}
one={(0,0,0):F(1)};Av={(1,0,0):F(1)};t={(0,1,0):F(1)};av={(0,0,1):F(1)};dv=add(sc(Av,2),one);bv=sc(add(Av,sc(one,3)),F(1,2))
dy=add(mul(dv,add(t,sc(one,-F(1,2)))),sc(mul(Av,add(av,sc(one,-F(1,2)))),-1),sc(one,-1))
dz=add(mul(t,dv),sc(mul(Av,av),-1),sc(bv,-1));assert dy==dz
threshold_num=add(mul(dv,add(t,sc(one,-F(1,2)))),sc(one,-1),sc(Av,-2));assert threshold_num==mul(dv,add(t,sc(one,-F(3,2))))
assert add(mul(sc(one,F(3,2)),dv),sc(bv,-1))==sc(Av,F(5,2))
# Reverse-time decay c-D/2 = -Aa-b0.
c=add(sc(mul(Av,add(av,sc(one,-F(1,2)))),-1),sc(one,-1));assert add(c,sc(dv,-F(1,2)))==add(sc(mul(Av,av),-1),sc(bv,-1))
vals={'k':k,'A':A,'D':Dval,'b0':b0,'theta_153_over_50':th,'phi_307_over_100':phi,'quadrant_counterexample_delta':F(5,2)*A,'quadrant_counterexample_inverse_norm':2/(5*A),'Y_counterexample_delta_minus':(A-3)/2}
scale=10**12;n=th.numerator*scale//th.denominator;window=[F(n,scale),F(n+1,scale)];assert window[0]<th<window[1]
out={'start_utc':start,'utc':now(),'status':'PASS_EXACT_RATIONAL_AND_GENERAL_POLYNOMIAL_THRESHOLDS_REQUIRES_INDEPENDENT_REVIEW','proof_sha256':sha(D/'PROOF.md'),'code_sha256':sha(Path(__file__)),'parents':parents,'parent_files':pins,'parent_pin_count':len(pins),'exact':{n:str(q) for n,q in vals.items()},'theta_strict_window':list(map(str,window)),'general_polynomial_identities':4,'unqualified_every_frozen_inverse_claim':'REFUTED_BY_POSITIVE_DELTA_QUADRANT_COUNTEREXAMPLE','PDE_endpoint':'UNRESOLVED'}
with (E/'check.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({n:out[n] for n in ['utc','status','parent_pin_count','theta_strict_window']}))
