"""Interval certification of the finite failure of a fixed two-plane model."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json,pickle
from flint import arb,fmpz,ctx
ctx.prec=2048


def unpack(t):
    m,e,r=t
    mid=arb(fmpz(m))*arb(2)**int(e)
    assert mid.is_exact()
    if r=='0':return mid
    if '*2^' in r:
        a,b=r.split('*2^'); rad=arb(fmpz(a))*arb(2)**int(b)
    else:rad=arb(r)*(1+arb('1e-9'))
    return arb(mid,rad)


def dot(u,v):return sum((a*b for a,b in zip(u,v)),arb(0))


def main():
    src=Path('../a4-num/ckpt/sqrt5_sin1_p1024.pkl');raw=src.read_bytes();data=pickle.loads(raw)
    ns=[572,573,574,636,700]; selected={n:data['f'][n] for n in ns}
    target=Path('research/23_correlation_audit')
    (target/'sources/interval_selected_coefficients.json').write_text(json.dumps(selected)+'\n')
    v={n:[unpack(t) for t in a] for n,a in selected.items()}
    norm={n:dot(a,a).sqrt() for n,a in v.items()}
    def corr(n,m):return dot(v[n],v[m])/(norm[n]*norm[m])
    a=corr(572,573);assert 1-a*a>0
    rows=[]
    for n in [574,636,700]:
        b=corr(572,n);d=corr(573,n)
        distance=(1-(b*b-2*a*b*d+d*d)/(1-a*a)).sqrt()
        lower={574:'0.0812',636:'0.9994',700:'0.99999999'}[n]
        assert distance>arb(lower)
        rows.append(dict(n=n,lag=n-572,correlation_with_572=str(b),distance_from_span_572_573=str(distance),strict_lower_bound=lower))
        print(n,'distance >',lower,'actual',distance.str(18),flush=True)
    out=dict(checked_at_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
             code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),source=str(src),source_sha256=sha256(raw).hexdigest(),
             arithmetic='Arb 2048-bit projection calculation from retained 1024-bit source coefficient balls',
             lag1_correlation=str(a),checks=rows,
             scope='Certified finite checkpoint statements conditional on source balls enclosing the recursion coefficients; no infinite asymptotic conclusion.')
    (target/'verification/interval_projection.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':main()
