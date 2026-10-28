"""Only the smooth other-pole kernels in the two local disks.
Same exact four-point cost as the already audited reflection certificate.
"""
from pathlib import Path
from datetime import datetime,timezone
from flint import arb,acb,ctx
from certify_reflection_chunk import positive_power
from certify_far_circles import upper_decimal
import argparse,json,hashlib,time
ctx.prec=160
PI=arb.pi();ROOT=Path(__file__).resolve().parents[1]
def main():
    p=argparse.ArgumentParser();p.add_argument('--cells',type=int,default=512);p.add_argument('--phases',type=int,default=16)
    p.add_argument('--alphas',default='1/2');p.add_argument('--out',default='data/cross_disk_certificate.json');args=p.parse_args()
    n=args.cells;m=args.phases;assert n>=8 and m>0
    texts=args.alphas.split(',');alphas=[arb(a) for a in texts]
    phases=[((PI*j/(2*m)).cos(),(PI*j/(2*m)).sin()) for j in range(m+1)]
    sums=[[arb(0) for _ in phases] for _ in alphas];started=time.monotonic()
    for i in range(n):
        radius=(arb(i)/(2*n)).union(arb(i+1)/(2*n))
        for j in range(n):
            theta=(PI*j/n).union(PI*(j+1)/n)
            z=acb(arb(1)/2+radius*theta.cos(),radius*theta.sin())
            kernel=1/(2*PI*(z+arb(1)/2)**2)
            kr=abs(kernel.real);ki=abs(kernel.imag)
            for ai,alpha in enumerate(alphas):
                hc=positive_power(2*abs(z.real),alpha);vc=positive_power(2*abs(z.imag),alpha);dc=positive_power(2*abs(z),alpha)
                for pi,(cc,ss) in enumerate(phases):
                    aa=kr*cc;bb=ki*ss
                    value=arb.max(aa*hc+bb*(dc-hc),aa*(dc-vc)+bb*vc)
                    sums[ai][pi]+=radius*PI*value
        if i%32==0:print(i,n,round(time.monotonic()-started,2),flush=True)
    rows=[dict(alpha=text,cross_phase_intervals=[(v/(n*n)).str(36,more=True) for v in values],safe_cross_upper=[upper_decimal(v/(n*n)) for v in values]) for text,values in zip(texts,sums)]
    paths=[Path(__file__),ROOT/'code/certify_reflection_chunk.py',ROOT/'code/certify_far_circles.py']
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),precision_bits=ctx.prec,cells_per_axis=n,phase_intervals=m,rows=rows,elapsed_seconds=time.monotonic()-started,source_hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},status='Smooth cross-disk remainder only; combine with all other regions for an operator upper bound.')
    (ROOT/args.out).write_text(json.dumps(out,indent=2)+'\n')
    for row in rows:print(row['alpha'],row['safe_cross_upper'],flush=True)
if __name__=='__main__':main()
