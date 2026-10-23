"""Measured cost and precision comparison, independent saved-state norm evaluator."""
import json,time,sys,hashlib
from pathlib import Path
from datetime import datetime,timezone
import mpmath as mp
from polar_derivative_norms import QNormEvaluator
sys.set_int_max_str_digits(1000000)
out=Path('evidence/q_derivative_norms/benchmark.json');out.parent.mkdir(parents=True,exist_ok=True)
rec=dict(started_utc=datetime.now(timezone.utc).isoformat(),status='RUNNING',rows=[],scope='Pointwise positive integrands, not radial integrals or a convergence conclusion.')
def save():out.write_text(json.dumps(rec,indent=2)+'\n')
save()
for N in [64,192]:
 p=Path(f'evidence/q_canonical_high_jets/R1C_CL3P0_N{N}/exact_input.json');raw=json.loads(p.read_text())
 for dps in [70,100]:
  t=time.monotonic();model=QNormEvaluator(raw['coefficients'],raw['L'],raw['kappa'],raw['ell'],dps=dps,kmax=6);init=time.monotonic()-t
  t=time.monotonic();values=model.at_radius(mp.mpf('0.01'));elapsed=time.monotonic()-t
  row=dict(N=N,dps=dps,working_dps=model.workdps,input_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),init_seconds=init,point_seconds=elapsed,r='0.01',values={str(k):{f:mp.nstr(v,60) for f,v in vals.items()} for k,vals in values.items()})
  rec['rows'].append(row);save();print(json.dumps(row),flush=True)
rec['status']='COMPUTED';rec['finished_utc']=datetime.now(timezone.utc).isoformat();save()
