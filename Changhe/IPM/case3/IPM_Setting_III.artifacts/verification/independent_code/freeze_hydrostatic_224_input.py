"""Result289 stable attempt2 numeric checkpoint. No producer module is imported."""
import os
for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[name]='1'
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,traceback,resource,time,uuid
resource.setrlimit(resource.RLIMIT_AS,(14*1024**3,14*1024**3))
R=Path('research/hydrostatic_c2_resolved_224_audit');V=R/'verification';tag='hsG_c2.0_N224_log';utc=lambda:datetime.now(timezone.utc).isoformat();sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();attempt_start='2026-10-21T20:59:21Z';log_header='# hs_solve 2026-10-21T20:59:22Z ';epoch=datetime.fromisoformat(attempt_start.replace('Z','+00:00')).timestamp()
checks=[];out=dict(status='AWAITING_INPUT',started_utc=utc(),attempt_start_utc=attempt_start,checks=checks,proof_sha256=sha(R/'SOURCE_PROOF.md'),review_proof_sha256=sha(R/'REVIEW_RESOLUTION_PROOF.md'),followup_proof_sha256=sha(R/'FOLLOWUP_RESOLUTION_PROOF.md'),final_preparation_proof_sha256=sha(R/'THIRD_REVIEW_RESOLUTION_PROOF.md'),driver_sha256=sha(__file__),source_candidates=[f'../numerics/artifacts/data/hs/{tag}.pt',f'../numerics/runs/{tag}.pt',f'../numerics/runs/{tag}.raw.pt'])
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def atomic_json(path,obj):
 temp=V/('.'+Path(path).name+'.'+uuid.uuid4().hex+'.tmp');temp.write_text(json.dumps(obj,indent=2)+'\n');os.replace(temp,path)
def save():
 out['updated_utc']=utc();atomic_json(V/'SOURCE_GATE.json',out)
if (V/'INPUTS.json').exists() or (V/'SOURCE_GATE.json').exists():
 valid=False
 try:
  old_input=json.loads((V/'INPUTS.json').read_text());old_gate=json.loads((V/'SOURCE_GATE.json').read_text())
  valid=old_gate['status']=='PASS' and old_gate['input_sha256']==sha(V/'INPUTS.json') and len(old_input['states'])==1 and all(sha(row['frozen'])==row['sha256']==old_gate['source_sha256'] and row['frozen']==old_gate['frozen'] and row['tag']==tag for row in old_input['states'])
  valid=valid and old_gate['count']==len(old_gate['checks']) and all(row['passed']for row in old_gate['checks']) and all(old_gate[key]==out[key]for key in ['driver_sha256','proof_sha256','review_proof_sha256','followup_proof_sha256','final_preparation_proof_sha256'])
  valid=valid and old_gate['log_sha256']==sha(V/'producer_log_at_freeze.txt') and old_gate['launcher_sha256']==sha(V/'producer_launcher_at_freeze.txt') and set(old_gate['modules'])=={str(Path('independent_code',name).resolve())for name in ['q_local_checkpoint.py','q_checkpoint_reader.py']} and all(sha(path)==digest for path,digest in old_gate['modules'].items())
 except Exception:pass
 if valid:
  print('Valid frozen input and admission PASS already exist; preserve them. Later full archive needs a separate comparison.');raise SystemExit(0)
 recovery=V/'source_recovery'/uuid.uuid4().hex;recovery.mkdir(parents=True)
 for old in [V/'INPUTS.json',V/'SOURCE_GATE.json']:
  if old.exists():(recovery/old.name).write_bytes(old.read_bytes())
 out['recovery_archive']=str(recovery)
try:
 log=Path(f'../numerics/runs/{tag}.log');log_bytes=log.read_bytes()if log.exists()else b'';launch=Path('../numerics/runs/hsG5.out');launch_bytes=launch.read_bytes()if launch.exists()else b''
 candidates=[Path(p)for p in out['source_candidates']];source=None
 for p in candidates:
  if not p.exists():continue
  marker=f'# raw state saved runs/{tag}.raw.pt'.encode()if '.raw.'in p.name else b'# RESULT '
  if marker not in log_bytes:continue
  source=p;break
 if source is None:save();print('AWAITING_INPUT',utc());raise SystemExit(0)
 ck('attempt2 log header',log_bytes.startswith(log_header.encode())and log_bytes.count(b'# hs_solve ')==1);ck('attempt2 launcher',launch_bytes.startswith(('START '+attempt_start+'\n').encode()));before=source.stat();ck('source newer than attempt start',before.st_mtime>=epoch,dict(mtime_ns=before.st_mtime_ns));content=source.read_bytes();time.sleep(2);second=source.read_bytes();after=source.stat();ck('stable bytes across two seconds',content==second and before.st_size==after.st_size==len(content)and before.st_mtime_ns==after.st_mtime_ns);ck('nonempty numeric archive',len(content)>0)
 stagedir=V/'source_staging';stagedir.mkdir(exist_ok=True);staged=stagedir/(uuid.uuid4().hex+'.pt');staged.write_bytes(content);frozen=V/source.name;out.update(source=str(source),staged=str(staged),frozen=str(frozen),source_sha256=hashlib.sha256(content).hexdigest(),bytes=len(content),source_mtime_ns=before.st_mtime_ns,raw='.raw.'in source.name)
 import numpy as np
 import torch
 import q_local_checkpoint as checkpoint_module
 import q_checkpoint_reader as checkpoint_base
 QLocalCheckpoint=checkpoint_module.QLocalCheckpoint
 torch.set_num_threads(1);actual_modules=[Path(checkpoint_module.__file__).resolve(),Path(checkpoint_base.__file__).resolve()];ck('actual reader module paths',actual_modules==[Path('independent_code/q_local_checkpoint.py').resolve(),Path('independent_code/q_checkpoint_reader.py').resolve()]);out['modules']={str(p):sha(p)for p in actual_modules}
 with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q=QLocalCheckpoint(staged)
 ck('exact dimensions',q.N==224 and q.M==56);ck('exact parameters',q.cl==2. and q.L==1. and q.kappa==2. and q.p==.5);ck('explicit local basis',q.basis=='local' and 'tk'in q.data and q.meta['basis_nodes_source']=='stored');ck('coefficient count',q.u.shape==(sum(225-k for k in range(56)),));ck('finite coefficients',np.isfinite(q.u).all());ck('binary64 values',q.u.dtype==np.dtype('float64')and q.tk.dtype==np.dtype('float64'));ck('stored ordered nodes',q.tk.shape==(225,)and q.tk[0]==-1 and q.tk[-1]<1 and np.all(np.diff(q.tk)>0)and np.isfinite(q.tk).all());ck('metadata consistency',float(q.data['map_exponent_P'])==q.kappa and float(q.data['tail_exponent'])==q.p and float(q.data['c'])==q.cl);ck('reader source hash',q.meta.get('sha256')==out['source_sha256'])
 if out['raw']:ck('raw diagnostics absent',q.data.get('result')is None)
 else:ck('full diagnostics record',isinstance(q.data.get('result'),dict)and q.data['result'].get('tag')==tag)
 out['metadata']={key:q.meta[key]for key in ['N','M','L','p','cl','basis','basis_nodes_source']};out['coefficient_count']=int(q.u.size);out['result_status']='missing by design, raw save before diagnostics'if out['raw']else'producer diagnostics present; not independently verified here';out['missing_metadata']=[key for key in ['map_formula','basis_nodes','cH','centre_defect_single']if key not in q.data]
 (V/'producer_log_at_freeze.txt').write_bytes(log_bytes);(V/'producer_launcher_at_freeze.txt').write_bytes(launch_bytes);out['log_sha256']=sha(V/'producer_log_at_freeze.txt');out['launcher_sha256']=sha(V/'producer_launcher_at_freeze.txt');out['u_binary_sha256']=hashlib.sha256(q.u.tobytes()).hexdigest();out['tk_binary_sha256']=hashlib.sha256(q.tk.tobytes()).hexdigest()
 if frozen.exists():ck('existing admitted bytes unchanged',frozen.read_bytes()==content)
 else:os.link(staged,frozen)
 staged.unlink();out['staged_retained']=False
 inp=dict(utc=utc(),states=[dict(tag=tag,source=str(source),frozen=str(frozen),bytes=len(content),sha256=out['source_sha256'],raw=out['raw'])]);temp_input=V/('.INPUTS.'+uuid.uuid4().hex+'.tmp');temp_input.write_text(json.dumps(inp,indent=2)+'\n');out.update(status='PASS',input_sha256=sha(temp_input),count=len(checks),finished_utc=utc(),admitted_manifest_source=str(frozen));save();os.replace(temp_input,V/'INPUTS.json');print('PASS',len(checks),out['source_sha256'],out['result_status'],utc())
except Exception:
 out.update(status='FAIL',count=len(checks),traceback=traceback.format_exc());save();raise
