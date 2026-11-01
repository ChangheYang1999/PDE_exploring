"""Independent finite-field irreducibility and Arb values of the tuned examples."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from decimal import Decimal
from math import isqrt,gcd
from functools import reduce
import json,time,sys
sys.dont_write_bytecode=True
import sympy as sp
from flint import arb,fmpq,ctx
from gmpy2 import mpq as Q
ctx.prec=512
start=time.monotonic()
root=Path('research/119_tuned_rational_series')
b=sp.Symbol('b')
coeff=[10532171936,-243275209320,2783057141280,-20675598499400,96180432855375,-222533688701250,176703765525000]
assert reduce(gcd,coeff)==1

def trim(v):
 while v and v[-1]==0:v.pop()
 return v

def rem(a,f,p):
 a=trim([v%p for v in a]);inv=pow(f[-1],-1,p)
 while len(a)>=len(f):
  d=len(a)-len(f);c=a[-1]*inv%p
  for j in range(len(f)):a[j+d]=(a[j+d]-c*f[j])%p
  trim(a)
 return a

def mul(a,c,f,p):
 v=[0]*(len(a)+len(c)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(c):v[i+j]=(v[i+j]+x*y)%p
 return rem(v,f,p)

def power(a,n,f,p):
 v=[1]
 while n:
  if n&1:v=mul(v,a,f,p)
  a=mul(a,a,f,p);n//=2
 return v

def euclid(f,g,p):
 chain=[f,g]
 while g:
  f,g=g,rem(f,g,p);chain.append(g)
 return [v*pow(f[-1],-1,p)%p for v in f],chain

def minusx(v,p):
 v=v+[0]*max(0,2-len(v));v[1]=(v[1]-1)%p
 return trim(v)

def peval(c,x):
 value=Q(0)
 for v in reversed(c):value=value*x+v
 return value

def ball(q):return arb(fmpq(str(q)))

def evalpoly(expr,x):
 poly=sp.Poly(expr,b,domain=sp.QQ);v=arb(0)
 for c in poly.all_coeffs():v=v*x+ball(Q(str(c)))
 return v

def rounding_match(value,text):
 q=Q(text);quantum=Q(10)**Decimal(text).as_tuple().exponent
 interval=ball(q).union(ball(q+quantum/2)).union(ball(q-quantum/2))
 assert interval.contains(value),(text,value.str(60,radius=True))
 return dict(reported=text,contains_computed_enclosure=True)

try:
 prime=None
 for p in range(2,2000):
  if any(p%d==0 for d in range(2,isqrt(p)+1)) or coeff[-1]%p==0:continue
  inv=pow(coeff[-1],-1,p);f=[v*inv%p for v in coeff]
  xp=[0,1];powers={}
  for n in range(1,7):xp=power(xp,p,f,p);powers[n]=list(xp)
  if powers[6]!=[0,1]:continue
  checks={n:euclid(f,minusx(powers[n],p),p) for n in [2,3]}
  if any(v[0]!=[1] for v in checks.values()):continue
  prime=p;break
 assert prime is not None
 irreducible=dict(prime=prime,monic_mod_p=f,frobenius_remainders={str(k):v for k,v in powers.items()},gcd_chains={str(k):v[1] for k,v in checks.items()},irreducible_over_Q=True)
 (root/'verification/finite_field_irreducibility.json').write_text(json.dumps(irreducible,indent=2)+'\n')
 responses=json.loads((root/'verification/sigma_integer_exact.json').read_text())['rows'];s2=sp.sympify(next(r['sigma'] for r in responses if r['k']==2))
 R2=sp.sympify(json.loads((root/'verification/r2_exact.json').read_text())['R2_mod_P6'])
 references=json.loads((root/'sources/r2_exact.json').read_text())['values']
 root_intervals=json.loads(Path('research/120_tuned_explicit_radius/verification/response_bound.json').read_text())['rows']
 d=arb(2);B=4;eta=arb(10)/3;a=2/eta;bb=6/eta;bet=a.gamma()*bb.gamma()/(a+bb).gamma();radius=4*d*(a*bet)**(1/a)
 rows=[]
 for index,row in enumerate(root_intervals):
  lo,hi=map(Q,row['interval']);flo,fhi=peval(coeff,lo),peval(coeff,hi)
  assert flo*fhi<0
  for _ in range(220):
   mid=(lo+hi)/2;fm=peval(coeff,mid)
   if flo*fm<0:hi=mid;fhi=fm
   else:lo=mid;flo=fm
  assert flo*fhi<0
  x=ball(lo).union(ball(hi));rr=evalpoly(R2,x);ss=evalpoly(s2,x);hh=-rr/ss
  ref=list(references.values())[index]
  matched={key:rounding_match(value,ref[key]) for key,value in [('R2',rr),('sigma2',ss),('H6',hh)]}
  growth=x/radius
  printed=['0.0684','0.1575'][index];rounding_match(growth,printed)
  lower=Q(['0.0683','0.1575'][index]);assert growth>ball(lower)
  rows.append(dict(root_index=index+1,root_interval=[str(lo),str(hi)],endpoint_signs=[1 if flo>0 else -1,1 if fhi>0 else -1],b=x.str(65,radius=True),R2=rr.str(60,radius=True),sigma2=ss.str(60,radius=True),H6=hh.str(60,radius=True),source_rounding_checks=matched,highest_mode_radius=radius.str(60,radius=True),growth_lower_bound=growth.str(60,radius=True),printed_rounded_value=printed,safe_decimal_lower=str(lower)))
 result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),precision_bits=512,all_checks_pass=True,finite_field_prime=prime,rows=rows,actual_elapsed_s=time.monotonic()-start)
 (root/'verification/algebraic_numeric_values.json').write_text(json.dumps(result,indent=2)+'\n')
 (root/'verification/tuned_algebraic_certificate.py.txt').write_bytes(Path(__file__).read_bytes())
 files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in [root/'verification/finite_field_irreducibility.json',root/'verification/algebraic_numeric_values.json',root/'verification/tuned_algebraic_certificate.py.txt']}
 (root/'verification/algebraic_supplement_manifest.json').write_text(json.dumps(dict(files=files),indent=2)+'\n')
 print(json.dumps(result,indent=2),flush=True)
except Exception as exc:
 import traceback
 frames=traceback.extract_tb(exc.__traceback__)
 print(json.dumps(dict(error_type=type(exc).__name__,error=str(exc),frames=[{'file':Path(f.filename).name,'line':f.lineno,'code':f.line} for f in frames])),flush=True)
 raise SystemExit(1)
