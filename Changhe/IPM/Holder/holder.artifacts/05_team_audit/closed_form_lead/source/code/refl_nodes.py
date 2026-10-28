"""Reflection-orbit upper plan (Theorem 3.4) at an arbitrary list of rational exponents.
Copy of the verifier's certify_reflection_orbits.py (version 2); the only changes are the --alphas option and the
inline interval evaluation of a2 and a3 by the formulas of check_explicit_bounds.py (same series, same tail bound).
"""
from pathlib import Path
from datetime import datetime,timezone
from flint import arb,acb,ctx,fmpq
from fractions import Fraction
import json,argparse,hashlib,time
ctx.prec=160
PI=arb.pi()
NSER=120
def positive_integral(a,p):
    # int_0^(1/2) s^(a+1+2p)/sqrt(1-s^2) ds, positive series with explicit tail
    e=a+2+2*p;coeff=arb(1);total=arb(0)
    for k in range(NSER):
        total+=coeff*arb(2)**(-(e+2*k))/(e+2*k);coeff*=arb(2*k+1)/arb(2*k+2)
    tail=arb(4)/3*arb(2)**(-(e+2*NSER))/(e+2*NSER)
    return total+arb(tail.upper()/2,tail.upper()/2)
def a2_of(a):return arb(2)**(1+a/2)/(PI*(a+2))
def a3_of(a):return 3*arb(2)**a/PI*(3*positive_integral(a,0)-4*positive_integral(a,1))
def pospow(x,a):
    if x>0:return x**a
    upper=arb(x.upper())
    if upper<=0:return arb(0)
    return arb(0).union(upper**a)
def safeupper(x,digits=10):
    q=int((arb(x.upper())*10**digits).ceil().unique_fmpz())
    return f'{q//10**digits}.{q%10**digits:0{digits}d}'
def main():
    p=argparse.ArgumentParser();p.add_argument('--cells',type=int,default=128);p.add_argument('--phases',type=int,default=16)
    p.add_argument('--alphas',required=True);p.add_argument('--out',required=True);args=p.parse_args()
    n=args.cells;m=args.phases;assert n>0 and m>0
    texts=args.alphas.split(',');fr=[Fraction(t) for t in texts];assert all(0<f<1 for f in fr)
    aa=[arb(fmpq(f.numerator,f.denominator)) for f in fr]
    cs=[(PI*j/(2*m)).cos() for j in range(m+1)];ss=[(PI*j/(2*m)).sin() for j in range(m+1)]
    accum=[[arb(0) for j in range(m+1)] for a in aa]; started=time.monotonic()
    for i in range(n):
        iu=(arb(i)/n).union(arb(i+1)/n)
        v=PI*iu/2;r=v.sin();cv=v.cos();s=iu/2
        for j in range(n):
            ju=(arb(j)/n).union(arb(j+1)/n)
            theta=PI/2-v+v*ju
            w=acb(r*theta.cos(),r*theta.sin()); g=w/(PI*(w*w-arb(1)/4)**2)
            qtheta=PI*ju;wq=acb(arb(1)/2+s*qtheta.cos(),s*qtheta.sin());q=1/(2*PI*(wq+arb(1)/2)**2)
            # Jacobians include factors 2 from the symmetry reductions.
            weightmid=r*cv*v*PI
            weightcross=s*PI
            midpowers=[(pospow(2*abs(w.real),a),pospow(2*abs(w.imag),a),pospow(2*r,a)) for a in aa]
            crosspowers=[(pospow(2*abs(wq.real),a),pospow(2*abs(wq.imag),a),pospow(2*abs(wq),a)) for a in aa]
            gr=abs(g.real);gi=abs(g.imag);qr=abs(q.real);qi=abs(q.imag)
            for k,(c,si) in enumerate(zip(cs,ss)):
                am=gr*c;bm=gi*si;aq=qr*c;bq=qi*si
                for l in range(len(aa)):
                    hc,vc,dcost=midpowers[l];mid=arb.max(am*hc+bm*(dcost-hc),am*(dcost-vc)+bm*vc)
                    hc,vc,dcost=crosspowers[l];cross=arb.max(aq*hc+bq*(dcost-hc),aq*(dcost-vc)+bq*vc)
                    accum[l][k]+=weightmid*mid+weightcross*cross
        if i%16==0: print(i,n,round(time.monotonic()-started,2),flush=True)
    rows=[];N=32
    for text,a,values in zip(texts,aa,accum):
        vals=[val/(n*n) for val in values]; mx=vals[0]
        for value in vals[1:]:mx=arb.max(mx,value)
        reg=mx/(PI/(4*m)).cos()
        a2=a2_of(a);a3=a3_of(a)
        tail=2*a3/(1-a)
        for k in range(1,N):
            h=2*k+3;ak=(2*h*(PI/(2*h)).cos()/(h*h-1))**a/PI
            tail+=2*(k+1)*arb(4)**(-k)*ak/(2*k+1-a)
        err=(1+arb(1)/N)/PI*arb(4)**(-N)/(1-arb(1)/4)
        tail+=arb(0).union(err)
        near=2*a2*arb(2)**(-a)/a
        A=((a+2)/2).gamma()/(2*PI.sqrt()*((a+3)/2).gamma())
        dc=2*A*arb(2)**(-a)/a+arb(1)/2+tail+reg
        cc=near+tail+reg
        assert cc.is_finite() and dc.is_finite()
        rows.append(dict(alpha=text,a2=a2.str(30,more=True),a3=a3.str(30,more=True),regular_grid=[z.str(30,more=True) for z in vals],regular_all_phases=reg.str(30,more=True),
                         near=near.str(30,more=True),harmonic_tail=tail.str(30,more=True),upper_C=cc.str(30,more=True),upper_D=dc.str(30,more=True),
                         safe_upper_C=safeupper(cc),safe_upper_D=safeupper(dc)))
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),precision_bits=ctx.prec,cells_per_axis=n,phase_intervals=m,
             method='four-point reflection-orbit transport (Theorem 3.4) at listed nodes',phase_inflation=(1/(PI/(4*m)).cos()).str(30,more=True),tail_terms=N,rows=rows,elapsed_seconds=time.monotonic()-started,
             source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             conclusion='Upper endpoints bound the Theorem 3.4 right side U(alpha), hence C_alpha (upper_C) and D_alpha (upper_D).')
    Path(args.out).write_text(json.dumps(out,indent=2)+'\n')
    for row in rows:print(row['alpha'],row['safe_upper_C'],row['safe_upper_D'],flush=True)
if __name__=='__main__':main()
