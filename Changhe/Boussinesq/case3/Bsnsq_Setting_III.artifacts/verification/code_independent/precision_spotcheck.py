"""High precision checks of serialized field values and stream derivatives.

This script evaluates the displayed coefficient formula directly with mpmath.
It imports neither the fitting code nor the value-only/finite-difference code.
"""
import json
from pathlib import Path
from datetime import datetime, timezone
import mpmath as mp

mp.mp.dps=70
source=Path('runs/rational_campaign_01/030_d8_b3_s0/candidate.json')
d=json.loads(source.read_text(),parse_float=mp.mpf)
beta=mp.mpf(d['beta'])

def value(x,y,kind):
    total=mp.mpf(0)
    for t,c in zip(d[kind+'_terms'],d[kind+'_coeff']):
        i,j=t['i'],t['j'];L=mp.mpf(t['scale']);k=t['tail_order']
        target=1-(k+1)/beta if kind=='theta' else 2-k/beta
        amplitude=1 if kind=='theta' else 2
        total+=mp.mpf(c)*L**(amplitude-i-j)*x**i*y**j*(1+(x*x+y*y)/(L*L))**((target-i-j)/2)
    return total

v0=mp.diff(lambda x:value(x,mp.mpf(0),'psi'),mp.mpf(0))
points=[('0','0'),('0','.2'),('.4','-.3'),('1','.8'),('3','-2')]
vel=[]
for xs,ys in points:
    x,y=mp.mpf(xs),mp.mpf(ys)
    vel.append([-mp.diff(lambda z:value(x,z,'psi'),y),mp.diff(lambda z:value(z,y,'psi'),x)-v0])
audit=json.loads(Path('verification/rational_campaign_01_d8_b3.json').read_text())
rows=[]
for row in audit['inverse']:
    err=max(abs(mp.mpf(str(row['velocity'][i][j]))-vel[i][j]) for i in range(len(points)) for j in range(2))
    rows.append({'radius':row['radius'],'order':row['order'],'error_against_70_digit_velocity':float(err)})
out={'utc':datetime.now(timezone.utc).isoformat(),'precision_decimal_digits':mp.mp.dps,'source':str(source),
     'points':points,'stream_v0':str(v0),'velocity':[[str(t) for t in v] for v in vel],
     'inverse_comparisons':rows,'verdict':'A numerical precision check, not an interval error bound.'}
Path('verification/rational_candidate_precision.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'v0':str(v0),'inverse_comparisons':rows},indent=2))
