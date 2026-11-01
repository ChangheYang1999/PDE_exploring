"""Exact arithmetic checks for the sharp common factorial-weight threshold."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
from math import gcd,factorial
import json,time,sys
sys.dont_write_bytecode=True
from flint import fmpq,fmpq_poly
start=time.monotonic();root=Path('research/89_sharp_column_weight');checks=0;params=0;witnesses=[]
for b in range(2,81):
 for a in range(1,b):
  if gcd(a,b)!=1:continue
  g=gcd(a,2);period=2*b//g;eps=int(a//g==1);params+=1
  n0=next(n for n in range(1,2*b+1) if (a*n+g)%(2*b)==0)
  for k in [0,1,7,32]:
   n=n0+period*(k+eps+2);m=(a*n+g)//b-2
   assert m>0 and m%2==0 and m-1<=2*n-1
   assert Q(2)-Q(a*n,b)+m==Q(g,b)
   assert k<=max(0,(n-1)//period-eps)
   checks+=3
mu=fmpq(2,3)
for k in range(101):
 p=fmpq_poly([(-1)**h*fmpq(factorial(k),factorial(k-h))/mu**(h+1) for h in range(k,-1,-1)])
 assert p.derivative()+p*mu==fmpq_poly([0]*k+[1]);checks+=1
 for s in [fmpq(1),fmpq(3,2),fmpq(2)]:
  ratio=sum(abs(v)*factorial(q)*s**q for q,v in enumerate(p))/ (2*factorial(k)*s**k)
  expected=sum((mu*s)**(-h) for h in range(k+1))/(2*mu)
  assert ratio==expected;checks+=1
  if s==2:assert ratio<3;checks+=1
  if s==fmpq(3,2):assert ratio==fmpq(3*(k+1),4);checks+=1
  if k in [0,1,10,50,100]:witnesses.append(dict(k=k,s=str(s),ratio=str(ratio)))
out=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),actual_elapsed_s=time.monotonic()-start,parameter_count=params,exact_checks=checks,witnesses=witnesses,scope='Finite checks supplement the standalone all-order operator proof.')
(root/'verification/checks.json').write_text(json.dumps(out,indent=2)+'\n');(root/'sources/sharp_column_weight_audit.py.txt').write_bytes(Path(__file__).read_bytes())
print(json.dumps({k:v for k,v in out.items() if k!='witnesses'}))
