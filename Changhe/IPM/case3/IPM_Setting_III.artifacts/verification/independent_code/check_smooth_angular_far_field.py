"""Exact independent Cartesian-operator gates for the smooth-angular expansion.
Signed Fourier coefficients and rational log polynomials; no producer code.
The finite gates supplement the proof, not its infinite-angular estimates.
"""
from fractions import Fraction as F
from pathlib import Path
from math import gcd
from datetime import datetime,timezone
import hashlib,json,time
start=time.monotonic();counts={}
def trim(a):
    a=list(a)
    while a and a[-1]==0:a.pop()
    return a
def add(a,b):
    return trim([(a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0))for i in range(max(len(a),len(b)))])
def scale(a,c):return trim([c*x for x in a])
def der(a):return trim([i*a[i] for i in range(1,len(a))])
def clean(spec):return {n:trim(a)for n,a in spec.items() if trim(a)}
def plus(a,b):
    out=dict(a)
    for n,v in b.items():out[n]=add(out.get(n,[]),v)
    return clean(out)
def dcart(spec,q,axis):
    # partial_x, and partial_y divided by i. A second y derivative
    # therefore has the negative of two applications of axis='y'.
    out={}
    for n,P in spec.items():
        if axis=='x':vplus=add(scale(P,q-n),der(P));vminus=add(scale(P,q+n),der(P))
        else:vplus=add(scale(P,n-q),scale(der(P),-1));vminus=add(scale(P,n+q),der(P))
        for j,v in [(n+1,vplus),(n-1,vminus)]:out[j]=add(out.get(j,[]),scale(v,F(1,2)))
    return clean(out)
def negative_lap(spec,q):
    xx=dcart(dcart(spec,q,'x'),q-1,'x');yy=dcart(dcart(spec,q,'y'),q-1,'y')
    return plus({n:scale(a,-1)for n,a in xx.items()},yy)
def solve(source,s):
    q=s+1;out={}
    for n,g in source.items():
        assert n!=0 and n%2==0
        eigen=F(n*n)-q*q
        if eigen:
            a=[F(0)]*(len(g)+2)
            for j in range(len(g)-1,-1,-1):a[j]=(g[j]+2*q*(j+1)*a[j+1]+(j+2)*(j+1)*a[j+2])/eigen
            out[n]=trim(a)
        else:
            assert q<0
            v=[];term=g;j=0
            while term:
                v=add(v,scale(term,1/((-2*q)**(j+1))));term=der(term);j+=1
            out[n]=trim([F(0)]+[v[j]/(j+1)for j in range(len(v))])
    return clean(out)
def check(group,ok,detail=None):
    assert ok,(group,detail)
    counts[group]=counts.get(group,0)+1
slopes=sorted(set([F(-m-1)for m in range(2,14,2)]+[F(v,3)for v in [-25,-20,-16,-11,-7,-2,0,1,2]]+[F(-23,5),F(-2),F(-1)]))
for s in slopes:
    for n in range(1,16,2):
        for d in range(6):
            P=[F((-1)**j*(j+2),j+3)for j in range(d+1)];density={n:P,-n:scale(P,-1)}
            source=dcart(density,s,'x');stream=solve(source,s)
            check('Cartesian_Poisson',negative_lap(stream,s+1)==source,(str(s),n,d))
            check('source_parity',all(m%2==0 and m!=0 and source.get(-m)==scale(v,-1)for m,v in source.items()))
            if any(F(m*m)==(s+1)**2 for m in source):
                check('resonant_log_degree',all(len(stream[m])==len(source[m])+1 for m in source if F(m*m)==(s+1)**2) and max(len(v)for v in stream.values())<=d+2,(str(s),n,d))
            else:check('nonresonant_log_degree',max(len(v)for v in stream.values())<=d+1,(str(s),n,d))
# A many-mode source also checks signed cancellation at mode zero.
for s in slopes:
    density={}
    for n in range(1,34,2):
        P=[F(1,2**n),F(n,3**n),F(-1,5**n)]
        density=plus(density,{n:P,-n:scale(P,-1)})
    source=dcart(density,s,'x');check('many_mode_Cartesian_Poisson',negative_lap(solve(source,s),s+1)==source)
# Independent check of T using its differential equation.
for ell in [F(3,2),F(2),F(5,2),F(3),F(7,2)]:
    p=1/ell
    for loss in [F(1,7),F(1,2),F(1),F(3),F(13,2)]:
        s=p-loss
        for d in range(9):
            G=[F(j+1,2*j+3)for j in range(d+1)];H=[];term=G;j=0
            while term:H=add(H,scale(term,1/(ell*loss**(j+1))));term=der(term);j+=1
            got=scale(add(scale(H,s-p),der(H)),ell)
            check('radial_integral_operator',got==scale(G,-1))
# Degree arithmetic, with the resonant source condition tested separately.
for v in range(2,23):
    for u in range(1,v):
        if gcd(u,v)!=1:continue
        delta=F(u,v);p=1-delta
        hits=[j for j in range(1,2*v+1)if (j*u)%(2*v)==0]
        check('least_divisibility',hits[0]==2*v//gcd(u,2),(u,v,hits))
        for k in range(0,2*v):
            for l in range(0,5):
                s=p-k*delta-2*l
                if s.denominator==1 and s<=-3 and (-s.numerator-1)%2==0:
                    check('every_critical_degree_divisible',((k+1)*u)%(2*v)==0,(u,v,k,l,str(s)))
        for k1,l1,k2,l2 in [(0,0,0,0),(1,2,3,4),(3,0,7,2)]:
            t1=k1*delta+2*l1;t2=k2*delta+2*l2
            check('induced_degree_closure',delta+t1+t2==(1+k1+k2)*delta+2*(l1+l2))
            for m in [2,4,10]:check('harmonic_degree_closure',m+2+t2==k2*delta+2*(l2+(m+2)//2))
# Explicit logarithmic sign control from f=r^-3 sin(theta).
source=dcart({1:[F(1)],-1:[F(-1)]},F(-3),'x');q=solve(source,F(-3))
check('critical_example_sign',q=={2:[F(0),F(-1,2)],-2:[F(0),F(1,2)]},str(q))
proof=Path('research/smooth_angular_far_field/PROOF.md');out=proof.parent/'verification/EXACT_CHECKS.json'
data=dict(utc=datetime.now(timezone.utc).isoformat(),proof_sha256=hashlib.sha256(proof.read_bytes()).hexdigest(),code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),counts=counts,passed=sum(counts.values()),elapsed_seconds=time.monotonic()-start,scope='Exact finite power-log Cartesian derivatives, angular inversions, resonance sign/degree, radial integration and rational arithmetic. Infinite-angle convergence, cutoff estimates and nonlinear induction are established in the informal proof, not by these gates.')
out.write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(data))
