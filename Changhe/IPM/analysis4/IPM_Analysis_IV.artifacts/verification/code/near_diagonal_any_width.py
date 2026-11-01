"""Exact lower-degree witnesses for every tested positive band width."""
from pathlib import Path
from datetime import datetime,timezone
from math import factorial,comb
import json,time,sys
sys.dont_write_bytecode=True
from laurent_log_audit import Q,parse
from maximal_log_cartesian_check import poisson
start=time.monotonic();rows=[];den=3;delta=Q(2,den);c=Q(den,den-2)
for eta in [Q(1,4),Q(1),Q(3,2),Q(3),Q(10),Q(100)]:
 for size in [4,8,12]:
  k=int(size*(1+eta))+1;q=int(Q(k-1)/(1+eta));i=den*k+1;h=4*k-3;P=2-i*delta;p=P-1
  assert q>=1 and q<=k-1
  assert all(abs(s)>eta*q for s in [4-2*k-delta,2*k-delta])
  assert abs(2-2*delta)<=eta*2*q
  F=parse(p,{1:[0]*q+[1],h:[0]*q+[1]});G=poisson(F);J=G.X()*F.Y()-G.Y()*F.X()
  T=-(-2*P**2+(h-1)**2*P+4*(h+1))/(4*(P+h+1)*(P+2))
  assert 2*J.a[2*q][J.M+h+2]==T
  lam=(2*i-1)*(c-1)
  rows.append(dict(eta=str(eta),k=k,q=q,input_norm=str(Q(2,comb(k-1,q))),target_coefficient=str(T/lam),output_lower=str(factorial(2*q)*abs(T/lam)),all_exact=True))
record=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z'),all_passed=True,witness_count=len(rows),rows=rows,actual_elapsed_s=time.monotonic()-start)
p=Path('research/74_near_diagonal_norm');(p/'verification/general_width_checks.json').write_text(json.dumps(record,indent=2)+'\n');(p/'sources/near_diagonal_any_width.py.txt').write_bytes(Path(__file__).read_bytes())
print(json.dumps({k:v for k,v in record.items() if k!='rows'}))
