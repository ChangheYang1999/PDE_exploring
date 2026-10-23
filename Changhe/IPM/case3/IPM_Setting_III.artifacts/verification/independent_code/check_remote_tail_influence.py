#!/usr/bin/env python3
"""Exact independent scaled remote-tail moments and core bounds."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime, timezone
from math import comb
import hashlib,json,time
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research/remote_tail_influence/verification'
assert (OUT/'PROOF_WRITTEN_BEFORE_CODE.txt').exists()
START=time.monotonic();COUNT=0

def check(v,label):
    global COUNT
    COUNT+=1
    if not v:raise AssertionError(label)

def clean(P):return {k:v for k,v in P.items() if v}

def add(P,Q):
    R=dict(P)
    for k,v in Q.items():R[k]=R.get(k,F(0))+v
    return clean(R)

def mul(P,Q):
    R={}
    for i,a in P.items():
        for j,b in Q.items():R[i+j]=R.get(i+j,F(0))+a*b
    return clean(R)

def scalar(P,a):return clean({k:v*a for k,v in P.items()})

def shift(P,j):return {k+j:v for k,v in P.items()}

def derivative(P):return clean({k-1:k*v for k,v in P.items()})

def primitive(P):
    assert not P.get(-1,F(0)), 'unexpected logarithmic primitive in polynomial test'
    return clean({k+1:v/(k+1) for k,v in P.items()})

def value(P,x):return sum(v*x**k for k,v in P.items())

def integral(P,a,b):
    Q=primitive(P);return value(Q,b)-value(Q,a)

def exact(P):return {str(k):str(v) for k,v in sorted(P.items())}

def power(P,n):
    R={0:F(1)}
    for _ in range(n):R=mul(R,P)
    return R

def imag_z(n):
    return {(n-j,j):F(comb(n,j)*(-1)**((j-1)//2)) for j in range(1,n+1,2)}

def dx(P):return {(i-1,j):i*v for (i,j),v in P.items() if i}

def sc2(P,a):return {k:v*a for k,v in P.items() if a*v}

from math import factorial
import resource
resource.setrlimit(resource.RLIMIT_AS,(256*1024**2,256*1024**2))
resource.setrlimit(resource.RLIMIT_CPU,(25,25))

def dy(P):return {(i,j-1):j*v for (i,j),v in P.items() if j}
def ev2(P,x,y):return sum(v*x**i*y**j for (i,j),v in P.items())
cases=[]
for boundary in (2,4,8):
 bump=mul(power({1:F(1),0:F(-1)},boundary),power({0:F(2),1:F(-1)},boundary));norm=integral(bump,F(1),F(2));check(norm==F(factorial(boundary)**2,factorial(2*boundary+1)),('beta integral',boundary));f=shift(scalar(bump,1/norm),2)
 for R in (F(1,3),F(1),F(4),F(17)):
  fr={k:v*R**(1-k) for k,v in f.items()};check(integral(shift(fr,-2),R,2*R)==1,('fixed strain under outward scaling',boundary,R))
  first=derivative(fr);g2=scalar(add(first,scalar(shift(fr,-1),F(3))),F(1,2));g4=scalar(add(first,scalar(shift(fr,-1),F(-3))),F(1,2))
  for m,g in ((2,g2),(4,g4)):
   inside=integral(shift(g,1-m),R,2*R);outside=integral(shift(g,m+1),R,2*R)
   check(inside==(F(2) if m==2 else 0),('source Green interior moment',boundary,R,m))
   if m==2:check(outside==0,('no exterior mode2',boundary,R))
   else:check(outside==-4*integral(shift(fr,4),R,2*R),('exterior mode4 moment',boundary,R))
  for n in range(boundary):
   ftest=fr
   for _ in range(n):ftest=derivative(ftest)
   check(value(ftest,R)==value(ftest,2*R)==0,('scaled bump boundary derivatives',boundary,R,n))
  for C in (F(3,2),F(5,2),F(3)):
   c0=F(-2,7);dc=F(1);cw0=-c0/(C-1);cw1=-(c0+dc)/(C-1)
   check(cw1-cw0==-dc/(C-1),('instantaneous slope-gauge response',boundary,R,C))
  cases.append(dict(boundary_power=boundary,R=str(R),density_coefficient_scaling='h_R=R f(r/R) sin(3theta)',canonical_strain='1',interior_stream='xy',finite_regular_test='C^'+str(boundary-1)+' after extension; theorem uses smooth compact f'))
for p in (F(1,10),F(1,3),F(2,5),F(3,4),F(9,10)):
 delta=1-p
 for m in range(2,82,2):
  check(m/(m-p-1)<=2/delta,('uniform even-mode inverse ratio',p,m))
  check(m-p-1>0 and p+1-m<0,('source boundary decay and moment integrability',p,m))
 for q in (F(0),F(1,5),F(1,2),F(4,5),F(9,10)):
  n=19
  S=sum(q**(2*j-1) for j in range(1,n+1));tail=q**(2*n+1)/(1-q*q)
  check(S+tail==q/(1-q*q),('velocity geometric sum',p,q))
  D=sum((2*j-1)*q**(2*j-2) for j in range(1,n+1));Dtail=q**(2*n)*((2*n+1)-(2*n-1)*q*q)/(1-q*q)**2
  check(D+Dtail==(1+q*q)/(1-q*q)**2,('derivative geometric sum',p,q))
  check(sum(F(m,1)/(m-p-1)*q**(m-1) for m in range(2,2*n+1,2))<=2/delta*S,('summed velocity majorant',p,q))
  check(sum(F(m*(m-1),1)/(m-p-1)*q**(m-2) for m in range(2,2*n+1,2))<=2/delta*D,('summed Hessian majorant',p,q))
 check(-(2*p-3)-1==2*delta>0,('subleading tail integral exponent',p))
 check(1+(-2*delta)/delta==-1,('moving-radius inverse-amplitude decay',p))
for m in range(2,22,2):
 P=imag_z(m);Px=dx(P);Py=dy(P);Pxx=dx(Px);Pxy=dy(Px);Pyy=dy(Py)
 for rr in (F(1,5),F(2,3),F(4,3)):
  for xx,yy in ((F(3,5),F(4,5)),(F(5,13),F(12,13))):
   x,y=rr*xx,rr*yy
   check(ev2(Px,x,y)**2+ev2(Py,x,y)**2==m*m*rr**(2*m-2),('harmonic gradient exact norm',m,rr,xx))
   check(ev2(Pxx,x,y)**2+ev2(Pxy,x,y)**2==(m*(m-1))**2*rr**(2*m-4),('harmonic Hessian operator exact norm',m,rr,xx))
   check(ev2(Pxx,x,y)+ev2(Pyy,x,y)==0,('harmonic Hessian traceless',m,rr,xx))
res={'utc':datetime.now(timezone.utc).isoformat(),'seconds':time.monotonic()-START,'checks':COUNT,'passed':True,'proof_sha256':hashlib.sha256((OUT.parent/'PROOF.md').read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact remote-moment/scaling/core-bound arithmetic, smooth theorem distinct from finite-regularity bump tests; no DR trajectory computed','cases':cases}
(OUT/'EXACT_CHECKS.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps({k:v for k,v in res.items() if k!='cases'},indent=2))
