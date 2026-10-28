"""Directed positive-series reflection moments, checked by a separate recurrence."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
from datetime import datetime,timezone
import argparse,hashlib,json,sys
from flint import arb,ctx
from certify_optimal_disk_values import coeff,ep,decimal,aq
sys.set_int_max_str_digits(100000)
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'08_improved_upper_bounds/local_projection/strict_increment/phase_uniform_density'
OUT=BASE/'numerical_values'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def jcoeff(m):
    b,k=(Q(0),Q(1,4)) if m%2==0 else (Q(1,3),Q(0))
    for r in range(0 if m%2==0 else 1,m,2):
        ratio=Q(r+1,r+4);b*=ratio;k*=ratio
    return b,k

def terms(n,c,N):
    a=1-c;out=[]
    for k in range(N+1):
        b,p=Q(0),Q(0)
        for l in range(k+1):
            bb,pp=jcoeff(2*n+l);z=(-1)**l*comb(k,l);b+=z*bb;p+=z*pp
        z=(2*c)**k*a**(2*n+k+2);out.append((z*b,z*p))
    return out

def evalterms(ts,variant=False):
    pi=arb.pi()
    if not variant:return [aq(b)+aq(p)*pi for b,p in ts]
    return [pi*(aq(p)+aq(b)/pi) for b,p in ts]

def recurrence(n,c):
    a=1-c;A=aq(c*c+a*a);B=aq(2*c);Delta=aq(c*c-a*a)
    F=(A*arb.pi()/2-B*aq(a)-2*Delta*aq((c-a)/(c+a)).atan())/(B*B)
    for m in range(1,2*n+1):
        b,p=jcoeff(m-1);J=aq(a**(m+1))*(aq(b)+aq(p)*arb.pi());F=(J-A*F)/B
    return F

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--ledger',required=True);ap.add_argument('--analytic-ledger',required=True);args=ap.parse_args();hashes={}
    def bind(p):
        p=p.resolve();assert p.is_relative_to(ROOT);hashes[str(p.relative_to(ROOT))]=sha(p)
    def accept(p,v):
        d=json.loads(p.read_text());assert d['ledger']==v and d['verdict']=='CONFIRMED';bind(p)
        for name,h in d['sha256'].items():assert sha(ROOT/name)==h,name;bind(ROOT/name)
        return d
    accept(BASE/'verification/accepted.json',args.analytic_ledger)
    old=accept(ROOT/'08_improved_upper_bounds/local_projection/strict_increment/larger_disks/optimal_axis_disks/numerical_values/accepted.json','V226')
    c=Q(old['root']['chosen_c']);a=1-c;ratio=2*c*a;assert 0<ratio<1
    N=64;termsets={n:terms(n,c,N) for n in range(1,9)};moments=[];enclosures={}
    for n,ts in termsets.items():
        ctx.prec=384;vals=evalterms(ts);assert all(ep(x)>0 for x in vals)
        partial=sum(vals[:N],arb(0));upper=partial+vals[N]/aq(1-ratio);pl,ph=ep(partial),ep(partial,True);uh=ep(upper,True)
        ctx.prec=768;v2=evalterms(ts,True);p2=sum(reversed(v2[:N]),arb(0));full=recurrence(n,c)
        assert pl<=ep(p2)<=ep(p2,True)<=ph
        assert ph<ep(full)<=ep(full,True)<uh
        enclosures[n]=(pl,ph)
        moments.append(dict(n=n,partial_lower=str(pl),partial_upper=str(ph),full_upper=str(uh),full_closed_form=full.str(48)))
    rows=[]
    for r in old['rows']:
        alpha,s=Q(r['alpha_or_epsilon']),Q(r['rho']);uniform=r['mode']=='uniform';cutoff=r['kind']=='cutoff';assert 2*a*s<1
        def evaluate(variant=False):
            total=arb(0)
            for n,ts in termsets.items():
                vv=evalterms(ts,variant);I=sum(reversed(vv[:N]),arb(0)) if variant else sum(vv[:N],arb(0))
                bt=aq(Q(2**(2*n+1),comb(2*n,n)))*I/arb.pi()
                if cutoff:bt-=aq(s*s*a**(2*n+2)/Q(2*n+2)/(1-s)**2)
                assert ep(bt)>0
                total+=aq(coeff(n,alpha)*s**(2*n)/(alpha if uniform else 1))*bt
            return aq(Q(r['base_upper']))-total,total
        ctx.prec=384;value,gain=evaluate();lo,hi=ep(value),ep(value,True);gl,gh=ep(gain),ep(gain,True);safe=decimal(hi)
        ctx.prec=768;v2,g2=evaluate(True);assert lo<=ep(v2)<=ep(v2,True)<=hi;assert gl<=ep(g2)<=ep(g2,True)<=gh
        assert safe==decimal(ep(v2,True)) and Q(safe)<Q(r['safe_upper'])
        rows.append(dict(mode=r['mode'],kind=r['kind'],operator='D',alpha_or_epsilon=str(alpha),rho=str(s),safe_upper=safe,previous_upper=r['safe_upper'],base_upper=r['base_upper'],lower=str(lo),upper=str(hi),gain_lower=str(gl),gain_upper=str(gh)))
    for p in [OUT/'PROOF.md',Path(__file__),ROOT/'code/certify_optimal_disk_values.py']:bind(p)
    result=dict(time_utc=datetime.now(timezone.utc).isoformat(),ledger=args.ledger,verdict='CONFIRMED',c=str(c),a=str(a),positive_terms=N,reflection_terms=8,moments=moments,rows=rows,precision_bits=[384,768],sha256=hashes,scope='Positive partial reflection sums on fixed rational disks; independent closed-form moment check; original bases before reflection')
    (OUT/'accepted.json').write_text(json.dumps(result,indent=2)+'\n');print(result['time_utc'],args.ledger)
    for r in rows:print(r['mode'],r['alpha_or_epsilon'],r['rho'],r['safe_upper'])
if __name__=='__main__':main()
