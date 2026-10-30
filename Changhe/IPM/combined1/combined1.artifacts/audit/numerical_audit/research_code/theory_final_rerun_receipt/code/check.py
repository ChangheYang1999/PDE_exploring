"""Finite T1 final output comparison; never executes T1 code."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,re,os,time
R=Path(__file__).resolve().parents[3];B=R/'research/theory_final_rerun_receipt';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();read=lambda p:json.loads(p.read_text())
def norm(s):
 s=re.sub(r'(?<![A-Za-z0-9_.])\d+(?:\.\d+)? s\b','<seconds> s',s)
 s=re.sub(r'("seconds": *)[0-9.eE+-]+',r'\1<seconds>',s)
 return re.sub(r'\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d+)?(?:\+00:00|Z)','<UTC>',s)
def main():
 assert os.sched_getaffinity(0)=={57}and os.getpriority(os.PRIO_PROCESS,0)==19
 start=datetime.now(timezone.utc).isoformat();tick=time.monotonic();out=B/'verification/result.json';assert not out.exists();checks=[]
 def ck(v,label):checks.append({'check':label,'pass':bool(v)});assert v,label
 m=read(B/'verification/PROOF_FIRST.json');ck(not m['checker_exists']and not m['result_exists'],'proof before checker')
 for rel,h in m['inputs'].items():ck(sha(R/rel)==h,'binding '+rel)
 jobs=re.findall(r'(?:closure_calc|graded_calc|checks|transfer_checks)/[A-Za-z0-9_]+',(B/'source/run_all.sh').read_text());ck(len(jobs)==len(set(jobs))==len({j.split('/')[-1]for j in jobs})==69,'69uniquejobs');ck(jobs==[x['job']for x in m['pairs']],'manifestjoborder')
 log=(B/'source/run.log').read_text().splitlines();ck(len(log)==69,'69loglines');seconds=[]
 for j,line in zip(jobs,log):
  x=re.fullmatch(re.escape(j)+r' rc=(\d+) (\d+)s',line);ck(bool(x)and x[1]=='0','saved log rc0 '+j);seconds.append(int(x[2]))
 trailers={'closure_calc/six_branch_K','graded_calc/graded_l2','checks/check_T4013_T4017'};counts={'byte_identical':0,'rc_trailer_only':0,'timing_only':0};changes=[]
 for row in m['pairs']:
  a=(R/row['old']).read_text();b=(R/row['rerun']).read_text();j=row['job']
  if a==b:counts['byte_identical']+=1;ck(True,'byte identical '+j);continue
  al=a.splitlines();bl=b.splitlines()
  if j in trailers:
   ck(al[-1]=='rc=0'and al[:-1]==bl,'only explicit trailer '+j);counts['rc_trailer_only']+=1;changes.append({'job':j,'type':'rc_trailer_only','old_final':'rc=0'});continue
  ck(len(al)==len(bl),'same line count '+j);ck([norm(x)for x in al]==[norm(x)for x in bl],'only timing fields '+j);counts['timing_only']+=1;different=[]
  for i,(x,y)in enumerate(zip(al,bl),1):
   if x!=y:different.append({'line':i,'old':x,'rerun':y})
  ck(bool(different),'retained changed lines '+j);changes.append({'job':j,'type':'timing_only','changed_lines':different})
 ck(counts=={'byte_identical':51,'rc_trailer_only':3,'timing_only':15},'stated51+3+15counts')
 side=[]
 for row in m['side_json']:
  a=(R/row['old']).read_text();b=(R/row['rerun']).read_text();name=row['name']
  if name=='c_shift_diag.json':ck(a==b,'third sidejson byteidentical');side.append({'name':name,'type':'byte_identical'});continue
  x=json.loads(a);y=json.loads(b);t=x.pop('seconds');u=y.pop('seconds');ck(x==y and t!=u and isinstance(t,(int,float))and isinstance(u,(int,float))and t>=0 and u>=0,'only top-level seconds '+name);side.append({'name':name,'type':'top_level_seconds_only','old_seconds':t,'rerun_seconds':u})
 summary=(B/'source/compare_result.txt').read_text();ck('jobs=69 exact=51 timing_only=18 diff=0 missing=0'in summary,'peer summary matches combinedtiming');ck(sha(B/'source/normcmp.py')=='d5ac7636218e57560b1953c3dd288f24d045f0580376e566c436a3dd3e068f2f','nominated comparison source');ck(sha(B/'source/compare_result.txt')=='07580df23c764fa53cfdc2ab4d0904892c6b88ad2fbf910e5bf659d7142c3473','nominated comparison result')
 inputs=dict(m['inputs']);inputs.update({str(x.relative_to(R)):sha(x)for x in [Path(__file__),B/'verification/PROOF_FIRST.json']});d={'utc':datetime.now(timezone.utc).isoformat(),'started_utc':start,'inputs':inputs,'checks':checks,'check_count':len(checks),'counts':counts,'changed_jobs':changes,'side_json':side,'saved_log_rc0':69,'saved_log_elapsed_integer_seconds_sum':sum(seconds),'execution_witness':'not independently witnessed; saved receipt only','verdict':'CONFIRMED finite paired-output comparison in T1 note69','scope_exclusions':['no peer program executed','no fresh analytic certification','no continuous historical immutability claim','no provider model identity confirmation'],'elapsed_seconds':time.monotonic()-tick}
 with out.open('x')as f:json.dump(d,f,indent=2);f.write('\n')
 print(d['utc'],len(checks),'checks',len(inputs),'bindings',counts,sha(out))
if __name__=='__main__':main()
