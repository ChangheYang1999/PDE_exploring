from pathlib import Path
import datetime,json,os,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
for mode in ['continuous','interrupt','resume']:
 log=ROOT/'logs'/('stage-resume-'+mode+'.log')
 with log.open('w') as f:
  done=subprocess.run([sys.executable,'-B',str(ROOT/'validation/stage_resume_probe.py'),mode],stdout=f,stderr=subprocess.STDOUT,timeout=120)
 if done.returncode:raise RuntimeError((mode,done.returncode,log.read_text()[-3000:]))
import torch
a=torch.load(ROOT/'.tmp/stage-resume-probe/continuous/stage_probe/ckpt_last.pt',map_location='cpu',weights_only=False)
b=torch.load(ROOT/'.tmp/stage-resume-probe/resumed/stage_probe/ckpt_last.pt',map_location='cpu',weights_only=False)
diffs={k:float((v-b['model'][k]).abs().max()) for k,v in a['model'].items() if v.numel()}
maxdiff=max(diffs.values());assert maxdiff>1e-10,maxdiff
restored='restored saved batch drawn at step 0' in (ROOT/'logs/stage-resume-resume.log').read_text();assert restored
r=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),source_manifest='snapshots/repair-project-dd9c125438565393/MANIFEST.json',max_parameter_difference=maxdiff,parameter_differences=diffs,continuous_state=a['state'],resumed_state=b['state'],restored_previous_stage_batch=restored,verdict='REFUTED',scope='Two 2-step Adam stages, resample_every=5, genuine Euler training loss. Only validation replaced by deterministic inexpensive metrics; interruption injected immediately after atomic stage-advance checkpoint. No campaign-time credit.')
(ROOT/'evidence/stage_advance_resume_counterexample.json').write_text(json.dumps(r,indent=2)+'\n');print(maxdiff,restored,flush=True)
