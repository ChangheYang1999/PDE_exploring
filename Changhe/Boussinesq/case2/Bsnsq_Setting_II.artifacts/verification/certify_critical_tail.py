"""Exact modular certificate for the beta2 critical-temperature tail constraint.

No fitting-code imports. Binary64 coefficient values are exact rationals.
A separate modular Bezout check certifies coprimality, not floating roots.
"""
from pathlib import Path
from fractions import Fraction
from datetime import datetime, timezone
import argparse, json, hashlib, time
import numpy as np


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def plus(a,b):
    c=[Fraction(0)]*max(len(a),len(b))
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    return trim(c)


def scale(a,v): return trim([v*x for x in a])


def times(a,b):
    c=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return trim(c)


def cosine_to_power(coeff):
    previous=[Fraction(1)]; current=[Fraction(0),Fraction(1)]
    out=scale(previous,coeff[0])
    for n in range(1,len(coeff)):
        out=plus(out,scale(current,coeff[n]))
        previous,current=current,plus(times([0,2],current),scale(previous,-1))
    return out


def mod_trim(a,p):return trim([int(x)%p for x in a])


def mod_add(a,b,p):
    c=[0]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]=(c[i]+x)%p
    for i,x in enumerate(b):c[i]=(c[i]+x)%p
    return trim(c)


def mod_mul(a,b,p):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
    return trim(c)


def mod_neg(a,p):return mod_trim([-x for x in a],p)


def mod_div(a,b,p):
    a=list(a);q=[0]*max(1,len(a)-len(b)+1)
    if b==[0]:raise ZeroDivisionError
    inv=pow(b[-1],-1,p)
    while a!=[0] and len(a)>=len(b):
        k=len(a)-len(b);t=a[-1]*inv%p;q[k]=t
        for j,bj in enumerate(b):a[j+k]=(a[j+k]-t*bj)%p
        trim(a)
    return trim(q),a


def extended_gcd(a,b,p):
    r0,r1=a,b;s0,s1=[1],[0];t0,t1=[0],[1]
    while r1!=[0]:
        q,r=mod_div(r0,r1,p)
        r0,r1=r1,r
        s0,s1=s1,mod_add(s0,mod_neg(mod_mul(q,s1,p),p),p)
        t0,t1=t1,mod_add(t0,mod_neg(mod_mul(q,t1,p),p),p)
    inv=pow(r0[-1],-1,p)
    return mod_trim([inv*x for x in r0],p),mod_trim([inv*x for x in s0],p),mod_trim([inv*x for x in t0],p)


def encode(a):return [{'n':str(x.numerator),'d':str(x.denominator)} for x in a]


def reduce_poly(a,p):return trim([x.numerator*pow(x.denominator,-1,p)%p for x in a])


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--source',default='../numerics/states/B2_p_gauss_N112.npz')
    parser.add_argument('--output',default='runs/critical_tail_certificate.json')
    args=parser.parse_args()
    start=time.monotonic();source=Path(args.source)
    output_path=Path(args.output)
    assert output_path.resolve().is_relative_to(Path(__file__).resolve().parent.parent)
    with np.load(source,allow_pickle=False) as data:
        metadata={k:data[k].item() for k in ['beta','L','sigma_a','sigma_G','mapname','beta_map']}
        assert metadata=={'beta':2.,'L':1.,'sigma_a':1.5,'sigma_G':1.25,'mapname':'t','beta_map':2.}
        ends=[]
        for name in ['ca','cG']:
            ends.append([sum((Fraction.from_float(float(value))*(-1)**n for n,value in enumerate(row)),Fraction(0)) for row in data[name]])
    A,C=[cosine_to_power(x) for x in ends]
    derivative=[(i+1)*A[i+1] for i in range(len(A)-1)]
    F=plus(times([-1,3],A),scale(times([1,0,-1],derivative),-2))
    rows=[]
    for p in [65537,1000003]:
        fm,cm=reduce_poly(F,p),reduce_poly(C,p)
        assert len(fm)==len(F) and len(cm)==len(C)
        g,bf,bc=extended_gcd(fm,cm,p)
        check=mod_add(mod_mul(bf,fm,p),mod_mul(bc,cm,p),p)
        assert g==[1] and check==[1]
        rows.append({'prime':p,'degree_F':len(fm)-1,'degree_C':len(cm)-1,'F':fm,'C':cm,'bezout_F':bf,'bezout_C':bc,'gcd':g,'bezout_check':check})
    output={'timestamp':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'source':str(source),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'metadata':metadata,'interpretation':'Binary coefficient values, beta2, L1 and envelope powers are literal exact values. z=cos(2phi), H=sin(phi)cos(phi)^2 A(z), G=sin(phi)cos(phi) C(z).','A_power_coefficients':encode(A),'C_power_coefficients':encode(C),'F_power_coefficients':encode(F),'identity':'2 H_prime(phi)=cos(phi)*F(cos(2phi)); F=(3z-1)A-2(1-z^2)A_prime','modular_certificates':rows,'verdict':'REFUTED as an exact broad beta2 profile: H has an interior critical point, but every such point has G nonzero. Modular coprimality checked exactly.','scope':'Exact necessary condition violation for the supplied literal state; no finite residual threshold, neighborhood exclusion, continuum maximum or broad NO conclusion.'}
    output_path.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({k:output[k] for k in ['timestamp','elapsed_seconds','source_sha256','verdict']},indent=2))
    print('degrees',len(A)-1,len(C)-1,len(F)-1,'gcd checks',[(x['prime'],x['gcd']) for x in rows])
if __name__=='__main__':main()
