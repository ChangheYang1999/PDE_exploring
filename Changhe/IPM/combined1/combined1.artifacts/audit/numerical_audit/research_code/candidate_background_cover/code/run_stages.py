"""Bounded serial cover stages while the single production queue is paused."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,os,signal,subprocess,time
ROOT=Path(__file__).resolve().parents[3]
PYTHON='python3'
def now():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def run(first,last):
 log=ROOT/f'logs/candidate007_background_pause_{first:02d}_{last:02d}.json'
 assert not log.exists()
 state={'started_utc':now(),'production_group':97684,'stages':[]}
 os.killpg(97684,signal.SIGSTOP)
 try:
  for i in range(first,last+1):
   started=time.monotonic();stage={'index':i,'started_utc':now()}
   with (ROOT/f'logs/candidate007_background_cover_{i:02d}.log').open('x') as f:
    try:
     p=subprocess.run([PYTHON,'-B',str(ROOT/'research/candidate_background_cover/code/certify.py'),'cover','--seconds','420'],cwd=ROOT,stdout=f,stderr=subprocess.STDOUT,timeout=465)
     stage['returncode']=p.returncode
    except subprocess.TimeoutExpired:stage['returncode']='TIMEOUT'
   stage.update({'elapsed_seconds':time.monotonic()-started,'ended_utc':now()})
   state['stages'].append(stage);log.write_text(json.dumps(state,indent=2)+'\n')
   print(stage,flush=True)
   if stage['returncode']!=0:break
   data=json.loads((ROOT/'research/candidate_background_cover/verification/C1-N1-007-d2w-j7-e2bal_theta_2_25_768.json').read_text())
   if data['all_pass']:break
 finally:
  os.killpg(97684,signal.SIGCONT)
  state['ended_utc']=now();log.write_text(json.dumps(state,indent=2)+'\n')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('first',type=int);p.add_argument('last',type=int);args=p.parse_args();run(args.first,args.last)
