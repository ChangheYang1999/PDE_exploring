"""Direct raw-generator homogeneous expansion, independent of Cartesian jets."""
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict, Counter
from math import comb
from functools import lru_cache
import hashlib
import json
import sys
import time
from flint import fmpq as Q, arb, ctx

sys.set_int_max_str_digits(0)
ctx.prec = 768
B = Path(__file__).resolve().parents[1]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
ar = lambda q: arb(q.numerator)/q.denominator
enc = lambda d: {str(n):str(v) for n,v in sorted(d.items()) if v}

@lru_cache(None)
def binomial(a, k):
    out = Q(1)
    for i in range(k):
        out *= (a-i)/(i+1)
    return out

def put(d,n,v):
    if n < 0:
        n,v = -n,-v
    if n and v:
        d[n] = d.get(n,Q(0))+v
        if not d[n]:
            del d[n]

def main():
    start = time.monotonic()
    rawpath = B/'data/candidate018.json'
    raw = json.loads(rawpath.read_text())
    peerpath = B/'source/N4_direct.json'
    peer = json.loads(peerpath.read_text())
    tabpath = B/'source/N1_sector_table.json'
    table = json.loads(tabpath.read_text())
    basepath = B.parent/'weighted_tail_candidate_audit/data/007_sectors.json'
    base = json.loads(basepath.read_text())
    assert sha(rawpath) == peer['generator_sha256'] == '1c99bf4d77865f7c576a9ba6c08bc08cf008416a737d4a8626b5799ceb4a85e2'
    c = Q(raw['cl_exact']); gamma = 1/c; delta = 1-gamma
    assert c == Q(4076476460239181,2251799813685248)
    amps = defaultdict(lambda:Q(0)); kindcount = Counter(); scaled = []
    for g in raw['generators']:
        assert 'p' not in g
        j,m = int(g['j']),int(g['m'])
        spec=g['spec']; kind=spec[0]; w=int(spec[1])
        n=0 if kind=='mono' else int(spec[2])
        q=int(spec[3]) if kind in ['legq','legqs'] else 0
        R=Q(spec[4]) if kind=='legqs' else Q(1)
        assert kind in ['mono','leg','legqs']
        coef=Q(g['coef']); p=(3+gamma-j*delta)/2
        kindcount[kind]+=1
        if kind=='legqs':
            assert q==4 and R==25
            scaled.append((j,m,n,w,q,str(R)))
        for L in range(q,3):
            term=Q(0)
            for k in range(n+1):
                bk=Q((-1)**(n+k)*comb(n,k)*comb(n+k,k))
                term += bk*sum((binomial(p-m,a)*binomial(Q(-w-q-k),L-q-a)*R**(2*(L-a)) for a in range(L-q+1)),Q(0))
            amps[j,2*m,L]+=coef*term
    assert kindcount=={'mono':262,'leg':1660,'legqs':252}
    Th,Ps = {},{}
    for (j,n,L),A in amps.items():
        e=1-(j+1)*delta-2*L; d=e+3; key=(j+1,L)
        rr=Th.setdefault(key,{});ss=Ps.setdefault(key,{})
        put(rr,n+1,-A*(d*d-n*n)*(d-2-n)/2)
        put(rr,n-1,A*(d*d-n*n)*(d-2+n)/2)
        put(ss,n+2,A*(d-n)*(d-n-2)/4)
        put(ss,n-2,-A*(d+n)*(d+n-2)/4)
    expo=lambda key:1-key[0]*delta-2*key[1]
    keys=[(K,L) for K in range(1,17) for L in range(3) if expo((K,L))>=Q(-7,2)]
    keys.sort(key=expo,reverse=True)
    assert len(keys)==16 and len(set(map(expo,keys)))==16
    assert expo((17,0))<Q(-7,2) and expo((1,3))<Q(-7,2)
    peers={Q(r['exponent']):r for r in peer['sectors']}
    tabs={Q(r['exponent_exact']):r for r in table['rows']}
    assert set(tabs)==set(map(expo,keys))
    # N4 uses a rectangular K<=8,L<=1 list. Its thirteen common rows
    # are exact comparisons; N1 has the sixteen cutoff-selected rows.
    assert len(set(peers)&set(tabs))==13
    records=[]
    for key in keys:
        K,L=key;e=expo(key)
        rhs={}
        for n,A in Th.get(key,{}).items():
            put(rhs,n+1,(n-e)*A/2);put(rhs,n-1,-(n+e)*A/2)
        lhs={n:((e+1)**2-n*n)*A for n,A in Ps.get(key,{}).items() if ((e+1)**2-n*n)*A}
        assert lhs==rhs
        F={n:(c*e-1)*A for n,A in Th.get(key,{}).items() if (c*e-1)*A}
        for K1 in range(1,K):
            for L1 in range(L+1):
                k1=(K1,L1);k2=(K-K1,L-L1)
                ep,et=expo(k1),expo(k2)
                for m,A in Ps.get(k1,{}).items():
                    for n,V in Th.get(k2,{}).items():
                        put(F,n+m,A*V*(-et*m+(ep+1)*n)/2)
                        put(F,n-m,A*V*(-et*m-(ep+1)*n)/2)
        pr=peers.get(e);tr=tabs[e]
        if pr is not None:
            assert F=={int(n):Q(v) for n,v in pr['sine_coefficients'].items()}
            assert (not F)==pr['exact_zero']
        assert (not F)==(tr['status']=='EXACT-ZERO')
        norm=(arb.pi()*ar(sum((v*v for v in F.values()),Q(0)))).sqrt()
        if pr is not None:
            assert norm.overlaps(arb(pr['full_circle_norm']))
        assert (max(F) if F else 0)==tr['max_harmonic']
        if F:
            assert abs(float(norm)/tr['full_circle_L2']-1)<1e-12
        records.append({'K':K,'L':L,'exponent_exact':str(e),
                        'density':enc(Th.get(key,{})),'stream':enc(Ps.get(key,{})),
                        'residual':enc(F),'residual_zero':not F,
                        'angular_norm':norm.str(85),'poisson_exact':True,
                        'N4_exact_coefficients_equal':True if pr else None,
                        'N1_status_and_norm_agree':True})
    nonzero=[(r['K'],r['L']) for r in records if not r['residual_zero']]
    assert nonzero==[(4,1),(9,0),(5,1),(1,2),(10,0)]
    base_rows={(r['K'],r['L']):r for r in base['sectors']}
    leading=[]
    for K in range(1,5):
        br=base_rows[K,0]
        assert enc(Th[K,0])==br['density'] and enc(Ps[K,0])==br['stream']
        leading.append({'K':K,'density_equal007':True,'stream_equal007':True})
    exact=B/'data/exact_sectors.json'
    with exact.open('x') as f:
        json.dump({'candidate':peer['candidate'],'raw_sha256':sha(rawpath),'sectors':records},f,indent=2);f.write('\n')
    out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':peer['candidate'],
         'inputs':{str(p):sha(p) for p in [rawpath,peerpath,tabpath,basepath,B/'PROOF.md',Path(__file__)]},
         'generator_counts':dict(kindcount),'scaled_generators':len(scaled),
         'all_scaled_generators_have_Q4_R25':True,'complete_prefix_size':16,
         'zero_sectors':11,'nonzero_sectors':nonzero,'leading_four_profiles':leading,
         'all_13_common_exact_coefficient_maps_agree_N4':True,
         'all_13_common_norms_overlap_N4':True,
         'exact_sectors_sha256':sha(exact),'elapsed_seconds':time.monotonic()-start,
         'verdict':'CONFIRMED independent exact homogeneous expansion'}
    with (B/'verification/result.json').open('x') as f:
        json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
