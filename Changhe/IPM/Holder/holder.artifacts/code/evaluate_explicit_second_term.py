"""Outward evaluation of the two analytic cutoff bounds.

The floating search chooses a rational cutoff only. It proves no optimality.
Every reported bound is evaluated with Arb after the choice is fixed.
"""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
import hashlib, json, math
from flint import arb, ctx
ROOT=Path(__file__).resolve().parents[1]

def values(a,r,linear):
    pi=arb.pi(); two=arb(2); one=arb(1)
    a2=two**(1+a/2)/(pi*(a+2))
    A=((a+2)/2).gamma()/(2*pi.sqrt()*((a+3)/2).gamma())
    E=-(1-r*r).log()/2; N=one/2-2*r.log()/pi
    tail=two**(a+1)*a/pi*(1/(1-a)+one/2-(arb(3)/2).log())
    if linear:
        L=arb.max(-(1-2*r).log(),(1+2*r)*(1+2*r).log())
        BC=r*r/(1-r)**2*(-r.log()+arb(3)/2-two.log()/2)
        BD=3*r*r/(4*(1-r)**2)*(-r.log()+two.log()+arb(2)/3)
        base=two**a*N+(two**a-1)*E+tail
        C=2*a2*r**a/a+base+a*(BC+E*L)
        D=2*A*r**a/a+one/2+base+a*(BD+3*E*L)
    else:
        base=two**a*N+(two**a+(1+2*r)**a)*E+tail
        C=2*a2*r**a/a+base
        D=2*A*r**a/a+one/2+base
    return C,D

def pick(a,linear,idx):
    # Golden search in log radius, for selection only.
    lo,hi=math.log(1e-10),math.log(.499999)
    ratio=(math.sqrt(5)-1)/2
    def f(x):return float(values(arb(str(a)),arb(repr(math.exp(x))),linear)[idx].mid())
    p=hi-ratio*(hi-lo);q=lo+ratio*(hi-lo);fp,fq=f(p),f(q)
    for _ in range(75):
        if fp<fq:hi=q;q=p;fq=fp;p=hi-ratio*(hi-lo);fp=f(p)
        else:lo=p;p=q;fp=fq;q=lo+ratio*(hi-lo);fq=f(q)
    r=Q(math.floor(math.exp((lo+hi)/2)*10**12),10**12)
    assert 0<r<Q(1,2)
    return r

def record(v):
    assert v.is_finite()
    lo,hi=Q(str(v.lower().fmpq())),Q(str(v.upper().fmpq()))
    n=-((-hi*10**10).__floor__())
    return dict(lower=str(lo),upper=str(hi),upper_decimal_10=f'{n//10**10}.{n%10**10:010d}')

def independent(aq,rq,linear,idx):
    # Rearranged expression with rational constants and exp(log) powers.
    ctx.prec=256;a=arb(str(aq));r=arb(str(rq));pi=arb.pi();ln2=arb(2).log()
    p=(a*ln2).exp();ra=(a*r.log()).exp()
    loc=(arb(4)*(a*ln2/2).exp()/(pi*(a+2)) if idx==0 else
         ((a/2+1).gamma()/(pi.sqrt()*(a/2+arb(3)/2).gamma()))) * ra/a
    local_identity=arb(0) if idx==0 else arb(1)/2
    E=(1/(1-r*r)).log()/2
    rem=p/2-2*p*r.log()/pi+2*p*a/pi*(1/(1-a)+(arb(4)/9).log()/2+arb(1)/2)
    if not linear:return loc+local_identity+rem+(p+(a*(1+2*r).log()).exp())*E
    L=arb.max((1/(1-2*r)).log(),(1+2*r)*(1+2*r).log())
    if idx==0:B=r*r/((1-r)*(1-r))*((1/r).log()+arb(3)/2-ln2/2);factor=1
    else:B=3*r*r/(4*(1-r)*(1-r))*((2/r).log()+arb(2)/3);factor=3
    return loc+local_identity+rem+(p-1)*E+a*(B+factor*E*L)

def main():
    exponents=['1/1000000','1/100000','1/10000','1/1000','1/200','1/100','1/50','1/20','1/10','1/5','3/10','1/2','3/4','9/10']
    rows=[]
    for aa in exponents:
        aq=Q(aa);row=dict(alpha=str(aq),bounds={})
        for lin in [False,True]:
            for idx,name in [(0,'C'),(1,'D')]:
                ctx.prec=160;r=pick(aq,lin,idx)
                v=values(arb(str(aq)),arb(str(r)),lin)[idx]
                check=independent(aq,r,lin,idx)
                primary=record(v);second=record(check)
                assert Q(primary['lower'])<=Q(second['lower'])<=Q(second['upper'])<=Q(primary['upper'])
                key=('J_' if lin else 'H_')+name
                row['bounds'][key]=dict(rho=str(r),**second)
        rows.append(row)
        print(aa,{k:v['upper_decimal_10'] for k,v in row['bounds'].items()},flush=True)
    paths=['code/evaluate_explicit_second_term.py','08_improved_upper_bounds/explicit_second_term/PROOF.md',
           '08_improved_upper_bounds/explicit_second_term/linear_remainder/PROOF.md']
    output=dict(time_utc=datetime.now(timezone.utc).isoformat(),rows=rows,
        source_hashes={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
        method='160-bit evaluation, independent rearranged 256-bit expression; rational cutoffs selected by a noncertifying floating golden search.',
        status='Formula evaluations confirmed. The linear-remainder transport proof awaits the lead cross-read.')
    out=ROOT/'08_improved_upper_bounds/explicit_second_term/verification/rational_cutoffs.json'
    out.write_text(json.dumps(output,indent=2)+'\n')
    lines=['# Outward formula values','', 'Cutoffs are exact rationals in rational_cutoffs.json. They are selected values, not certified global minimizers.','',
           '| alpha | H_C | H_D | J_C | J_D |','|---|---:|---:|---:|---:|']
    for row in rows:lines.append('| '+row['alpha']+' | '+' | '.join(row['bounds'][k]['upper_decimal_10'] for k in ['H_C','H_D','J_C','J_D'])+' |')
    (out.parent/'TABLE.md').write_text('\n'.join(lines)+'\n')
if __name__=='__main__':main()
