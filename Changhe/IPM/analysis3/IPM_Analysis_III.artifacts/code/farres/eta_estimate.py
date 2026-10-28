#!/usr/bin/env python3
"""NUMERICAL estimate of the strong residual norm ||F(rho~)||_Y from directed point densities.

Input: far_points_160.json (t = 0, 1/4, ..., 20) and far_points_192.json (t = 2, 3, ..., 60), produced by
far_points.py from the original data with every residual sine mode. The densities are the axis part
omega(t) gamma(t)^2 and the remainder part omega(t) e_R(t) of the Y energy. The integral over [0, 20] is a
log-linear (piecewise exponential) quadrature of the midpoint values; it is not an enclosure. For t >= 20
the remainder density decays at the exact rate 4k - 5/4 (residual homogeneous of degree 2k - 1), which the
points t = 30, 45, 60 confirm; the tail is integrated at the fitted rate. For t < 0 the densities at
t = -10, -40 (V107) are below 1e-8 and are neglected.
"""
import json,math,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def mid(s):
    m=re.match(r"\[([-+0-9.e]+)",s['ball']) if isinstance(s,dict) else None
    return float(m.group(1)) if m else 0.0
def load(name):
    d=json.load(open(ROOT/name));out={}
    for r in d['results']:
        n,_,q=r['t'].partition('/');t=float(n)/(float(q) if q else 1.0)
        out[t]=(mid(r['axis_energy_density']),mid(r['remainder_energy_density']))
    return out
g=load('far_points_160.json');c=load('far_points_192.json')
def seg(t0,f0,t1,f1):
    if f0<=0 or f1<=0: return 0.5*(f0+f1)*(t1-t0)
    if abs(f1-f0)<1e-12*f0: return f0*(t1-t0)
    return (f1-f0)*(t1-t0)/math.log(f1/f0)
ts=sorted(g);regions=[(0,4),(4,8.135),(8.135,12),(12,20)]
res={'axis':0.0,'remainder':0.0,'regions':{}}
for a,b in regions: res['regions'][f'[{a},{b}]']=0.0
for t0,t1 in zip(ts,ts[1:]):
    for i,key in ((0,'axis'),(1,'remainder')):
        e=seg(t0,g[t0][i],t1,g[t1][i]);res[key]+=e
        for a,b in regions:
            lo,hi=max(a,t0),min(b,t1)
            if hi>lo: res['regions'][f'[{a},{b}]']+=e*(hi-lo)/(t1-t0)
rate=math.log(c[60.0][1]/c[30.0][1])/30.0;k=1615536043799051/2**53
tail=c[30.0][1]*math.exp(rate*(20-30))/(-rate)
ax_rate=math.log(c[60.0][0]/c[30.0][0])/30.0;ax_tail=g[20.0][0]/(-ax_rate)
res['regions']['[20,inf)']=tail+ax_tail
res['fitted_remainder_rate']=rate;res['predicted_rate_4k_minus_5/4']=4*k-1.25;res['fitted_axis_rate']=ax_rate
total=res['axis']+res['remainder']+tail+ax_tail
res['energy_total']=total;res['eta_Y_estimate']=math.sqrt(total)
res['shares']={k2:v/total for k2,v in res['regions'].items()}
res['label']='NUMERICAL: quadrature of directed point densities, not an enclosure'
print(json.dumps(res,indent=1))
(ROOT/'eta_estimate.json').write_text(json.dumps(res,indent=1)+'\n')
