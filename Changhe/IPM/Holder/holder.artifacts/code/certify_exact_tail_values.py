"""Directed fixed-radius evaluations with the unrelaxed exterior denominators."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import argparse, hashlib, json
from flint import arb, ctx
from certify_sharp_deficiency import finite, uniform, moments, rational_catalan, qball
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'08_improved_upper_bounds/explicit_second_term/tail_series'
OUT=BASE/'numerical_values'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def ep(x, high=False): return Q(str((x.upper() if high else x.lower()).fmpq()))
def aq(x): return arb(str(x))
def ceil10(x):
    q=x*10**10; n=-((-q.numerator)//q.denominator)
    return f'{n//10**10}.{n%10**10:010d}'
def bounds(a,n):
    terms=[Q(k+1,4**k)/((2*k+1-a)*(2*k+1)) for k in range(n)]
    lower=sum(terms,Q(0)); assert lower==sum(reversed(terms),Q(0))
    rem=Q(4,3)*Q(n+1,4**n)/((2*n+1-a)*(2*n+1))
    for k in range(n,n+16):
        assert Q(k+1)/((2*k+1-a)*(2*k+1)) >= Q(k+2)/((2*k+3-a)*(2*k+3))
    return lower,lower+rem,rem

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--ledger',required=True);ap.add_argument('--analytic-ledger',required=True)
    args=ap.parse_args(); hashes={}
    def bind(p):
        p=p.resolve(); assert p.is_relative_to(ROOT); hashes[str(p.relative_to(ROOT))]=sha(p)
    def accept(path,v):
        d=json.loads(path.read_text());assert d['verdict']=='CONFIRMED' and d['ledger']==v;bind(path)
        for name,h in d['sha256'].items():assert sha(ROOT/name)==h,name;bind(ROOT/name)
        return d
    aa=accept(BASE/'verification/accepted.json',args.analytic_ledger)
    assert aa['sha256'][str((BASE/'PROOF.md').relative_to(ROOT))]==sha(BASE/'PROOF.md')
    previous=accept(ROOT/'08_improved_upper_bounds/explicit_second_term/sharp_deficiency/numerical_values/accepted.json','V209')
    lo,hi=rational_catalan(512)
    assert (lo,hi)==(Q(previous['catalan']['lower']),Q(previous['catalan']['upper']))
    ctx.prec=384;g1=qball(lo,hi)
    rows=[]
    for row in previous['rows']:
        a,r=Q(row['alpha_or_epsilon']),Q(row['rho']);kind=row['operator'];mode=row['mode'];ref=row['retained_reflection']
        sl,su,rem=bounds(a,64);sl2,su2,rem2=bounds(a,128)
        assert sl<sl2<su2<su and rem2<rem
        def calc(g,variant=False):
            value=uniform(r,kind,g,variant) if mode=='uniform' else finite(a,r,kind,g,variant)
            if ref:
                m2,m4=moments(r,variant);A=aq(a)
                gain=(1-A)*m2+(1-A)*(2-A)*(3-A)*m4
                value-=gain if mode=='uniform' else A*gain
            A=aq(a);power=(A*arb(2).log()).exp()
            old=1/(1-A)+arb(1)/2-(arb(3)/2).log()
            if variant:
                difference=2*power/arb.pi()*(old-aq(su))
            else:
                difference=2*power*(old-aq(su))/arb.pi()
            assert ep(difference)>0
            reduction=difference if mode=='uniform' else A*difference
            return value-reduction,reduction
        ctx.prec=384;value,reduction=calc(g1);vl,vh=ep(value),ep(value,True);text=value.str(48);rt=reduction.str(48)
        safe=ceil10(vh)
        ctx.prec=768;fresh,_=calc(arb.const_catalan(),True)
        assert vl<=ep(fresh)<=ep(fresh,True)<=vh
        assert vh<=Q(safe)<vh+Q(1,10**10)
        assert Q(safe)<Q(row['safe_upper'])
        result=dict(row);result.update(previous_upper=row['safe_upper'],safe_upper=safe,ball=text,lower=str(vl),upper=str(vh),tail_lower=str(sl),tail_upper=str(su),tail_remainder=str(rem),tail_reduction_ball=rt)
        rows.append(result)
    for p in [BASE/'PROOF.md',OUT/'PROOF.md',ROOT/'code/certify_sharp_deficiency.py',Path(__file__)]:bind(p)
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),ledger=args.ledger,verdict='CONFIRMED',analytic_ledger=args.analytic_ledger,precision_bits=[384,768],tail_terms=64,rows=rows,sha256=hashes,scope='Fixed-radius finite bounds and specified whole-interval linear envelopes; no optimization claim')
    (OUT/'accepted.json').write_text(json.dumps(out,indent=2)+'\n')
    print(out['time_utc'],args.ledger)
    for r in rows:print(r['mode'],r['operator'],r['alpha_or_epsilon'],r['retained_reflection'],r['safe_upper'])
if __name__=='__main__':main()
