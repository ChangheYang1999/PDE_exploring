"""Verify the recorded objective lists as data; execute no publisher code."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,shlex,ast
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/candidate016_holdout'
SRC=ROOT/'research/heldout_probe_register/source'
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
inputs={}
def bind(p):
 p=Path(p);inputs[str(p.relative_to(ROOT))]=sha(p);return p
def read(p):return json.loads(bind(p).read_text())
def candidate(name):
 d=ROOT/'research/candidate_audits/data'/name;m=read(d/'MANIFEST.json')
 p=bind(d/m['coefficient_files'][0]['name']);assert sha(p)==m['coefficient_files'][0]['sha256']
 return m,p,read(p)
def command(filename,program,index):
 path=BASE/'source'/filename;path=path if path.exists() else SRC/filename
 text=bind(path).read_text();lines=[x for x in text.splitlines() if x.startswith('taskset ') and program in shlex.split(x)]
 assert len(lines)==1;words=shlex.split(lines[0]);args=words[words.index(program)+1:]
 raw=args[index];probes=[]
 for token in raw.split(','):
  pair=tuple(map(int,token.split(':'))) if ':' in token else (1,int(token))
  assert len(pair)==2;probes.append(pair)
 return args,probes,text
def rows(meta):return [(1,x) if isinstance(x,int) else tuple(x) for x in meta['pair_k']]
def main():
 current=read(BASE/'source/MANIFEST.json')
 for rel,entry in current['files'].items():assert sha(bind(ROOT/rel))==entry['sha256']
 assert sha(BASE/'source/N1_run_quot.py')==sha(SRC/'N1_run_quot.py')
 frozen=read(SRC/'FROZEN_015.json')
 for rel,entry in frozen['files'].items():assert sha(bind(ROOT/rel))==entry['sha256']
 reg=read(ROOT/'research/heldout_probe_register/verification/register.json')
 proof=bind(ROOT/'research/heldout_probe_register/PROOF.md');assert sha(proof)==reg['proof_sha256']
 m7,p7,d7=candidate('C1-N1-007-d2w-j7-e2bal')
 m13,p13,d13=candidate('C1-N1-013-pairU-from007')
 name='C1-N1-016-legqs25-quot013';m15,p15,d15=candidate(name)
 a13,r13,t13=command('N1_chainI_core54_cpu.sh','run_pair.py',15)
 a15,r15,t15=command('N1_chain016_core54_cpu.sh','run_quot.py',9)
 assert r13==rows(d13['meta']) and r15==rows(d15['meta'])
 assert len(r13)==27 and len(r15)==67 and len(set(r15))==67 and set(r13)<=set(r15)
 assert all(n==1 for n,k in r13)
 expected=[(n,(n-1)//2+s) for n in range(3,18,2) for s in [0,8,32,128,512]]
 assert [x for x in r15 if x[0]!=1]==expected
 assert a13[7]=='candD2/'+d7['meta']['tag']+'_coefs.npy'
 assert a15[0]=='candD2/'+d15['meta']['parent_json']
 assert 'IPM_ADD_LEGQS=1,2,3:9:15:25:12' in t15 and d15['meta']['added_legqs']=='1,2,3:9:15:25:12'
 added=[g for g in d15['generators'] if g['spec'][0]=='legqs']
 assert len(added)==252 and {(g['j'],g['m'],tuple(g['spec'])) for g in added}=={(j,m,('legqs',0,n,4,25)) for j in range(1,4) for m in range(9,16) for n in range(12)}
 assert int(a13[3])==d13['meta']['steps']==12 and int(a15[2])==d15['meta']['steps']==12
 assert float(a13[14])==d13['meta']['wpair'] and float(a15[8])==d15['meta']['wpair']
 for p,filename,count in [(p13,'N1_d2w_j7_n4_E2bal_pairU_cpu_m16.out',27),(p15,'N1_016.out',67)]:
  path=BASE/'source'/filename;path=path if path.exists() else SRC/filename
  text=bind(path).read_text();assert sha(p) in text and 'pair rows '+str(count) in text
 qp=ROOT/'research/optimizer_quotient_audit/source/N1_013_quot_exact.json';q=read(qp)
 assert q['meta']['quotient_of']==p13.name==d15['meta']['quotient_meta']
 assert q['meta']['quotient_of_sha256']==sha(p13)
 qa=read(ROOT/'research/optimizer_quotient_audit/verification/result.json')
 for rel,digest in qa['inputs'].items():assert sha(bind(ROOT/rel))==digest
 selected=[r for r in qa['rows'] if r['candidate']==m13['id']];assert len(selected)==1
 assert selected[0]['all_canonical_coefficients_equal'] and selected[0]['new_source_sha256']==sha(qp)
 assert qa['inputs'][str(p13.relative_to(ROOT))]==sha(p13)
 assert datetime.fromisoformat(reg['utc'])<datetime.fromisoformat(m15['created_utc'].replace('Z','+00:00'))
 # Parsing ensures the frozen files inspected for the analytic row construction are intact Python.
 for filename in ['N1_ipm_opt3.py','N1_ipm_opt2.py','N1_run_quot.py','N1_run_pair.py']:
  ast.parse(bind(SRC/filename).read_text(),filename)
 lib=(SRC/'N1_ipm_opt3.py').read_text()
 assert 'return base*r*u0**2*t**K*torch.sin(n*th)' in lib
 assert 'return base*y*t**q*u0**2' in lib
 for e in m15['evaluator_code']:
  if Path(e['path']).name=='ipm_opt2.py':assert sha(SRC/'N1_ipm_opt2.py')==e['sha256']
 probes=[]
 for n,K in reg['pairs']+[[21,522]]:
  exponents=sorted(k for m,k in r15 if m==n)
  assert not exponents
  probes.append({'n':n,'K':K,'objective_exponents_at_n':exponents,'coefficient_of_tK_in_objective_span':0,'outside_span':True,'member_of_25_register':[n,K] in reg['pairs']})
 bind(Path(__file__));bind(BASE/'PROOF.md')
 result={'utc':datetime.now(timezone.utc).isoformat(),'candidate':name,'raw_sha256':sha(p15),
 'registration_utc':reg['utc'],'snapshot_utc':m15['created_utc'],'stage013_rows':len(r13),'stage016_rows':len(r15),
 'historical_scope':'Recorded 007 -> 013 -> exact quotient -> 016 stages; 007 is the initial input. No earlier or unrecorded campaign claim.',
 'objective_scope':'Analytic weak-probe span only, not all information in sampled residual objectives or statistical independence.',
 'probe_rows':probes,'inputs':inputs,'publisher_code_executed':False,'status':'CONFIRMED explicit polynomial coefficient test and recorded objective provenance'}
 with (BASE/'verification/result.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print('CONFIRMED',len(probes),'outside declared67-row span',sha(BASE/'verification/result.json'))
if __name__=='__main__':main()
