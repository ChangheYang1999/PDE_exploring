from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,shlex,ast,sys
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[3]; B=ROOT/'research/candidate019_holdout'
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def main():
 inputs={}
 def bind(p,h=None):
  p=Path(p);d=sha(p);assert h is None or d==h,(p,d,h);inputs[str(p.relative_to(ROOT))]=d;return p
 def read(p):return json.loads(bind(p).read_text())
 prep=read(B/'source/MANIFEST.json');bind(B/'PROOF.md',prep['proof_sha256']);bind(Path(__file__))
 for n,d in prep['files'].items():bind(B/'source'/n,d['sha256'])
 prior=read(ROOT/'research/candidate017_holdout/verification/result.json')
 for p,h in prior['inputs'].items():bind(ROOT/p,h)
 name='C1-N1-019-legqs50-cont12';D=ROOT/'research/candidate_audits/data'/name;manifest=read(D/'MANIFEST.json');e=manifest['coefficient_files'][0];rawp=bind(D/e['name'],e['sha256']);raw=read(rawp)
 parentD=ROOT/'research/candidate_audits/data/C1-N1-017-legqs50-quot013';pm=read(parentD/'MANIFEST.json');pe=pm['coefficient_files'][0];pp=bind(parentD/pe['name'],pe['sha256']);parent=read(pp)
 assert prior['raw_sha256']==sha(pp) and raw['meta']['parent_json']==pp.name
 assert raw['cl_exact']==parent['cl_exact'] and raw['meta']['added_legqs'] is None
 shape=lambda g:(g['j'],g['m'],tuple(g['spec']))
 assert list(map(shape,raw['generators']))==list(map(shape,parent['generators'])) and len(raw['generators'])==2174
 script=bind(B/'source/N1_chain019.sh').read_text();assert 'IPM_ADD_LEGQS=' not in script
 lines=[s for s in script.splitlines() if s.startswith('taskset ') and 'run_quot.py' in shlex.split(s)];assert len(lines)==1
 words=shlex.split(lines[0]);args=words[words.index('run_quot.py')+1:]
 rows=[tuple(map(int,s.split(':'))) if ':' in s else (1,int(s)) for s in args[9].split(',')]
 rawrows=[(1,z) if isinstance(z,int) else tuple(z) for z in raw['meta']['pair_k']]
 prows=[(1,z) if isinstance(z,int) else tuple(z) for z in parent['meta']['pair_k']]
 assert rows==rawrows==prows and len(set(rows))==67 and max(n for n,k in rows)==17
 assert args[0]=='candD2/'+pp.name and int(args[2])==raw['meta']['steps']==12 and float(args[8])==raw['meta']['wpair']==1e12 and args[10]==raw['meta']['pair_mode']=='penalty'
 text=bind(B/'source/N1_019.out').read_text();assert sha(rawp) in text and 'pair rows 67' in text and 'generators 2174' in text
 current=bind(B/'source/N1_run_quot.py').read_text();old=bind(ROOT/'research/candidate017_holdout/source/N1_run_quot.py').read_text();assert current==old;ast.parse(current)
 reg=read(ROOT/'research/heldout_probe_register/verification/register.json');assert datetime.fromisoformat(reg['utc'])<datetime.fromisoformat(manifest['created_utc'].replace('Z','+00:00'))
 probes=[]
 for n,K in reg['pairs']+[[21,522]]:
  assert n>17 and K>=(n-1)//2 and not any(m==n for m,k in rows)
  probes.append({'n':n,'K':K,'outside_span':True,'objective_exponents_at_n':[],'coefficient_of_tK_in_objective_span':0,'member_of_25_register':[n,K] in reg['pairs']})
 out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':name,'raw_sha256':sha(rawp),'parent_sha256':sha(pp),'registration_utc':reg['utc'],'snapshot_utc':manifest['created_utc'],'continuation_rows':len(rows),'historical_scope':'Recorded 007 -> 013 -> quotient -> 017 -> 019 stages only','objective_scope':'Analytic weak-probe rows; no independence from sampled residual information or unrecorded history','probe_rows':probes,'inputs':inputs,'publisher_code_executed':False,'status':'CONFIRMED exact continuation-row provenance and analytic objective-span separation'}
 with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],out['status'],sha(B/'verification/result.json'))
if __name__=='__main__':main()
