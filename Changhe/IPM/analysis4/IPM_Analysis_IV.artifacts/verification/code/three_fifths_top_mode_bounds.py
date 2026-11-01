"""Directed necessary-radius constants and independent top recurrence checks."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,sys,time
sys.dont_write_bytecode=True
from flint import arb,ctx
from gmpy2 import mpq
from pure_cartesian_ball import refine_root,Tuning,sine
from certified_initial_majorants import pack
ROOT=Path('research/222_three_fifths_top_mode_bounds')
def text(x):return x.str(60,radius=True)
def main():
    start=time.monotonic();ctx.prec=512
    source=Path('research/200_three_fifths_tuning/verification/obstruction_checks.json');raw=source.read_bytes();data=json.loads(raw);assert data['all_checks_pass']
    d=arb(3)/2;delta=arb(3)/5;eta=arb(17)/5;a=arb(10)/17;beta=arb(30)/17;nu=1/beta
    RH=4*d*((a*a.gamma()*beta.gamma()/(a+beta).gamma()).log()/a).exp()
    assert RH>arb('3.1373305') and RH<arb('3.1373315')
    roots=[]
    for index,(item,quoted) in enumerate(zip(data['real_roots'],['0.0016','0.0037','0.026','0.062']),1):
        b,I=refine_root(data['primitive_coefficients'],item['interval'],576)
        radius=((abs(b)/RH).log()/delta).exp()
        lower_integer=int((radius.lower()*10**9).floor().unique_fmpz())
        lower=arb(lower_integer)/10**9
        assert lower<radius
        roots.append(dict(index=index,root_interval=I,root=text(b),necessary_radius=text(radius),radius_ball=pack(radius),quoted_decimal=quoted,quoted_is_strict_lower_bound=bool(arb(quoted)<radius),quoted_exceeds_exact_bound=bool(arb(quoted)>radius),safe_decimal_lower_bound=f'{lower_integer//10**9}.{lower_integer%10**9:09d}'))
    hs=[arb(0),arb(1)];N=1500;inv=[arb(0)]+[8/(eta*i+2) for i in range(1,N+1)]
    for n in range(2,N+1):
        value=arb(0)
        for i in range(1,(n+1)//2):
            j=n-i;value+=(inv[i]*j+inv[j]*i-2)*hs[i]*hs[j]
        if n%2==0:
            i=n//2;value+=(inv[i]*i-1)*hs[i]*hs[i]
        hs.append(value/(4*(n-1)*d))
    corrected=hs[N-1]/hs[N]*((arb(N-1)/N).log()*(1+nu)).exp()
    solver=Tuning(3,10,4);f={1:sine(mpq(2,5),1,arb(1))+sine(mpq(2,5),3,arb(7)/10)};g={1:solver.poisson(f[1],1)};low=[]
    for n in range(2,9):
        f[n]=solver.order(n,f,g);g[n]=solver.poisson(f[n],n)
        observed=f[n].sine(4*n-1);predicted=(-1)**(n-1)*(arb(7)/10)**n*hs[n];assert observed.overlaps(predicted)
        low.append(dict(n=n,observed=text(observed),predicted=text(predicted)))
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,bits=512,R_H=text(RH),R_H_ball=pack(RH),root_source=dict(path=str(source),sha256=sha256(raw).hexdigest()),roots=roots,scalar_order=N,corrected_ratio=text(corrected),ratio_relative_error=text(abs(corrected/RH-1)),cartesian_top_checks=low,scope='The displayed lower bounds are necessary only; no full-series growth estimate.',actual_elapsed_s=time.monotonic()-start)
    (ROOT/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
    for name in ['three_fifths_top_mode_bounds.py','pure_cartesian_ball.py','certified_initial_majorants.py']:(ROOT/'sources'/name).write_bytes(Path('code',name).read_bytes())
    print(json.dumps(result),flush=True)
if __name__=='__main__':main()
