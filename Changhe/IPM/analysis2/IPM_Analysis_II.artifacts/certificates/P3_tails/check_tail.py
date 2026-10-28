"""Exact angular tail reconstruction, independent of archived farfield860.py."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
from datetime import datetime,timezone
import json,sys

BASE=Path(__file__).resolve().parents[2]

def add_sine(out,n,v):
    if n<0: n,v=-n,-v
    if n and v: out[n]=out.get(n,Q(0))+v

def density_stream(C,s):
    # Directly differentiate r^s cos(n theta) in polar coordinates.
    F={}; P={}
    for n,v in C.items():
        add_sine(F,n+1,-v*(s*s-n*n)*(s-2-n)/2)
        add_sine(F,n-1,+v*(s*s-n*n)*(s-2+n)/2)
        add_sine(P,n+2,+v*(s-n)*(s-n-2)/4)
        add_sine(P,n-2,-v*(s+n)*(s+n-2)/4)
    return F,P

def advection(P,F,stream_exponent,density_exponent):
    # -psi_theta * rho_r/r + psi_r * rho_theta/r.
    out={}
    for m,b in P.items():
        for n,a in F.items():
            v=-m*b*density_exponent*a/2
            add_sine(out,n+m,v);add_sine(out,n-m,v)
            v=stream_exponent*b*n*a/2
            add_sine(out,m+n,v);add_sine(out,m-n,v)
    return {n:v for n,v in out.items() if v}

def enc(x):return f'{x.numerator}/{x.denominator}'
def rational_enclosure(x,digits=24):
    den=10**digits;lo=x.numerator*den//x.denominator
    return [enc(Q(lo,den)),enc(Q(lo+1,den))]

def arb_interval(x):
    # Store Arb's ball string at high precision. No rounding of that string is used in proofs.
    return x.str(50)

def run(state):
    d=json.loads((BASE/'source_audit'/f'state{state:03d}_exact.json').read_text())
    c=Q(d['exact_parameters']['cl']);gamma=1/c
    a=list(map(Q,d['canonical_coefficients']))
    C=[{} for _ in range(4)]
    for v,(j,m,k) in zip(a,d['canonical_order']): C[j][2*m]=C[j].get(2*m,Q(0))+v
    F=[];P=[];powers=[]
    for j in range(4):
        alpha=gamma-j*(1-gamma);powers.append(alpha)
        f,p=density_stream(C[j],alpha+3);F.append(f);P.append(p)
    E={}
    for h in range(1,8):
        out={n:(c*powers[h]-1)*v for n,v in F[h].items()} if h<4 else {}
        for i in range(4):
            j=h-1-i
            if 0<=j<4:
                for n,v in advection(P[i],F[j],powers[i]+1,powers[j]).items():add_sine(out,n,v)
        E[h]={n:v for n,v in out.items() if v}
    n=18;s=3+gamma
    aa=-C[0][18]*(s*s-n*n)*(s-2-n)/2
    bb=C[0][18]*(s-n)*(s-n-2)/4
    expected=(19-gamma)*aa*bb/2
    assert E[1][39]==expected and expected<0 and 2*gamma-1>0
    # Interval values have exact rational coefficients and Arb enclosure of pi/square root.
    from flint import arb,ctx
    ctx.prec=256
    def toarb(q):return arb(q.numerator)/arb(q.denominator)
    norms={};norm_displays={};squares={}
    for h in range(1,4):
        normsq=sum((v*v for v in E[h].values()),Q(0))/4
        norm=(arb.pi()*toarb(normsq)).sqrt()
        norms[h]=arb_interval(norm);norm_displays[h]=float(norm.mid());squares[h]=enc(normsq)
    f0sq=sum((v*v for v in F[0].values()),Q(0))/4
    tailfrac=(toarb(sum((v*v for n,v in E[1].items() if n>19),Q(0)))/toarb(sum((v*v for v in E[1].values()),Q(0)))).sqrt()
    output={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'), 'state':state,
        'canonical_serialization_sha256':d['canonical_serialization_sha256'],
        'gamma_exact':enc(gamma),'leading_residual_power_exact':enc(2*gamma-1),
        'E1_sin39_exact':enc(expected),'E1_sin39_enclosure':rational_enclosure(expected),
        'E1_sin39_display':float(expected),
        'leading_density_angular_coefficients':{n:enc(v) for n,v in F[0].items()},
        'E_coefficients':{h:{n:enc(v) for n,v in es.items()} for h,es in E.items()},
        'E_norm_squared_divided_by_pi':squares,'E_norm_arb':norms,
        'leading_density_norm_squared_divided_by_pi':enc(f0sq),
        'leading_density_norm_arb':arb_interval((arb.pi()*toarb(f0sq)).sqrt()),
        'E1_fraction_above_harmonic19_arb':arb_interval(tailfrac),
        'conclusion':'E1 has a nonzero sin39 coefficient and leading exponent 2/c-1>0. The unnormalized density residual grows in angular L2; normalized objective does not bound it in an unweighted decay space.',
        'scope':'Exact coefficients for the supplied rational checkpoint. Binomial expansion proof supplies uniform angular asymptotics; Arb norms rely on python-flint/Arb correctness.'}
    dest=Path(__file__).parent/f'state{state:03d}_tail.json';dest.write_text(json.dumps(output,indent=2)+'\n')
    print(state, 'power=',float(2*gamma-1),'sin39=',float(expected),'norms=',norm_displays,'high fraction=',tailfrac.str(20))

if __name__=='__main__':
    for state in (88,131):run(state)
