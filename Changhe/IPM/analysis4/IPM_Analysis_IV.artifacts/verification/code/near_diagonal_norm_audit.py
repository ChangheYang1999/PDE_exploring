"""Exact Cartesian witnesses for the near-diagonal mixed-norm obstruction."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from math import factorial,comb
import json,time,sys
sys.dont_write_bytecode=True
from laurent_log_audit import Q,parse
from maximal_log_cartesian_check import poisson
start=time.monotonic();root=Path('research/74_near_diagonal_norm');rows=[];linear=0
for den in [3,4,5,9,17]:
 delta=Q(2,den);c=Q(den,den-2)
 for k in [4,5,6,8,10,14,18]:
  i=den*k+1;n=2*i;q=k-1;h=4*k-3;P=2-i*delta;p=P-1
  F=parse(p,{1:[0]*q+[1],h:[0]*q+[1]});G=poisson(F)
  bL=-1/(2*(P+2));bH=-1/(2*(P+h+1))
  assert 2*G.a[q][G.M+2]==bL
  assert 2*G.a[q][G.M+h+1]==bH
  J=G.X()*F.Y()-G.Y()*F.X()
  T=(bH*(P-p*(h+1))+bL*(P*h-2*p))/2
  displayed=-(-2*P**2+(h-1)**2*P+4*(h+1))/(4*(P+h+1)*(P+2))
  assert T==displayed
  actual=2*J.a[2*q][J.M+h+2];assert actual==T,(den,k,actual,T)
  lam=(n-1)*(c-1);term=J.scale(1/lam);H=term
  while term.a:term=term.dt().scale(c/lam);H=H+term
  assert (H.scale(lam)-H.dt().scale(c)-J).zero()
  assert 2*H.a[2*q][H.M+h+2]==T/lam
  lower=Q((h-1)**2,4*(h+1));assert abs(T)>=lower
  distances=[4-2*k-delta,2*k-delta];outdist=2-2*delta
  assert outdist==(h+2)+3-n*delta
  bands=[]
  for eta in [Q(1,4),Q(1),Q(3,2)]:
   off=all(abs(s)>eta*q for s in distances);near=abs(outdist)<=eta*2*q
   bands.append(dict(eta=str(eta),both_inputs_off=off,output_near=near,witness_active=off and near))
  rows.append(dict(Q=den,k=k,order=i,output_order=n,degree=q,output_degree=2*q,frequency=h+2,T=str(T),output_coefficient=str(T/lam),mixed_output_lower=str(factorial(2*q)*abs(T/lam)),all_exact_identities=True,bands=bands))
for q in range(1,81):
 for C in [Q(1,4),Q(1,2),Q(1),Q(2),Q(5)]:
  s=Q(q)/C
  exact=sum((Q(factorial(q),factorial(q-h))/s**(h+1) for h in range(q+1)),Q(0))
  bound=Q(q+1)/s*max(Q(1),C)**q
  assert exact<=bound;linear+=1
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z'),cartesian_witnesses=len(rows),linear_estimates=linear,all_passed=True,rows=rows,actual_elapsed_s=time.monotonic()-start)
(root/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
for name in ['near_diagonal_norm_audit.py','maximal_log_cartesian_check.py','laurent_log_audit.py']:(root/'sources'/(name+'.txt')).write_bytes(Path('code',name).read_bytes())
print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
