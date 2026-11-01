"""Resume after a successful audit of the actual saved N410 checkpoint."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,subprocess,sys
base=Path('research/91_candidate_checkpoint_audit/verification')
roots=sorted(base.glob('N410_*'));assert len(roots)==1
root=roots[0];record=json.loads((root/'checks.json').read_text());N=record['maximum_order'];assert N==410
manifest=dict(created_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),checkpoint_sha256=record['checkpoint_sha256'],checkpoint_bytes=record['checkpoint_bytes'],files={})
for p in root.rglob('*'):
 if p.is_file() and p.name!='MANIFEST.json':
  h=sha256()
  with p.open('rb') as f:
   while block:=f.read(1024*1024):h.update(block)
  manifest['files'][str(p.relative_to(root))]={'bytes':p.stat().st_size,'sha256':h.hexdigest()}
(root/'MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
for label,args,timeout in [
 ('archive_C007_N390',['code/delta_archive_checkpoint.py',str(root/'input_checkpoint.pkl.gz'),str(base/'N390_20261031T065156Z/input_checkpoint.pkl.gz'),'--remove-original','--decode-timeout','200'],580),
 ('candidate_refresh_nonlinear',['code/candidate_laurent_residual_audit.py',str(root/'input_checkpoint.pkl.gz'),'--orders',str(N),'--seconds','500'],580)]:
 with open('logs/'+label+'.jsonl','w') as out:
  result=subprocess.run([sys.executable,'-u',*args],stdout=out,stderr=subprocess.STDOUT,timeout=timeout)
 print(json.dumps(dict(step=label,maximum_order=N,returncode=result.returncode)),flush=True)
 if result.returncode:raise SystemExit(result.returncode)
