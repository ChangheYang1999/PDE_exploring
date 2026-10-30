"""Exact file comparison only. Executes no peer or research programs."""
from pathlib import Path
from datetime import datetime,timezone
from decimal import Decimal
import json,re,hashlib,os,time,difflib
B=Path(__file__).resolve().parents[1];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 tick=time.monotonic();start=datetime.now(timezone.utc).isoformat();checks=[]
 def ck(v,label):
  checks.append({'check':label,'pass':bool(v)})
  if not v:raise AssertionError(label)
 ck(os.sched_getaffinity(0)=={50,51} and os.getpriority(os.PRIO_PROCESS,0)==19,'assigned execution constraints')
 m=json.loads((B/'data/manifest.json').read_text())
 for rel,h in m['inputs'].items():ck(sha(B/rel)==h,'bound '+rel)
 p=json.loads((B/'data/PROOF_FIRST.json').read_text());ck(not p['checker_exists'] and p['proof_sha256']==sha(B/'PROOF.md'),'proof before checker')
 source=json.loads((B/'data/initial_sources.json').read_text())['rows'];ck(len(source)==149,'149 bound copied files')
 for r in source:ck(sha(B/r['local'])==r['sha256'],'copied '+r['local'])
 jobs=re.findall(r'(?:closure_calc|graded_calc|checks|transfer_checks)/[A-Za-z0-9_]+',(B/'source/run_all.sh').read_text());ck(jobs==json.loads((B/'data/jobs.json').read_text()),'independent job list');ck(len(jobs)==len(set(jobs))==69,'69 distinct jobs');ck(len(set(j.rsplit('/',1)[1] for j in jobs))==69,'distinct output names')
 log=(B/'source/run.log').read_text().splitlines();ck(len(log)==69,'69 exact log lines');logged=[]
 for j,line in zip(jobs,log):
  v=re.fullmatch(r'([^ ]+) rc=([0-9]+) ([0-9]+)s',line);ck(v is not None,'complete log parse '+j);ck(v[1]==j and int(v[2])==0,'matching logged zero return '+j);logged.append({'job':j,'seconds_integer':int(v[3])})
 def mask(text):
  text=re.sub(r'(?<![\w.])[0-9]+(?:\.[0-9]+)?(?= s\b)','<seconds>',text)
  text=re.sub(r'("seconds":\s*)[0-9]+(?:\.[0-9]+)?',r'\1<seconds>',text)
  text=re.sub(r'("(?:started_utc|finished_utc)":\s*")\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ(")',r'\1<utc>\2',text)
  return text
 exact=[];terminal=[];timing=[];changes=[]
 for job in jobs:
  name=job.rsplit('/',1)[1];a=(B/'source/old'/f'{name}.out').read_text();b=(B/'source/new'/f'{name}.out').read_text()
  if a==b:exact.append(job);ck(True,'byte identical '+job)
  elif a.endswith('rc=0\n') and a[:-5]==b:terminal.append(job);ck(True,'only terminal rc line '+job)
  else:
   ck(mask(a)==mask(b),'only inspected runtime tokens '+job);timing.append(job)
  aa=a.splitlines();bb=b.splitlines()
  if aa!=bb:
   edits=[{'tag':tag,'old_start':i+1,'old_end':j,'new_start':k+1,'new_end':l,'old':aa[i:j],'new':bb[k:l]} for tag,i,j,k,l in difflib.SequenceMatcher(a=aa,b=bb,autojunk=False).get_opcodes() if tag!='equal'];changes.append({'job':job,'edits':edits})
 ck(changes==json.loads((B/'data/changes.json').read_text()),'every changed text block reconstructed')
 ck((len(exact),len(terminal),len(timing))==(51,3,15),'independent51/3/15 partition')
 ck(set(terminal)=={'closure_calc/six_branch_K','graded_calc/graded_l2','checks/check_T4013_T4017'},'three named terminal lines')
 sides=[]
 for name in ['check_T4182.json','c_shift_diag.json','check_T4185.json']:
  raw_a=(B/'source/old'/name).read_text();raw_b=(B/'source/new'/name).read_text();a=json.loads(raw_a,parse_float=Decimal);b=json.loads(raw_b,parse_float=Decimal);ck(a.keys()==b.keys(),'side keys '+name);different=[k for k in a if a[k]!=b[k]]
  if name=='c_shift_diag.json':ck(raw_a==raw_b and not different,'byte identical side '+name)
  else:
   ck(different==['seconds'],'only seconds side '+name);ck(isinstance(a['seconds'],Decimal) and isinstance(b['seconds'],Decimal) and a['seconds']>=0 and b['seconds']>=0,'nonnegative exact decimal times '+name)
  sides.append({'name':name,'different_keys':different,'raw_identical':raw_a==raw_b})
 ck('jobs=69 exact=51 timing_only=18 diff=0 missing=0' in (B/'source/peer_comparison.txt').read_text(),'peer comparison consistent after separating3 terminal cases')
 r={'utc':datetime.now(timezone.utc).isoformat(),'started_utc':start,'check_count':len(checks),'checks':checks,'inputs':m['inputs'],'job_count':69,'byte_identical_jobs':exact,'terminal_rc_only_jobs':terminal,'runtime_only_jobs':timing,'side_records':sides,'logged_jobs':logged,'verdict':'CONFIRMED finite output partition51/3/15 and69 logged zero exits. No mathematical claim promoted.','scope':'Output text and exact-decimal side JSON only. No independent process-execution, wall-time or affinity attestation, no new mathematical replay, no peer execution.','elapsed_seconds':time.monotonic()-tick}
 with (B/'verification/result.json').open('x') as f:json.dump(r,f,indent=2);f.write('\n')
 print('PASS',len(checks),'checks',len(m['inputs']),'bindings',r['elapsed_seconds'],'seconds',sha(B/'verification/result.json'))
if __name__=='__main__':main()
