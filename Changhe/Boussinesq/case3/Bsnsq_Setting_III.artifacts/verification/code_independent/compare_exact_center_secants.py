"""Exact saved scalar secants. No inference of derivative bounds or a fold."""
from pathlib import Path
from datetime import datetime,timezone
import json,numpy as np
from certify_center_strain import block,q
r=Path('verification/L2_physical_continuity_20261021T1239Z');cfg=json.loads((r/'inputs.json').read_text());centers={};records=[]
def enc(v):return {'numerator':str(v.numerator),'denominator':str(v.denominator)}
for p in cfg['archives']:
 with np.load(p['frozen'],allow_pickle=False) as z:
  meta={k:z[k].item() for k in z.files if z[k].ndim==0};_,cs=block(meta,z['cG']);_,cf=block(meta,z['cG_f'],True);bb=q(meta['beta']);ll=q(meta['lam']);m=cs+ll*cf-1-bb/2
  centers[p['name']]={'beta':bb,'lambda':ll,'m':m,'c_self':cs,'c_seed':cf}
for name,labels in cfg['secants'].items():
 for a,b in zip(labels[:-1],labels[1:]):
  c,d=centers[a],centers[b];assert c['beta']==d['beta'];dl=d['lambda']-c['lambda'];dm=d['m']-c['m'];assert dl!=0
  records.append({'first':a,'second':b,'beta':float(c['beta']),'delta_lambda':enc(dl),'delta_m':enc(dm),'slope':enc(dm/dl),'slope_decimal':float(dm/dl)})
out={'utc':datetime.now(timezone.utc).isoformat(),'method':'Exact rational center moment from raw binary arrays using the previously checked packet160/163 moment implementation. These are secant slopes, not pointwise derivative bounds.','centers':{name:{k:enc(v) for k,v in values.items()} for name,values in centers.items()},'secant_slopes':records}
(r/'exact_center_secants.json').write_text(json.dumps(out,indent=2)+'\n');print(len(records),min(v['slope_decimal'] for v in records),max(v['slope_decimal'] for v in records))
