"""Directed finite and uniform evaluations; proof written before execution."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
from flint import arb, ctx
import argparse, hashlib, json
ROOT = Path(__file__).resolve().parents[1]
SHARP = ROOT/'08_improved_upper_bounds/explicit_second_term/sharp_deficiency'
EXACT = ROOT/'08_improved_upper_bounds/local_projection/strict_increment/larger_disks/exact_radial_density'
OUT = SHARP/'numerical_values'

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def ep(x, high=False): return Q(str((x.upper() if high else x.lower()).fmpq()))
def aq(q): return arb(str(q))
def ceil10(q):
    t=q*10**10; n=-((-t.numerator)//t.denominator)
    return f'{n//10**10}.{n%10**10:010d}'
def qball(lo,hi): return aq((lo+hi)/2)+arb(0,aq((hi-lo)/2))
def rational_catalan(n):
    b=h=Q(1);total=Q(0)
    for k in range(n):
        total+=b*h/Q(2**(k+1))
        b*=Q(2*k+2,2*k+3);h+=Q(1,2*k+3)
    return total,total+Q(1,2**n)
def quantities(r,g):
    pi=arb.pi();r=aq(r);lr=r.log();ln2=arb(2).log()
    E=-(1-r*r).log()/2;N=arb(1)/2-2*lr/pi
    x=-(1-2*r).log();y=(1+2*r)*(1+2*r).log()
    assert ep(x)>ep(y,True) or ep(y)>ep(x,True)
    L=x if ep(x)>ep(y,True) else y
    bc=r*r/(2*(1-r)**2)*(-lr+arb(1)/2+2*g/pi)
    bd=r*r/(2*(1-r)**2)*(-lr+arb(1)/2+ln2)
    oldbc=r*r/(1-r)**2*(-lr+arb(3)/2-ln2/2)
    oldbd=3*r*r/(4*(1-r)**2)*(-lr+ln2+arb(2)/3)
    return pi,r,lr,ln2,E,N,L,bc,bd,oldbc,oldbd

def uniform(r,kind,g,variant=False):
    pi,r,lr,l2,E,N,L,bc,bd,oldbc,oldbd=quantities(r,g)
    e=arb(1)/100;power=(e*l2).exp();P=(power-1)/e
    tail=2*power/pi*(1/(1-e)+arb(1)/2-(arb(3)/2).log())
    Z=N*P+E*P+tail if variant else (N+E)*P+tail
    ell=lr+l2/2-arb(1)/2 if kind=='C' else lr+l2-1
    derivative=arb(1)/4 if kind=='C' else 1-pi*pi/12
    new=bc if kind=='C' else bd;old=oldbc if kind=='C' else oldbd
    linear=new if not variant else old-(old-new)
    return (ell*ell+derivative)/pi+Z+linear+(1 if kind=='C' else 3)*E*L

def finite(a,r,kind,g,variant=False):
    pi,r,lr,l2,E,N,L,bc,bd,oldbc,oldbd=quantities(r,g)
    a=aq(a);power=(a*l2).exp();localpow=(a*lr).exp()
    if kind=='C':angular=2*(a*l2/2).exp()/(pi*(2+a))
    elif variant:angular=((1+a/2).lgamma()-(arb(3)/2+a/2).lgamma()).exp()/(2*pi.sqrt())
    else:angular=(1+a/2).gamma()/(2*pi.sqrt()*(arb(3)/2+a/2).gamma())
    near=2*angular*localpow/a+(arb(1)/2 if kind=='D' else 0)
    tail=2*power/pi*a*(1/(1-a)+arb(1)/2-(arb(3)/2).log())
    new=bc if kind=='C' else bd;old=oldbc if kind=='C' else oldbd
    linear=new if not variant else old-(old-new)
    return near+power*N+(power-1)*E+tail+a*(linear+(1 if kind=='C' else 3)*E*L)

def moments(r,variant=False):
    r=aq(r);l=arb(4).log()-arb(3).log() if variant else (arb(4)/3).log()
    j=-arb(31)/32+arb(27)/8*l;k=-arb(233)/1024+arb(405)/512*l
    m2=j*r*r-r**4/(512*(1-r)**2);m4=k*r**4-r**6/(49152*(1-r)**2)
    assert ep(m2)>0 and ep(m4)>0
    return m2,m4

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--ledger',required=True);ap.add_argument('--analytic-ledger',required=True)
    ap.add_argument('--radial-ledger');args=ap.parse_args();hashes={}
    def bind(p):
        p=p.resolve();assert p.is_relative_to(ROOT);hashes[str(p.relative_to(ROOT))]=sha(p)
    def check(p,ledger):
        d=json.loads(p.read_text());assert d['verdict']=='CONFIRMED' and d['ledger']==ledger;bind(p)
        for name,digest in d['sha256'].items():assert sha(ROOT/name)==digest,name;bind(ROOT/name)
        return d
    check(ROOT/'08_improved_upper_bounds/explicit_second_term/verification/accepted.json','V118')
    accepted=check(SHARP/'verification/accepted.json',args.analytic_ledger)
    assert accepted['sha256'][str((SHARP/'PROOF.md').relative_to(ROOT))]==sha(SHARP/'PROOF.md')
    if args.radial_ledger:check(EXACT/'verification/accepted.json',args.radial_ledger)
    lo,hi=rational_catalan(512);ctx.prec=768;g2=arb.const_catalan()
    assert lo<ep(g2)<ep(g2,True)<hi
    ctx.prec=384;g1=qball(lo,hi);assert ep(g1)<=lo<hi<=ep(g1,True)
    rows=[]
    cases=[('uniform','C',Q(1,100),Q(34891,100000)),('uniform','D',Q(1,100),Q(15993,50000))]
    for a,nc,nd in [(Q(1,1000),34880,31975),(Q(1,200),34868,31961),(Q(1,100),34853,31944)]:
        cases.extend([('finite','C',a,Q(nc,100000)),('finite','D',a,Q(nd,100000))])
    for mode,kind,a,r in cases:
        for reflection in ([False,True] if kind=='D' and args.radial_ledger else [False]):
            def evaluate(g,variant=False):
                value=uniform(r,kind,g,variant) if mode=='uniform' else finite(a,r,kind,g,variant)
                if reflection:
                    m2,m4=moments(r,variant);aa=aq(a)
                    gain=(1-aa)*m2+(1-aa)*(2-aa)*(3-aa)*m4
                    value-=gain if mode=='uniform' else aa*gain
                return value
            ctx.prec=384;value=evaluate(g1);vl,vh=ep(value),ep(value,True);text=value.str(45);safe=ceil10(vh)
            ctx.prec=768;fresh=evaluate(g2,True)
            assert vl<=ep(fresh)<=ep(fresh,True)<=vh
            assert vh<=Q(safe)<vh+Q(1,10**10)
            if mode=='uniform':assert Q(safe)<=Q('2.4945' if kind=='C' else '2.7442')
            rows.append(dict(mode=mode,operator=kind,alpha_or_epsilon=str(a),rho=str(r),retained_reflection=reflection,ball=text,lower=str(vl),upper=str(vh),safe_upper=safe))
    for p in [SHARP/'PROOF.md',SHARP/'catalan_evaluation/PROOF.md',OUT/'PROOF.md',Path(__file__)]:bind(p)
    record=dict(time_utc=datetime.now(timezone.utc).isoformat(),ledger=args.ledger,verdict='CONFIRMED',analytic_ledger=args.analytic_ledger,radial_ledger=args.radial_ledger,precision_bits=[384,768],catalan=dict(terms=512,lower=str(lo),upper=str(hi)),rows=rows,sha256=hashes,scope='Fixed rational upper evaluations and whole-interval linear envelope; no optimality assertion')
    (OUT/'accepted.json').write_text(json.dumps(record,indent=2)+'\n')
    for row in rows:print(row['mode'],row['operator'],row['alpha_or_epsilon'],row['rho'],row['retained_reflection'],row['safe_upper'])
if __name__=='__main__':main()
