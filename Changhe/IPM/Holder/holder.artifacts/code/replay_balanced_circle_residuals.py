"""Replay the fixed local angular extraction once for ten Holder exponents.

No transport optimizer is called. Each row is checkpointed atomically, with
all integer masses and exact endpoint records. Geometric/source validation
and complete old-certificate recombination are performed separately.
"""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
import argparse, hashlib, json, time
from flint import arb, ctx
from certify_local_circles_greedy import angular_data, UNIT
ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT/'08_improved_upper_bounds/local_disk_transport/balanced_residual/existing_certificates'
ALPHAS = ['1/1000','1/100','1/20','1/10','1/5','3/10','1/2','3/4','9/10','99/100']
N, NR, M = 512, 256, 16
ctx.prec = 160
PI = arb.pi()

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def up(x): return arb(x.upper())
def rec(x):
    assert x.is_finite()
    return dict(lower=str(x.lower().fmpq()), upper=str(x.upper().fmpq()), display=x.str(42,more=True))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--start',type=int,default=0)
    ap.add_argument('--stop',type=int,default=NR);ap.add_argument('--out',default=str(BASE.relative_to(ROOT)/'verification/mass_replay'))
    args=ap.parse_args();out=(ROOT/args.out).resolve();assert out.is_relative_to(ROOT)
    assert 0<=args.start<args.stop<=NR;out.mkdir(parents=True,exist_ok=True)
    dependencies=[Path(__file__),ROOT/'code/certify_local_circles_greedy.py',BASE/'PROOF.md',BASE.parent/'PROOF.md']
    hashes={str(p.relative_to(ROOT)):sha(p) for p in dependencies}
    assert hashes['code/certify_local_circles_greedy.py']=='38b0dd756ac0656f07bbf6889199810d9be31475e440acc08870499bcc72a16b'
    delta=arb(1)/64;R=arb(1)/2;alphas=list(map(arb,ALPHAS));started=time.monotonic()
    for row in range(args.start,args.stop):
        path=out/f'row_{row:03d}.json'
        if path.exists():
            previous=json.loads(path.read_text());assert previous['source_hashes']==hashes and previous['row']==row
            continue
        a=delta+(R-delta)*row/NR;b=delta+(R-delta)*(row+1)/NR;lr=(b/a).log()
        results=[]
        for j in range(M+1):
            phase=PI*j/(2*M);masses,tv,arcs,mids=angular_data(a,b,phase,N)
            assert masses[N:]==[-x for x in masses[:N]]
            right=masses[:N];sm=sum(right);sa=sum(map(abs,right))
            remaining=tv-arb(sa)/UNIT;assert remaining>=0
            V=remaining*lr;Vhat=up(V)
            signed=-phase.cos()*(b*b-a*a)/2-arb(sm)/UNIT*lr
            Qhat=up(abs(signed));assert abs(signed).lower()<=Vhat.upper()
            h=arb.min(Vhat,Qhat);old={};new={}
            for alpha,text in zip(alphas,ALPHAS):
                outside=(1+2*b)**alpha;inside=(2*b)**alpha
                old_a=outside*remaining*lr
                old_b=remaining*(outside*lr)
                old[text]=rec(old_a.union(old_b))
                bound=Vhat*inside+h*(outside-inside)
                assert bound>=0
                new[text]=rec(bound)
            results.append(dict(phase=j,masses=right,signed_integer_sum=sm,absolute_integer_sum=sa,
                angular_variation=rec(tv),variation=rec(V),signed_residual=rec(signed),old=old,new=new))
        data=dict(time_utc=datetime.now(timezone.utc).isoformat(),row=row,radial_left=rec(a),radial_right=rec(b),
            angles=N,radial_rows=NR,phase_intervals=M,integer_unit=UNIT,precision_bits=160,
            alphas=ALPHAS,phases=results,source_hashes=hashes,
            scope='Angular extraction and residual costs only; requires accepted-source identity and complete recombination')
        temporary=path.with_suffix('.pending');temporary.write_text(json.dumps(data,separators=(',',':'))+'\n');temporary.replace(path)
        print(data['time_utc'],'row',row+1,'/',NR,'seconds',round(time.monotonic()-started,2),flush=True)
    print('COMPLETE',args.start,args.stop,datetime.now(timezone.utc).isoformat(),flush=True)

if __name__=='__main__':main()
