"""Replay every compact nodal quadrature, with bounded radial chunks.

The positive rectangle formulas are those already audited in V037. This
separate implementation combines all 59 exponents in each geometry pass.
Exact row coverage and outward endpoint sums are checked separately.
"""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
import argparse, hashlib, json, time
from flint import arb, acb, ctx, fmpq
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'09_uniform_comparison/lead_certificate'
OUT=BASE/'verification/recomputed'
ctx.prec=160

def power(t,a):
    if t>0:return t**a
    if t.upper()<=0:return arb(0)
    return arb(0).union(arb(t.upper())**a)

def interval(v):
    return [v.lower().str(60,more=True),v.upper().str(60,more=True)]

def main():
    p=argparse.ArgumentParser();p.add_argument('--start',type=int,required=True);p.add_argument('--stop',type=int,required=True);args=p.parse_args()
    n=384;m=16;assert 0<=args.start<args.stop<=n
    texts=[];inputs=['upper_n384.json','upper_n384_b.json']
    for name in inputs:
        d=json.loads((BASE/'data'/name).read_text());assert d['cells_per_axis']==n and d['phase_intervals']==m
        texts.extend(r['alpha'] for r in d['rows'])
    assert len(texts)==len(set(map(Fraction,texts)))==59
    texts.sort(key=Fraction)
    aa=[arb(fmpq(Fraction(t).numerator,Fraction(t).denominator)) for t in texts]
    pi=arb.pi(); phases=[((pi*k/(2*m)).cos(),(pi*k/(2*m)).sin()) for k in range(m+1)]
    sums=[[arb(0) for _ in phases] for _ in aa];started=time.monotonic()
    for i in range(args.start,args.stop):
        unit=(arb(i)/n).union(arb(i+1)/n);v=pi*unit/2;r=v.sin();cv=v.cos();s=unit/2
        for j in range(n):
            unit2=(arb(j)/n).union(arb(j+1)/n);theta=pi/2-v+v*unit2
            w=acb(r*theta.cos(),r*theta.sin());g=w/(pi*(w*w-arb(1)/4)**2)
            qt=pi*unit2;wq=acb(arb(1)/2+s*qt.cos(),s*qt.sin());q=1/(2*pi*(wq+arb(1)/2)**2)
            wm=r*cv*v*pi;wc=s*pi
            mp=[(power(2*abs(w.real),a),power(2*abs(w.imag),a),power(2*r,a)) for a in aa]
            cp=[(power(2*abs(wq.real),a),power(2*abs(wq.imag),a),power(2*abs(wq),a)) for a in aa]
            gr=abs(g.real);gi=abs(g.imag);qr=abs(q.real);qi=abs(q.imag)
            for k,(c,si) in enumerate(phases):
                am=gr*c;bm=gi*si;aq=qr*c;bq=qi*si
                for ell in range(len(aa)):
                    hc,vc,dc=mp[ell];mid=arb.max(am*hc+bm*(dc-hc),am*(dc-vc)+bm*vc)
                    hc,vc,dc=cp[ell];cross=arb.max(aq*hc+bq*(dc-hc),aq*(dc-vc)+bq*vc)
                    sums[ell][k]+=wm*mid+wc*cross
        if (i-args.start)%8==0:print(i,n,round(time.monotonic()-started,3),flush=True)
    result=dict(time_utc=datetime.now(timezone.utc).isoformat(),row_start=args.start,row_stop=args.stop,cells_per_axis=n,phase_intervals=m,precision_bits=ctx.prec,
        rows=[dict(alpha=t,regular_grid_endpoints=[interval(z/(n*n)) for z in vals]) for t,vals in zip(texts,sums)],elapsed_seconds=time.monotonic()-started,
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),input_sha256={name:hashlib.sha256((BASE/'data'/name).read_bytes()).hexdigest() for name in inputs})
    target=OUT/f'upper_r{args.start}_{args.stop}.json';target.write_text(json.dumps(result,indent=2)+'\n');print(target,flush=True)
if __name__=='__main__':main()
