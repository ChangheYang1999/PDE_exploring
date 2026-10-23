"""Result229. Reuse only our independently written result227 inverse engine."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,traceback
import audit_hydrostatic_resolved_maps as impl
ROOT=Path('research/hydrostatic_cusp_row_audit');V=ROOT/'verification'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
gate=json.loads((V/'CUSP_GATE.json').read_text())
assert gate['status']=='PASS' and gate['count']==651
assert gate['module_sha256']==sha('independent_code/hydrostatic_cusp_functional.py')
assert gate['proof_sha256']==sha(ROOT/'PROOF.md')
files=[__file__,'independent_code/hydrostatic_cusp_functional.py','independent_code/check_hydrostatic_cusp_functional.py',V/'CUSP_GATE.json']
r=dict(status='RUNNING',utc_started=datetime.now(timezone.utc).isoformat(),pid=os.getpid(),files={str(p):sha(p)for p in files},reuse='Own result227 engine, not producer code; own manufactured cusp gate651PASS')
path=V/'WRAPPER_PROVENANCE.json'
def save():path.write_text(json.dumps(r,indent=2)+'\n')
save()
try:
    impl.ROOT=ROOT;impl.V=V;impl.main()
    assert all(sha(p)==h for p,h in r['files'].items())
    r.update(status='DONE',utc_finished=datetime.now(timezone.utc).isoformat(),pipeline_sha256=sha(V/'PIPELINE.json'));save()
except Exception:
    r.update(status='FAILED',utc_finished=datetime.now(timezone.utc).isoformat(),error=traceback.format_exc());save();raise
