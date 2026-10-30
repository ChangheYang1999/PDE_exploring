"""Literal completion and finite selection, no field evaluation or peer code."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from hashlib import sha256
import json,re,time,os
R=Path(__file__).resolve().parents[3];B=R/'research/numerics_final_repairs'
sha=lambda p:sha256(p.read_bytes()).hexdigest()
def main():
 start=time.monotonic();inputs={};checks={}
 assert os.sched_getaffinity(0)=={57} and os.getpriority(os.PRIO_PROCESS,0)==19
 def bind(p,h=None):
  assert p.resolve().is_relative_to(R)
  v=sha(p);assert h is None or h==v,(str(p),h,v)
  k=str(p.relative_to(R));assert k not in inputs or inputs[k]==v;inputs[k]=v
  return p
 def load(p,h=None):return json.loads(bind(p,h).read_text())
 def check(k,v):assert k not in checks;checks[k]=bool(v);assert v,k
 marker=load(B/'verification/PROOF_FIRST_v03.json')
 check('proof_before_code',not marker['checker_exists'] and not marker['result_exists'])
 bind(B/'LITERAL_COMPLETION_PROOF_v03.md',marker['proof_sha256']);bind(Path(__file__))
 for p,e in marker['files'].items():bind(R/p,e['sha256'])
 repair=load(B/'verification/result_v02.json','b18059380aec73b7e387bc40013d7f9d4420f47175d0ae17662b7e57a65d42b7')
 for p,h in repair['inputs'].items():bind(R/p,h)
 old=load(R/'research/numerics_final_literal_audit/verification/result_v02.json','8158262abd44beccee63605aeacf061304b7bbe207abc827b1cdc10ecf28009b')
 recon=load(R/'research/candidate024_hash_reconstruction/verification/result.json','490ad1a4c7bb935c9e8332be8fa3c21d1fe0669f93bddb6ae44620569e962b59')
 check('prior_233_pass',repair['check_count']==233 and all(repair['checks'].values()))
 before=(B/'source/report.md').read_text();after=(B/'source/report_v03.md').read_text()
 a,b=before.splitlines(),after.splitlines();check('same_line_count',len(a)==len(b))
 changed=[(i+1,x,y) for i,(x,y) in enumerate(zip(a,b)) if x!=y]
 check('exactly_two_changed_lines',len(changed)==2)
 phase=next(v for v in changed if '023 at its final endpoint' in v[2])
 registration=next(v for v in changed if v[2].startswith('- Held-out registration:'))
 check('old_scope_errors_present','the four largest values change by 0.94 to 1.04' in phase[1] and 'sha256 in NOTES 09:13Z; the hash cited there, 58586004...' in registration[1])
 check('old_scope_errors_removed','the four largest values change by 0.94 to 1.04' not in phase[2] and 'sha256 in NOTES 09:13Z; the hash cited there, 58586004...' not in registration[2])
 pat=r'\((\d+), (\d+)\) ([0-9.e+\-]+) -> ([0-9.e+\-]+) \(x([0-9.]+)\)'
 rows=re.findall(pat,after);check('same_200_rows',rows==re.findall(pat,before) and len(rows)==200)
 for i,(g,row) in enumerate(zip(rows,old['probe_rows'])):
  expected=(str(row['probe'][0]),str(row['probe'][1]),row['display']['old'],row['display']['new'],row['display']['factor'])
  check(f'row_{i}_transfer',tuple(g)==expected and all(row['nearest_display_checks'].values()))
 ratio={tuple(v['probe']):Q(v['ratio_exact']) for v in old['phase_final_over12_rows']}
 final={tuple(v['probe']):Q(v['new_exact']) for v in old['probe_rows'] if v['comparison']=='023/016'}
 check('complete_25_register',set(ratio)==set(final)=={(n,k) for n in [19,23,25,29,31] for k in [600,900,1200,1800,2400]})
 initial={p:final[p]/ratio[p] for p in final};selected=[(19,1800),(23,2400),(25,2400),(31,2400)]
 for n,p in zip([19,23,25,31],selected):
  check(f'selected_mode_{n}',all(initial[p]>v for q,v in initial.items() if q[0]==n and q!=p))
 ranked=sorted(final,key=final.get,reverse=True)
 check('global_final_four',ranked[:4]==[(19,1800),(19,1200),(19,2400),(23,2400)])
 low,high=min(ratio[p] for p in selected),max(ratio[p] for p in selected)
 check('min_nearest_09389',abs(low-Q('.9389'))<=Q('.00005'))
 check('max_nearest_10109',abs(high-Q('1.0109'))<=Q('.00005'))
 check('selection_literal','the largest value within each of the modes 19, 23, 25 and 31 at the 12-iteration stage' in phase[2])
 check('selected_range_literal','change by factors 0.9389 to 1.0109' in phase[2])
 check('global_literal','the four largest final values on the full register are (19,1800), (19,1200), (19,2400), (23,2400)' in phase[2])
 check('phase_FLOAT_scope','Reading (FLOAT comparison' in phase[2])
 notes=(B/'source/N1_NOTES_v03.md').read_text();worklog=(B/'source/N1_WORKLOG.md').read_text()
 note09=notes.split('## 2026-10-29T09:13Z:',1)[1].split('\n## ',1)[0]
 note11=notes.split('## 2026-10-29T11:00Z:',1)[1].split('\n## ',1)[0]
 log09=next(s for s in worklog.splitlines() if s.startswith('- 2026-10-29T09:13Z'))
 current=recon['current_sha256'];reconstructed=recon['reconstructed_sha256']
 check('current_hash09note',current in note09 and reconstructed not in note09)
 check('current_hash09log',current[:12] in log09 and reconstructed[:8] not in log09)
 check('old_hash11note',reconstructed[:8] in note11)
 check('reconstruction_accepted',all(recon[k] for k in ['hash_matches_claim','one_replacement_only','all_other_bytes_equal','all60_pairs_preserved']))
 check('current_registration_literal','the saved file hashes e171c051..., which is what the 09:13Z note and the WORKLOG print' in registration[2])
 check('reconstructed_registration_literal','the hash 58586004... printed in the 024 snapshot INDEX line and in the 11:00Z note is the reconstructed hash' in registration[2])
 check('save_time_testimony_literal',"the save times are this lane's testimony" in registration[2])
 for p,h in inputs.items():assert sha(R/p)==h,p
 out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'inputs':inputs,'checks':checks,'check_count':len(checks),'display_transfer_count':600,'revised_report_sha256':sha(B/'source/report_v03.md'),'changed_lines':[{'line':i,'before':x,'after':y} for i,x,y in changed],'selected_probes':[list(p) for p in selected],'selected_range_exact':[str(low),str(high)],'final_largest_four':[list(p) for p in ranked[:4]],'initial_exact':{str(p):str(initial[p]) for p in initial},'verdict':'CONFIRMED the two specified literal repairs and all600 unchanged serialized displays','scope':'Finite source values and attribution only. Historical save times remain publisher testimony. No complete report, PDE norm, candidate or existence promotion.'}
 target=B/'verification/result_v03.json'
 with target.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],out['verdict'],'checks',len(checks),'bindings',len(inputs),'seconds',out['elapsed_seconds'],'sha256',sha(target),flush=True)
if __name__=='__main__':main()
