"""Partial compact-region interval integral, with exact rectangle coverage.
A chunk alone is not an operator upper bound. Use merge_reflection_chunks.py.
"""
from pathlib import Path
from datetime import datetime,timezone
from flint import arb,acb,ctx
import argparse,json,hashlib,time
ctx.prec=160
PI=arb.pi();ROOT=Path(__file__).resolve().parents[1]
def positive_power(value,alpha):
    if value>0:return value**alpha
    endpoint=arb(value.upper())
    if endpoint<=0:return arb(0)
    return arb(0).union(endpoint**alpha)
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--cells',type=int,default=768)
    parser.add_argument('--start',type=int,required=True)
    parser.add_argument('--stop',type=int,required=True)
    parser.add_argument('--phases',type=int,default=16)
    parser.add_argument('--out',required=True)
    args=parser.parse_args();n=args.cells;m=args.phases
    assert n>0 and m>0 and 0<=args.start<args.stop<=n
    source=ROOT/'data/explicit_bounds_intervals.json'
    old=json.loads(source.read_text())['rows'];alphas=[arb(row['alpha']) for row in old]
    phases=[((PI*k/(2*m)).cos(),(PI*k/(2*m)).sin()) for k in range(m+1)]
    sums=[[arb(0) for phase in phases] for alpha in alphas];began=time.monotonic()
    for row_index in range(args.start,args.stop):
        row_parameter=(arb(row_index)/n).union(arb(row_index+1)/n)
        middle_angle=PI*row_parameter/2
        middle_radius=middle_angle.sin();middle_cosine=middle_angle.cos()
        cross_radius=row_parameter/2
        for col_index in range(n):
            col_parameter=(arb(col_index)/n).union(arb(col_index+1)/n)
            theta=PI/2-middle_angle+middle_angle*col_parameter
            point=acb(middle_radius*theta.cos(),middle_radius*theta.sin())
            kernel=point/(PI*(point*point-arb(1)/4)**2)
            cross_angle=PI*col_parameter
            cross_point=acb(arb(1)/2+cross_radius*cross_angle.cos(),cross_radius*cross_angle.sin())
            cross_kernel=1/(2*PI*(cross_point+arb(1)/2)**2)
            middle_weight=middle_radius*middle_cosine*middle_angle*PI
            cross_weight=cross_radius*PI
            middle_costs=[(positive_power(2*abs(point.real),alpha),positive_power(2*abs(point.imag),alpha),positive_power(2*middle_radius,alpha)) for alpha in alphas]
            cross_costs=[(positive_power(2*abs(cross_point.real),alpha),positive_power(2*abs(cross_point.imag),alpha),positive_power(2*abs(cross_point),alpha)) for alpha in alphas]
            real_kernel=abs(kernel.real);imag_kernel=abs(kernel.imag)
            real_cross=abs(cross_kernel.real);imag_cross=abs(cross_kernel.imag)
            for phase_index,(cosine,sine) in enumerate(phases):
                ma=real_kernel*cosine;mb=imag_kernel*sine
                ca=real_cross*cosine;cb=imag_cross*sine
                for alpha_index in range(len(alphas)):
                    hc,vc,dc=middle_costs[alpha_index]
                    middle=arb.max(ma*hc+mb*(dc-hc),ma*(dc-vc)+mb*vc)
                    hc,vc,dc=cross_costs[alpha_index]
                    cross=arb.max(ca*hc+cb*(dc-hc),ca*(dc-vc)+cb*vc)
                    sums[alpha_index][phase_index]+=middle_weight*middle+cross_weight*cross
        if row_index%16==0:print(row_index,args.stop,round(time.monotonic()-began,2),flush=True)
    rows=[dict(alpha=oldrow['alpha'],regular_grid=[(value/(n*n)).str(40,more=True) for value in values]) for oldrow,values in zip(old,sums)]
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),precision_bits=ctx.prec,cells_per_axis=n,phase_intervals=m,
             row_start=args.start,row_stop=args.stop,rows=rows,elapsed_seconds=time.monotonic()-began,
             source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),input_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
             status='Partial regular integral only. Not an operator upper bound until exact row coverage is verified and chunks are summed.')
    (ROOT/args.out).write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
