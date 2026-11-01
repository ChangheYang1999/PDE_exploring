"""Integer Bareiss and primitive Sturm certificates; CAS is only an expression parser."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction as F
from math import gcd,lcm
from functools import reduce
import json,time,sys
sys.dont_write_bytecode=True
import sympy as sp
root=Path('research/136_three_mode_responses');start=time.monotonic()
b,t=sp.symbols('b tau')
Odata=json.loads(Path('research/125_explicit_compatible_shape/verification/obstruction_polynomial.json').read_text())
O={(r['b_degree'],r['tau_degree']):F(r['coefficient']) for r in Odata['terms']}
Sdata=json.loads((root/'verification/symbolic_response.json').read_text())
Spoly=sp.Poly(sp.sympify(Sdata['sigma_infinity']),b,t,domain=sp.QQ)
S={m:F(str(c)) for m,c in Spoly.terms()}
Rdata=json.loads((root/'verification/limiting_resultant.json').read_text())
Rpoly=sp.Poly(sp.sympify(Rdata['resultant']),t,domain=sp.QQ)
R=[F(str(c)) for c in reversed(Rpoly.all_coeffs())]
assert max(i+j for i,j in O)==6 and max(i+j for i,j in S)==3
assert max(i for i,j in O)==6 and max(i for i,j in S)==3
assert all(j==0 for i,j in O if i==6) and all(j==0 for i,j in S if i==3)
dO=reduce(lcm,(c.denominator for c in O.values()),1);dS=reduce(lcm,(c.denominator for c in S.values()),1)
Oi={m:int(c*dO) for m,c in O.items()};Si={m:int(c*dS) for m,c in S.items()}
def trim(a):
 a=list(a)
 while a and a[-1]==0:a.pop()
 return a

def horner(a,x):
 y=0
 for c in reversed(a):y=y*x+c
 return y

def at_tau(poly,degree,value):
 a=[0]*(degree+1)
 for (i,j),c in poly.items():a[i]+=c*value**j
 return a

def bareiss(A):
 A=[row[:] for row in A];n=len(A);sign=1;prev=1
 for k in range(n-1):
  if A[k][k]==0:
   pivot=next((r for r in range(k+1,n) if A[r][k]),None)
   if pivot is None:return 0
   A[k],A[pivot]=A[pivot],A[k];sign=-sign
  a=A[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    top=A[i][j]*a-A[i][k]*A[k][j]
    assert top%prev==0
    A[i][j]=top//prev
   A[i][k]=0
  prev=a
 return sign*A[-1][-1]

def resultant(f,g):
 m=len(f)-1;n=len(g)-1;A=[]
 for shift in range(n):A.append([0]*shift+list(reversed(f))+[0]*(n-1-shift))
 for shift in range(m):A.append([0]*shift+list(reversed(g))+[0]*(m-1-shift))
 return bareiss(A)

samples=[]
for value in range(19):
 det=resultant(at_tau(Oi,6,value),at_tau(Si,3,value));expected=horner(R,F(value))*dO**3*dS**6
 assert expected.denominator==1 and det==expected.numerator
 samples.append(dict(tau=value,sylvester_determinant=str(det),matches=True))

def primitive(a):
 a=trim(a)
 if not a:return []
 d=reduce(lcm,(F(c).denominator for c in a),1);ints=[int(c*d) for c in a];g=reduce(gcd,(abs(c) for c in ints),0)
 return [c//g for c in ints]

def remainder(a,b):
 a=list(map(F,trim(a)));b=list(map(F,trim(b)))
 while a and len(a)>=len(b):
  q=a[-1]/b[-1];shift=len(a)-len(b)
  for j,c in enumerate(b):a[shift+j]-=q*c
  a=trim(a)
 return a

seq=[primitive(R)];seq.append(primitive([i*c for i,c in enumerate(seq[0])][1:]))
while len(seq[-1])>1:
 r=primitive([-c for c in remainder(seq[-2],seq[-1])]);assert r
 seq.append(r)
assert len(seq[-1])==1

def sign(v):return (v>0)-(v<0)
def variations(signs):
 a=[v for v in signs if v];return sum(x!=y for x,y in zip(a,a[1:]))
def vf(x):return variations([sign(horner(a,x)) for a in seq])
def vi(negative):return variations([sign(a[-1])*(-1 if negative and (len(a)-1)%2 else 1) for a in seq])
roots=[]
for row in Rdata['real_root_intervals']:
 lo,hi=map(F,row['interval']);a,c=vf(lo),vf(hi);assert a-c==1
 roots.append(dict(interval=row['interval'],sturm_variations=[a,c],simple=True))
assert vi(True)-vi(False)==2 and vf(F(-3))-vf(F(98))==0
# An independent finite-field certificate for the two specialization polynomials.
def mt(a,p):
 return trim([int(c)%p for c in a])
def mr(a,b,p):
 a=mt(a,p);b=mt(b,p);inv=pow(b[-1],-1,p)
 while len(a)>=len(b):
  q=a[-1]*inv%p;s=len(a)-len(b)
  for j,c in enumerate(b):a[s+j]=(a[s+j]-q*c)%p
  a=trim(a)
 return a
def mm(a,b,p):
 out=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]=(out[i+j]+x*y)%p
 return trim(out)
def mp(a,e,f,p):
 out=[1]
 while e:
  if e%2:out=mr(mm(out,a,p),f,p)
  a=mr(mm(a,a,p),f,p);e//=2
 return out
def ms(a,b,p):return mt([(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))],p)
def mg(a,b,p):
 while b:a,b=b,mr(a,b,p)
 return mt([c*pow(a[-1],-1,p) for c in a],p)
def irred(a,p,tests):
 a=mt(a,p);a=mt([c*pow(a[-1],-1,p) for c in a],p);h=[0,1];rows=[]
 for j in range(1,len(a)):
  h=mp(h,p,a,p)
  if j in tests:
   g=mg(a,ms(h,[0,1],p),p);assert g==[1];rows.append(dict(order=j,gcd=g))
 assert ms(h,[0,1],p)==[]
 return dict(prime=p,monic_coefficients_ascending=a,gcd_checks=rows,final_frobenius_remainder=[],irreducible=True)
P6=primitive(at_tau(O,6,F(0)))
P10=list(map(int,json.loads(Path('research/130_period_five_tuning/verification/irreducibility_sturm_checks.json').read_text())['primitive_coefficients_ascending']))
modular=[irred(P6,19,{2,3}),irred(P10,11,{2,5})]
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,degree_bound=18,obstruction_clear_denominator=str(dO),response_clear_denominator=str(dS),nineteen_sylvester_checks=samples,primitive_sturm_sequence=[[str(c) for c in a] for a in seq],sturm_variations_at_infinities=[vi(True),vi(False)],real_root_count=2,isolating_intervals=roots,variations_at_minus3_and98=[vf(F(-3)),vf(F(98))],no_real_resultant_zero_in_minus3_to98=True,specialization_irreducibility=modular,actual_elapsed_s=time.monotonic()-start)
(root/'verification/independent_resultant_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
(root/'sources/independent_resultant_certificate.py').write_bytes(Path('code/independent_resultant_certificate.py').read_bytes())
files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}
(root/'verification/MANIFEST.json').write_text(json.dumps(dict(files=files),indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['primitive_sturm_sequence','nineteen_sylvester_checks']},indent=2),flush=True)
