"""Exact finite checks of the polynomial half-line counterexamples."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
from math import comb,factorial,gcd
import json,time
from flint import fmpq,fmpq_poly,arb,ctx
fq=lambda value:fmpq(str(value))
ctx.prec=256
start=time.monotonic();stamp=datetime.now(timezone.utc)
root=Path('research/92_halfline_poisson_obstruction/verification')/stamp.strftime('%Y%m%dT%H%M%SZ')
root.mkdir();(root/'sources').mkdir()
checks=0;rows=[]
for eta in [Q(1,100),Q(1,3),Q(1),Q(3)]:
 for mu in [Q(1,7),Q(2,3),Q(1),Q(3)]:
  for k in range(1,61):
   coeff=[fq(comb(k,j)*(-2*eta)**j/factorial(j)) for j in range(k+1)]
   p=fmpq_poly(coeff);y=fmpq_poly();term=p
   for j in range(k+1):
    y+=term*fq((-1)**j/mu**(j+1));term=term.derivative()
   assert y.derivative()+y*fq(mu)==p
   assert y[0]==fq((1+2*eta/mu)**k/mu)
   checks+=2
  ratio=arb(fq((1+2*eta/mu)**60/mu))/(2*arb(1).exp()*61)
  rows.append(dict(eta=str(eta),mu=str(mu),degree=60,ratio_lower_bound=ratio.str(30,radius=True)))
for b in range(2,31):
 for a in range(1,b):
  if gcd(a,b)>1:continue
  g=gcd(a,2);q0=2*b//g;eps=int(a//g==1)
  base=next(n for n in range(1,q0+1) if (a*n+g)%(2*b)==0)
  for k in [1,10,60,100]:
   n=base
   while max(0,(n-1)//q0-eps)<k or (a*n+g)//b-2<=0:n+=q0
   m=(a*n+g)//b-2
   assert m%2==0 and 1<=m-1<=2*n-1
   assert Q(2)-n*Q(a,b)+m==Q(g,b)
   checks+=2
for name in ['halfline_poisson_checks.py']:(root/'sources'/(name+'.txt')).write_bytes(Path('code',name).read_bytes())
result=dict(checked_at_utc=stamp.isoformat(timespec='seconds'),exact_checks=checks,rows=rows,actual_elapsed_s=time.monotonic()-start,scope='Finite exact identity and admissibility checks; the all-order proof is in PROOF.md.')
(root/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(output_directory=str(root),checks=checks,actual_elapsed_s=result['actual_elapsed_s'])),flush=True)
