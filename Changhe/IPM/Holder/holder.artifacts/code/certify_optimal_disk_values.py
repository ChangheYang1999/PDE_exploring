"""Directed eight-moment savings for a rational disk inside the maximal family."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
from math import comb, factorial
import argparse, hashlib, json, sys
from flint import arb, ctx
from certify_sharp_deficiency import finite, uniform, rational_catalan, qball
from certify_exact_tail_values import bounds
sys.set_int_max_str_digits(100000)
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'08_improved_upper_bounds/local_projection/strict_increment/larger_disks/optimal_axis_disks'
OUT=BASE/'numerical_values'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def aq(x):return arb(str(x))
def ep(x,high=False):return Q(str((x.upper() if high else x.lower()).fmpq()))
def ceilgrid(x,n=10):
    scale=10**n;y=x*scale;return Q(-((-y.numerator)//y.denominator),scale)
def decimal(x,n=10):
    v=ceilgrid(x,n)*10**n;assert v.denominator==1
    return f'{v.numerator//10**n}.{v.numerator%10**n:0{n}d}'
def poly(x):return 2*x**4-3*x*x+4*x-1
def isolate():
    l,u=Q(0),Q(1,3)
    for _ in range(256):
        m=(l+u)/2
        if poly(m)<0:l=m
        else:u=m
    assert poly(l)<0<poly(u)
    v=lambda x:1-2*x+2*x**3
    n=lambda x:(1-2*x*x)**2
    cl,cu=n(u)/(2*v(l)),n(l)/(2*v(u))
    c=ceilgrid(cu,30)
    assert Q(49,66)<cl<cu<=c<Q(3,4)
    return l,u,cl,cu,c

def moment_coeff(m,c):
    constant=(-c)**m*(1/c-1)
    constant+=sum((Q(comb(m,j))*(-c)**(m-j)*(1-c**(j-1))/(j-1) for j in range(2,m+1)),Q(0))
    return constant,m*(-c)**(m-1)
def moment(m,c,variant=False):
    cc=aq(c)
    if not variant:
        b,k=moment_coeff(m,c);return aq(b)+aq(k)*(1/cc).log()
    return ((-cc)**m*(1/cc-1)-m*(-cc)**(m-1)*cc.log()+sum((comb(m,j)*(-cc)**(m-j)*(1-cc**(j-1))/(j-1) for j in range(2,m+1)),arb(0)))
def positive_moment(m,c,N=96):
    a=1-c
    terms=[c**(m-1)*comb(m+k-1,k)*a**(m+k+1)/Q(m+k+1) for k in range(N)]
    lo=sum(terms,Q(0));assert lo==sum(reversed(terms),Q(0))
    first=c**(m-1)*comb(m+N-1,N)*a**(m+N+1)/Q(m+N+1)
    q=a*Q(m+N,N+1);assert 0<q<1
    return lo,lo+first/(1-q)
def coeff(n,alpha):
    v=2*alpha/Q(factorial(n)**2)
    for k in range(1,2*n):v*=k-alpha
    return v

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--ledger',required=True);args=ap.parse_args();hashes={}
    def bind(p):
        p=p.resolve();assert p.is_relative_to(ROOT);hashes[str(p.relative_to(ROOT))]=sha(p)
    def accept(rel,v):
        p=ROOT/rel;d=json.loads(p.read_text());assert d['ledger']==v and d['verdict']=='CONFIRMED';bind(p)
        for name,h in d['sha256'].items():assert sha(ROOT/name)==h,name;bind(ROOT/name)
        return d
    accept(str((BASE/'verification/accepted.json').relative_to(ROOT)),'V224')
    accept('08_improved_upper_bounds/local_projection/strict_increment/all_even_moments/verification/accepted.json','V223')
    accept('08_improved_upper_bounds/explicit_second_term/tail_series/verification/accepted.json','V222')
    prev=accept('08_improved_upper_bounds/explicit_second_term/tail_series/numerical_values/accepted.json','V225')
    old=accept('08_improved_upper_bounds/local_projection/strict_increment/larger_disks/exact_radial_density/cross4096_values/accepted.json','V220')
    l,u,cl,cu,c=isolate();a=1-c;moment_bounds={};moment_rows=[]
    ctx.prec=384
    for m in range(3,20,2):
        ml,mh=positive_moment(m,c);z=moment(m,c);zl,zh=ep(z),ep(z,True)
        assert 0<ml<zl<=zh<mh
        ctx.prec=768;zz=moment(m,c,True);assert zl<=ep(zz)<=ep(zz,True)<=zh
        ctx.prec=384
        moment_bounds[m]=(ml,mh)
        moment_rows.append(dict(m=m,positive_lower=str(ml),positive_upper=str(mh),ball=z.str(50),lower=str(zl),upper=str(zh)))
    catl,cath=rational_catalan(512)
    cases=[]
    for row in old['rows']:
        if row['kind']=='unperturbed local':cases.append(dict(mode='finite',kind='unperturbed',alpha=Q(row['alpha']),rho=Q(row['radius']),base=Q(row['previous_upper_D']),old_upper=Q(row['safe_upper_D'])))
    for aa,r in [(Q(1,1000),Q(31977,100000)),(Q(1,200),Q(31963,100000)),(Q(1,100),Q(15973,50000))]:
        older=min(Q(t['safe_upper']) for t in prev['rows'] if t['mode']=='finite' and t['operator']=='D' and Q(t['alpha_or_epsilon'])==aa)
        cases.append(dict(mode='finite',kind='cutoff',alpha=aa,rho=r,old_upper=older))
    older=min(Q(t['safe_upper']) for t in prev['rows'] if t['mode']=='uniform' and t['operator']=='D')
    cases.append(dict(mode='uniform',kind='cutoff',alpha=Q(1,100),rho=Q(31987,100000),old_upper=older))
    rows=[]
    for case in cases:
        aa,r,mode,kind=case['alpha'],case['rho'],case['mode'],case['kind'];assert 2*a*r<1
        retained=kind=='cutoff';assert not retained or 0<r<Q(1,2)
        tail=bounds(aa,64)[1]
        def evaluate(variant=False):
            g=arb.const_catalan() if variant else qball(catl,cath)
            if kind=='unperturbed':base=aq(case['base'])
            else:
                base=uniform(r,'D',g,variant) if mode=='uniform' else finite(aa,r,'D',g,variant)
                A=aq(aa);power=(A*arb(2).log()).exp()
                oldtail=1/(1-A)+arb(1)/2-(arb(3)/2).log()
                reduction=2*power*(oldtail-aq(tail))/arb.pi()
                base-=reduction if mode=='uniform' else A*reduction
            parts=[]
            for n in range(1,10):
                m=2*n+1;b=moment(m,c,variant)
                remove=r*r*a**(m+1)/Q(m+1)/(1-r)**2 if retained else Q(0)
                b-=aq(remove);assert ep(b)>0
                k=coeff(n,aa)*r**(2*n)/(aa if mode=='uniform' else 1)
                parts.append(aq(k)*b)
                ml,mh=moment_bounds[m];assert 0<ml-remove<=ep(b)<=ep(b,True)<=mh-remove
            gain=sum(parts[:8],arb(0));omitted=parts[8]/aq(1-(2*a*r)**2)
            return base-gain,gain,omitted,base
        ctx.prec=384;value,gain,omitted,base=evaluate();vl,vh=ep(value),ep(value,True);text=value.str(48);safe=decimal(vh)
        gl,gh=ep(gain),ep(gain,True);gaintext=gain.str(48);tailtext=omitted.str(32);basehi=ep(base,True)
        ctx.prec=768;fresh,fg,_,_=evaluate(True);assert vl<=ep(fresh)<=ep(fresh,True)<=vh;assert gl<=ep(fg)<=ep(fg,True)<=gh
        assert vh<=Q(safe)<vh+Q(1,10**10)
        assert Q(safe)<case['old_upper']
        rows.append(dict(mode=mode,operator='D',kind=kind,alpha_or_epsilon=str(aa),rho=str(r),safe_upper=safe,previous_upper=decimal(case['old_upper']),base_upper=str(basehi),ball=text,lower=str(vl),upper=str(vh),gain_lower=str(gl),gain_upper=str(gh),gain_ball=gaintext,omitted_positive_saving_upper=tailtext))
    for p in [OUT/'PROOF.md',Path(__file__),ROOT/'code/certify_sharp_deficiency.py',ROOT/'code/certify_exact_tail_values.py']:bind(p)
    result=dict(time_utc=datetime.now(timezone.utc).isoformat(),ledger=args.ledger,verdict='CONFIRMED',root=dict(lower=str(l),upper=str(u),c_star_lower=str(cl),c_star_upper=str(cu),chosen_c=str(c),chosen_a=str(a)),moments=moment_rows,rows=rows,precision_bits=[384,768],positive_moment_terms=96,reflection_terms=8,sha256=hashes,scope='Explicit rational disks; eight positive reflection moments; finite rows and one uniform linear coefficient; no optimality claim')
    (OUT/'accepted.json').write_text(json.dumps(result,indent=2)+'\n');print(result['time_utc'],args.ledger)
    print('c',decimal(c,30),'a',decimal(a,30))
    for row in rows:print(row['mode'],row['alpha_or_epsilon'],row['rho'],row['safe_upper'])
if __name__=='__main__':main()
