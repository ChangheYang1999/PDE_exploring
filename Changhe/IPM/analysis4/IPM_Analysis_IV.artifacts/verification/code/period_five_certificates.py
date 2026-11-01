"""Exact modular irreducibility and Sturm certificates for the Q=5 obstruction."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time,sys,itertools
sys.dont_write_bytecode=True
import sympy as sp
from flint import nmod_poly
root=Path('research/130_period_five_tuning');start=time.monotonic();b=sp.Symbol('b')
data=json.loads((root/'verification/obstruction_checks.json').read_text())
O=sp.Poly(sp.sympify(data['O10']),b,domain=sp.QQ);den,P=O.clear_denoms();cont,P=P.primitive()
if P.LC()<0:P=-P
# Polynomial arithmetic below uses ascending coefficient lists modulo p.
def trim(a,p):
 a=[int(c)%p for c in a]
 while a and not a[-1]:a.pop()
 return a
def rem(a,f,p):
 a=trim(a,p);f=trim(f,p);inv=pow(f[-1],-1,p)
 while len(a)>=len(f):
  q=a[-1]*inv%p;d=len(a)-len(f)
  for j,c in enumerate(f):a[d+j]=(a[d+j]-q*c)%p
  a=trim(a,p)
 return a
def mul(a,b,p):
 c=[0]*(max(0,len(a)+len(b)-1))
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
 return trim(c,p)
def power(a,n,f,p):
 r=[1]
 while n:
  if n%2:r=rem(mul(r,a,p),f,p)
  a=rem(mul(a,a,p),f,p);n//=2
 return r
def sub(a,b,p):return trim([(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))],p)
def gcd(a,b,p):
 while b:a,b=b,rem(a,b,p)
 if a:a=[x*pow(a[-1],-1,p)%p for x in a]
 return a
def irreducible(f,p):
 d=len(f)-1;x=[0,1];h=x;rows=[]
 for r in range(1,d+1):
  h=power(h,p,f,p)
  if d%r==0 and sp.isprime(d//r):
   g=gcd(f,sub(h,x,p),p);assert len(g)==1;rows.append(dict(frobenius_order=r,gcd=g))
 assert rem(sub(h,x,p),f,p)==[]
 return dict(degree=d,prime_divisor_gcd_checks=rows,final_frobenius_remainder=[])
try:
 possible=set(range(1,P.degree()));rows=[]
 for p in list(sp.primerange(2,1000)):
  if int(P.LC())%p==0:continue
  factors=nmod_poly([int(c)%p for c in reversed(P.all_coeffs())],p).factor()[1];pro=[1];degrees=[];cert=[]
  for fac,mult in factors:
   f=trim(fac.coeffs(),p);mult=int(mult);check=irreducible(f,p)
   cert.append(dict(coefficients_ascending=f,multiplicity=mult,irreducibility=check))
   for _ in range(mult):pro=mul(pro,f,p);degrees.append(len(f)-1)
  target=trim(list(reversed(P.all_coeffs())),p);scalar=target[-1]*pow(pro[-1],-1,p)%p
  assert trim([scalar*c for c in pro],p)==target
  subset={0}
  for d in degrees:subset|={x+d for x in tuple(subset)}
  possible&=subset
  rows.append(dict(prime=p,factor_degrees=degrees,factors=cert,product_scalar=scalar,remaining_possible_rational_factor_degrees=sorted(possible)))
  if not possible:break
 assert not possible,'No modular irreducibility certificate found under1000'
 sturm=sp.sturm(P.as_expr(),b)
 def changes(signs):
  signs=[s for s in signs if s];return sum(x!=y for x,y in zip(signs,signs[1:]))
 def vfinite(x):return changes([int(sp.sign(s.subs(b,x))) for s in sturm])
 def vinfty(neg=False):return changes([int(sp.sign(sp.Poly(s,b).LC()))*(-1 if neg and sp.degree(s,b)%2 else 1) for s in sturm])
 real=[]
 for rr in data['real_roots']:
  lo,hi=map(sp.Rational,rr['interval']);vl,vh=vfinite(lo),vfinite(hi);assert vl-vh==1
  real.append(dict(interval=rr['interval'],approx=str(sp.N((lo+hi)/2,30)),sturm_variations=[vl,vh],width=str(hi-lo)))
 assert vinfty(True)-vinfty(False)==len(real)==6
 result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,primitive_polynomial=str(P.as_expr()),primitive_coefficients_ascending=list(map(str,reversed(P.all_coeffs()))),irreducible_over_Q=True,modular_certificates=rows,real_root_count=6,sturm_variations_at_infinities=[vinfty(True),vinfty(False)],real_roots=real,actual_elapsed_s=time.monotonic()-start)
 (root/'verification/irreducibility_sturm_checks.json').write_text(json.dumps(result,indent=2)+'\n')
 (root/'sources/period_five_certificates.py').write_bytes(Path('code/period_five_certificates.py').read_bytes())
 files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}
 (root/'verification/MANIFEST.json').write_text(json.dumps(dict(files=files),indent=2)+'\n')
 print(json.dumps(result),flush=True)
except Exception as e:
 import traceback
 failure=dict(error_type=type(e).__name__,error=str(e),frames=[dict(file=Path(f.filename).name,line=f.lineno) for f in traceback.extract_tb(e.__traceback__)],actual_elapsed_s=time.monotonic()-start)
 (root/'verification/CERTIFICATE_FAILURE.json').write_text(json.dumps(failure,indent=2)+'\n');print(json.dumps(failure),flush=True);raise SystemExit(1)
