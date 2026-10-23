"""Independent scalar MP differentiation on preselected actual node witnesses."""
from pathlib import Path
from datetime import datetime,timezone
import os,json,hashlib,time,traceback
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
R=Path('research/hydrostatic_actual_node_export_audit');V=R/'verification';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();start=datetime.now(timezone.utc).isoformat();tick=time.perf_counter();checks=[];bindings={};rows=[]
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def bind(p,h=None):
 p=Path(p).resolve().relative_to(Path.cwd());z=sha(p);ck('binding '+str(p),h is None or h==z);bindings[str(p)]=z;return p
def save(status,error=None):
 out=dict(status=status,started_utc=start,updated_utc=datetime.now(timezone.utc).isoformat(),elapsed_monotonic_seconds=time.perf_counter()-tick,count=len(checks),checks=checks,bindings=bindings,rows=rows,error=error,scope='MP local jets only on deterministic17-node witness set. No multiple-precision inverse or certified rounding. Primary unresolved.')
 p=V/'ACTUAL_MP_JETS.json.tmp';p.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n');p.replace(V/'ACTUAL_MP_JETS.json')
try:
 for p in [Path(__file__),R/'ACTUAL_JET_STAGE_PROOF.md',V/'ACTUAL_JETS.json','independent_code/scalar_mp_hydrostatic_density.py','independent_code/q_local_checkpoint.py','independent_code/q_checkpoint_reader.py']:bind(p)
 a=json.loads((V/'ACTUAL_JETS.json').read_text());ck('complete2468jets',a['status']=='PASS_ACTUAL_NODE_JETS_AND_EXACT_FIXED_MAP_ARITHMETIC'and a['count']==len(a['checks'])==2468 and all(z['passed']for z in a['checks']))
 for p,h in a['bindings'].items():bind(p,h)
 indices=a['mp_witness_indices'];ck('17 unique declared witnesses',len(indices)==len(set(indices))==17 and indices==sorted(indices))
 import numpy as np
 import torch
 import mpmath as mp
 from q_local_checkpoint import QLocalCheckpoint
 from scalar_mp_hydrostatic_density import ScalarMPDensity
 torch.set_num_threads(1)
 state=json.loads((V/'PROVENANCE_INPUTS.json').read_text())['state']['frozen']
 with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q=QLocalCheckpoint(state)
 with np.load(V/'actual_node_jets.npz',allow_pickle=False)as f:d={k:f[k]for k in f.files}
 for i in indices:
  x,y=float(d['X'][i]),float(d['Y'][i]);vv=[]
  for digits in [72,108]:
   with mp.workdps(digits):
    m=ScalarMPDensity(q.coeff,q.L,q.kappa,q.basis,q.tk);vv.append([mp.nstr(z,digits)for z in m.jet(x,y)])
  errors={}
  with mp.workdps(108):
   lo,hi=[list(map(mp.mpf,z))for z in vv];delta=[abs(a-b)/max(abs(b),mp.mpf('1e-60'))for a,b in zip(lo,hi)]
   for k,e in enumerate(delta):ck('MP72/108 stability '+str((i,k)),e<mp.mpf('1e-52'),mp.nstr(e,35))
   for who,arr in [('own',d['own_jet'][i]),('producer',d['producer_jet'][i])]:
    ee=[]
    for k,a in enumerate(arr):
     a=mp.mpf(float(a));b=hi[k];ab=abs(a-b);den=max(abs(a),abs(b));ee.append(dict(component=['g','gx','gy','gxx'][k],absolute=mp.nstr(ab,55),relative=mp.nstr(ab/den,55)if den else None,both_zero=not bool(den)))
    errors[who]=ee
  rows.append(dict(index=i,x=x,y=y,digits=[72,108],jets=vv,precision_change=[mp.nstr(z,55)for z in delta],errors=errors));save('RUNNING');print('MP_NODE',i,datetime.now(timezone.utc).isoformat(),flush=True)
 ck('all17MPwitnesses computed',[z['index']for z in rows]==indices)
 for p,h in list(bindings.items()):ck('stable '+p,sha(p)==h)
 save('PASS_ACTUAL_LOCAL_MP_JET_WITNESSES');print('PASS',len(checks),time.perf_counter()-tick,flush=True)
except Exception:save('FAIL',traceback.format_exc());raise
