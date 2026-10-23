"""Exact rational checks independent of Fourier transforms and shooting codes."""
from fractions import Fraction as F
from math import comb
from datetime import datetime, timezone
import json
from pathlib import Path

# Dict keys represent x^i y^j (x*x+y*y)^e, with rational coefficients.
def add(*terms):
    out={}
    for t in terms:
        for key,val in t.items():
            out[key]=out.get(key,F(0))+val
    return {k:v for k,v in out.items() if v}
def scale(t,a): return {k:a*v for k,v in t.items() if a*v}
def deriv(t,axis):
    out={}
    for (i,j,e),c in t.items():
        degrees=[i,j]
        if degrees[axis]:
            key=list((i,j,e)); key[axis]-=1
            out=add(out,{tuple(key):c*degrees[axis]})
        key=list((i,j,e)); key[axis]+=1; key[2]-=1
        out=add(out,{tuple(key):2*e*c})
    return out
def mulcoord(t,axis):
    out={}
    for key,c in t.items():
        key=list(key); key[axis]+=1; out[tuple(key)]=c
    return out
def iterate(t,axis,n):
    for _ in range(n): t=deriv(t,axis)
    return t
def lap(t): return add(iterate(t,0,2),iterate(t,1,2))
def canonical(t):
    if not t: return {}
    base=min(k[2] for k in t)
    out={}
    for (i,j,e),c in t.items():
        gap=e-base
        assert gap.denominator==1 and gap>=0
        gap=int(gap)
        for a in range(gap+1):
            key=(i+2*a,j+2*(gap-a),base)
            out[key]=out.get(key,F(0))+c*comb(gap,a)
    return {k:v for k,v in out.items() if v}

def main():
    checks=[]
    for A in (F(3,2),F(5,3),F(7,4),F(11,5)):
        for m,n in ((0,0),(1,0),(0,1),(1,1),(2,0),(0,2),(2,2)):
            d=(2*m+1)*A-2*m
            if d.denominator==1: continue
            a0=(A-1)*((2*m+1)*A+2*n+3)
            s=d+2*m+2*n+1
            eta=iterate(iterate({(0,0,s/2):F(1)},0,2*m),1,2*n+1)
            chi=scale(iterate(iterate({(0,0,(s+2)/2):F(1)},0,2*m+1),1,2*n+1),-1/(s+2)**2)
            pois=canonical(add(scale(lap(chi),-1),scale(deriv(eta,0),-1)))
            trans=canonical(add(scale(mulcoord(deriv(eta,0),0),A),mulcoord(deriv(eta,1),1),scale(eta,-1),scale(deriv(chi,0),a0)))
            assert canonical(eta) and not pois and not trans,(A,m,n,pois,trans)
            # Perturbing a0 by 1 must fail, so a zero evaluator cannot pass.
            negative=canonical(add(scale(mulcoord(deriv(eta,0),0),A),mulcoord(deriv(eta,1),1),scale(eta,-1),scale(deriv(chi,0),a0+1)))
            assert negative
            checks.append(dict(A=str(A),m=m,n=n,d=str(d),a0=str(a0),poisson_zero=True,transport_zero=True,negative_control_nonzero=True,eta_terms=len(canonical(eta))))
    dest=Path('research/indicial_fourier/verification/exact_examples.json')
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(dict(utc=datetime.now(timezone.utc).isoformat(),method='exact Fraction monomial differentiation, common radial power and binomial expansion',checks=checks),indent=2)+'\n')
    print(f'{len(checks)} exact examples and negative controls passed; {dest}')
if __name__=='__main__':main()
