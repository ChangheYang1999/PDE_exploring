"""Rigorous polynomial aggregation of every column-pair triangle bound."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from math import factorial
import gzip, json, pickle, random, sys, time
sys.dont_write_bytecode = True
from flint import arb, arb_poly, ctx
from stream_precision_audit import unpack

ROOT = Path('research/81_factorial_triangle_bounds')
INPUT = Path('research/78_factorial_product_losses/verification/input_checkpoint.pkl.gz')
ctx.prec = 640
started = time.monotonic()
text = lambda x: x.str(35, radius=True)
for name in ['sources', 'verification']:
    (ROOT/name).mkdir(parents=True, exist_ok=True)

facts = [arb(factorial(q)) for q in range(300)]
def weight(poly):
    return sum((facts[q]*v for q,v in enumerate(poly)),arb(0))
def bound(A, At, B, Bt, P, p):
    return weight(P*A*Bt+p*At*B+A.derivative()*Bt+At*B.derivative())

rng = random.Random(811031)
checks = 0
for trial in range(100):
    av = [rng.randrange(9) for _ in range(rng.randrange(1,8))]
    at = [rng.randrange(9) for _ in av]
    bv = [rng.randrange(9) for _ in range(rng.randrange(1,8))]
    bt = [rng.randrange(9) for _ in bv]
    P,p = rng.randrange(9),rng.randrange(9)
    exact = 0
    for u,a in enumerate(av):
        for v,b in enumerate(bv):
            exact += factorial(u+v)*(P*a*bt[v]+p*at[u]*b)
            if u+v:
                exact += factorial(u+v-1)*(u*a*bt[v]+v*at[u]*b)
    got = bound(*map(arb_poly,[av,at,bv,bt]),P,p)
    assert got.contains(exact)
    checks += 1
print(json.dumps(dict(synthetic_exact_aggregations=checks)),flush=True)
raw = gzip.decompress(INPUT.read_bytes())
digest = sha256(raw).hexdigest()
state = pickle.loads(raw)
del raw
assert state['ring']=='arb' and state['prec']==512 and (state['A'],state['B'])==('2','3')
N = max(state['f'])
polys, norms, pnorms = {}, {}, {}
for field in ['f','g']:
    polys[field],norms[field],pnorms[field] = {},{},{}
    for n,cols in sorted(state[field].items()):
        cn,dn = [],[]
        for col in cols:
            values = [abs(arb(*unpack(z))) for z in col]
            cn.append(sum(values,arb(0)))
            dn.append(sum(((2*j+(field=='f'))*z for j,z in enumerate(values)),arb(0)))
        A,At = arb_poly(cn),arb_poly(dn)
        norms[field][n] = weight(A)
        cn[0],dn[0] = arb(0),arb(0)
        Ap,Atp = arb_poly(cn),arb_poly(dn)
        pnorms[field][n] = weight(Ap)
        polys[field][n] = (A,At,Ap,Atp)
del state
reference = json.loads(Path('research/78_factorial_product_losses/verification/checks.json').read_text())
assert reference['checkpoint_sha256']==digest
full = {r['n']:arb(r['forcing_factorial_norm']) for r in reference['full_ratios']}
refs = {(r['n'],r['subset']):arb(r['sum_all_pair_upper_bounds']) for r in reference['ranked_pairs']}
result = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),
    checkpoint_path=str(INPUT),checkpoint_sha256=digest,maximum_order=N,precision_bits=640,
    synthetic_exact_aggregations=checks,source_sha256={},rows=[],rank_comparisons=[])
for name in ['factorial_triangle_audit.py','stream_precision_audit.py']:
    source=Path('code',name).read_bytes()
    (ROOT/'sources'/(name+'.txt')).write_bytes(source)
    result['source_sha256'][name]=sha256(source).hexdigest()

def save():
    result['actual_elapsed_s']=time.monotonic()-started
    (ROOT/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')

for n in range(2,N+1):
    agg,aggp = arb_poly([]),arb_poly([])
    den,pden = arb(0),arb(0)
    for i in range(1,n):
        j=n-i
        P,p=abs(arb(2)-arb(2*i)/3),abs(arb(1)-arb(2*j)/3)
        A,At,Ap,Atp=polys['g'][i]
        B,Bt,Bp,Btp=polys['f'][j]
        agg += P*A*Bt+p*At*B+A.derivative()*Bt+At*B.derivative()
        aggp += P*Ap*Btp+p*Atp*Bp+Ap.derivative()*Btp+Atp*Bp.derivative()
        w=2*j*(P+1)+2*i*(p+1)
        den += w*norms['g'][i]*norms['f'][j]
        pden += w*pnorms['g'][i]*pnorms['f'][j]
    total,pp = weight(agg),weight(aggp)
    assert total >= 0 and pp >= 0
    for subset,value in [('all',total),('positive',pp)]:
        if (n,subset) in refs:
            assert value.overlaps(refs[n,subset]),(n,subset,text(value),text(refs[n,subset]))
            result['rank_comparisons'].append(dict(n=n,subset=subset,overlaps=True))
    row=dict(n=n,triangle_bound=text(total),full_baseline=text(den),
        triangle_over_baseline=text(total/den),triangle_over_forcing=text(total/full[n]),
        positive_triangle_bound=text(pp),positive_baseline=text(pden),
        positive_triangle_over_baseline=text(pp/pden) if pden>0 else None,
        positive_triangle_over_full_triangle=text(pp/total))
    result['rows'].append(row)
    if n%10==0 or n==N:
        save()
        print(json.dumps(dict(n=n,triangle_over_baseline=row['triangle_over_baseline'],
             positive_triangle_over_baseline=row['positive_triangle_over_baseline'],elapsed_s=result['actual_elapsed_s'])),flush=True)
result['complete']=True
save()
print(json.dumps(dict(complete=True,elapsed_s=result['actual_elapsed_s'])),flush=True)
