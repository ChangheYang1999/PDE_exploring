"""One CPU18 Candidate007 refresh, archive preservation, and nonlinear high-order audit."""
from pathlib import Path
import json,subprocess,sys
base=Path('research/91_candidate_checkpoint_audit/verification')
before=set(base.glob('N*'))
with open('logs/candidate_refresh_audit.jsonl','w') as out:
 result=subprocess.run([sys.executable,'-u','code/candidate_checkpoint_audit.py','--freeze'],stdout=out,stderr=subprocess.STDOUT,timeout=580)
print('candidate_refresh_audit',result.returncode,flush=True)
if result.returncode:raise SystemExit(result.returncode)
new=set(base.glob('N*'))-before
assert len(new)==1,new
root=new.pop();record=json.loads((root/'checks.json').read_text());N=record['maximum_order']
assert N>390
with open('logs/archive_C007_N390.jsonl','w') as out:
 result=subprocess.run([sys.executable,'-u','code/delta_archive_checkpoint.py',str(root/'input_checkpoint.pkl.gz'),str(base/'N390_20261031T065156Z/input_checkpoint.pkl.gz'),'--remove-original','--decode-timeout','200'],stdout=out,stderr=subprocess.STDOUT,timeout=640)
print('archive_C007_N390',result.returncode,flush=True)
if result.returncode:raise SystemExit(result.returncode)
with open('logs/candidate_refresh_nonlinear.jsonl','w') as out:
 result=subprocess.run([sys.executable,'-u','code/candidate_laurent_residual_audit.py',str(root/'input_checkpoint.pkl.gz'),'--orders',str(N),'--seconds','500'],stdout=out,stderr=subprocess.STDOUT,timeout=580)
print('candidate_refresh_nonlinear',result.returncode,flush=True)
raise SystemExit(result.returncode)
