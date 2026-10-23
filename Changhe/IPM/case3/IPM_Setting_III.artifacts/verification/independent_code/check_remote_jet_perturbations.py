#!/usr/bin/env python3
"""Exact independent Green-moment and Cartesian remote-jet tests."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime, timezone
from math import comb
import hashlib,json,time
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research/remote_jet_perturbations/verification'
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

cases=[]
for m in (2,4,6,8,10,12):
    for q in (3,5,8):
        phi=mul(power({1:F(1),0:F(-1)},q),power({0:F(2),1:F(-1)},q))
        normalization=integral(phi,F(1),F(2));phi=scalar(phi,1/normalization)
        f=shift(phi,m)
        check(integral(phi,F(1),F(2))==1,('bump normalization',m,q))
        for j in range(q):
            phi_j=phi
            for _ in range(j):phi_j=derivative(phi_j)
            check(value(phi_j,F(1))==value(phi_j,F(2))==0,('boundary vanishing',m,q,j))
        fp=derivative(f)
        gminus=scalar(add(fp,scalar(shift(f,-1),F(m+1))),F(1,2))
        gplus=scalar(add(fp,scalar(shift(f,-1),F(-m-1))),F(1,2))
        I=integral(shift(f,-m),F(1),F(2));J=integral(shift(f,m+2),F(1),F(2))
        check(I==1,('inner moment',m,q))
        moments=[]
        for k,g in ((m,gminus),(m+2,gplus)):
            inner=integral(shift(g,1-k),F(1),F(2))
            outer=integral(shift(g,k+1),F(1),F(2))
            check(inner==(m*I if k==m else 0),('inner source moment',m,q,k))
            check(outer==(0 if k==m else -(m+2)*J),('outer source moment',m,q,k))
            # Green formula inside the annulus, with independent exact antiderivatives.
            Ap=primitive(shift(g,k+1));A=add(Ap,{0:-value(Ap,F(1))})
            Bp=primitive(shift(g,1-k));B=add(scalar(Bp,F(-1)),{0:value(Bp,F(2))})
            P=scalar(add(shift(A,-k),shift(B,k)),F(1,2*k))
            radial_lap=add(add(derivative(derivative(P)),shift(derivative(P),-1)),scalar(shift(P,-2),F(-k*k)))
            check(scalar(radial_lap,F(-1))==g,('radial Poisson polynomial',m,q,k))
            Pin={k:inner/F(2*k)} if inner else {}
            Pout={-k:outer/F(2*k)} if outer else {}
            for order in range(2):
                check(value(P,F(1))==value(Pin,F(1)),('Green inner join',m,q,k,order))
                check(value(P,F(2))==value(Pout,F(2)),('Green outer join',m,q,k,order))
                P=derivative(P);Pin=derivative(Pin);Pout=derivative(Pout)
            moments.append({'frequency':k,'inner_source_moment':str(inner),'outer_source_moment':str(outer)})
        stream=sc2(imag_z(m),I/2)
        velocity_y=dx(stream)
        check(velocity_y==sc2(imag_z(m-1),m*I/2),('Cartesian harmonic derivative',m,q))
        c=stream.get((1,1),F(0))
        check(c==(I if m==2 else 0),('strain threshold',m,q))
        a=F(3,7);epsilon=F(5,11)
        response=sc2(velocity_y,-a*epsilon)
        if m==4:
            check(response[(2,1)]==-6*a*epsilon*I,('cubic xxy',q))
            check(response[(0,3)]==2*a*epsilon*I,('cubic yyy',q))
            check(response[(2,1)]+3*response[(0,3)]==0,('allowed cubic direction',q))
        cases.append({'m':m,'bump_boundary_power':q,'source_regularities':'phi and f extended by zero are C^'+str(q-1)+'; manufactured arithmetic test only, not smooth-primary candidate','I':str(I),'J':str(J),'interior_stream_coefficient':str(I/2),'exterior_stream_coefficient':str(-J/2),'canonical_strain':str(c),'source_moments':moments,'density_radial_polynomial':exact(f),'center_response_at_a_3over7_epsilon_5over11':{f'{i},{j}':str(v) for (i,j),v in sorted(response.items())}})
res={'utc':datetime.now(timezone.utc).isoformat(),'seconds':time.monotonic()-START,'checks':COUNT,'passed':True,'proof_sha256':hashlib.sha256((OUT.parent/'PROOF.md').read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'The theorem is for smooth compact bumps; these polynomial beta bumps are explicitly finite-regularity arithmetic tests. No stability or primary endpoint.','cases':cases}
(OUT/'EXACT_CHECKS.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps({k:v for k,v in res.items() if k!='cases'},indent=2))
for case in cases:
 if case['m']==4 and case['bump_boundary_power']==8:print(json.dumps(case,indent=2))
