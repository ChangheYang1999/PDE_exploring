from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,shlex,ast,sys,time,difflib
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parents[3];B=R/'research/candidate021_holdout';sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def main():
 start=time.monotonic();inputs={};checks={}
 def bind(p,h=None):
  p=Path(p);d=sha(p);assert h is None or d==h,(p,d,h);inputs[str(p.relative_to(R))]=d;return p
 def read(p,h=None):return json.loads(bind(p,h).read_text())
 prep=read(B/'source/MANIFEST.json');bind(B/'PROOF.md',prep['proof_sha256']);bind(Path(__file__),prep['code_sha256'])
 for name,v in prep['files'].items():bind(B/'source'/name,v['sha256'])
 prior=read(R/'research/candidate020_holdout/verification/result.json');assert prior['status'].startswith('CONFIRMED')
 for path,h in prior['inputs'].items():bind(R/path,h)
 name='C1-N1-021-heldin14-legqs25p50';D=R/'research/candidate_audits/data'/name;m=read(D/'MANIFEST.json');assert m['id']==name and len(m['coefficient_files'])==1;e=m['coefficient_files'][0];rawp=bind(D/e['name'],e['sha256']);raw=read(rawp)
 assert sha(rawp)=='c6ed292b9f7129ad236f8441140745ec6accc3918d477ca2268e55bf7efc85c8'
 PD=R/'research/candidate_audits/data/C1-N1-020-legqs25p50-quot013';pm=read(PD/'MANIFEST.json');pe=pm['coefficient_files'][0];pp=bind(PD/pe['name'],pe['sha256']);parent=read(pp)
 assert prior['raw_sha256']==sha(pp) and raw['meta']['parent_json']==pp.name and raw['cl_exact']==parent['cl_exact']=='4076476460239181/2251799813685248';checks['exact_c_and_parent']=True
 shape=lambda g:(g['j'],g['m'],tuple(g['spec']));actual=list(map(shape,raw['generators']));old=list(map(shape,parent['generators']));assert actual==old and len(actual)==len(set(actual))==2426 and raw['meta']['added_legqs'] is None;checks['all2426_shapes_unchanged']=True
 assert prior['actual_shapes_match_accepted_rank'] and prior['potential_dimension']==prior['density_dimension']==2426;checks['accepted_rank_hypotheses_bound']=True
 priorrows=[(1,k) if isinstance(k,int) else tuple(k) for k in parent['meta']['pair_k']];new=[(n,(n-1)//2+s) for s in [128,512] for n in range(19,32,2)];expected=priorrows+new
 script=bind(B/'source/N1_chain021.sh').read_text();frozen=bind(R/'research/expanded_objective_span/data/N1_chain021.sh').read_text();assert script==frozen
 lines=[line for line in script.splitlines() if line.startswith('taskset ') and 'run_quot.py' in shlex.split(line)];assert len(lines)==1;words=shlex.split(lines[0]);args=words[words.index('run_quot.py')+1:];rows=[tuple(map(int,s.split(':'))) if ':' in s else (1,int(s)) for s in args[9].split(',')];rawrows=[(1,k) if isinstance(k,int) else tuple(k) for k in raw['meta']['pair_k']]
 assert rows==rawrows==expected and len(priorrows)==67 and len(rows)==len(set(rows))==81 and all(n%2==1 and K>=(n-1)//2 for n,K in rows);checks['complete81_rows_and14_difference']=True
 assert args[0]=='candD2/'+pp.name and int(args[1])==raw['meta']['angular_midpoint']==180 and int(args[2])==raw['meta']['steps']==40 and int(args[5])==raw['meta']['middle_order']==16 and float(args[8])==raw['meta']['wpair']==1e12 and args[10]==raw['meta']['pair_mode']=='penalty';checks['recorded_run_parameters']=True
 log=bind(B/'source/N1_021.out').read_text();assert sha(rawp) in log and 'pair rows 81 weight 1000000000000.0' in log and 'generators 2426' in log and 'it  40 obj ' in log and 'per-row weights:' not in log;checks['completed_log_matches_immutable_output']=True
 before=bind(R/'research/candidate020_holdout/source/N1_run_quot.py').read_text();after=bind(B/'source/N1_run_quot.py').read_text();ast.parse(before);ast.parse(after);assert before!=after
 parser="PAIRK = tuple(_parse(x) for x in sys.argv[10].split(','))";assert parser in before and parser in after and 'pair_k=PAIRK' in before and 'pair_k=PAIRK' in after and "IPM_NHELDIN" not in before and "IPM_NHELDIN" in after
 diff=''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='frozen_parent020',tofile='inspected_current021'));(B/'verification/current_source_delta.diff').write_text(diff);bind(B/'verification/current_source_delta.diff');checks['current_source_change_explicitly_retained']=True
 impl=bind(B/'source/N1_ipm_opt3.py').read_text();ast.parse(impl);assert 'for q, w in zip(self.pair_k, ws)' in impl and 'phi_(n,K)' in impl;checks['probe_list_passed_without_added_rows']=True
 reg=read(R/'research/heldout_probe_register/verification/register.json');assert datetime.fromisoformat(reg['utc'])<datetime.fromisoformat('2026-10-29T08:32:00+00:00')<datetime.fromisoformat(m['created_utc'].replace('Z','+00:00'));checks['public25_register_predates_launch']=True
 probes=[]
 for n,K in reg['pairs']+[[n,(n-1)//2+s] for n in range(19,32,2) for s in [0,8,32]]:
  exps=sorted(k for j,k in rows if j==n);assert n%2 and K>=(n-1)//2 and K not in exps
  probes.append({'n':n,'K':K,'outside_span':True,'objective_exponents_at_n':exps,'coefficient_of_tK_in_objective_span':0,'member_of_25_register':[n,K] in reg['pairs']})
 assert len(probes)==46 and (21,522) in rows;checks['all46_outside_and21_522_is_design']=True
 out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':name,'raw_sha256':sha(rawp),'parent_sha256':sha(pp),'registration_utc':reg['utc'],'snapshot_utc':m['created_utc'],'continuation_rows':81,'exact_objective_rows':[list(x) for x in rows],'generator_count':2426,'actual_shapes_match_accepted_rank':True,'potential_dimension':2426,'density_dimension':2426,'historical_scope':'Recorded007->013->quotient->016->020->021 only; current source bytes differ and are not asserted historical','objective_scope':'Analytic weak rows only; no independence from sampled residual data or unrecorded history','probe_rows':probes,'probe_21_522_is_objective_row':True,'inputs':inputs,'publisher_code_executed':False,'checks':checks,'check_count':len(checks),'elapsed_seconds':time.monotonic()-start,'status':'PASS exact actual shapes, recorded81-row history and polynomial span separation; new expanded-span proof independent review OPEN'}
 with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print('PASS',out['utc'],sha(B/'verification/result.json'),'checks',len(checks),'bindings',len(inputs),'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
