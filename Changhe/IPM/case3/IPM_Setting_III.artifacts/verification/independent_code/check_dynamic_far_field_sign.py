#!/usr/bin/env python3
"""Own rational checks of DR tail coefficient, map extraction and scalar law."""
from fractions import Fraction as F
from pathlib import Path
from math import comb,factorial
from datetime import datetime,timezone
import json,hashlib,time
START=time.monotonic();OUT=Path('research/dynamic_far_field_sign/verification');assert(OUT/'PROOF_WRITTEN_BEFORE_CODE.txt').exists();counts={}
def check(x,group):
 counts[group]=counts.get(group,0)+1
 if not x:raise AssertionError(group)
def clean(a):return{k:v for k,v in a.items() if v}
def add(a,b):
 c=dict(a)
 for k,v in b.items():c[k]=c.get(k,F())+v
 return clean(c)
def scale(a,z):return clean({k:z*v for k,v in a.items()})
def mul(a,b):
 c={}
 for (i,j),v in a.items():
  for(k,l),w in b.items():c[(i+k,j+l)]=c.get((i+k,j+l),F())+v*w
 return clean(c)
def circle(a):
 c={}
 for(i,j),v in a.items():
  for k in range(i//2+1):c[(i%2,j+2*k)]=c.get((i%2,j+2*k),F())+v*comb(i//2,k)*(-1)**k
 return clean(c)
x={(1,0):F(1)};y={(0,1):F(1)};one={(0,0):F(1)}
sin3={(2,1):F(3),(0,3):F(-1)}
cases=[]
for C in (F(3,2),F(2),F(5,2),F(3),F(7),F(101,100)):
 p=1/C;delta=1-p;s=2*p-1
 for A in (F(1),F(-3,7),F(11,5)):
  H=-A/(2*(p+3))
  gx=scale(add(y,scale(mul(mul(x,x),y),p-1)),2*H)
  gy=scale(add(x,scale(mul(x,mul(y,y)),p-1)),2*H)
  rx=scale(mul(x,y),A*(p-1));ry=scale(add(one,scale(mul(y,y),p-1)),A)
  adv=add(scale(mul(gy,rx),-1),mul(gx,ry))
  want=scale(add(scale(y,3*p+1),scale(sin3,delta)),-A*A/(4*(p+3)))
  check(not circle(add(adv,scale(want,-1))),'Cartesian_advection')
  check((4-(p+1)**2)*H==A*(p-1)/2,'Poisson_leading')
  check(1-C*p==0 and 1-C*s==C-1,'rate_and_trace')
  Q=A*A*delta/(4*(p+3));check(Q>0,'positive_forcing')
  for cw in (F(1,8),F(3,10),F(7,3)):
   lam=(C-1)*cw;bstar=-Q/lam
   check(bstar==-A*A/(4*C*cw*(p+3)) and bstar<0,'steady_sign_and_normalization')
  if A==1:cases.append(dict(C=str(C),p=str(p),degree=str(s),Q=str(Q),constant_cw_1_8_steady_b3=str(-Q/((C-1)*F(1,8)))))
# Formal power series operations, independently solve integrating factor and ODE.
K=14
def sa(a,b):return[(a[i] if i<len(a) else F())+(b[i] if i<len(b) else F()) for i in range(min(K,max(len(a),len(b))))]
def sm(a,b):return[sum((a[j]*b[i-j] for j in range(max(0,i-len(b)+1),min(i+1,len(a)))),F()) for i in range(min(K,len(a)+len(b)-1))]
def sd(a):return[F(i)*a[i] for i in range(1,len(a))]
def si(a):return[F()]+[v/(i+1) for i,v in enumerate(a[:K-1])]
def ss(a,c):return[v*c for v in a]
def se(a):
 assert a[0]==0
 out=[F(1)]+[F() for _ in range(K-1)];power=[F(1)]
 for n in range(1,K):power=sm(power,a);out=sa(out,ss(power,F(1,factorial(n))))
 return out
for lam in ([F(2)],[F(-3,7)],[F()],[F(1),F(-2),F(3,5)],[F(-1),F(7,4)]):
 for Q in (F(1,60),F(3,68),F(7,9)):
  L=si(lam);inside=si(se(ss(L,-1)));ifac=ss(sm(se(L),inside),Q)
  direct=[F() for _ in range(K)]
  for j in range(1,K):direct[j]=((Q if j==1 else 0)+sum((lam[i]*direct[j-1-i] for i in range(min(len(lam),j))),F()))/j
  check(ifac==direct,'integrating_factor_series')
  rhs=sa(sm(lam,direct),[Q]);check(sd(direct)==rhs[:K-1],'scalar_ODE_series')
  check(direct[1]==Q,'initial_positive_derivative')
# Endpoint expansion from finite Chebyshev polynomials in w, independent of E/E'.
def trim(a,n=5):return a[:n]+[F() for _ in range(max(0,n-len(a)))]
def poly_add(a,b):return trim(sa(a,b))
def poly_mul(a,b):return trim(sm(a,b))
def pow1minus(alpha):
 out=[F(1)];z=F(1)
 for j in range(1,5):z=z*(alpha-j+1)/j;out.append((-1)**j*z)
 return out
def chebs_w(N):
 out=[trim([F(1)]),trim([F(1),F(-2)])]
 for j in range(2,N+1):out.append(poly_add(ss(poly_mul([F(1),F(-2)],out[-1]),2),ss(out[-2],-1)))
 return out[:N+1]
for delta in (F(1,3),F(2,3),F(3,5),F(7,8)):
 for k in range(8):
  for N in (0,1,3,7,12):
   for seed in range(3):
    u=[F((-1)**(j+seed)*(j+1)*(seed+1),j+seed+2) for j in range(N+1)]
    beta=[F()]*5
    for v,T in zip(u,chebs_w(N)):beta=poly_add(beta,ss(T,v))
    E=sum(u,F());Ep=sum((j*j*v for j,v in enumerate(u)),F())
    check(beta[0]==E and beta[1]==-2*Ep,'Chebyshev_endpoint')
    weighted=poly_mul(pow1minus(k+delta/2),beta)
    H=(k+delta/2)*E+2*Ep
    check(weighted[0]==E and weighted[1]==-H,'Q_map_first_correction')
# Direct odd-sine conversion of sin(theta)*cos(2k theta).
for k in range(8):
 H=F(3*k+2,k+1);sines={}
 for n,c in ((1+2*k,H/2),(1-2*k,H/2)):
  nn=abs(n);sines[nn]=sines.get(nn,F())+(c if n>0 else -c)
 expected=H/2 if k==1 else -H/2 if k==2 else F()
 check(sines.get(3,F())==expected,'third_mode_extraction')
# A pure radial constant start: map lower first mode may be present, third never is.
for delta in (F(2,3),F(3,5),F(1,3)):
 for beta0 in (F(1),F(-1),F(7,9)):
  D=F(1,2);A=D*beta0;B1=-D*D*delta*beta0/2;Q=A*A*delta/(4*(4-delta))
  check(B1!=0 and Q>0,'constant_start')
for source in json.loads((OUT/'sources.json').read_text())['files']:
 check(hashlib.sha256(Path(source['frozen']).read_bytes()).hexdigest()==source['sha256'],'source_hash')
result=dict(utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-START,status='PASS',checks=sum(counts.values()),counts=counts,cases=cases,proof_sha256=hashlib.sha256((OUT.parent/'PROOF.md').read_bytes()).hexdigest(),code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='Exact finite coefficient identities and scalar ODE checks. Time-uniform asymptotic expansion remains an explicit hypothesis; no DR existence/stability theorem.')
(OUT/'EXACT_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
