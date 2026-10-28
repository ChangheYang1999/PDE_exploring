"""Sequential bounded commands for the selected independent table replay."""
from pathlib import Path
from datetime import datetime,timezone
import subprocess,sys,os,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'05_team_audit/table37_lead/verification/replay_a20'
def stamp():return datetime.now(timezone.utc).isoformat()
def main():
 sources={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (ROOT/'code').glob('*.py')}
 (BASE/'queue_start.json').write_text(json.dumps(dict(time_utc=stamp(),source_hashes=sources),indent=2)+'\n')
 jobs=[]
 for start in range(32,512,32):
  out=BASE/f'middle_{start}_{start+32}.json'
  jobs.append((out,[sys.executable,'-B','-u','code/certify_middle_chunks.py','--alphas','1/5','--angles','512','--radial','512','--phases','16','--start',str(start),'--stop',str(start+32),'--out',str(out.relative_to(ROOT))]))
 out=BASE/'far.json'
 jobs.append((out,[sys.executable,'-B','-u','code/certify_far_circles.py','--alphas','1/5','--angles','512','--radial','128','--phases','16','--out',str(out.relative_to(ROOT))]))
 for out,cmd in jobs:
  if out.exists():print(stamp(),'existing',out.name,flush=True);continue
  print(stamp(),'START',out.name,flush=True)
  with out.with_suffix('.log').open('w') as f:r=subprocess.run(cmd,cwd=ROOT,stdout=f,stderr=subprocess.STDOUT,timeout=540)
  assert r.returncode==0 and out.exists(),(out.name,r.returncode)
  print(stamp(),'DONE',out.name,flush=True)
 for p,h in sources.items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,('source changed',p)
 (BASE/'queue_complete.json').write_text(json.dumps(dict(time_utc=stamp(),source_unchanged=True),indent=2)+'\n')
 print(stamp(),'COMPLETE',flush=True)
if __name__=='__main__':main()
