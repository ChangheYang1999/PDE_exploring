"""Outward interval Riemann enclosures of the exact gated-witness integrals.

All weights are integrated exactly with Arb. The cell evaluations enclose the
whole continuous integrand, including the removable values at zero.
"""
import argparse
import json
from datetime import datetime,timezone
from pathlib import Path
from flint import arb, fmpq, ctx

ctx.prec=160
pi=arb.pi()
k=1/arb(2).sqrt()
q=arb(2).sqrt()-1

def H(s,b,r):
    d0=r*r+(s*r+b)**2
    d1=(r+1)**2+(s*r+b)**2
    return s*(d0/d1).log()/4+(((2*r+s*b)/b).atan()-((2*r+1+s*b)/(b-s)).atan())/2

def Ksmall(t):
    c=k*t; a=(1-t)/2
    p0=4*a**4+c**4
    p1=((1-a)**2+a*a+c*c)**2-4*a*a*c*c
    val=arb(2).log()+(1-c**4).log()/2+(p0/p1).log()/4
    val+=(-(c/(1-t+c)).atan()+(c/(1-t-c)).atan()
          +((t-c)/(1+c)).atan()+((t+c)/(1-c)).atan())/2
    return val/pi

def Klarge(t):
    c=k*t; ell=(t-1)/2
    val=(1+c*c).log()/2-arb(3)/2*c.log()+(1+c).log()/2-H(-1,c,ell)
    return (val+2*t.log())/pi

def decreasing_ratio(z,kind):
    lo=z.lower(); hi=z.upper()
    # The mathematical input is nonnegative. A cell containing zero may have
    # an outward-rounding fringe below zero, which is safely intersected away.
    if lo<0: lo=arb(0)
    assert hi>=0
    def value(x):
        if x==0: return arb(1)
        return (1+x).log()/x if kind=='log' else x.atan()/x
    return value(hi).union(value(lo))

def R(s):
    d=(1-s)**2/4+((1-s)/2+k)**2
    a=(1+2*k-s)/(2+2*k-(1+2*k)*s)
    return (decreasing_ratio(s/d,'log')/(4*d)
            +a*decreasing_ratio(s*a,'atan')/2
            +decreasing_ratio(s/k,'log')/(2*k))/pi

def cell(left,right):
    return arb((left+right)/2,(right-left)/2)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--cells',type=int,default=8192)
    parser.add_argument('--out',default='data/gated_lower_intervals.json')
    args=parser.parse_args(); n=args.cells
    samples=[(1,1000),(1,100),(1,50),(1,20),(1,10),(1,5),(1,4),(3,10),
             (2,5),(1,2),(3,5),(7,10),(3,4),(4,5),(9,10),(19,20),(99,100)]
    aa=[arb(fmpq(p,d)) for p,d in samples]
    caps=[2/(pi*a) for a in aa]
    tails=[arb(0) for a in aa]
    for left,right,fun in [(arb(0),q,Ksmall),(q,arb(1),Klarge)]:
        for i in range(n):
            x0=left+(right-left)*i/n
            x1=left+(right-left)*(i+1)/n
            f=fun(cell(x0,x1))
            assert f.is_finite()
            for j,a in enumerate(aa):
                caps[j]+=(x1**a-x0**a)*f
        print('Completed K segment',left,right,flush=True)
    for i in range(n):
        x0=arb(fmpq(i,n));x1=arb(fmpq(i+1,n))
        f=R(cell(x0,x1)); assert f.is_finite()
        for j,a in enumerate(aa):
            tails[j]+=a/(1-a)*(x1**(1-a)-x0**(1-a))*f
    rows=[]
    for (p,d),a,cap,tail in zip(samples,aa,caps,tails):
        total=cap+tail
        row={'alpha':f'{p}/{d}','capped_lower_integral':str(cap),'tail_integral':str(tail),
             'uncapped_lower_integral':str(total),'uncapped_lower_endpoint':total.lower().str(18,radius=False),
             'uncapped_upper_endpoint':total.upper().str(18,radius=False),
             'safe_decimal_lower_10_places':str(fmpq((total.lower()*10**10).floor().unique_fmpz(),10**10))}
        rows.append(row);print(row,flush=True)
    out={'generated_utc':datetime.now(timezone.utc).isoformat(),'precision_bits':ctx.prec,
         'cells_per_segment':n,'segments':3,'status':'Certified integrals of explicit admissible witnesses, not exact operator norms.',
         'method':'Outward interval Riemann sums with exact positive power weights. See gated_witness/PROOF.md.',
         'rows':rows}
    Path(args.out).write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':main()
