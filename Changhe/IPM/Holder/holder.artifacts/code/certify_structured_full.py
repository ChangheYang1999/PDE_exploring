"""Full polygonal-witness enclosures, with rigorously regularized endpoint tails.
Proof: 05_team_audit/structured_endpoints/PROOF.md.
All quadrature uses Arb interval inclusions. Floating output is diagnostic only.
"""
from flint import arb, ctx
from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib, json, time
from certify_structured_layercake import line, circle, level, PI, RT
ctx.prec=160

def zero_to(v):
    return arb(0).union(v)

def regular_near(t,a):
    s=a+(RT-2)*t
    ans=((4*t**4).log1p()-2*arb(2).log())/PI
    ans+=4*(-line(s,arb(0),1+t)+line(s,1/RT,1+(2*t-a)/RT)
            +line(a,arb(0),t)+circle(PI/6,t,a)-circle(arb(0),t,a)
            -line(a+t/2,-1/RT,(2*t+a)/RT))
    return ans

def unit_log1p(z,N=18):
    r=arb(abs(z).upper())
    if not r<arb(1)/4:raise ValueError('log quotient outside series range')
    total=arb(0);power=arb(1)
    for k in range(N):
        total+=((-1)**k)*power/(k+1)
        power*=z
    err=r**N/((N+1)*(1-r))
    return total+arb(0,err.upper())

def unit_atan(z,N=18):
    r=arb(abs(z).upper())
    if not r<arb(1)/4:raise ValueError('atan quotient outside series range')
    total=arb(0);power=arb(1)
    for k in range(N):
        total+=((-1)**k)*power/(2*k+1)
        power*=z*z
    err=r**(2*N)/((2*N+1)*(1-r*r))
    return total+arb(0,err.upper())

def regular_tail(u,a):
    X=RT+(1-a/RT)*u
    A=(2*RT+(1-2*a/RT)*u)/(1+(RT-a*u/RT)**2)
    B=1/(1+X*(X-u))
    E=1/(4+(2*a-RT)*u)
    return 3/(4*PI)*A*unit_log1p(u*A)+RT/(2*PI)*B*unit_atan(u*B)+RT/PI*E*unit_atan(u*E)

def safe_decimal(value,upper=False,digits=10):
    endpoint=arb(value.upper() if upper else value.lower())*10**digits
    q=int((endpoint.ceil() if upper else endpoint.floor()).unique_fmpz())
    return f'{q//10**digits}.{q%10**digits:0{digits}d}'

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--alphas',default='1/2');p.add_argument('--a',default='1/2')
    p.add_argument('--step',type=int,default=2000)
    p.add_argument('--log-lo',type=int,default=-20);p.add_argument('--log-hi',type=int,default=20)
    p.add_argument('--out',default='data/structured_full_half.json')
    args=p.parse_args();astr=args.alphas.split(',');alphas=[arb(s) for s in astr];a=arb(args.a)
    assert a>0 and all(x>0 and x<1 for x in alphas) and args.step>0 and args.log_hi>args.log_lo
    t0=arb(args.log_lo).exp();u0=arb(-args.log_hi).exp()
    assert t0<a/(3-RT) and t0<a and t0<arb(1)/2
    assert 1/u0>2*a and 1/u0>2
    kval=regular_near(zero_to(t0),a);rval=regular_tail(zero_to(u0),a)
    if not kval.is_finite() or not rval.is_finite():raise ArithmeticError('nonfinite endpoint enclosure')
    h=arb(1)/args.step;n=(args.log_hi-args.log_lo)*args.step
    mids=[arb(0) for _ in alphas];wsteps=[(x*h).expm1() for x in alphas]
    start=time.monotonic()
    for i in range(n):
        s=arb(args.log_lo)+arb(i)/args.step
        j=level(s.exp().union((s+h).exp()),a)
        if not j.is_finite():raise ArithmeticError(('nonfinite middle',i))
        for k,alpha in enumerate(alphas):mids[k]+=j*(alpha*s).exp()*wsteps[k]
        if i and i%50000==0:print(i,n,round(time.monotonic()-start,2),flush=True)
    rows=[]
    for text,alpha,mid in zip(astr,alphas,mids):
        scale=arb(2)**(alpha-1)
        near=scale*(alpha*args.log_lo).exp()*(4/PI*(1/alpha-args.log_lo)+kval)
        far=scale*alpha*rval*(-args.log_hi*(1-alpha)).exp()/(1-alpha)
        mid*=scale;full=near+mid+far
        rows.append(dict(alpha=text,near=near.str(30),middle=mid.str(30),far=far.str(30),full=full.str(30),
                         safe_decimal_lower_10_places=safe_decimal(full),safe_decimal_upper_10_places=safe_decimal(full,True)))
    out=dict(time_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),a=args.a,precision_bits=ctx.prec,
             cells=n,cells_per_log_unit=args.step,log_lo=args.log_lo,log_hi=args.log_hi,
             regular_near_enclosure=kval.str(30),regular_tail_enclosure=rval.str(30),rows=rows,
             source_hashes={path.name:hashlib.sha256(path.read_bytes()).hexdigest() for path in [Path(__file__),Path(__file__).with_name('certify_structured_layercake.py')]},
             elapsed_seconds=time.monotonic()-start,conclusion='The full interval encloses the exact admissible witness I(alpha,a). Its lower endpoint bounds C_alpha and D_alpha from below; its upper endpoint is not an operator norm upper bound.')
    Path(args.out).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
