"""Manufactured analytic inverse before adaptive evaluation of trial data."""
import os
for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']: os.environ[name]='1'
from pathlib import Path
from datetime import datetime,timezone
import math,json,hashlib
import numpy as np
from adaptive_hydrostatic_velocity import AdaptiveVerticalVelocity
R=Path('research/hydrostatic_velocity_sequence_audit');V=R/'verification'
assert V.resolve().is_relative_to(Path('verification')), 'Writes must stay in the verifier lane'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
checks=[];rows=[]
def ck(name,b,e=None): checks.append(dict(name=name,passed=bool(b),evidence=e))
def jet(x,y):
    x,y=np.broadcast_arrays(x,y)
    e=np.exp(-x*x-y*y)
    return np.stack([y*e,-2*x*y*e,(1-2*y*y)*e,(4*x*x-2)*y*e],axis=-1)
points=[(0,0),(0,.03),(.03,0),(.1,.1),(.7,1.3),(2.1,.6),(-.7,1.3),(.7,-1.3),(-.7,-1.3)]
for split in [7,37]:
    inv=AdaptiveVerticalVelocity(jet,.5,split=split)
    for x,y in points:
        q=inv.at(x,y)
        exact=[x*math.exp(-x*x-y*y),(4*x*x-2)*math.exp(-x*x)*math.sqrt(math.pi)*math.erf(y)/4]
        err=max(abs(a-b) for a,b in zip(q['V'],exact))
        name=str((split,x,y))
        ck('exact Gaussian '+name,err<2e-12,err)
        ck('no warnings '+name,not q['messages'],q['messages'])
        ck('finite error '+name,np.isfinite(q['estimated_error']).all())
        rows.append(dict(split=split,x=x,y=y,exact=exact,actual=q))
out=dict(status='PASS' if all(q['passed'] for q in checks) else 'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,rows=rows,proof_sha256=sha(R/'WITNESS_PROOF.md'),module_sha256=sha('independent_code/adaptive_hydrostatic_velocity.py'),driver_sha256=sha(__file__))
(V/'ADAPTIVE_MANUFACTURE.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['status'],len(checks));print([q for q in checks if not q['passed']])
raise SystemExit(out['status']!='PASS')
