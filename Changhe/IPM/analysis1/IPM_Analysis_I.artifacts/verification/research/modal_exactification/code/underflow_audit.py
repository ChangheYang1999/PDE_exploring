"""An exact dyadic counterexample to the snapshotted midrad matrix enclosure."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import sys,json,hashlib
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import numpy as np
BASE=Path(__file__).resolve().parents[3]
source=BASE/'research/modal_exactification/evidence/refreshed_1435/midrad.py'
sys.path.insert(0,str(source.parent))
from midrad import MR,mr_matmul
K=100;eta=F(1,2**1074)
a=np.full((1,K),2.**-537);b=np.full((K,1),2.**-538)
z=mr_matmul(MR(a,a),MR(b,b))
m,r=F.from_float(float(z.m[0,0])),F.from_float(float(z.r[0,0]))
# Exact all-upper-endpoint matrix product, not a floating reference.
true=K*(2*F.from_float(float(a[0,0])))*(2*F.from_float(float(b[0,0])))
assert m==0 and r==105*eta and true==200*eta and m+r<true
out={'utc':datetime.now(timezone.utc).isoformat(),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'K':K,'A_mid_and_radius_hex':float(a[0,0]).hex(),'B_mid_and_radius_hex':float(b[0,0]).hex(),'computed_midpoint_units_eta':str(m/eta),'computed_radius_units_eta':str(r/eta),'exact_upper_endpoint_units_eta':str(true/eta),'result':'REFUTED: computed interval excludes an exact product of admissible endpoints','scope':'Counterexample in the claimed gradual-underflow model; does not show actual residual run reaches this regime.'}
(BASE/'research/modal_exactification/evidence/underflow_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
