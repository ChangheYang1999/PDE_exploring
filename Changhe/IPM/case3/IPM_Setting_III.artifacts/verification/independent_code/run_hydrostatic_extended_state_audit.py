"""Sequential result206 field audits, after the sole N44 job and its audit."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys,contextlib,runpy,traceback
root=Path('verification');os.chdir(root)
v=Path('research/hydrostatic_extended_state_audit/verification');prior=Path('research/hydrostatic_state_audit/verification')
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
now=lambda:datetime.now(timezone.utc).isoformat()
inputs=json.loads((v/'INPUTS.json').read_text())
for row in inputs['files']:assert sha(v/row['name'])==row['sha256']
assert json.loads(Path('research/smooth_N44_refinement_audit/verification/AUDIT_PIPELINE.json').read_text())['status']=='DONE'
for tag in inputs['tags']:
 src=v/'states'/(tag+'.pt');dst=prior/'states'/src.name
 if dst.exists():assert sha(dst)==sha(src),'Do not overwrite a different previously audited state'
 else:dst.write_bytes(src.read_bytes())
result=dict(started_utc=now(),pid=os.getpid(),status='RUNNING',input_sha256=sha(v/'INPUTS.json'),code_sha256={str(p):sha(p)for p in[Path(__file__),Path('independent_code/audit_hydrostatic_states_numeric.py'),Path('independent_code/audit_hydrostatic_states.py'),Path('independent_code/independent_hydrostatic.py'),Path('independent_code/q_local_checkpoint.py'),v.parent/'PROOF.md']},phases=[])
def save():result['updated_utc']=now();(v/'PIPELINE.json').write_text(json.dumps(result,indent=2)+'\n')
save()
for tag in inputs['tags']:
 phase=dict(tag=tag,started_utc=now(),status='RUNNING',log=str(v/(tag+'.audit.log')));result['phases'].append(phase);save();print(now(),'START',tag,flush=True)
 phase['pid']=os.getpid();phase['execution_mode']='same process, no waiting Python coordinator';save()
 with Path(phase['log']).open('w')as log,contextlib.redirect_stdout(log),contextlib.redirect_stderr(log):
  saved_argv=sys.argv[:];sys.argv=['independent_code/audit_hydrostatic_states_numeric.py','--tags',tag,'--stage','all'];rc=0
  try:runpy.run_path('independent_code/audit_hydrostatic_states_numeric.py',run_name='__main__')
  except SystemExit as exc:rc=exc.code if isinstance(exc.code,int)else (0 if exc.code is None else 1)
  except Exception as exc:phase['error']=repr(exc);traceback.print_exc();rc=1
  finally:sys.argv=saved_argv
 phase.update(returncode=rc,finished_utc=now(),status='DONE'if rc==0 else'FAILED')
 if rc:
  result.update(status='FAILED',finished_utc=now());save();raise SystemExit(rc)
 data=prior/(tag+'.json');q=json.loads(data.read_text());assert q['status']=='DONE';assert q['source_sha256']==sha(v/'states'/(tag+'.pt'))
 phase.update(result_path=str(data),result_sha256=sha(data),center=q['exact']['delta_float'],a=q['exact']['a_float'],B=q['exact']['b'],E=q['exact']['E'],annulus=q['regions']['annulus']['R_Nf']['R_Nf'],far=q['regions']['far']['R_Nf']['R_Nf']);save();print(now(),'DONE',tag,phase['center'],phase['annulus'],phase['far'],flush=True)
result.update(status='DONE',finished_utc=now());save();print(now(),'DONE',flush=True)
