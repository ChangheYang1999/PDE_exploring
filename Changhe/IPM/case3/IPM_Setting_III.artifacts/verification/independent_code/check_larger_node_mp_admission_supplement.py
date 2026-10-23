from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import os,sys,json,hashlib,subprocess
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
import numpy as np
import torch
from q_local_checkpoint import QLocalCheckpoint
R=Path('research/hydrostatic_larger_node_audit');V=R/'verification';checks=[];bindings={};sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e));assert b,(n,e)
def bind(p,h=None):
 p=str(p);v=sha(p);ck('binding '+p,h is None or h==v);bindings[p]=v;return Path(p)
for p in [__file__,R/'MP_FINAL_ADMISSION_PROOF.md','independent_code/q_local_checkpoint.py','independent_code/q_checkpoint_reader.py','independent_code/launch_larger_node_mp.py','independent_code/run_larger_node_mp.py']:bind(p)
u=1-F(1,2**40);pol=lambda u:F(1,2**41)*u+(1+F(9,2**164))*u**4-1;ck('exact far root bracket',pol(u)<0<pol(F(1)))
i=json.loads(bind(V/'INPUTS.json').read_text());torch.set_num_threads(1)
for s in i['states']:
 bind(s['path'],s['sha256'])
 with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q=QLocalCheckpoint(s['path'])
 ck('actual weights_only source '+str(s['N']),q.meta['sha256']==s['sha256']and q.N==s['N']and q.M==s['M']and q.cl==2 and q.kappa==2 and q.L==1 and q.p==.5 and q.basis=='local'and q.meta['basis_nodes_source']=='stored'and np.isfinite(q.u).all())
 del q
j=json.loads(bind(V/'JOB.json').read_text());driver=bind('independent_code/run_larger_node_audit.py',j['driver_sha256']).read_text();ck('real producer exact schema fields',all(s in driver for s in ['source=state','local_mp_indices=mp_ids','integrand_mp_indices=[globalrf]','_targets.npz','_SELECTION.json','_COMPLETE.json','COMPLETE_FINITE_LARGER_NODES_REQUIRES_MP_AND_FINAL_REVIEW']))
p=Path('/proc')/str(j['pid']);ck('known active allnode worker',p.exists()and b'run_larger_node_audit.py'in(p/'cmdline').read_bytes()and(p/'stat').read_text().split(') ',1)[1].split()[0]!='Z')
z=subprocess.run([sys.executable,'independent_code/launch_larger_node_mp.py'],capture_output=True,text=True,timeout=15);(V/'MP_ACTIVE_JOB_REFUSAL.log').write_text(z.stdout+z.stderr);ck('actual wrapper refuses active B without MP child',z.returncode!=0 and 'all-node process still active'in z.stderr)
for p,h in bindings.items():ck('stable '+p,sha(p)==h)
out=dict(status='PASS_MP_ADMISSION_SUPPLEMENT',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,scope='Read-only actual checkpoint admission and active-job refusal. No candidate MP run.')
(V/'MP_ADMISSION_SUPPLEMENT.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(checks))
