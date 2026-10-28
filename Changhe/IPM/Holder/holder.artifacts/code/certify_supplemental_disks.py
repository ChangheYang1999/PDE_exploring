"""Directed moments for four additional disjoint reflection disk pairs."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
from datetime import datetime,timezone
import argparse,hashlib,json,sys
from flint import arb,ctx
from certify_phase_uniform_density import jcoeff,evalterms
from certify_optimal_disk_values import coeff,ep,decimal,aq
sys.set_int_max_str_digits(100000)
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'08_improved_upper_bounds/local_projection/strict_increment/phase_uniform_density/supplemental_disks'
OUT=BASE/'numerical_values'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def terms(n,c,a,N):
    M=(c+a)**2;out=[]
    for k in range(N+1):
        b,p=Q(0),Q(0)
        for l in range(k+1):
            bb,pp=jcoeff(2*n+l);z=(-1)**l*comb(k,l);b+=z*bb;p+=z*pp
        z=(2*c/M)**k*a**(2*n+k+2)/M;out.append((z*b,z*p))
    return out

def recurrence(n,c,a):
    A=aq(c*c+a*a);B=aq(2*c);Delta=aq(c*c-a*a)
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
    old=accept(BASE.parent/'numerical_values/accepted.json','V231')
    geo=json.loads((BASE/'geometry.json').read_text());assert geo['result']=='EXACT_GEOMETRY_PASSED';bind(BASE/'geometry.json')
    pairs=[(Q(r['c']),Q(r['a'])) for r in geo['disks']];assert len(pairs)==4
    N=64;termsets={};moments=[]
    for i,(c,a) in enumerate(pairs):
        ratio=2*c*a/(c+a)**2;assert 0<ratio<1 and 0<a<c/2 and c+a<=1
        for n in range(1,9):
            ts=terms(n,c,a,N);termsets[i,n]=ts
            ctx.prec=384;vals=evalterms(ts);assert all(ep(x)>0 for x in vals)
            partial=sum(vals[:N],arb(0));upper=partial+vals[N]/aq(1-ratio);pl,ph,uh=ep(partial),ep(partial,True),ep(upper,True)
            ctx.prec=768;v2=evalterms(ts,True);p2=sum(reversed(v2[:N]),arb(0));full=recurrence(n,c,a)
            assert pl<=ep(p2)<=ep(p2,True)<=ph,(i,n,'partial')
            assert ph<ep(full)<=ep(full,True)<uh,(i,n,'full')
            moments.append(dict(disk=i,n=n,c=str(c),a=str(a),ratio=str(ratio),partial_lower=str(pl),partial_upper=str(ph),full_upper=str(uh),full_closed_form=full.str(48)))
    rows=[]
    for r in old['rows']:
        alpha,s=Q(r['alpha_or_epsilon']),Q(r['rho']);uniform=r['mode']=='uniform';cutoff=r['kind']=='cutoff';assert all(2*a*s<1 for _,a in pairs)
        def evaluate(variant=False):
            total=arb(0)
            for i,(c,a) in enumerate(pairs):
                for n in range(1,9):
                    vv=evalterms(termsets[i,n],variant);I=sum(reversed(vv[:N]),arb(0)) if variant else sum(vv[:N],arb(0))
                    bt=aq(Q(2**(2*n+1),comb(2*n,n)))*I/arb.pi()
                    if cutoff:bt-=aq(s*s*a**(2*n+2)/Q(2*n+2)/(1-s)**2)
                    assert ep(bt)>0
                    total+=aq(coeff(n,alpha)*s**(2*n)/(alpha if uniform else 1))*bt
            return aq(Q(r['upper']))-total,total
        ctx.prec=384;value,gain=evaluate();lo,hi=ep(value),ep(value,True);gl,gh=ep(gain),ep(gain,True);safe=decimal(hi)
        ctx.prec=768;v2,g2=evaluate(True);assert lo<=ep(v2)<=ep(v2,True)<=hi;assert gl<=ep(g2)<=ep(g2,True)<=gh
        assert safe==decimal(ep(v2,True)) and Q(safe)<Q(r['safe_upper'])
        rows.append(dict(mode=r['mode'],kind=r['kind'],operator='D',alpha_or_epsilon=str(alpha),rho=str(s),safe_upper=safe,previous_upper=r['safe_upper'],base_upper=r['upper'],lower=str(lo),upper=str(hi),gain_lower=str(gl),gain_upper=str(gh)))
    for p in [OUT/'PROOF.md',Path(__file__),ROOT/'code/certify_phase_uniform_density.py',ROOT/'code/certify_optimal_disk_values.py']:bind(p)
    result=dict(time_utc=datetime.now(timezone.utc).isoformat(),ledger=args.ledger,verdict='CONFIRMED',pairs=[dict(c=str(c),a=str(a)) for c,a in pairs],positive_terms=N,reflection_terms=8,moments=moments,rows=rows,precision_bits=[384,768],sha256=hashes,scope='Four additional disjoint disk pairs; positive partial moments and independent arctangent recurrence; V231 exact upper endpoints before supplemental savings')
    (OUT/'accepted.json').write_text(json.dumps(result,indent=2)+'\n');print(result['time_utc'],args.ledger)
    for r in rows:print(r['mode'],r['alpha_or_epsilon'],r['rho'],r['safe_upper'])
if __name__=='__main__':main()
