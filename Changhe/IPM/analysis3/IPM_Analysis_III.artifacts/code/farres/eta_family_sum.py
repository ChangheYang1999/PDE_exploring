#!/usr/bin/env python3
"""NUMERICAL: integrate the strong remainder energy of the residual for angular exponents a and far radial
shifts Delta (weight factor e^{-2 Delta t} for t >= 0), from eta_family.log. Not an enclosure."""
import json,math
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parent
rows=[json.loads(l) for l in open(ROOT/'eta_family.log')]
pts={float(F(r['t'])):r for r in rows}
ts=sorted(t for t in pts if t<=20)
def seg(t0,f0,t1,f1):
    if f0<=0 or f1<=0: return 0.5*(f0+f1)*(t1-t0)
    if abs(f1-f0)<1e-12*f0: return f0*(t1-t0)
    return (f1-f0)*(t1-t0)/math.log(f1/f0)
k=1615536043799051/2**53;out={}
for a in ('3.6','3.8','4.0','4.25'):
    key='eR_a%s_unweighted'%a
    for Delta in (0.0,0.1,0.2,0.3,0.4,0.5):
        w=lambda t:math.exp((27/4-2*Delta)*t)*pts[t][key]
        E=sum(seg(t0,w(t0),t1,w(t1)) for t0,t1 in zip(ts,ts[1:]))
        rate=math.log(pts[30.0][key]/pts[20.0][key])/10+27/4-2*Delta
        E+=w(20.0)/(-rate) if rate<0 else float('inf')
        out['a=%s,Delta=%.1f'%(a,Delta)]={'eta_remainder':math.sqrt(E),'far_rate':rate}
for kk,v in out.items(): print(kk,'eta_R ~ %.4g'%v['eta_remainder'],'rate %.4f'%v['far_rate'])
(ROOT/'eta_family.json').write_text(json.dumps(out,indent=1)+'\n')
