"""Result231. Sequential pipeline using only the verifier's own earlier code."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,traceback
import audit_hydrostatic_resolved_maps as inverse
import summarize_hydrostatic_cusp_128 as summary
import audit_hydrostatic_cusp_axis as cuspaxis
R=Path('research/hydrostatic_cusp_128_audit');V=R/'verification';parent=Path('research/hydrostatic_cusp_row_audit')
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
utc=lambda:datetime.now(timezone.utc).isoformat()
files=[Path(__file__),Path('independent_code/audit_hydrostatic_resolved_maps.py'),Path('independent_code/summarize_hydrostatic_cusp_128.py'),Path('independent_code/audit_hydrostatic_cusp_axis.py'),R/'PROOF.md',R/'AXIS_TAIL_PROOF.md',R/'REVIEW_ADDENDUM.md',R/'SUMMARY_PROOF.md']
for name in ['CUSP_GATE.json','AXIS_SERIES_GATE.json']:
 assert (V/name).read_bytes()==(parent/'verification'/name).read_bytes()
 gate=json.loads((V/name).read_text());assert gate['status']=='PASS'
 proof=parent/('PROOF.md'if name=='CUSP_GATE.json'else'AXIS_TAIL_PROOF.md')
 assert gate['proof_sha256']==sha(proof)
 files += [V/name,proof]
out=dict(status='RUNNING',utc_started=utc(),pid=os.getpid(),files={str(p):sha(p)for p in files},stage='inverse',reuse='Own Cartesian jets/power-tail inverse, own exact cusp and own beta-axis engine. No producer code.')
def save():out['utc_updated']=utc();(V/'WRAPPER_PROVENANCE.json').write_text(json.dumps(out,indent=2)+'\n')
save()
try:
 inverse.ROOT=R;inverse.V=V;inverse.main()
 out['stage']='summary';save();summary.main()
 out['stage']='cusp_axis';save();cuspaxis.R=R;cuspaxis.V=V;cuspaxis.main()
 assert all(sha(p)==h for p,h in out['files'].items())
 out.update(status='DONE',stage='complete',utc_finished=utc(),pipeline_sha256=sha(V/'PIPELINE.json'),summary_sha256=sha(V/'SUMMARY.json'),cusp_axis_sha256=sha(V/'CUSP_AXIS_CHECKS.json'));save()
except Exception:
 out.update(status='FAILED',utc_failed=utc(),error=traceback.format_exc());save();raise
