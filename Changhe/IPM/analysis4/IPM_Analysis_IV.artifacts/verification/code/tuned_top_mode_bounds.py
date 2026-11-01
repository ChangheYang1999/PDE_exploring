"""Interval beta radii and exact-root necessary bounds for tuned profiles."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction as F
import json,sys,time
sys.dont_write_bytecode=True
from flint import arb,ctx
from gmpy2 import mpq
from pure_cartesian_ball import ball,refine_root,Tuning,sine
ctx.prec=512;start=time.monotonic();root=Path('research/170_tuned_top_mode_obstruction')
text=lambda x:x.str(65,radius=True)
specs=[(2,5,'130_period_five_tuning/verification/irreducibility_sturm_checks.json','1.475398'),(1,2,'142_period_four_tuning/verification/root_response_certificates.json','2.151872'),(1,3,'154_period_six_tuning/verification/root_response_certificates.json','1.127213'),(4,9,'146_four_ninths_profiles/verification/algebraic_certificates.json','1.748618')]
rows=[]
for num,den,path,quoted in specs:
    p=Path('research')/path;raw=p.read_bytes();data=json.loads(raw)
    delta=arb(num)/den;d=delta/(1-delta);eta=4-delta;a=2/eta;beta=6/eta;nu=1/beta
    RH=4*d*((a*a.gamma()*beta.gamma()/(a+beta).gamma()).log()/a).exp()
    assert RH>arb(quoted)-arb('0.0000005') and RH<arb(quoted)+arb('0.0000005')
    polynomial=data.get('primitive_coefficients_ascending',data.get('primitive_coefficients'))
    rootrows=[]
    for index,item in enumerate(data['real_roots'],1):
        b,I=refine_root(polynomial,item['interval'],576)
        radius=((abs(b)/RH).log()/delta).exp()
        if (num,den,index)!=(4,9,5):assert radius<arb('0.16')
        else:assert radius>arb('1.1435') and radius<arb('1.1445')
        rootrows.append(dict(index=index,root_interval=I,b=text(b),necessary_radius=text(radius)))
    N=1500;hs=[arb(0),arb(1)];inv=[arb(0)]+[8/(eta*i+2) for i in range(1,N+1)]
    for n in range(2,N+1):
        value=arb(0)
        for i in range(1,(n+1)//2):
            j=n-i;value+=(inv[i]*j+inv[j]*i-2)*hs[i]*hs[j]
        if n%2==0:
            i=n//2;value+=(inv[i]*i-1)*hs[i]*hs[i]
        hs.append(value/(4*(n-1)*d))
    Rrec=hs[N-1]/hs[N]*((arb(N-1)/N).log()*(1+nu)).exp()
    row=dict(delta=f'{num}/{den}',R_H=text(RH),quoted_rounding_confirmed=True,roots=rootrows,source=path,source_sha256=sha256(raw).hexdigest(),scalar_order=N,corrected_ratio=text(Rrec),ratio_absolute_error=text(abs(Rrec-RH)),ratio_relative_error=text(abs(Rrec/RH-1)))
    rows.append(row);print(json.dumps({k:v for k,v in row.items() if k not in ['roots','source_sha256']}),flush=True)
# The low-order test does not cross a resonance and uses independent Cartesian differentiation.
solver=Tuning(2,9,4);f={1:sine(mpq(5,9),1,arb(1))+sine(mpq(5,9),3,arb(7)/10)};g={1:solver.poisson(f[1],1)}
delta=arb(4)/9;d=delta/(1-delta);eta=4-delta;hs=[arb(0),arb(1)];low=[]
for n in range(2,6):
    value=sum((8*(n-i)/(eta*i+2)-1)*hs[i]*hs[n-i] for i in range(1,n))/(4*(n-1)*d)
    hs.append(value);f[n]=solver.order(n,f,g);g[n]=solver.poisson(f[n],n)
    top=f[n].sine(4*n-1);predicted=(-1)**(n-1)*(arb(7)/10)**n*hs[n]
    assert top.overlaps(predicted)
    low.append(dict(n=n,cartesian=text(top),scalar=text(predicted)))
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,arithmetic_bits=ctx.prec,rows=rows,low_order_checks=low,actual_elapsed_s=time.monotonic()-start)
(root/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
for name in ['tuned_top_mode_bounds.py','pure_cartesian_ball.py']:(root/'sources'/name).write_bytes(Path('code',name).read_bytes())
(root/'sources/lead_top_mode_bracket.py').write_bytes(Path('../a4-lead/code/review/top_mode_bracket.py').read_bytes())
print(json.dumps(dict(all_checks_pass=True,actual_elapsed_s=result['actual_elapsed_s'])),flush=True)
