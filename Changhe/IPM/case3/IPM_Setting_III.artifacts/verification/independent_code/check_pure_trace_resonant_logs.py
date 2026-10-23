#!/usr/bin/env python3
"""Own independent exact real-trig and Cartesian Laurent recurrences."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, time

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'research/pure_trace_resonant_logs/verification'
assert (OUT/'PROOF_WRITTEN_BEFORE_CODE.txt').exists()
START = time.monotonic()
CHECKS = 0

def check(value, label):
    global CHECKS
    CHECKS += 1
    if not value:
        raise AssertionError(label)

def clean(a):
    return {k:v for k,v in a.items() if v}

def add(a,b):
    c=dict(a)
    for k,v in b.items(): c[k]=c.get(k,F(0))+v
    return clean(c)

def scale(a,c): return clean({k:v*c for k,v in a.items()})

def rsine_add(a,n,v):
    if n:
        n,v=(n,v) if n>0 else (-n,-v)
        a[n]=a.get(n,F(0))+v

def rsource(P,s):
    out={}
    for n,a in P.items():
        rsine_add(out,n+1,a*(s-n)/2)
        rsine_add(out,n-1,a*(s+n)/2)
    return clean(out)

def rinverse(P,s):
    out={}
    for n,a in rsource(P,s).items():
        assert n*n!=(s+1)**2
        out[n]=a/(n*n-(s+1)**2)
    return clean(out)

def rbilinear(H,P,si,sj):
    out={}
    for m,h in H.items():
        for n,a in P.items():
            rsine_add(out,n+m,h*a*(-m*sj+(si+1)*n)/2)
            rsine_add(out,n-m,h*a*(-m*sj-(si+1)*n)/2)
    return clean(out)

# Second implementation: signed Laurent coefficients, Cartesian derivatives.
def cart_x(a,q):
    out={}
    for n,v in a.items():
        for target,factor in ((n+1,(q-n)/2),(n-1,(q+n)/2)):
            out[target]=out.get(target,F(0))+factor*v
    return clean(out)

def cart_y_over_i(a,q):
    out={}
    for n,v in a.items():
        for target,factor in ((n+1,(n-q)/2),(n-1,(n+q)/2)):
            out[target]=out.get(target,F(0))+factor*v
    return clean(out)

def convolution(a,b):
    out={}
    for n,v in a.items():
        for m,w in b.items():out[n+m]=out.get(n+m,F(0))+v*w
    return clean(out)

def cinverse(D,s):
    source=cart_x(D,s)
    return {n:v/(n*n-(s+1)**2) for n,v in source.items()}

def cbilinear(S,D,si,sj):
    one=convolution(cart_y_over_i(S,si+1),cart_x(D,sj))
    two=convolution(cart_x(S,si+1),cart_y_over_i(D,sj))
    return add(one,scale(two,F(-1)))

def to_laurent(P):
    out={}
    for n,v in P.items():out[n]=-v/2;out[-n]=v/2
    return clean(out)

def exact_dict(a):return {str(n):str(v) for n,v in sorted(a.items())}

# Manufactured derivative/advection checks independent of the cascade samples.
for s in (F(1,3),F(2,5),F(-3),F(-7,4),F(-5)):
    for n in range(1,16,2):
        P={n:F(n+1,7)}
        check(cart_x(to_laurent(P),s)==to_laurent(rsource(P,s)),('source',s,n))
        for m in range(2,14,2):
            H={m:F(3-m,11)};si=F(2,7)
            check(cbilinear(to_laurent(H),to_laurent(P),si,s)==to_laurent(rbilinear(H,P,si,s)),('advection',s,n,m))

cases=[]
for ell,kstar,mstar in ((F(3),5,2),(F(5,2),9,4)):
    p=1/ell;delta=1-p
    sr=[p-k*delta for k in range(kstar+1)]
    R=[{1:F(1)}];C=[{1:F(-1,2),-1:F(1,2)}]
    RH=[];CH=[]
    for k in range(kstar+1):
        if k:
            rsum={};csum={}
            for i in range(k):
                j=k-1-i
                rsum=add(rsum,rbilinear(RH[i],R[j],sr[i],sr[j]))
                csum=add(csum,cbilinear(CH[i],C[j],sr[i],sr[j]))
            R.append(scale(rsum,1/(ell*k*delta)))
            C.append(scale(csum,1/(ell*k*delta)))
        check(to_laurent(R[k])==C[k],('density',ell,k))
        check(all(n>0 and n%2==1 for n in R[k]),('density parity',ell,k))
        check(cart_x(C[k],sr[k])==to_laurent(rsource(R[k],sr[k])),('sources',ell,k))
        if k<kstar:
            RH.append(rinverse(R[k],sr[k]));CH.append(cinverse(C[k],sr[k]))
            check(to_laurent(RH[k])==CH[k],('stream',ell,k))
            q=sr[k]+1
            lap=add(scale(cart_x(cart_x(CH[k],q),q-1),F(-1)),cart_y_over_i(cart_y_over_i(CH[k],q),q-1))
            check(lap==cart_x(C[k],sr[k]),('Cartesian Poisson',ell,k))
            check(all(n%2==0 for n in RH[k]),('stream parity',ell,k))
    check(R[1]=={1:-(3*p+1)/(4*ell*delta*(p+3)),3:-1/(4*ell*(p+3))},('first correction',ell))
    check(sr[kstar]==-mstar-1,('resonant degree',ell))
    source=rsource(R[kstar],sr[kstar]);g=source.get(mstar,F(0))
    check(cart_x(C[kstar],sr[kstar]).get(mstar,F(0))==-g/2,('resonant numerator',ell))
    critical_previous=mstar-1
    check(g==-mstar*R[kstar].get(critical_previous,F(0)),('critical low mode formula',ell))
    # No resonance of any sector occurs before this one; the first is pure.
    found=[]
    target=p+mstar+1
    for k in range(kstar+1):
        for l in (0,*range(2,10)):
            t=k*delta+2*l
            if t>target:continue
            for m in range(2,mstar+1,2):
                if p-t==-m-1:found.append((k,l,m))
    check(found==[(kstar,0,mstar)],('sector arithmetic',ell,found))
    log_stream={mstar:g/(2*mstar)}
    # Highest-log part checked by Cartesian differentiation, including Poisson.
    q=F(-mstar)
    highest_log_lap=add(scale(cart_x(cart_x(to_laurent(log_stream),q),q-1),F(-1)),cart_y_over_i(cart_y_over_i(to_laurent(log_stream),q),q-1))
    check(highest_log_lap=={},('resonant harmonic coefficient',ell))
    # -[(q+d_z)^2-m^2](g z/(2m)) = g, exactly.
    check(-2*q*g/(2*mstar)==g,('resonant log Poisson',ell))
    log_density=scale(cbilinear(to_laurent(log_stream),C[0],F(-mstar-1),p),1/(ell*(mstar+2)))
    expected={mstar-1:-g*delta/(4*ell*(mstar+2)),mstar+1:-g*(1+p)/(4*ell*(mstar+2))}
    check(log_density==to_laurent(expected),('first density log',ell))
    # All formula dimensions and amplitude exponents tracked separately.
    check(p-mstar-2==p-(kstar+1)*delta,('density log degree',ell))
    cases.append({'ell':str(ell),'p':str(p),'delta':str(delta),'first_resonance_k':kstar,'stream_frequency':mstar,'source_coefficient_A_power':kstar+1,'g_star_at_A1':str(g),'nonzero':bool(g),'g_star_float_for_orientation_only':float(g),'source_degree':str(sr[kstar]-1),'stream_log_degree':str(-mstar),'stream_log_coefficient_at_A1':str(g/(2*mstar)),'density_log_degree':str(p-mstar-2),'density_log_A_power':kstar+2,'density_log_coefficients_at_A1':exact_dict(expected),'density_coefficients_at_A1':[{'k':k,'degree':str(sr[k]),'sine':exact_dict(P)} for k,P in enumerate(R)],'stream_coefficients_at_A1':[{'k':k,'degree':str(sr[k]+1),'sine':exact_dict(H)} for k,H in enumerate(RH)],'resonant_source_sine':exact_dict(source),'sector_resonances_at_or_before_target':found})

result={'utc':datetime.now(timezone.utc).isoformat(),'seconds':time.monotonic()-START,'checks':CHECKS,'passed':True,'actual_model':'GPT-6 referee, verifier','scope':'Finite exact arithmetic. All asymptotic implications require the stated proof hypotheses. No primary endpoint.','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256((OUT.parent/'PROOF.md').read_bytes()).hexdigest(),'cases':cases}
(OUT/'EXACT_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
for c in cases:print(json.dumps({k:v for k,v in c.items() if k not in ('density_coefficients_at_A1','stream_coefficients_at_A1','resonant_source_sine')},indent=2))
print(json.dumps({'checks':CHECKS,'seconds':result['seconds'],'passed':True}))
