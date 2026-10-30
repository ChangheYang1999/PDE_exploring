from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,shlex,ast,sys,time
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parents[3];B=R/'research/candidate020_holdout'
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def main():
 start=time.monotonic();inputs={}
 def bind(p,h=None):
  p=Path(p);d=sha(p);assert h is None or d==h,(p,d,h);inputs[str(p.relative_to(R))]=d;return p
 def read(p,h=None):return json.loads(bind(p,h).read_text())
 prep=read(B/'source/MANIFEST.json');bind(B/'PROOF.md',prep['proof_sha256']);bind(Path(__file__))
 for n,d in prep['files'].items():bind(B/'source'/n,d['sha256'])
 prior=read(R/'research/candidate016_holdout/verification/result.json')
 for p,h in prior['inputs'].items():bind(R/p,h)
 name='C1-N1-020-legqs25p50-quot013';D=R/'research/candidate_audits/data'/name;manifest=read(D/'MANIFEST.json');e=manifest['coefficient_files'][0];rawp=bind(D/e['name'],e['sha256']);raw=read(rawp)
 assert sha(rawp)=='bddbd3120852a815cfe850635564cb09ab52a98ec596a4cce3b72c98cf04f7cf'
 parentD=R/'research/candidate_audits/data/C1-N1-016-legqs25-quot013';pm=read(parentD/'MANIFEST.json');pe=pm['coefficient_files'][0];pp=bind(parentD/pe['name'],pe['sha256']);parent=read(pp)
 assert prior['raw_sha256']==sha(pp) and raw['meta']['parent_json']==pp.name
 assert raw['cl_exact']==parent['cl_exact'] and raw['meta']['added_legqs']=='1,2,3:9:15:50:12'
 shape=lambda g:(g['j'],g['m'],tuple(g['spec']))
 actual=list(map(shape,raw['generators']));old=list(map(shape,parent['generators']));new=[(j,m,('legqs',0,N,4,50)) for j in range(1,4) for m in range(9,16) for N in range(12)]
 assert actual==old+new and len(actual)==len(set(actual))==2426 and len(old)==2174 and len(new)==252
 rank=read(R/'research/joint_scaled_rank_peer/verification/result.json','8652b3c60d9c857f04fd7ee25d93cb7f0739a6719a9934a6a329ef57c96eb8b7')
 for p,h in rank['inputs'].items():bind(R/p,h)
 for d in rank['frozen_sources'].values():bind(R/d['local'],d['stored_sha256'])
 assert rank['verdict'].startswith('CONFIRMED') and rank['potential_dimension']==rank['density_dimension']==2426
 abstract=read(R/'research/joint_scaled_density_rank/verification/abstract_shapes.json');assert actual==list(map(shape,abstract['generators'])) and abstract['c_exact']==raw['cl_exact']
 script=bind(B/'source/N1_chain020.sh').read_text();assert 'export IPM_ADD_LEGQS=1,2,3:9:15:50:12' in script
 lines=[s for s in script.splitlines() if s.startswith('taskset ') and 'run_quot.py' in shlex.split(s)];assert len(lines)==1
 words=shlex.split(lines[0]);args=words[words.index('run_quot.py')+1:]
 rows=[tuple(map(int,s.split(':'))) if ':' in s else (1,int(s)) for s in args[9].split(',')]
 rawrows=[(1,z) if isinstance(z,int) else tuple(z) for z in raw['meta']['pair_k']];prows=[(1,z) if isinstance(z,int) else tuple(z) for z in parent['meta']['pair_k']]
 assert rows==rawrows==prows and len(set(rows))==67 and max(n for n,k in rows)==17
 assert args[0]=='candD2/'+pp.name and int(args[1])==raw['meta']['angular_midpoint']==180 and int(args[2])==raw['meta']['steps']==12 and int(args[5])==raw['meta']['middle_order']==16 and float(args[8])==raw['meta']['wpair']==1e12 and args[10]==raw['meta']['pair_mode']=='penalty'
 text=bind(B/'source/N1_020.out').read_text();assert sha(rawp) in text and 'pair rows 67' in text and 'generators 2426' in text and 'added legqs functions 252' in text
 current=bind(B/'source/N1_run_quot.py').read_text();oldsource=bind(R/'research/candidate019_holdout/source/N1_run_quot.py').read_text();assert current==oldsource;ast.parse(current)
 reg=read(R/'research/heldout_probe_register/verification/register.json');assert datetime.fromisoformat(reg['utc'])<datetime.fromisoformat(manifest['created_utc'].replace('Z','+00:00'))
 probes=[]
 for n,K in reg['pairs']+[[21,522]]:
  assert n>17 and K>=(n-1)//2 and not any(m==n for m,k in rows)
  probes.append({'n':n,'K':K,'outside_span':True,'objective_exponents_at_n':[],'coefficient_of_tK_in_objective_span':0,'member_of_25_register':[n,K] in reg['pairs']})
 out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':name,'raw_sha256':sha(rawp),'parent_sha256':sha(pp),'registration_utc':reg['utc'],'snapshot_utc':manifest['created_utc'],'continuation_rows':len(rows),'generator_count':len(actual),'actual_shapes_match_accepted_rank':True,'potential_dimension':2426,'density_dimension':2426,'historical_scope':'Recorded 007 -> 013 -> quotient -> 016 -> 020 stages only','objective_scope':'Analytic weak-probe rows; no independence from sampled residual information or unrecorded history','probe_rows':probes,'inputs':inputs,'publisher_code_executed':False,'elapsed_seconds':time.monotonic()-start,'status':'CONFIRMED exact candidate-shape identity, recorded row provenance and analytic objective-span separation'}
 with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(out['utc'],out['status'],sha(B/'verification/result.json'),out['elapsed_seconds'])
if __name__=='__main__':main()
