"""Certify the complete two-cusp self integral and moment cross bound."""
from flint import arb, fmpq, ctx
from pathlib import Path
from datetime import datetime,timezone
import mpmath as mp
import math,json
ctx.prec=256
mp.mp.dps=70
N=180
q=arb(2).sqrt()-1
P=arb(fmpq(1,15))+(arb(fmpq(15,16))).log()/4
rows=[]
for ar in ['1/1000','1/100','1/20','1/10','1/5','3/10','1/2','3/4','9/10','99/100']:
    aq=fmpq(ar);a=arb(aq)
    # Positive finite sum; all omitted terms are enclosed by the proof's tail.
    total=arb(0)
    for n in range(N):
        inner=sum((arb((n-k+1)*(n-k+2))/2/(a+k) for k in range(n+1)),arb(0))
        total+=q**(a+n+2)/(a+n+2)*inner
    S0=4/arb.pi()*total
    tail=4/(arb.pi()*a)*math.comb(N+3,3)*q**(a+N+2)/(a+N+2)/(1-q*arb(fmpq(N+4,N+1)))
    S=S0+arb(tail/2,tail/2)
    lower=2*S-2*q**a/arb.pi()*P
    ma=mp.mpf(int(aq.numerator))/int(aq.denominator)
    def integrand(t):
        b=mp.sin(t)/(1+mp.sin(t))
        return mp.sin(2*t)*(b**ma/ma+b**(ma+1)/(ma+1)*mp.hyp2f1(1,ma+1,ma+2,b))
    ms=2/mp.pi*mp.quad(integrand,[0,mp.pi/4])
    assert abs(mp.mpf(S.mid().str(70,radius=False))-ms)<mp.mpf('1e-60')
    rows.append({'alpha':ar,'S_interval':str(S),'cross_abs_upper_interval':str(q**a/arb.pi()*P),
                 'C_and_D_lower_interval':str(lower),'tail_upper_interval':str(tail),
                 'mpmath_S_crosscheck':mp.nstr(ms,65)})
    print(ar,lower)
Path('data/cusp_refinement_intervals.json').write_text(json.dumps({
    'created_utc':datetime.now(timezone.utc).isoformat(),'precision_bits':ctx.prec,'series_terms':N,
    'proof':'03_lower_bounds/two_cusp_refinement/PROOF.md',
    'note':'Arb enclosures certify formula evaluations; mpmath quadrature is diagnostic only.','rows':rows},indent=2)+'\n')
