from pathlib import Path
import datetime,json,subprocess,sys
BASE=Path(__file__).resolve().parent
started=datetime.datetime.now(datetime.timezone.utc).isoformat()
for mode in ['continuous','interrupt','resume']:
 log=BASE/(mode+'.log')
 with log.open('w') as f:
  done=subprocess.run([sys.executable,'-B',str(BASE/'worker.py'),mode],stdout=f,stderr=subprocess.STDOUT,timeout=120)
 if done.returncode: raise RuntimeError((mode,done.returncode,log.read_text()[-2000:]))
import torch
a=torch.load(BASE/'runs/continuous/stage_probe/ckpt_last.pt',map_location='cpu',weights_only=False)
b=torch.load(BASE/'runs/resumed/stage_probe/ckpt_last.pt',map_location='cpu',weights_only=False)
diffs={k:float((v-b['model'][k]).abs().max()) for k,v in a['model'].items() if v.numel()}
same_sampler=torch.equal(a['sampler']['generator_state'],b['sampler']['generator_state']) if 'generator_state' in a['sampler'] else None
r=dict(started_utc=started,ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),source_manifest='SOURCE_MANIFEST.json',max_parameter_difference=max(diffs.values()),parameter_differences=diffs,continuous_state=a['state'],resumed_state=b['state'],sampler_generator_equal=same_sampler,verdict='CONFIRMED' if max(diffs.values())==0 else 'REFUTED',scope='Post-stop four-step Euler Adam lifecycle comparison with inexpensive deterministic validation stub. Two stages, retained batches, interruption immediately after atomic stage advance. No campaign-time credit and no append to either frozen ledger.')
(BASE/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({k:r[k] for k in ['max_parameter_difference','verdict','scope']},indent=2),flush=True)
