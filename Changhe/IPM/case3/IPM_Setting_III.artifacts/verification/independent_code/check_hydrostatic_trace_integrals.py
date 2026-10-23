"""Selected-state full improper integral checks of result208 moments."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
import numpy as np
import mpmath as mp
import torch
from q_local_checkpoint import QLocalCheckpoint
from hydrostatic_trace_coefficients import *
torch.set_num_threads(1)
v=Path('research/hydrostatic_trace_compatibility_diagnostic/verification');inputs=json.loads((v/'INPUTS.json').read_text());records=[];t0=time.monotonic()
for tag in ['hsA_c3.0_N128','hsE_c3.0_N128_hr','hsE_c2.0_N128_hr']:
 row=next(t for t in inputs['states']if t['tag']==tag);assert hashlib.sha256(Path(row['file']).read_bytes()).hexdigest()==row['sha256']
 with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q=QLocalCheckpoint(row['file'])
 b,_=stored_endpoint_data(q)
 with mp.workdps(70):
  p=1-1/exactmp(q.kappa);pref=exactmp(q.L)**(1/exactmp(q.kappa))/2;a=monomials(b,pref);val=moments(a,p)
  for S in [4,8]:
   res=integral_check(a,p,S,160);errs={k:abs(res[k]-val['Cp'])for k in ['q','moment']}
   records.append(dict(tag=tag,S=S,terms=160,digits=70,Cp=mp.nstr(val['Cp'],65),integrals={k:mp.nstr(res[k],65)for k in res},errors={k:mp.nstr(e,30)for k,e in errs.items()},pass_=all(e<mp.mpf('1e-35')*(1+abs(val['Cp']))for e in errs.values())))
   print(tag,S,records[-1]['errors'],records[-1]['pass_'],flush=True)
   (v/'INTEGRAL_CHECKS.json').write_text(json.dumps(dict(status='RUNNING',records=records),indent=2)+'\n')
out=dict(status='PASS'if all(t['pass_']for t in records)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-t0,records=records,module_sha256=hashlib.sha256(Path('independent_code/hydrostatic_trace_coefficients.py').read_bytes()).hexdigest());(v/'INTEGRAL_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['elapsed_seconds'],flush=True)
if out['status']!='PASS':raise SystemExit(1)
