"""Certify failure of diagonal-direction maximality for the cutoff sphere.

This is a direct interval Riemann integral enclosure at alpha=99/100.
Every mathematical input is exact and the test function is explicit.
"""
from pathlib import Path
from datetime import datetime,timezone
import json
from flint import arb, fmpq, ctx

ROOT=Path(__file__).resolve().parents[1]
ctx.prec=128
alpha=arb(fmpq(99,100))
N=32768
pi=arb.pi()
step=pi/(2*N)
total=arb(0)
for k in range(N):
    interval=arb((k+arb(1)/2)*step,step/2)
    cosine=interval.cos()
    u=2-(5-4*cosine).sqrt()
    lo=u.lower()
    hi=u.upper()
    if hi<=0:
        positive=arb(0)
    else:
        if lo<0:lo=arb(0)
        positive=arb((lo+hi)/2,(hi-lo)/2)
    # A ball touching zero may slightly extend below zero. Evaluate endpoint
    # powers separately and then form the resulting positive interval.
    if hi<=0:
        value=arb(0)
    else:
        power_lo=lo**alpha
        power_hi=hi**alpha
        powered=arb((power_lo+power_hi)/2,(power_hi-power_lo)/2)
        value=(2*interval).cos()*cosine*arb(2)**(alpha-1)*powered
    total+=value*step
axis=2*total/pi
diagonal=arb(2)**alpha/pi*((alpha+2)/2).gamma()*arb(fmpq(3,2)).gamma()/((alpha+5)/2).gamma()
gap=axis-diagonal
assert gap>0
out={'generated_utc':datetime.now(timezone.utc).isoformat(),
     'alpha':'99/100','precision_bits':128,'riemann_cells':N,
     'axis_witness_integral':str(axis),'diagonal_exact_norm':str(diagonal),'gap':str(gap),
     'verdict':'CONFIRMED: the diagonal direction is not a maximizer at alpha=99/100.'}
(ROOT/'data/shell_counterexample_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
