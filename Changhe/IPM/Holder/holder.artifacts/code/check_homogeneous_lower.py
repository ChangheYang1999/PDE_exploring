"""Arb enclosures for the homogeneous n=3 witness. No external computation."""
from flint import arb, fmpq, ctx
import mpmath as mp
import json
from pathlib import Path
from datetime import datetime, timezone
ctx.prec = 256
mp.mp.dps = 70
N = 120

def integral(a):
    # sin(beta*asin(v))/sqrt(1-v^2) = sum d_k v^(2k+1).
    # d_0=beta; d_1<0 and every subsequent d_k<0. Their
    # absolute values are <=beta for 2<beta<3. Since v<=1/2,
    # the omitted integral is enclosed in [-tail,0].
    beta = a+2
    d = beta
    total = arb(0)
    for k in range(N):
        t = a+2+2*k
        total += d*arb(2)**(-t)/t
        d *= ((k+1)**2-beta**2/4)/((k+1)*arb(fmpq(2*k+3,2)))
    t = a+2+2*N
    tail = beta*arb(fmpq(4,3))*arb(2)**(-t)/t
    return total + arb(-tail/2, tail/2)

rows=[]
for q in ['1/1000','1/100','1/20','1/10','1/5','3/10','1/2','3/4','9/10','99/100']:
    a=arb(fmpq(q)); j=integral(a)
    M=(a+1)*arb(2)**(a-1)*j/((a+2)*arb.pi()/6).cos()
    c=arb(2)**(1-a)*(M+arb(fmpq(1,4)))
    d=arb(2)**(1-a)*M
    ma=mp.mpf(str(fmpq(q).numerator))/int(fmpq(q).denominator)
    mj=mp.quad(lambda t:mp.sin((ma+2)*t)*mp.sin(t)**ma,[0,mp.pi/6])
    jmid=mp.mpf(j.mid().str(70, radius=False))
    assert abs(mj-jmid)<mp.mpf('1e-65')
    rows.append({'alpha':q,'J_interval':str(j),'M_interval':str(M),
                 'C_lower_interval':str(c),'D_lower_interval':str(d),
                 'mpmath_J_crosscheck':mp.nstr(mj,65)})
    print(q,c,d)
data={'created_utc':datetime.now(timezone.utc).isoformat(),'precision_bits':ctx.prec,
      'series_terms':N,'proof':'03_lower_bounds/homogeneous_degree_three/PROOF.md',
      'note':'Arb intervals prove these evaluations. The mpmath comparison is diagnostic only.',
      'rows':rows}
Path('data/homogeneous_lower_intervals.json').write_text(json.dumps(data,indent=2)+'\n')
