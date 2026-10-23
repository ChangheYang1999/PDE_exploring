#!/usr/bin/env python3
"""Independent exact Mellin, Green, logarithm and angular-grade checks.

The complete proposed proof was written before this checker. No producer,
lead, or earlier verifier implementation is imported. All arithmetic below
is rational; no symbolic integration package or model-generated proof is
being treated as a formal certificate.
"""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import time

start=time.monotonic()
count=0

def ck(ok,label):
    global count
    if not ok:
        raise AssertionError(label)
    count+=1

def trim(a):
    a=list(a)
    while a and not a[-1]: a.pop()
    return a

def add(a,b):
    c=[F(0)]*max(len(a),len(b))
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    return trim(c)

def scale(a,c): return trim([x*c for x in a])
def der(a): return trim([i*a[i] for i in range(1,len(a))])
def monomial(d): return [F(0)]*d+[F(1)]

def first_inverse(P,lam):
    ck(lam != 0,'nonzero first-order diagonal')
    Q=[F(0)]*len(P)
    for i in range(len(P)-1,-1,-1):
        Q[i]=(P[i]-(i+1)*Q[i+1] if i+1<len(Q) else P[i])/lam
    ck(add(scale(Q,lam),der(Q))==trim(P),'first-order Euler inverse')
    return trim(Q)

def mellin_inverse(P,lam,m):
    # Solve -Q''-2lam Q'+(m^2-lam^2)Q=P by descending coefficients.
    a=m*m-lam*lam
    if a:
        Q=[F(0)]*len(P)
        for i in range(len(P)-1,-1,-1):
            extra=F(0)
            if i+1<len(Q):extra+=2*lam*(i+1)*Q[i+1]
            if i+2<len(Q):extra+=(i+2)*(i+1)*Q[i+2]
            Q[i]=(P[i]+extra)/a
    else:
        ck(lam == -m,'only decaying resonance used')
        # Solve 2m Q'-Q''=P. Fix Q(0)=0.
        Q=[F(0)]*(len(P)+1)
        for i in range(len(P)-1,-1,-1):
            extra=(i+2)*(i+1)*Q[i+2] if i+2<len(Q) else F(0)
            Q[i+1]=(P[i]+extra)/(2*m*(i+1))
    Q=trim(Q)
    result=add(add(scale(Q,a),scale(der(Q),-2*lam)),scale(der(der(Q)),-1))
    ck(result==trim(P),'Mellin polynomial equation')
    return Q

resonances=[]
green_cases=0
for m in [2,4,6,8,12,16]:
    for s in [F(1,3),F(2,5),F(-1,7),F(-2),F(-m-1),F(-m-3,1),F(-m-1)+F(1,11),F(-m-1)-F(1,13)]:
        lam=s+1; beta=m+lam; gam=lam-m
        ck(gam<0,'outer Green integral converges')
        for d in range(6):
            P=monomial(d)
            Q=mellin_inverse(P,lam,m)
            Jg=first_inverse(P,gam)
            if beta:
                Jb=first_inverse(P,beta)
                G=scale(add(Jb,scale(Jg,-1)),F(1,2*m))
                ck(G==Q,'independent integrated Green polynomial agrees')
                harmonic=-Jb[0]/(2*m)
                # Match the outer Green stream and derivative at r=1 to the
                # regular interior multiple r^m, where source vanishes.
                interior=-Jg[0]/(2*m)
                ck(Q[0]+harmonic==interior,'Green value at inner cutoff')
                qprime=der(Q)
                ck(lam*Q[0]+(qprime[0] if qprime else 0)-m*harmonic==m*interior,
                   'Green first derivative at inner cutoff')
                ck((beta>0)==(s>-m-1),'multipole remainder threshold')
            else:
                integ=scale(monomial(d+1),F(1,d+1))
                G=scale(add(integ,scale(Jg,-1)),F(1,2*m))
                difference=add(G,scale(Q,-1))
                ck(len(difference)<=1,'resonant inverse differs only by harmonic constant')
                ck(len(Q)==d+2,'resonance increases log degree exactly once')
                ck(Q[0]==0,'resonant normalization is stated')
                gp=der(G)
                interior=-Jg[0]/(2*m)
                ck(G[0]==interior,'resonant Green value at cutoff')
                ck(lam*G[0]+gp[0]==m*interior,'resonant Green derivative at cutoff')
                resonances.append({'m':m,'s':str(s),'source_log_degree':d,'stream_log_degree':len(Q)-1})
            green_cases+=1

# Transport integral: verify the Euler differential identity, using an
# independently assembled factorial-moment expression for the integral.
from math import comb, factorial
transport_cases=0
for p in [F(1,9),F(1,3),F(2,5),F(1,2),F(7,8)]:
    ell=1/p
    for s in [2*p-1,3*p-2,F(-3),F(-5),p-F(1,17)]:
        ck(s<p,'transport integration endpoint')
        for d in range(8):
            Q=[F(0)]*(d+1)
            for j in range(d+1):
                Q[d-j]+=F(comb(d,j)*factorial(j),1)/(ell*(p-s)**(j+1))
            lhs=add(scale(Q,ell*s-1),scale(der(Q),ell))
            ck(lhs==scale(monomial(d),-1),'Volterra integral solves Euler equation')
            ck(len(trim(Q))==d+1,'transport does not add logarithms')
            transport_cases+=1

# Exact grade propagation. Inputs include interior multipoles and coincident
# radial costs. The checks do not assume the costs have unique representations.
collisions=0
boundary_modes=0
for p in [F(1,3),F(2,5),F(1,2),F(7,8)]:
    delta=1-p
    cost_reps={}
    for k in range(13):
        for l in range(4):cost_reps.setdefault(k*delta+2*l,[]).append((k,l))
    collisions+=sum(len(v)>1 for v in cost_reps.values())
    costs=sorted(cost_reps)[:16]
    for n in [1,3,5,9]:
        C=(n+1)/delta
        ck(C>2,'positive grade gap')
        for t in costs:
            bound=n+C*t
            density_modes=[j for j in range(1,int(bound)+1,2)]
            chosen=set(density_modes[:2]+density_modes[-2:])
            for j in chosen:
                ck(j<=bound,'input grade')
                for m in [j-1,j+1]:
                    if m:
                        ck(m<=n+1+C*t,'inverse preserves grade')
                        if m==n+1+C*t:
                            ck(j==bound and m==j+1,'equality uses top source')
            for m in range(2,18,2):
                q=p+m+1
                ck(m<n+1+C*q,'free multipole strict grade')
                for j in chosen:
                    newcost=t+m+2
                    ck(m+j<n+C*newcost,'harmonic interaction strictly below boundary')
            for u in costs:
                outcost=delta+t+u
                ck((n+1+C*t)+(n+C*u)==n+C*outcost,'induced transport exact grade')
        for k in range(60):
            s=(k+1)*p-k
            j=(k+1)*(n+1)-1
            m=j+1
            ck(j==n+C*(k*delta),'formal cascade reaches grade boundary')
            ck(m>abs(s+1),'boundary inverse never resonates')
            ck(j-s>0 and j+s+2>0,'factored nonresonance')
            if k:
                ck(s/p-1==-k*(1/p-1),'boundary Euler coefficient')
            boundary_modes+=1

out={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'PASS','exact_checks':count,
     'elapsed_seconds':time.monotonic()-start,'green_cases':green_cases,
     'resonant_green_cases':resonances,'transport_cases':transport_cases,
     'coincident_costs_in_samples':collisions,'boundary_modes_checked':boundary_modes,
     'method':'Independent rational polynomial Euler inverses and integrated Green formulas, including logarithmic resonance, matching and strict angular grades',
     'scope':'Supporting exact algebra only. Exterior all-order finite-expansion induction and its hypotheses require the standalone written proof and review.',
     'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
p=Path('research/exterior_finite_angular/verification/CHECK.json')
p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='resonant_green_cases'},indent=2))
