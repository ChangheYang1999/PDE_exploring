"""Outward residual costs from radius-by-radius pairing, no new optimizer."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import argparse, hashlib, json, time
from flint import arb, ctx
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'08_improved_upper_bounds/local_disk_transport/balanced_residual'
OLD=BASE/'existing_certificates'
OUT=BASE/'radial_refinement'
ctx.prec=256

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p): return json.loads(p.read_text())
def ar(q): return arb(str(q))
def upper(x):
    assert x.is_finite()
    return Q(str(x.upper().fmpq()))
def lower(x):
    assert x.is_finite()
    return Q(str(x.lower().fmpq()))
def endpoints(d):
    x,y=Q(d['lower']),Q(d['upper']);assert x<=y;return x,y
def rec(x): return dict(lower=str(lower(x)),upper=str(upper(x)),display=x.str(40,more=True))
def ceil10(q):
    k=-((-q*10**10).__floor__());return f'{k//10**10}.{k%10**10:010d}'

def main():
    p=argparse.ArgumentParser();p.add_argument('--subdivisions',type=int,default=8);args=p.parse_args()
    assert args.subdivisions>=1
    started=time.monotonic();hashes={}
    def bind(p):
        p=p.resolve();assert p.is_relative_to(ROOT);hashes[str(p.relative_to(ROOT))]=sha(p)
    ac=OLD/'verification/accepted.json';accept=load(ac)
    assert accept['verdict']=='CONFIRMED' and accept['ledger']=='V152';bind(ac)
    for name,h in accept['sha256'].items(): assert sha(ROOT/name)==h;bind(ROOT/name)
    old=load(OLD/'verification/independent_audit.json');alphas=[r['alpha'] for r in old['rows']]
    aa=list(map(arb,alphas));original={r['alpha']:r for r in old['rows']}
    newtot={a:[Q(0)]*17 for a in alphas};oldtot={a:[Q(0)]*17 for a in alphas}
    improved={a:0 for a in alphas};details=[]
    for k in range(256):
        src=OLD/'verification/mass_replay'/f'row_{k:03d}.json';d=load(src);bind(src)
        assert d['row']==k and d['integer_unit']==2**44
        s0,s1=endpoints(d['radial_left']);t0,t1=endpoints(d['radial_right'])
        assert s0==s1 and t0==t1 and s0<t0
        edges=[s0+(t0-s0)*i/args.subdivisions for i in range(args.subdivisions+1)]
        # These coefficients do not depend on the phase.
        bins=[]
        for sq,tq in zip(edges,edges[1:]):
            s,t=ar(sq),ar(tq);L=(t/s).log();H=arb(1)/2-s*s*L/(t*t-s*s)
            assert lower(H)>0 and lower(L-H)>0
            powers=[]
            for a in aa:
                exact=(arb(2)**a)*(t**a-s**a)/a
                gap=(1+2*s)**a-(2*s)**a
                assert lower(exact)>0 and lower(gap)>0
                powers.append((exact,gap))
            bins.append((sq,tq,L,H,powers))
        row=[]
        for j,v in enumerate(d['phases']):
            assert v['phase']==j and sum(v['masses'])==v['signed_integer_sum']
            assert sum(map(abs,v['masses']))==v['absolute_integer_sum']
            tau=endpoints(v['angular_variation'])[1]-Q(v['absolute_integer_sum'],2**44)
            S=Q(v['signed_integer_sum'],2**44);assert tau>=0
            c=arb(0) if j==16 else (arb.pi()*j/32).cos()
            costs=[arb(0) for _ in alphas]
            for sq,tq,L,H,powers in bins:
                qs=-c*ar(sq*sq)-ar(S);qt=-c*ar(tq*tq)-ar(S)
                J=(L-H)*abs(qs)+H*abs(qt)
                Jhat=min(upper(J),upper(ar(tau)*L));assert Jhat>=0
                for i,(exact,gap) in enumerate(powers):
                    costs[i]+=ar(tau)*exact+ar(Jhat)*gap
            selected={}
            for i,a in enumerate(alphas):
                oldhi=endpoints(v['new'][a])[1];candidate=upper(costs[i]);assert candidate>=0
                best=min(oldhi,candidate)
                newtot[a][j]+=best;oldtot[a][j]+=oldhi
                improved[a]+=best<oldhi
                selected[a]=str(best)
            row.append(dict(phase=j,new_upper=selected))
        details.append(dict(row=k,phases=row))
        if (k+1)%32==0:print(datetime.now(timezone.utc).isoformat(),'row',k+1,'seconds',round(time.monotonic()-started,2),flush=True)
    result=[]
    factor=1/(arb.pi()/64).cos()
    for a in alphas:
        r=original[a];prior=list(map(Q,r['phase_upper']))
        assert oldtot[a]==list(map(Q,r['new_residual_upper']))
        phases=[prior[j]-oldtot[a][j]+newtot[a][j] for j in range(17)]
        assert all(0<=p<=q for p,q in zip(phases,prior))
        j=max(range(17),key=lambda j:phases[j]);up=ar(Q(r['small_upper']))+factor*ar(phases[j])
        safe=ceil10(upper(up));assert Q(safe)<=Q(r['new_C_upper'])
        result.append(dict(alpha=a,safe_upper_C=safe,previous_upper_C=r['new_C_upper'],worst_phase=j,
            upper=rec(up),phase_upper=list(map(str,phases)),residual_upper=list(map(str,newtot[a])),improved_row_phases=improved[a]))
        print(a,r['new_C_upper'],'->',safe,'phase',j,'improved',improved[a],flush=True)
    bind(Path(__file__));bind(OUT/'PROOF.md')
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),subdivisions=args.subdivisions,precision_bits=ctx.prec,
        rows=result,sha256=hashes,details=details,status='NUMERICAL CHECK PASSED; analytic cross-read and acceptance pending')
    (OUT/'verification/independent_audit.json').write_text(json.dumps(out,indent=2)+'\n')
    print('COMPLETE',out['time_utc'],flush=True)

if __name__=='__main__':main()
