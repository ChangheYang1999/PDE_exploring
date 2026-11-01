"""Exact sine-product check independent of the Cartesian edge generator."""
from collections import defaultdict
from datetime import datetime,timezone
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json,time

def parse(x):
    return {(int(q),int(m)):Q(v) for q,row in x.items() for m,v in row.items() if Q(v)}

def add(out,q,m,v):
    if m<0:m=-m;v=-v
    if m and v:out[q,m]+=v

def clean(x):return {k:v for k,v in x.items() if v}

def radial(x,p):
    out=defaultdict(Q)
    for (q,m),v in x.items():
        out[q,m]+=p*v
        if q:out[q-1,m]+=q*v
    return clean(out)

def source(g,f,P,p):
    out=defaultdict(Q)
    for (q,k),v in radial(g,P).items():
        for (s,m),w in f.items():
            add(out,q+s,k+m,v*m*w/2);add(out,q+s,k-m,v*m*w/2)
    for (q,k),v in g.items():
        for (s,m),w in radial(f,p).items():
            add(out,q+s,k+m,-k*v*w/2);add(out,q+s,k-m,k*v*w/2)
    return clean(out)

def main():
    start=time.monotonic();root=Path('research/102_edge_recurrence_reference');raw=(root/'verification/exact_reference.json').read_bytes();data=json.loads(raw)
    assert data['complete'];count=0;paircount=0;canonical=0
    for tag,rows in [('full',data['full_prefix'])]+[(k,v['rows']) for k,v in data['variants'].items()]:
        F={};G={}
        for row in rows:
            n=row['n'];p=1-Q(2*n,3);P=p+1;f=parse(row['density']);g=parse(row['stream']);F[n]=f;G[n]=g
            assert all(m%2 for q,m in f) and all(m%2==0 for q,m in g)
            rho_x=defaultdict(Q)
            for (q,m),v in f.items():
                add(rho_x,q,m+1,(p-m)*v/2);add(rho_x,q,m-1,(p+m)*v/2)
                if q:add(rho_x,q-1,m+1,q*v/2);add(rho_x,q-1,m-1,q*v/2)
            neg_lap=defaultdict(Q)
            for (q,m),v in g.items():
                neg_lap[q,m]+=(m*m-P*P)*v
                if q:neg_lap[q-1,m]-=2*P*q*v
                if q>=2:neg_lap[q-2,m]-=q*(q-1)*v
            assert clean(neg_lap)==clean(rho_x),(tag,n,'poisson')
            count+=len(set(neg_lap)|set(rho_x))
            if P.denominator==1 and P<0 and int(P)%2==0:
                assert g.get((0,-int(P)),0)==0,(tag,n,'canonical');canonical+=1
            nonlinear=defaultdict(Q)
            pairs=row['pairs'];assert len(pairs)==len(set(map(tuple,pairs)))
            for i,j in pairs:
                assert i+j==n
                if tag!='full':assert min(i,j)<=int(tag)
                for key,value in source(G[i],F[j],2-Q(2*i,3),1-Q(2*j,3)).items():nonlinear[key]+=value
                paircount+=1
            density=defaultdict(Q)
            if n>=2:
                for (q,m),v in f.items():
                    density[q,m]+=2*(n-1)*v
                    if q:density[q-1,m]-=3*q*v
            assert clean(density)==clean(nonlinear),(tag,n,'stationary')
            count+=len(set(density)|set(nonlinear))
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),actual_elapsed_s=time.monotonic()-start,
                input_sha256=sha256(raw).hexdigest(),coefficient_identity_checks=count,ordered_pair_products=paircount,
                zero_resonant_constant_checks=canonical,verified_orders=sum(len(v['rows']) for v in data['variants'].values())+len(data['full_prefix']),
                scope='Finite exact Poisson and modified stationary identities by sine product-to-sum formulas.')
    source_raw=Path('code/edge_sine_audit.py').read_bytes();result['code_sha256']=sha256(source_raw).hexdigest();(root/'sources/edge_sine_audit.py.txt').write_bytes(source_raw)
    (root/'verification/sine_audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
if __name__=='__main__':main()
