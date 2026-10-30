from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import gzip,json,os,signal,time,shutil
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/weighted_tail_candidate_review';P=ROOT.parent/'c1-t4/research/weighted_tail_candidate_audit'
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
now=lambda:datetime.now(timezone.utc).isoformat()
output=BASE/'source/MANIFEST.json';assert not output.exists()
pid=1554541;paused=False;started=now();files={}
try:
 if Path(f'/proc/{pid}').exists():
  command=Path(f'/proc/{pid}/cmdline').read_bytes();assert b'check_candidates.py' in command
  os.kill(pid,signal.SIGSTOP);paused=True
  for _ in range(100):
   state=Path(f'/proc/{pid}/stat').read_text().split(') ')[1].split()[0]
   if state in ['T','t']:break
   time.sleep(.01)
  assert state in ['T','t']
 def freeze(src,name,compressed=False):
  src=Path(src);dst=BASE/'source'/name;assert not dst.exists()
  digest=sha(src)
  if compressed:
   with src.open('rb') as inp,dst.open('xb') as out,gzip.GzipFile(filename='',mode='wb',fileobj=out,compresslevel=1,mtime=0) as gz:
    shutil.copyfileobj(inp,gz,1024*1024)
   with gzip.open(dst,'rb') as f:assert sha256(f.read()).hexdigest()==digest
  else:shutil.copy2(src,dst)
  assert sha(src)==digest
  files[name]={'original':str(src),'sha256':digest,'frozen_sha256':sha(dst),'gzip':compressed,'original_bytes':src.stat().st_size,'frozen_bytes':dst.stat().st_size}
 for src,name in [(P/'PROOF.md','T4_PROOF.md'),(P/'code/check.py','T4_check.py'),(P/'verification/result.json','T4_result.json'),(P/'data/inputs.json','T4_inputs.json'),(P/'source/T2_REVIEW_T4_249.md','T2_REVIEW_T4_249.md'),(ROOT.parent/'c1-t4/research/weighted_forced_tails/PROOF.md','T4_weighted_forced_tails_PROOF.md')]:freeze(src,name)
 result=json.loads((BASE/'source/T4_result.json').read_text());rows={r['candidate']:r for r in result['rows']}
 for name in ['006','008','009','012','013','014']:
  row=rows[name];src=P/f'data/{name}_sectors.json';assert sha(src)==row['exact_data_sha256']
  freeze(src,f'T4_{name}_sectors.json.gz',True)
  src=Path(row['source']['path']);assert sha(src)==row['source']['sha256']
  freeze(src,f'T4_{name}_canonical.json.gz',True)
 with output.open('x') as f:json.dump({'utc':now(),'files':files,'foreign_code_executed':False,'code_sha256':sha(Path(__file__))},f,indent=2);f.write('\n')
 print('FROZEN',len(files),'bytes',sum(x['frozen_bytes'] for x in files.values()),'manifest',sha(output),flush=True)
finally:
 if paused:
  os.kill(pid,signal.SIGCONT)
 with (BASE/'verification/freeze_serial_pause.json').open('x') as f:json.dump({'started':started,'ended':now(),'pid':pid,'paused':paused,'resumed':paused,'reason':'lossless peer data freeze, no concurrent busy calculations'},f,indent=2);f.write('\n')
