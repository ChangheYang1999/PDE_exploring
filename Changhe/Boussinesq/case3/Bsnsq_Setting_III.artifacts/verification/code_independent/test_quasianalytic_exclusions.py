"""Independent exact controls for the already written informal proof185.
These finite identities do not prove a universal derivative estimate or B2 existence.
"""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
from time import perf_counter
import json
import sympy as s
root=Path('research/185_quasianalytic_B2_exclusions/verification')
root.mkdir(parents=True,exist_ok=True)
t0=perf_counter();started=datetime.now(timezone.utc).isoformat();checks=[];negative=[]
def check(name,condition,detail=''):
    assert bool(condition),name
    checks.append({'name':name,'pass':True,'detail':detail})
def reject(name,condition,detail):
    assert bool(condition),name
    negative.append({'name':name,'detected':True,'detail':detail})
t,E=s.symbols('t E',positive=True);L=s.log(t+E)
g=t*s.log(L)
rhs=(2*L-t/(t+E)*(L+1))/((t+E)*L**2)
check('log-weight second derivative',s.simplify(s.diff(g,t,2)-rhs)==0)
# Monotone ratio examples need not satisfy the divergent sum. This finite
# induction algebra tests exactly the bounds used before taking the limit.
for family in ['constant','linear','quadratic']:
 for a in [Q(1,100),Q(1,8),Q(1,4)]:
  for n in range(1,9):
   mu={j: Q(2) if family=='constant' else Q(j) if family=='linear' else Q(j*j) for j in range(1,n+1)}
   M={0:Q(1)}
   for j in range(1,n+1):M[j]=M[j-1]*mu[j]
   F={(j,n+1):Q(0) for j in range(n+1)}
   for k in range(n,0,-1):
    F[k,k]=M[k]
    for j in range(k-1,-1,-1):
     F[j,k]=F[j,k+1]+a/mu[k]*F[j+1,k]
     check(f'interval induction {family} a{a} n{n} k{k} s{j}',F[j,k] <= (2*a)**(k-j)*M[j])
   check(f'final interval {family} a{a} n{n}',F[0,1]<=2*a)
# Exact multinomial line derivatives, independently expanded through degree8.
x,y,u,v=s.symbols('x y u v')
for k in range(9):
 f=(x+2*y)**(k+2)+x**2*y**(k+1)
 direct=s.diff(f.subs({x:x+t*u,y:y+t*v},simultaneous=True),t,k).subs(t,0)
 multi=sum(s.binomial(k,j)*u**j*v**(k-j)*s.diff(f,x,j,y,k-j) for j in range(k+1))
 check(f'multinomial degree{k}',s.expand(direct-multi)==0)
 check(f'line coefficient sum{k}',s.expand(sum(s.binomial(k,j)*u**j*v**(k-j) for j in range(k+1))-(u+v)**k)==0)
# Jet transport eigenvalues used at an endpoint.
for k in range(8):
 for j in range(k+1):
  f=x**(k-j)*y**j
  check(f'endpoint vorticity monomial {k},{j}',s.expand(4*y*s.diff(f,y)+f-(4*j+1)*f)==0 and 4*j+1>0)
  check(f'endpoint thermal monomial {k},{j}',s.expand(4*y*s.diff(f,y)-4*j*f)==0)
# Two derivative-closure steps and summable-majorant bookkeeping are symbolic.
D=s.symbols('D',positive=True)
for j in range(1,11):
 check(f'two closure factors {j}',s.expand(D**j*D**(j+1)-D**(2*j+1))==0)
 check(f'Fourier constants {j}',s.expand(8**(j+2)*D**(2*j+1)-64*D*(8*D**2)**j)==0)
check('summable upper bound',sum(Q(1,n*n) for n in range(2,101)) < sum(Q(1,n*(n-1)) for n in range(2,101)) < 1)
for n in range(2,11):check(f'telescoping majorant{n}',Q(1,n*(n-1))==Q(1,n-1)-Q(1,n))
# Exact all-order symbolic identities in the coupled polynomial control.
Theta=x*x;Omega=2*x;W=(0,4*y-x*x);Psi=2*x*y-x**3/s.Integer(3)
U=(s.diff(Psi,y),-s.diff(Psi,x))
check('analytic polynomial thermal equation',s.expand(W[0]*s.diff(Theta,x)+W[1]*s.diff(Theta,y))==0)
check('analytic polynomial vorticity equation',s.expand(W[0]*s.diff(Omega,x)+W[1]*s.diff(Omega,y)+Omega-s.diff(Theta,x))==0)
check('analytic polynomial elliptic equation',s.expand(-s.diff(Psi,x,2)-s.diff(Psi,y,2)-Omega)==0)
reject('reversed streamfunction convention fails W',s.expand(2*x+U[0]-W[0])!=0,'Using U=(Psi_y,−Psi_x) has the opposite sign to Omega=−DeltaPsi. The valid control below uses U=(−Psi_y,Psi_x).')
# This polynomial uses Psi for the opposite velocity convention if U=+nabla-perp
# here; use the B2 convention U=(-Psi_y,Psi_x) below, not a silent sign change.
U=(-s.diff(Psi,y),s.diff(Psi,x))
check('analytic polynomial correct B2 velocity convention',s.expand(2*x+U[0]-W[0])==0 and s.expand(2*y+U[1]-W[1])==0)
reject('dropping sublinear velocity creates false analytic NO',s.Poly(U[1],x,y).total_degree()==2,'The coupled polynomial satisfies both transport equations but U=(−2x,2y−x²) is not o(r).')
reject('dropping zeroth derivative makes uniqueness false',s.diff(s.Integer(1),x)==0 and s.Integer(1)!=0,'The constant1 has all positive derivatives zero but is not flat including order0.')
reject('dropping connectedness makes global uniqueness false',s.Integer(0)!=s.Integer(1),'On disjoint intervals use constants0 and1: both are analytic; flatness on the first says nothing about the second.')
reject('summand bounds do not imply series bounds',sum(Q(1) for _ in range(10))>1,'Ten summands each bounded by1 already exceed1. The proof uses an n^−2 majorant instead.')
reject('interval induction threshold is necessary for this estimate',2*Q(1,2)+Q(1,2)>1,'For constant ratios and a=1/2 the displayed induction bracket is3/2, not at most1.')
# Smooth flat function shows why removing the reciprocal-sum assumption fails.
z=s.symbols('z',positive=True);h=s.exp(-1/z**2)
for j in range(7):check(f'flat Gevrey manufacture derivative{j}',s.limit(s.diff(h,z,j),z,0,dir='+')==0)
reject('nonquasianalytic smooth extension stays nonzero',h.subs(z,1)==s.exp(-1) and h.subs(z,1)!=0,'exp(−1/t²) on t>0 extended by0 is smooth flat and nonzero; no unrestricted smooth NO follows.')
ended=datetime.now(timezone.utc).isoformat();out={'verdict':'PASS','started_utc':started,'ended_utc':ended,'elapsed_seconds':perf_counter()-t0,'exact_count':len(checks),'negative_count':len(negative),'exact_checks':checks,'negative_controls':negative,'scope':'Finite exact algebra and explicit counterexamples only. Universal inequalities and B2 geometric conclusions rely on the complete prior informal proof, not these finite cases.'}
(root/'controls.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k not in ['exact_checks','negative_controls']})
