"""Recheck interval outputs against a rational necessary-condition bound."""
from pathlib import Path
from datetime import datetime, timezone
from flint import arb, ctx
import json
ctx.prec=256
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'verification/point_witnesses.json').read_text())
rows=[]
for point in data['results']:
    f=arb(point['F_abs']); v=arb(point['V_norm']); g=arb(point['gradient_norm'])
    upper=v/240+arb(3)/100000*(1+g)+arb(1)/8000000
    gap=f-upper
    if gap>0:
        item={'candidate':point['candidate'],'point':point['point'],
              'F_abs':point['F_abs'],'uniform_necessary_upper':upper.str(60),
              'gap':gap.str(60),'excludes_every_positive_baseline_gap_ball':True}
        rows.append(item)
        print(point['candidate'],point['point'],'gap',gap.str(14))
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PENDING-N4',
     'scope':'Exact rational corollary applied to the saved Arb intervals; depends on candidate conversion and point evaluator audit.',
     'source':'point_witnesses.json','results':rows}
(root/'verification/uniform_gap_witnesses.json').write_text(json.dumps(out,indent=2)+'\n')
