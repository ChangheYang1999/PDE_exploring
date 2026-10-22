#!/usr/bin/env python3
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from math import comb
import json,hashlib,time
V=Path('research/328_leading_weighted_temperature/verification');D=Path('research/324_nonlinear_formal_jet_checks/verification');start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();checks=[]
def ck(n,t,d=None):checks.append(dict(name=n,passed=bool(t),detail=d))
def L(poly,k):
 out={}
 for(a,b),c in poly.items():
  out[(a,b)]=out.get((a,b),F(0))+(10*a-b)*c
  if b:out[(a+1,b-1)]=out.get((a+1,b-1),F(0))+k*b*c
 return {e:c for e,c in out.items()if c}
for C,k in [(F(1),F(-1)),(F(2),F(1,2)),(F(-3),F(2)),(F(1,3),F(-2,5))]:
 key=str((C,k));q={(0,1):F(1),(1,0):-k/11};ck(key+'_q_eigen',L(q,k)=={e:-c for e,c in q.items()});ck(key+'_r_eigen',L({(1,0):F(1)},k)=={(1,0):F(10)})
 p={(a+1,10-a):C*F(comb(10,a),2)*(-k/11)**a for a in range(11)}
 ck(key+'_temperature_invariant',L(p,k)=={});ck(key+'_coefficient_of_rs10',p[(1,10)]==C/2)
 wrong=p.copy();wrong[(2,9)]+=1;ck(key+'_single_coefficient_negative',bool(L(wrong,k)))
 for ell in range(2,12):
  prev=p[(ell-1,12-ell)];curr=p[(ell,11-ell)]
  ck(key+f'_scalar_leading_recursion_{ell}',-11*(ell-1)*curr==k*(12-ell)*prev)
for degree in range(1,45):
 ker=[a for a in range(degree+1)if 10*a-(degree-a)==0];want=[degree//11]if degree%11==0 else[];ck(f'degree{degree}_diagonal_kernel',ker==want)
inputs=[]
for tag in ['n8w160','n5w110_C2khalf','n10w190']:
 f=D/(tag+'_coefficients.json');r=D/(tag+'.json')
 if not f.exists()or not r.exists():continue
 meta=json.loads(r.read_text())
 if meta['status']!='COMPLETE':continue
 dat=json.loads(f.read_text());C=F(meta['parameters']['C']);k=F(meta['parameters']['k']);inputs.append(dict(tag=tag,sha256=hashlib.sha256(f.read_bytes()).hexdigest(),parameters=meta['parameters']))
 for key,j in dat['theta'].items():
  ell=int(key)
  if not 1<=ell<=11:continue
  lead=11-ell;cs={int(e):F(c)for e,c in j['coefficients'].items()};assert lead<j['known_high']
  ck(f'{tag}_theta{ell}_lower_vanish',all(cs.get(i,F(0))==0 for i in range(lead)),dict(known_high=j['known_high'],tested_below=lead))
  val=C*F(comb(10,ell-1),2)*(-k/11)**(ell-1);ck(f'{tag}_theta{ell}_leading',cs.get(lead,F(0))==val,dict(actual=str(cs.get(lead,F(0))),expected=str(val)))
r=dict(started_utc=start,ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-tick,passed=sum(x['passed']for x in checks),total=len(checks),checks=checks,inputs=inputs,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='Exact algebra and finite coefficient controls of formal lowest-degree theorem; no convergence or actual zero curve.')
(V/'checks.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items()if k!='checks'},indent=2));print('FAILED',[c for c in checks if not c['passed']])
