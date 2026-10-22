from pathlib import Path
from datetime import datetime,timezone
import json,numpy as np
r=Path('verification/exact_L2_seed_return_20261021T1514Z');a=r/'archives';rows=[]
with np.load(a/'fb30y25g24_eps0.npz',allow_pickle=False) as x,np.load(a/'fb30y25g24_eps0_a01.npz',allow_pickle=False) as y:
 for k in ['cF','cG']:
  e=float(np.max(abs(x[k]/4.332010-y[k])));assert e==0;rows.append({'key':k,'rounded_divisor':4.332010,'max_binary64_division_discrepancy':e,'pass':True})
result={'utc':datetime.now(timezone.utc).isoformat(),'checks':rows,'status':'PASS','scope':'Exact equality of binary64 division outputs for all stored coefficients, not exact rational scaling or spatial scaling symmetry.'}
(r/'seed_normalization_supplement.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
