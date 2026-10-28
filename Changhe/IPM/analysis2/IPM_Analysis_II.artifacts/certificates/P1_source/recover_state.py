"""Independent exact reconstruction; never imports the archived numerical code."""
from __future__ import annotations
from pathlib import Path
from fractions import Fraction as Q
from math import comb, factorial
from datetime import datetime, timezone
import hashlib, json, sys

HERE = Path(__file__).resolve().parent
COPY = HERE.parent/'case4'/'IPM_case4.artifacts'
CANON = [(j,m,k) for j in range(4) for m in range(10) for k in range(m,26)]
LOW = [(j,m,k) for j in range(4) for m in range(5) for k in range(m,5)]
HIGH = [(j,m,n) for j in range(4) for m in range(10) for n in range(26-max(5,m))]
INDEX = {v:i for i,v in enumerate(CANON)}

def qhex(s): return Q.from_float(float.fromhex(s))
def choose(x,n):
    r=Q(1)
    for k in range(n): r *= (x-k)/Q(k+1)
    return r

def polyadd(a,b,scale=1):
    r=a.copy()
    for k,v in b.items(): r[k]=r.get(k,Q(0))+scale*v
    return {k:v for k,v in r.items() if v}

# Differentiate using exact integer falling factorials.
def derivative(a,x=0,y=0):
    return {(i-x,j-y): v*(factorial(i)//factorial(i-x))*(factorial(j)//factorial(j-y))
            for (i,j),v in a.items() if i>=x and j>=y}

def polymul(a,b,maxdegree=5):
    r={}
    for (i,j),v in a.items():
        for (k,l),w in b.items():
            if i+j+k+l<=maxdegree: r[(i+k,j+l)]=r.get((i+k,j+l),Q(0))+v*w
    return {k:v for k,v in r.items() if v}

def taylor_generator(j,m,k,c,degree=8):
    p=(3+1/c-j*(1-1/c))/2
    out={}
    for ell in range((degree-2*k)//2+1):
        radial=choose(p-k,ell)
        n=k-m+ell
        for b in range(m+1):
            angular=(-1)**b*comb(2*m,2*b)
            for d in range(n+1):
                ij=(2*m-2*b+2*d,2*b+2*(n-d))
                out[ij]=out.get(ij,Q(0))+radial*angular*comb(n,d)
    return out

def enc(x): return f'{x.numerator}/{x.denominator}'
def interval(x,digits=22):
    n=x.numerator*10**digits//x.denominator
    return [enc(Q(n,10**digits)),enc(Q(n+1,10**digits))]
def read_state(state):
    folder='state088_handoff' if state==88 else 'state131_last_unverified'
    path=COPY/'checkpoints'/folder/f'accepted_{state:08d}.json'
    d=json.loads(path.read_text())
    low=list(map(qhex,d['P_hex'])); c=low[0]
    assert len(low)==60 and len(d['high_hex'])==800
    high=list(map(qhex,d['high_hex'])); norms=list(map(qhex,d['frozen_Nn_hex']))
    # Obtain all center strains by independent Cartesian Taylor expansion.
    columns=[taylor_generator(*ijk,c) for ijk in LOW]
    strain=[4*col.get((2,2),Q(0)) for col in columns]
    low[0]=(1-c-sum((u*v for u,v in zip(strain[1:],low[1:])),Q(0)))/strain[0]
    a=[Q(0)]*860
    for v,ijk in zip(low,LOW): a[INDEX[ijk]]+=v
    for v,(j,m,n) in zip(high,HIGH):
        for k in range(n+1):
            a[INDEX[j,m,max(5,m)+k]] += v*norms[n]*(-1)**(n-k)*comb(n,k)*comb(n+k,k)
    serial=(f'cl {enc(c)}\n'+'\n'.join(map(enc,a))).encode()
    digest=hashlib.sha256(serial).hexdigest()
    assert digest==d['input_exact_for_checkpoint']['canonical_serialization_sha256']
    # Cross-check each hex string with the JSON display and NPZ binary inputs.
    import numpy as np
    z=np.load(path.with_suffix('.npz'),allow_pickle=False)
    assert all(Q.from_float(float(v))==qhex(h) for v,h in zip(z['P'],d['P_hex']))
    assert all(Q.from_float(float(v))==qhex(h) for v,h in zip(z['high'],d['high_hex']))
    assert hashlib.sha256(path.with_suffix('.npz').read_bytes()).hexdigest()==d['snapshot_arrays_sha256']
    chi={}
    for v,col in zip(low,columns): chi=polyadd(chi,col,v)
    lap=polyadd(derivative(chi,x=2),derivative(chi,y=2))
    rho={k:-v for k,v in derivative(lap,y=1).items()}
    psi=derivative(chi,x=1,y=1)
    ux={k:-v for k,v in derivative(psi,y=1).items()}; uy=derivative(psi,x=1)
    assert psi.get((1,1),Q(0))==1-c
    a0=rho[(0,1)]
    residual={ij:(c*sum(ij)-1)*v for ij,v in rho.items()}
    residual=polyadd(residual,polymul(ux,derivative(rho,x=1)))
    residual=polyadd(residual,polymul(uy,derivative(rho,y=1)))
    residual={k:v for k,v in residual.items() if sum(k)<=5}
    assert residual.get((0,1),Q(0))==0
    gamma=1/c; lam=2*c-1; sigma=a0/(lam-1)
    params={'cl':c,'a0':a0,'strain':1-c,'lambda_origin':lam,'sigma':sigma,'gamma':gamma,
            'residual_leading_power':2*gamma-1,'energy_origin_x':3*c+a0,'energy_origin_y':c+2}
    record={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'), 'state':state,
        'source_json_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'canonical_serialization_sha256':digest,
        'exact_parameters':{k:enc(v) for k,v in params.items()},
        'decimal_display':{k:float(v) for k,v in params.items()},
        'rational_enclosures':{k:interval(v) for k,v in params.items()},
        'canonical_order':CANON,'canonical_coefficients':list(map(enc,a)),
        'origin_rho_coefficients':{str(k):enc(v) for k,v in sorted(rho.items())},
        'origin_residual_coefficients_through_degree5':{str(k):enc(v) for k,v in sorted(residual.items())},
        'origin_residual_decimal_display':{str(k):float(v) for k,v in sorted(residual.items())},
        'stored_objectives_unverified':d['objectives'],
        'stored_mesh_residual_squared_norm_diagnostic':float(z['residual']@z['residual']),
        'uncertainty_scope':'Exact rational checkpoint, not an uncertainty enclosure for any true PDE profile.'}
    dest=HERE/f'state{state:03d}_exact.json'; dest.write_text(json.dumps(record,indent=2)+'\n')
    print(state,params.keys())
    print(json.dumps(record['decimal_display'],indent=2))
    print('Taylor residual',record['origin_residual_decimal_display'])
    print('SHA match',digest)
    return c,a,record

if __name__=='__main__':
    for state in (88,131): read_state(state)
