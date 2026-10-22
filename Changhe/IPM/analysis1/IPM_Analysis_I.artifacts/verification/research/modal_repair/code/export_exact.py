"""Export the pinned binary64 modal input to exact JSON; no fitted numbers recomputed."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import io,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
BASE=Path(__file__).resolve().parents[3];p=BASE/'research/modal_exactification/evidence/trial_v2_h0.008.npz';data=p.read_bytes();expected='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874';assert hashlib.sha256(data).hexdigest()==expected
with np.load(io.BytesIO(data),allow_pickle=False) as d:
 arrays={key:{'shape':list(d[key].shape),'hex':[float(x).hex() for x in d[key].reshape(-1)]} for key in ['S','D','Aout','Ei','Eo','knots']}
 scalars={key:float(d[key]).hex() for key in ['k','L','rmin','R0','bi','bo']};degree=int(d['p'])
out={'source_npz_sha256':expected,'utc':datetime.now(timezone.utc).isoformat(),'convention':'All hex strings denote exact binary64 dyadics. Joins and normalization are defined in the modal_repair proof. rmin,R0 are stored for provenance only; exact boundaries use endpoint knots.','degree':degree,'outer_jl':[[j,0] for j in range(6)]+[[j,1] for j in range(3)]+[[0,2]],'scalars_hex':scalars,'arrays':arrays}
p=BASE/'data_exact/modal_v2.json';p.write_text(json.dumps(out,separators=(',',':'))+'\n');print(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'file':str(p.relative_to(BASE)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}))
