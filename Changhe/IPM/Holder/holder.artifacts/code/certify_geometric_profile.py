"""Arb covering certificate for the exact projection-profile two-point quotient."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
from flint import arb,ctx
import argparse,json,time,hashlib
ctx.prec=160;ROOT=Path(__file__).resolve().parents[1];PI=arb.pi()
def A(x):return arb(x.numerator)/x.denominator if isinstance(x,Fraction) else arb(x)
def up(x):return arb(x.upper())
def lo(x):return arb(x.lower())
def nonnegative(x):return arb.max(arb(0),x)

def bound(box,alpha):
    ul,uh,al,ah,bl,bh=map(A,box)
    tlo=PI*(al+bl)
    if tlo>=PI/2:return arb(1)
    u=ul.union(uh);R=u**alpha;k=1/(1-alpha)
    coarseA=(1-u)**(-alpha)
    coarseB=((1+R**k)/2)**(1/k)+(1-R)/(2*(1-u)**alpha)
    cb=arb.min(up(coarseA),up(coarseB))
    sa=arb.min(arb(1),up((2*PI*al.union(ah)).sin()))
    sb=arb.min(arb(1),up((2*PI*bl.union(bh)).sin()))
    num=arb.min(arb(1),up((1+sa**alpha-ul**alpha*(1-sb**alpha))/2))
    ct=tlo.cos();st=tlo.sin()
    if uh<ct:ds=(uh-ct)**2+st**2
    elif ul>ct:ds=(ul-ct)**2+st**2
    else:ds=st**2
    simple=(1-uh)**2+4*ul*(tlo/2).sin()**2
    ds=arb.max(nonnegative(lo(ds)),nonnegative(lo(simple)))
    if ds>0:cb=arb.min(cb,up(num/ds**(alpha/2)))
    return cb

def main():
    p=argparse.ArgumentParser();p.add_argument('--alpha',required=True);p.add_argument('--target',required=True);p.add_argument('--out',required=True);p.add_argument('--max-boxes',type=int,default=2000000);args=p.parse_args()
    alpha=arb(args.alpha);target=arb(args.target);assert 0<alpha<=arb(1)/2 and target>1
    eps=Fraction(1,1000000);e=A(eps);k=1/(1-alpha);rs=(1-e)**alpha;c=alpha/(1-e)**(1-alpha)
    left=(1-e)**(-alpha);right=1+(k-1)*c*c*e*e/(8*rs)+c*e**(1-alpha)/2
    assert left<target and right<target
    stack=[(eps,1-eps,Fraction(0),Fraction(1,2),Fraction(0),Fraction(1,2))]
    checked=0;accepted=0;maxdepth=0;started=time.monotonic();depths=[0];worst=arb(1)
    while stack:
        box=stack.pop();depth=depths.pop();v=bound(box,alpha);checked+=1
        if v<=target:
            accepted+=1;worst=arb.max(worst,v);maxdepth=max(maxdepth,depth)
        else:
            assert checked<args.max_boxes,('box limit',checked,len(stack),box,v)
            widths=[box[1]-box[0],2*(box[3]-box[2]),2*(box[5]-box[4])]
            d=max(range(3),key=lambda j:widths[j]);m=(box[2*d]+box[2*d+1])/2
            child1=list(box);child2=list(box);child1[2*d+1]=m;child2[2*d]=m
            stack.extend([tuple(child1),tuple(child2)]);depths.extend([depth+1,depth+1])
        if checked%10000==0:print(checked,accepted,len(stack),round(time.monotonic()-started,2),flush=True)
    paths=['code/certify_geometric_profile.py','07_diagonal_identity_term/geometric_profile_constant/PROOF.md','07_diagonal_identity_term/refined_profile_constant/PROOF.md','07_diagonal_identity_term/extended_range/PROOF.md']
    paths=[p for p in paths if (ROOT/p).exists()]
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),alpha=args.alpha,certified_upper=args.target,precision_bits=ctx.prec,epsilon=str(eps),checked_boxes=checked,accepted_boxes=accepted,maxdepth=maxdepth,largest_accepted_bound=worst.str(40,more=True),left_endpoint=left.str(40,more=True),right_endpoint=right.str(40,more=True),elapsed_seconds=time.monotonic()-started,source_hashes={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},status='Complete exact rational covering; every accepted Arb upper bound is at most target')
    (ROOT/args.out).write_text(json.dumps(out,indent=2)+'\n');print(out,flush=True)
if __name__=='__main__':main()
