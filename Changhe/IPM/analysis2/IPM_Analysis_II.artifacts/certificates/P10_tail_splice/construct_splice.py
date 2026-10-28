"""Exact finite homogeneous potential inversion and explicit exterior bounds.
Original canonical rational coefficients and verified stationary-tail coefficients only.
All output stays inside this lane. No archived executable is imported.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import comb,factorial,ceil
from datetime import datetime,timezone
import hashlib,json,sys
from flint import arb,ctx
HERE=Path(__file__).resolve().parent; BASE=HERE.parents[1]
sys.path.insert(0,str(BASE/'05_tails/verification'))
from check_tail import density_stream
ctx.prec=384;sys.set_int_max_str_digits(0)

def enc(x):return str(x)
def clean(d):return {k:v for k,v in d.items() if v}
def invert(F,s):
    left=F.copy(); C={}
    assert max(F)%2==1
    for k in range(max(F),0,-2):
        m=k-1
        diag=-s*s*(s-2) if m==0 else -(s*s-m*m)*(s-2-m)/2
        assert diag
        v=left.get(k,Q(0))/diag
        if v:
            C[m]=v
            contrib,_=density_stream({m:v},s)
            for n,a in contrib.items():left[n]=left.get(n,Q(0))-a
    assert not clean(left)
    return clean(C)

def fall(t,n):
    ans=Q(1)
    for i in range(n):ans*=t-i
    return ans

def radial_bound(k,b,d):
    # A single coordinate derivative of H_(k,m)(X)*(r^2+t)^b, 0<=t<=1.
    # Factor 2^max(b,0) is applied outside this expression.
    ans=Q(0)
    for ell in range(min(d,2*k)+1):
        n=d-ell
        radial=sum((Q(factorial(n)*2**(n-2*p),factorial(n-2*p)*factorial(p))*abs(fall(b,n-p)) for p in range(n//2+1)),Q(0))
        ans+=comb(d,ell)*fall(Q(2*k),ell)*radial
    return ans

def hom_bound(s,m,d):
    # Each derivative changes the angular frequency by at most one.
    v=Q(1)
    for ell in range(d):v*=abs(s-ell)+m+ell
    return v

def log2ceil(q):
    n=0
    while Q(2)**n<q:n+=1
    return n

src=BASE/'source_audit/state131_exact.json';tail=BASE/'05_tails/verification/state131_formal_tail.json'
x=json.loads(src.read_text());t=json.loads(tail.read_text())
assert x['canonical_serialization_sha256']==t['input_sha256']
c=Q(x['exact_parameters']['cl']);gamma=1/c;delta=1-gamma
assert Q(9,5)<c<Q(37,20) and Q(1,2)<gamma<Q(3,5)
Cs={};ps={};checks={}
for n in range(1,7):
    F={int(k):Q(v) for k,v in t['stationary_density_orders'][str(n)]['coefficients'].items()}
    p=Q(t['stationary_density_orders'][str(n)]['power']);s=p+3
    assert p==1-n*delta and s.denominator!=1
    C=invert(F,s); G,P=density_stream(C,s)
    expected={int(k):Q(v) for k,v in t['stationary_stream_orders'][str(n)].items()}
    assert clean(G)==F and clean(P)==expected
    Cs[n]=C;ps[n]=p
    checks[n]={'density_exact':True,'canonical_stream_exact':True,'maximum_potential_harmonic':max(C)}
lead={}
for (j,m,k),a in zip(x['canonical_order'],x['canonical_coefficients']):
    if j==0:lead[2*m]=lead.get(2*m,Q(0))+Q(a)
assert clean(lead)==Cs[1]
original={d:Q(0) for d in range(11)}
AA={d:Q(0) for d in range(11)}
for (j,m,k),a in zip(x['canonical_order'],x['canonical_coefficients']):
    assert k>=m
    a=abs(Q(a)); sj=3+gamma-j*delta; b=sj/2-k
    assert b<2
    for d in range(11):
        original[d]+=4*a*radial_bound(k,b,d)
        if j==0:
            assert b-1<1
            AA[d]+=2*a*abs(b)*radial_bound(k,b-1,d)
        else:AA[d]+=4*a*radial_bound(k,b,d)
for n in range(2,7):
    for m,v in Cs[n].items():
        for d in range(11):AA[d]+=abs(v)*hom_bound(ps[n]+3,m,d)
cut={0:Q(1)}
for d in range(1,11):
    cut[d]=sum((Q(factorial(d),factorial(d-2*b)*factorial(b)*2**b)*Q(4,3)**(d-2*b)*Q(2,3)**b*factorial(d-b)*4096**(d-b) for b in range(d//2+1)),Q(0))
BB={d:sum((comb(d,l)*2**l*cut[l]*AA[d-l] for l in range(d+1)),Q(0)) for d in range(11)}
# Covers the SUM of full ordered rho and U tensors at every derivative order0..7.
# Original r^(gamma-j) plus perturbation r^(p2-j) <= same symbol for r>=1.
KK={j:2**(j+3)*(original[j+3]+BB[j+3]) for j in range(8)}
Cmax=max(KK.values());cpow=log2ceil(Cmax)
# Use the rational gamma<3/5 to avoid a numerical comparison of powers.
Rpow=1024
assert Q(cpow)-Q(2,5)*Rpow<-10
assert Rpow>=3
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'verdict':'CONFIRMED',
 'canonical_sha256':x['canonical_serialization_sha256'],'source_file_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
 'stationary_tail_file_sha256':hashlib.sha256(tail.read_bytes()).hexdigest(),
 'c':str(c),'gamma':str(gamma),'p2':str(ps[2]),'p7':str(1-7*delta),
 'homogeneous_potential_orders':{str(n):{'exponent':str(ps[n]+3),'cosine_coefficients':{str(k):str(v) for k,v in Cs[n].items()},'checks':checks[n]} for n in Cs},
 'leading_potential_exactly_preserved':True,
 'original_potential_component_symbol_bounds':{str(k):str(v) for k,v in original.items()},
 'difference_potential_component_symbol_bounds':{str(k):str(v) for k,v in AA.items()},
 'cutoff_component_derivative_bounds':{str(k):str(v) for k,v in cut.items()},
 'cutoff_difference_component_symbol_bounds':{str(k):str(v) for k,v in BB.items()},
 'combined_density_velocity_symbol_bounds':{str(k):str(v) for k,v in KK.items()},
 'uniform_symbol_power_two_exponent':cpow,'R':'2^1024','R_power':Rpow,
 'exterior_symbol_smallness_power_two_exponent':str(Q(cpow)-Q(2,5)*Rpow),
 'exterior_smallness_target':'1/1024','scope':'Exact potential repair, original center preserved, explicit derivative symbol bound. No residual smallness or existence claimed.'}
(HERE/'state131_splice.json').write_text(json.dumps(out,indent=2)+'\n')
summary={k:out[k] for k in ('utc','verdict','gamma','p2','p7','leading_potential_exactly_preserved','uniform_symbol_power_two_exponent','R','exterior_symbol_smallness_power_two_exponent','exterior_smallness_target')}
summary['potential_max_harmonics']={n:max(C) for n,C in Cs.items()}
print(json.dumps(summary,indent=2),flush=True)
