"""Independent modular-minor rank proof and direct exact relation checks."""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
from hashlib import sha256
from math import isqrt
from datetime import datetime, timezone
import json,time,sys
sys.set_int_max_str_digits(0)
root=Path(__file__).resolve().parents[1]
start=time.monotonic()
manifest=json.loads((root/'source/MANIFEST.json').read_text())
for name,rec in manifest['files'].items():
    assert sha256((root/'source'/name).read_bytes()).hexdigest()==rec['sha256']
raw=json.loads((root/'source/candidate007.json').read_text())
peer=json.loads((root/'source/N4_result.json').read_text())
rels=json.loads((root/'source/N4_relations.json').read_text())['relations']
prime=2147483647
assert all(prime%d for d in range(2,isqrt(prime)+1))
cache={0:[Q(1)],1:[Q(-1),Q(2)]}
def leg(n):
    if n in cache: return cache[n]
    for k in range(1,n):
        if k+1 in cache: continue
        v=[Q(0)]*(k+2)
        for i,x in enumerate(cache[k]):
            v[i]-=(2*k+1)*x/(k+1)
            v[i+1]+=2*(2*k+1)*x/(k+1)
        for i,x in enumerate(cache[k-1]): v[i]-=k*x/(k+1)
        cache[k+1]=v
    return cache[n]
columns=[]; blocks=defaultdict(list)
for i,g in enumerate(raw['generators']):
    spec=g['spec']; base=[Q(1)] if spec[0]=='mono' else leg(int(spec[2]))
    assert spec[0] in ('mono','leg')
    poly={int(spec[1])+k:int(x) for k,x in enumerate(base) if x}
    assert all(x.denominator==1 for x in base)
    columns.append(poly);blocks[int(g['j']),int(g['m'])].append(i)
def modrank(rows):
    rows=[row[:] for row in rows]
    n=len(rows); width=len(rows[0]); rank=0
    for col in range(width):
        pivot=next((i for i in range(rank,n) if rows[i][col]%prime),None)
        if pivot is None: continue
        rows[rank],rows[pivot]=rows[pivot],rows[rank]
        inv=pow(rows[rank][col],prime-2,prime)
        rows[rank]=[x*inv%prime for x in rows[rank]]
        for i in range(rank+1,n):
            scale=rows[i][col]
            if scale: rows[i]=[(a-scale*b)%prime for a,b in zip(rows[i],rows[rank])]
        rank+=1
        if rank==n: break
    return rank
peerblocks={(b['j'],b['m']):b for b in peer['block_results']}
result=[];rank=0
for key,inds in sorted(blocks.items()):
    support=sorted(set().union(*(set(columns[i]) for i in inds)))
    mat=[[columns[i].get(k,0)%prime for i in inds] for k in support]
    lower=modrank(mat);upper=min(len(inds),len(support))
    assert lower==upper,(key,lower,upper)
    assert lower==peerblocks[key]['rank']
    rank+=lower;result.append(dict(j=key[0],m=key[1],columns=len(inds),rank=lower,upper_bound=upper))
nonpivots={r['unit_nonpivot_index'] for r in rels}
assert len(nonpivots)==len(rels)
for r in rels:
    combined=defaultdict(Q); coeffs={int(i):Q(v) for i,v in r['coefficients'].items()}
    assert coeffs[r['unit_nonpivot_index']]==1
    assert set(coeffs)&nonpivots=={r['unit_nonpivot_index']}
    for i,v in coeffs.items():
        g=raw['generators'][i]; assert (int(g['j']),int(g['m']))==(r['j'],r['m'])
        for k,x in columns[i].items(): combined[k]+=v*x
    assert not any(combined.values())
c=Q(raw.get('cl',raw.get('cl_exact')));delta=1-1/c
js=sorted({key[0] for key in blocks}); pairs=0
for i,j in enumerate(js):
    for k in js[i+1:]:
        assert ((k-j)*delta/2).denominator!=1;pairs+=1
canonical=defaultdict(Q)
for i,g in enumerate(raw['generators']):
    for k,x in columns[i].items(): canonical[int(g['j']),int(g['m']),int(g['m'])+k]+=Q(g['coef'])*x
canonical={k:v for k,v in canonical.items() if v}
expected=json.loads((root/'source/canonical007.json').read_text())
expected={tuple(map(int,k)):Q(v) for k,v in zip(expected['order'],expected['coefficients'])}
assert canonical==expected
assert rank==1922 and len(columns)-rank==1060==len(rels)
res=dict(utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,status='CONFIRMED by modular minor lower bounds and support upper bounds',prime=prime,primality='exact trial division',generators=len(columns),rank=rank,kernel_dimension=len(rels),nonresonance_pairs=pairs,canonical_entries=len(canonical),blocks=result,source_manifest_sha256=sha256((root/'source/MANIFEST.json').read_bytes()).hexdigest(),proof_sha256=sha256((root/'PROOF.md').read_bytes()).hexdigest(),code_sha256=sha256(Path(__file__).read_bytes()).hexdigest())
with (root/'verification/result.json').open('x') as f:json.dump(res,f,indent=2)
print(json.dumps({k:v for k,v in res.items() if k!='blocks'},indent=2))
