"""Independent polar density/stream construction and rational power integration."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import json,hashlib,time,sys
from flint import fmpq as Q,fmpq_poly as P,arb,ctx
sys.set_int_max_str_digits(0);ctx.prec=1024
ROOT=Path(__file__).resolve().parents[1]
T=P([0,1]);U=P([1,-1]);Z=P([])
def q(x):
 f=Fraction(str(x));return Q(f.numerator,f.denominator)
def ar(x):return arb(x.numerator)/x.denominator
def put(A,j,n,V):
 if n==0 or not V:return
 if n<0:n,V=-n,-V
 A[j,n]=A.get((j,n),Z)+V
 if not A[j,n]:del A[j,n]
def divide(V):
 assert V[0]==0 and V[1]==0
 return P(list(V)[2:])
def rad(V,p):return 2*p*T*V+2*T*U*V.derivative()
def td(V,a,k=1):return (k-2*a*T)*V+2*T*U*V.derivative()
start=time.monotonic();src=ROOT/'data/state131.json';d=json.loads(src.read_text());c=q(d['cl']);delta=1-1/c
pot={}
for (j,m,k),x in zip(d['order'],d['coefficients']):
 pot[j,2*m]=pot.get((j,2*m),Z)+q(x)*T**k
rho={};stream={}
for (j,n),V in pot.items():
 p=(3+1/c-j*delta)/2
 B=rad(rad(V,p),p)-n*n*V;E=rad(B,p)-2*B
 put(rho,j,n-1,(E+n*B)/2);put(rho,j,n+1,-(E-n*B)/2)
 plus=rad(V,p)-n*V;plus=rad(plus,p)-(n+2)*plus
 minus=rad(V,p)+n*V;minus=rad(minus,p)+(n-2)*minus
 put(stream,j,n+2,plus/4);put(stream,j,n-2,-minus/4)
rho={k:divide(V) for k,V in rho.items()};stream={k:divide(V) for k,V in stream.items()}
F={}
for (j,n),V in rho.items():put(F,j,n,c*td(V,(j+1)*delta/2)-V)
for (j,m),S in stream.items():
 a=(j+1)*delta/2;BS=td(S,a,2)
 for (k,n),V in rho.items():
  b=(k+1)*delta/2;TV=td(V,b)
  put(F,j+k+1,n+m,(-m*S*TV+n*V*BS)/2)
  put(F,j+k+1,n-m,(-m*S*TV-n*V*BS)/2)
# Transform each whole polynomial exactly, then integrate the exact square.
a=Q(221,200);R=Q(2**29);by_mode={}
for (j,n),V in F.items():
 QV=V(U);order=next(k for k,x in enumerate(QV) if x)
 assert a-3+(j+1)*delta+2*order>-1
 by_mode.setdefault(n,[]).append((j+1,QV))
groups={}
for n,terms in by_mode.items():
 for i,(ell,V) in enumerate(terms):
  for k in range(i,len(terms)):
   ell2,W=terms[k];power=(ell+ell2)*delta/2-3
   groups[power]=groups.get(power,Z)+(1 if i==k else 2)*U*V*W
# All polynomial cancellation and grouping occurred over Q.
def primitive(power,V,upper,shift=Q(0)):
 x=ar(upper);total=arb(0)
 for k,coeff in enumerate(V):
  if not coeff:continue
  e=power+k+shift+1
  total+=ar(coeff)*x.log() if e==0 else ar(coeff/e)*x**ar(e)
 return total
rows=[];target_path=ROOT/'source/N4_state131.json';target=json.loads(target_path.read_text())
for t in target['annuli']:
 A=q(t['inner_radius']);B=q(t['outer_radius']);ua=1/(1+A*A);ub=1/(1+B*B)
 value=arb.pi()/2*sum((primitive(e,V,ua)-primitive(e,V,ub) for e,V in groups.items()),arb(0))
 lower=(value*(1+ar(B/R)**2)**ar(-a)).sqrt()
 assert value>0 and value.overlaps(arb(t['unweighted_mass'])) and lower.overlaps(arb(t['weighted_norm_lower']))
 rows.append({'inner_radius':str(A),'outer_radius':str(B),'unweighted_mass':value.str(80),'weighted_norm_lower':lower.str(80),'N4_overlap':True})
end=1/(1+R*R)
# Only nonzero combined monomials occur; check zero-endpoint primitive validity.
assert all(e+k+a+1>0 for e,V in groups.items() for k,v in enumerate(V) if v)
ext=arb.pi()/2*sum((primitive(e,V,end,a) for e,V in groups.items()),arb(0))
lower=((ar(R*R/2)**ar(a))*ext).sqrt()
assert lower>Q(25963336062) and lower.overlaps(arb(target['exterior_norm_lower']))
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'method':'Direct Laplacian plus polar stream-function products; all square coefficients rational before power evaluation','candidate':'state131','a':str(a),'R':str(R),'precision_bits':ctx.prec,'residual_modes':len(F),'power_groups':len(groups),'annuli':rows,'exterior_norm_lower':lower.str(100),'N4_exterior_overlap':True,'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'target_sha256':hashlib.sha256(target_path.read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'elapsed_seconds':time.monotonic()-start}
(ROOT/'verification/reproduction.json').write_text(json.dumps(out,indent=2)+'\n')
print('modes',len(F),'groups',len(groups),'exterior lower',lower.str(45),'seconds',out['elapsed_seconds'])
