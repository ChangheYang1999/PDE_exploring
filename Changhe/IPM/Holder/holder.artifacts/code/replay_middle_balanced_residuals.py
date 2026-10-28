"""Replay the original middle-cell extraction and sharpen only its residual.

No transport optimizer is called. Original 160-bit cell masses, variation and
integer unit are preserved. Each completed row is immutable and checkpointed.
"""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
import argparse, hashlib, json, time
from flint import arb, ctx
from certify_middle_chunks import bin_data
from certify_far_circles import cell_measures
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'08_improved_upper_bounds/middle_circle_transport/balanced_residual'
N,NR,M,UNIT=512,512,16,2**44
ALPHAS=['3/10','1/2','3/4','9/10']
ctx.prec=160
PI=arb.pi()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rec(x):
    assert x.is_finite()
    return dict(lower=str(x.lower().fmpq()),upper=str(x.upper().fmpq()),display=x.str(42,more=True))
def uq(x):return Q(str(x.upper().fmpq()))
def ar(x):return arb(str(x))
def signed_mass(t,ss):
    r=t.sin();s=r*r
    j=(1+8*s).log()+8*s*(1-4*s)/(1+8*s)
    return -2*r*t.cos()*ss*j/PI

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--start',type=int,default=0)
    ap.add_argument('--stop',type=int,default=NR);ap.add_argument('--subdivisions',type=int,default=8)
    ap.add_argument('--out',default=str(BASE.relative_to(ROOT)/'verification/mass_replay'))
    args=ap.parse_args();out=(ROOT/args.out).resolve();assert out.is_relative_to(ROOT)
    assert 0<=args.start<args.stop<=NR and args.subdivisions>=1
    out.mkdir(parents=True,exist_ok=True)
    dependencies=[Path(__file__),ROOT/'code/certify_middle_chunks.py',ROOT/'code/certify_far_circles.py',BASE/'PROOF.md',BASE.parent/'PROOF.md']
    hashes={str(p.relative_to(ROOT)):sha(p) for p in dependencies}
    original=json.loads((ROOT/'data/middle_circle_certificate_n512.json').read_text())
    for name in ['code/certify_middle_chunks.py','code/certify_far_circles.py']:
        assert hashes[name]==original['source_hashes'][name]
    phases=[((PI*j/(2*M)).cos(),(PI*j/(2*M)).sin()) for j in range(M+1)]
    alphas=list(map(arb,ALPHAS));started=time.monotonic()
    for row in range(args.start,args.stop):
        path=out/f'row_{row:03d}.json'
        if path.exists():
            d=json.loads(path.read_text());assert d['row']==row and d['source_hashes']==hashes and d['subdivisions']==args.subdivisions
            continue
        lo,hi,rmax,values,M1,M2=bin_data(row,NR,N);results=[]
        sub=[]
        for k in range(args.subdivisions):
            left=lo+(hi-lo)*k/args.subdivisions;right=lo+(hi-lo)*(k+1)/args.subdivisions
            t=left.union(right);r=arb.min(arb(1),arb(right.sin().upper()))
            costs=[]
            for a in alphas:
                A=uq((2*r*r)**a);B=max(A,uq((2*r)**a))
                costs.append((A,B))
            sub.append((t,right-left,costs))
        for j,(cc,ss) in enumerate(phases):
            masses,tv=cell_measures(values,cc,ss,M1,M2,arb(2)/N,UNIT)
            rightm=masses[:N];S=sum(rightm);V=tv-arb(sum(map(abs,rightm)))/UNIT
            assert V>=0;tau=uq(V);old={};new={};subrecords=[]
            accum=[arb(0) for _ in ALPHAS]
            for t,width,costs in sub:
                q=signed_mass(t,ss)-arb(S)/UNIT;h=min(tau,uq(abs(q)));assert 0<=h<=tau
                subrecords.append(dict(signed_residual=rec(q),used_unbalanced_mass=str(h)))
                for k,(A,B) in enumerate(costs):
                    accum[k]+=(ar(tau-h)*ar(A)+ar(h)*ar(B))*width
            for text,a,newcost in zip(ALPHAS,alphas,accum):
                oldcost=(2*rmax)**a*V*(hi-lo)
                assert newcost>=0
                # Either complete bound is valid. Keep the better upper endpoint.
                selected=min(uq(newcost),uq(oldcost))
                old[text]=rec(oldcost);new[text]=dict(upper=str(selected),computed=rec(newcost))
            results.append(dict(phase=j,masses=rightm,signed_integer_sum=S,absolute_integer_sum=sum(map(abs,rightm)),
                variation=rec(V),old=old,new=new,subintervals=subrecords))
        data=dict(time_utc=datetime.now(timezone.utc).isoformat(),row=row,radial_left=rec(lo),radial_right=rec(hi),
            angles=N,radial_rows=NR,phase_intervals=M,integer_unit=UNIT,precision_bits=160,subdivisions=args.subdivisions,
            alphas=ALPHAS,phases=results,source_hashes=hashes,
            scope='Original middle extraction and residual replacement only; analytic and full-operator acceptance are separate')
        temporary=path.with_suffix('.pending');temporary.write_text(json.dumps(data,separators=(',',':'))+'\n');temporary.replace(path)
        print(data['time_utc'],'row',row+1,'/',NR,'seconds',round(time.monotonic()-started,2),flush=True)
    print('COMPLETE',args.start,args.stop,datetime.now(timezone.utc).isoformat(),flush=True)
if __name__=='__main__':main()
