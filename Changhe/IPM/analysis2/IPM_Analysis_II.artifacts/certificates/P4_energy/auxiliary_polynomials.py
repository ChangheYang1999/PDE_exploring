"""Even-order compactified derivative polynomials for stronger energy estimates."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
from datetime import datetime,timezone
from flint import ctx
import json,sys,time
from compact_matrix import derivative,add,chebyshev,encode,BASE
CHOICES={'chi13':'xyyy','chi24':'xxyyyy','chi06':'yyyyyy','chi33':'xxxyyy','chi15':'xyyyyy','chi42':'xxxxyy','chi51':'xxxxxy'}

def run(state):
    d=json.loads((BASE/'source_audit'/f'state{state:03d}_exact.json').read_text())
    old=json.loads(Path(__file__).with_name(f'state{state:03d}_compact_polynomials.json').read_text())
    gamma=1/Q(d['exact_parameters']['cl']);delta=1-gamma
    polys=dict(old['polynomials'])
    for label,axes in CHOICES.items():
        order=len(axes);half=order//2;extra=half-2
        for branch in range(4):
            trig={};p=(3+gamma-branch*delta)/2
            for (j,m,k),a in zip(d['canonical_order'],d['canonical_coefficients']):
                if j!=branch:continue
                T={('c',2*m,0):Q(a)}
                for di,axis in enumerate(axes):T=derivative(T,p,k,di,axis)
                for (kind,n,l),v in T.items():add(trig,kind,n,k-half+l,v)
            assert all(l>=0 for kind,n,l in trig)
            P={}
            for (kind,n,l),v in trig.items():
                assert n%2==0 and kind==('s' if axes.count('y')%2 else 'c')
                C=chebyshev(n//2-1,'U') if kind=='s' else chebyshev(n//2)
                for i in range(extra+1):
                    radial=Q((-1)**i*comb(extra,i))
                    for zdeg,c in enumerate(C):P[l+i,zdeg]=P.get((l+i,zdeg),Q(0))+v*radial*c
            polys[f'{label}_{branch}']=encode({key:v for key,v in P.items() if v})
    out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'state':state,'delta':str(delta),'input_sha256':d['canonical_serialization_sha256'],'polynomials':polys}
    Path(__file__).with_name(f'state{state:03d}_auxiliary_polynomials.json').write_text(json.dumps(out,indent=2)+'\n')
    print(state,'auxiliary polynomials saved',flush=True)

if __name__=='__main__':
    for state in (88,131):run(state)
