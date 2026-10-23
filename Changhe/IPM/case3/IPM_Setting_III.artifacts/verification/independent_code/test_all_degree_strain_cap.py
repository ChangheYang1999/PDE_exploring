"""Independent exact polynomial-dictionary and positive-moment audit."""
from fractions import Fraction as F
from math import comb,prod
from pathlib import Path
from datetime import datetime,timezone
import json

def rising(x,k):return prod((x+j for j in range(k)),start=F(1))
def clean(p):return {k:v for k,v in p.items() if v}
def add(p,q,scale=1):
 z=dict(p)
 for k,v in q.items():z[k]=z.get(k,F(0))+scale*v
 return clean(z)
def der(p,coord):
 z={}
 for k,v in p.items():
  if k[coord]:
   j=list(k);j[coord]-=1;z[tuple(j)]=v*k[coord]
 return z
def lap(p):return add(der(der(p,0),0),der(der(p,1),1))
def euler(p,A):return clean({(i,j):(A*i+j-1)*v for (i,j),v in p.items()})
def jets(K,A,a):
 B=A-1;N=2*K;n=N+1;eta=1+F(K)/B;chi=1+F(N-a,2)/B
 g=[(-1)**j*comb(N,2*j)*rising(eta,j)*rising(chi+j,K-j) for j in range(K+1)]
 phi={(2*j+1,n-2*j):g[j]/F((2*j+1)*(n-2*j)) for j in range(K+1)}
 h={(2*j,n-2*j):-a*g[j]/F((n-2*j)*(N+2*B*j)) for j in range(K+1)}
 assert not add(euler(h,A),der(phi,0),a)
 assert not add(lap(phi),der(h,0))
 actual=der(der(phi,0),1)
 assert clean(actual)==clean({(2*j,N-2*j):g[j] for j in range(K+1)})
 for j in range(K):
  assert (2*j+2)*(2*j+1)*(j+chi)*g[j+1]+(N-2*j)*(N-2*j-1)*(j+eta)*g[j]==0
 return eta,chi,g
rows=[];moment=0;resonances=0
for K in range(1,16):
 for A in (F(101,100),F(3,2),F(2),F(5),F(37)):
  N=2*K;B=A-1;threshold=N*A
  av=[F(-2),F(1,3),threshold-F(1,100),threshold,threshold+1]+[N+2*B*j for j in range(1,K)]
  for a in av:
   eta,chi,g=jets(K,A,a)
   if a<threshold:
    u=chi+K-1;assert u>0
    expectation=F(0)
    for j in range(K+1):
     tm=rising(u,j)/prod((F(K,1)-F(1,2)-k for k in range(j)),start=F(1))
     sm=rising(F(1,2),j)/rising(eta,j)
     expectation+=g[j]*tm*sm
    assert expectation==0,(K,A,a,expectation)
    moment+=1
   if a==threshold:
    assert all(v==0 for v in g[:-1]) and g[-1]!=0
   if a>threshold:assert all(v*g[0]>0 for v in g)
   resonance=next((j for j in range(1,K+1) if a==N+2*B*j),None)
   if resonance is not None:
    assert all(v==0 for v in g[:resonance]) and g[resonance]!=0;resonances+=1
   rows.append({'K':K,'A':str(A),'a':str(a),'subthreshold':a<threshold,'resonance_index':resonance})
# Independently chosen gradient-only counterexample, different from the audited source.
A=F(37);a=F(-2)
h={(0,5):F(1,10),(2,3):F(-2,39),(4,1):F(38,2925)}
phi={(1,5):F(1,5),(3,3):F(-76,117),(5,1):F(2812,14625)}
assert not add(euler(h,A),der(phi,0),a)
assert not add(lap(phi),der(h,0))
g=der(der(phi,0),1);P1=sum(g.values());assert P1==F(-11363,2925)
Qdisc=F(1,169)-4*F(1,4)*F(19,2925);assert Qdisc==F(-22,38025)
# Nonlinear remainder polynomial: only degree9, since both leading equations hold.
D=F(18);ell=F(19)
rho=add(h,{(0,1):a});ps=add(phi,{(1,1):-D})
U1={k:-v for k,v in der(ps,1).items()};U2=der(ps,0)
W1=add(U1,{(1,0):ell});W2=add(U2,{(0,1):ell})
def mul(p,q):
 z={}
 for (i,j),v in p.items():
  for (k,l),w in q.items():z[(i+k,j+l)]=z.get((i+k,j+l),F(0))+v*w
 return clean(z)
R=add(add(mul(W1,der(rho,0)),mul(W2,der(rho,1))),rho,-1)
assert R and set(i+j for i,j in R)=={9}
res={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','exact_polynomial_cases':len(rows),'positive_moment_zero_checks':moment,'resonance_checks':resonances,'cases':rows,'gradient_counterexample':{'ell':str(ell),'a':str(a),'P_at_1':str(P1),'Q_discriminant':str(Qdisc),'nonlinear_residual_degrees':[9]},'scope':'Finite exact implementation checks support, but do not replace, the all-K positive integral proof. No global capped profile constructed.'}
Path('research/all_degree_strain_cap/verification/checks.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps({k:v for k,v in res.items() if k not in ('cases','scope')}),flush=True)
