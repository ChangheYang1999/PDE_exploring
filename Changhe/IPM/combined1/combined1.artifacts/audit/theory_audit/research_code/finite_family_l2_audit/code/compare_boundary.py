from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from flint import arb,ctx
import json,hashlib
ctx.prec=512;root=Path(__file__).resolve().parents[1]
p=root/'verification/reproduction.json';q=root/'source/N4_boundary.json'
a=json.loads(p.read_text())['four_branch_cutoff'];b=json.loads(q.read_text())
assert a['last_excluded_K']==b['last_excluded_degree']==25929
assert a['first_K_not_excluded_by_this_floor']==b['first_inconclusive_degree']==25930
checks={key:(arb(a[field])*163840).overlaps(arb(b[key])) for key,field in [('last_ratio','previous_X_lower'),('next_ratio','current_X_lower')]}
assert all(checks.values())
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'checks':checks,'last_excluded_K':25929,'first_nonexcluded_K':25930,
'inputs':{str(x.name):hashlib.sha256(x.read_bytes()).hexdigest() for x in [p,q]},'scope':'Independent direct product and N4 gamma formula agree. No feasibility claim at larger K.'}
(root/'verification/boundary_comparison.json').write_text(json.dumps(out,indent=2)+'\n')
print(checks)
