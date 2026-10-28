"""Arb certification of a finite part of a nonnegative exact layer-cake integral.
The omitted parts are nonnegative. Output lower_bound is a bound for C and D.
No adaptive floating-point error estimates are used.
"""
from flint import arb, acb, ctx
from pathlib import Path
from datetime import datetime, timezone
import argparse, json, math, time, hashlib

ctx.prec=160
PI=arb.pi(); RT=arb(3).sqrt(); HALF=arb(1)/2

def sqrt_positive_range(v):
    lo=max(arb(0),arb(v.lower()))
    hi=max(arb(0),arb(v.upper()))
    return lo.sqrt().union(hi.sqrt())

def line(y,m,b):
    # Stable difference of two individual rational primitives.
    x=m*y+b; aa=1+m*m
    dprev=(x-1)**2+y*y
    if abs(2*x-1)<dprev/2:
        log_ratio=((2*x-1)/dprev).log1p()
    else:
        log_ratio=(x*x+y*y).log()-dprev.log()
    angle=acb(y*y+x*(x-1),y).arg()
    return (log_ratio/2+m*angle)/(2*PI*aa)

def circle(th,t,a):
    zz=acb(0,th).exp()
    def one(q):
        w=acb(q,a); cb=w.conjugate()
        return abs(w+t*zz).log()/2-((t/cb)*zz-(t*t/(cb*cb))*(cb*zz+t).log()).real/2
    return (one(0)-one(-1))/(2*PI)

def level(t,a):
    switch=a+(RT-2)*t
    high=arb.max(t,switch)
    pos=line(t,arb(0),1+t)-line(high,arb(0),1+t)
    pos+=line(high,1/RT,1+(2*t-a)/RT)
    neg=arb(0)
    if not (t>=a or t>=HALF):
        ell=arb.min(t,HALF)
        high=arb.max(t,a)
        neg+=line(high,arb(0),ell)-line(t,arb(0),ell)
    if not (t>=2*a or t>=1/RT):
        v=arb.max(arb(0),1-a/t)
        theta_y=v.asin()
        theta_width=sqrt_positive_range(4*t*t-1).atan()
        low=arb.min(PI/6,arb.max(theta_y,theta_width))
        neg+=circle(PI/6,t,a)-circle(low,t,a)
    low=arb.max(t,arb.max(a+t/2,a+2*t-RT/2))
    neg-=line(low,-1/RT,(2*t+a)/RT)
    return arb.max(4*(pos+neg),arb(0))

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--alpha',default='1/2');p.add_argument('--a',default='1/2')
    p.add_argument('--step',type=int,default=1000,help='cells per unit logarithmic radius')
    p.add_argument('--log-lo',type=int,default=-40);p.add_argument('--log-hi',type=int,default=40)
    p.add_argument('--out',default='data/structured_layercake_certificate.json')
    args=p.parse_args(); alpha=arb(args.alpha);a=arb(args.a)
    assert alpha>0 and alpha<1 and a>0 and args.step>0
    start=time.monotonic();n=(args.log_hi-args.log_lo)*args.step;total=arb(0)
    h=arb(1)/args.step;weighted_step=(alpha*h).expm1()
    lo=arb(args.log_lo).exp();ratio=h.exp();small=0
    for i in range(n):
        # Recompute endpoints from exact rational exponents to prevent recurrence widening.
        s=arb(args.log_lo)+arb(i)/args.step
        lo=s.exp();hi=(s+h).exp();tb=lo.union(hi)
        j=level(tb,a)
        weight=(alpha*s).exp()*weighted_step
        v=j*weight
        if not v.is_finite():raise ArithmeticError((i,str(tb),str(j)))
        total+=v
        if i and i%20000==0: print(i,n,'elapsed',round(time.monotonic()-start,2),flush=True)
    total*=arb(2)**(alpha-1)
    lower=arb(total.lower())
    # Decimal floor is below the rigorous lower endpoint, represented by exact integer arithmetic.
    safe_int=int((lower*10**10).floor().unique_fmpz())
    safe=f'{safe_int//10**10}.{safe_int%10**10:010d}'
    out=dict(time_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),alpha=args.alpha,a=args.a,
             source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),precision_bits=ctx.prec,cells=n,log_lo=args.log_lo,log_hi=args.log_hi,cells_per_log_unit=args.step,
             finite_integral=total.str(30),safe_decimal_lower_10_places=safe,
             conclusion='C_alpha and D_alpha are at least safe_decimal_lower_10_places. Omitted level tails are nonnegative.',
             elapsed_seconds=time.monotonic()-start)
    Path(args.out).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
