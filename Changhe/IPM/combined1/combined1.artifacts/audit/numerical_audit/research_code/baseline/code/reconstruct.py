"""Independent rational recovery via polynomial Legendre recurrence."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
from datetime import datetime, timezone
import hashlib, json
ROOT=Path(__file__).resolve().parents[3]
DATA=ROOT/'research/baseline/data'

def encode(v): return f'{v.numerator}/{v.denominator}'
def hexq(s): return Q(float.fromhex(s))
def poly_add(a,b,scale=1):
    out=a.copy()+[Q(0)]*max(0,len(b)-len(a))
    for k,x in enumerate(b): out[k]+=scale*x
    return out

def legendre_shifted(nmax):
    ps=[[Q(1)],[Q(-1),Q(2)]]
    for n in range(1,nmax):
        p=poly_add([-v for v in ps[n]],[Q(0)]+[2*v for v in ps[n]])
        p=[(2*n+1)*v for v in p]
        p=poly_add(p,ps[n-1],-n)
        ps.append([v/(n+1) for v in p])
    return ps[:nmax+1]

def reconstruct(path):
    d=json.loads(path.read_text()); c=hexq(d['P_hex'][0]); g=1/c
    ps=[(3+g-j*(1-g))/2 for j in range(4)]
    low_order=[(j,m,k) for j in range(4) for m in range(5) for k in range(m,5)]
    order=[(j,m,k) for j in range(4) for m in range(10) for k in range(m,26)]
    a={key:Q(0) for key in order}
    for key,value in zip(low_order[1:],d['P_hex'][1:]): a[key]=hexq(value)
    def strain(j,m,k):
        p=ps[j]
        return {(0,0):4*p*(p-1),(0,1):8*(p-1),(0,2):Q(8),(2,2):Q(-24)}.get((m,k),Q(0))
    a[0,0,0]=(1-c-sum(a[key]*strain(*key) for key in low_order[1:]))/strain(0,0,0)
    leg=legendre_shifted(25); high=iter(d['high_hex']); norms=list(map(hexq,d['frozen_Nn_hex']))
    for j in range(4):
        for m in range(10):
            v=max(5,m)
            for n in range(26-v):
                h=hexq(next(high))*norms[n]
                for k,p in enumerate(leg[n]): a[j,m,v+k]+=h*p
    try: next(high); raise AssertionError('high count mismatch')
    except StopIteration: pass
    def choose(x,n):
        val=Q(1)
        for k in range(n): val*= (x-k)/(k+1)
        return val
    center_strain=sum(a[key]*strain(*key) for key in order)
    C=sum(a[j,m,k]*(-1)**m*choose(ps[j]-k,2-k) for j,m,k in order if k<=2)
    a0=-center_strain-24*C
    serial=(f'cl {encode(c)}\n'+'\n'.join(encode(a[key]) for key in order)).encode()
    sha=hashlib.sha256(serial).hexdigest()
    assert sha==d['input_exact_for_checkpoint']['canonical_serialization_sha256']
    assert a[0,0,0]==Q(d['input_exact_for_checkpoint']['a000_exact'])
    assert center_strain==1-c
    return d,c,order,a,a0,sha

if __name__=='__main__':
    results=[]
    for number in (88,131):
        path=DATA/f'checkpoint{number:03d}.json'
        d,c,order,a,a0,sha=reconstruct(path)
        out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'state':number,
             'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
             'canonical_serialization_sha256':sha,'cl':encode(c),'a0':encode(a0),'strain':encode(1-c),
             'order':order,'coefficients':[encode(a[key]) for key in order]}
        (DATA/f'state{number:03d}_independent.json').write_text(json.dumps(out,indent=2)+'\n')
        if number==131:
            prior=json.loads((DATA/'prior_state131_exact.json').read_text())
            assert [Q(v) for v in prior['canonical_coefficients']]==[a[key] for key in order]
            assert a0==Q(prior['exact_parameters']['a0'])
        result={'state':number,'canonical_sha':sha,'cl':float(c),'a0':float(a0),'strain':float(1-c),'exact_center_check':True,'num_coefficients':len(order)}
        results.append(result);print(result,flush=True)
    import numpy as np
    z=np.load(DATA/'checkpoint131.npz',allow_pickle=False)
    d=json.loads((DATA/'checkpoint131.json').read_text())
    assert all(Q(float(v))==hexq(s) for v,s in zip(z['P'],d['P_hex']))
    assert all(Q(float(v))==hexq(s) for v,s in zip(z['high'],d['high_hex']))
    assert hashlib.sha256((DATA/'checkpoint131.npz').read_bytes()).hexdigest()==d['snapshot_arrays_sha256']
    result={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'states':results,'npz_inputs_match_hex':True,
            'stored_mesh_squared_norm':float(z['residual']@z['residual']),'scope':'Exact reconstruction and saved array check; not fresh objective evaluation.'}
    (ROOT/'research/baseline/verification/reconstruction.json').write_text(json.dumps(result,indent=2)+'\n')
