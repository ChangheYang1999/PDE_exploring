from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction as Q
import json,shlex,ast,time
B=Path(__file__).resolve().parents[1];R=B.parent
hash=lambda p:sha256(p.read_bytes()).hexdigest()
def main():
 start=time.monotonic();inputs={}
 def read(p,h=None):
  d=hash(p);assert h is None or d==h,(p,d,h);inputs[str(p)]=d
  return json.loads(p.read_text())
 raw=read(B/'data/candidate020.json','bddbd3120852a815cfe850635564cb09ab52a98ec596a4cce3b72c98cf04f7cf')
 parent=read(B/'data/parent016.json','a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42')
 rank=read(R/'joint_scaled_rank_audit/verification/result.json','0d167869fb0d49e68a7cc2bcbc2a29420629eccf43f3c5c57651d73129755aa9')
 for name,d in rank['inputs'].items():assert hash(Path(name))==d;inputs[name]=d
 abstract=read(R/'joint_scaled_rank_audit/source/N4_shapes.json')
 assert rank['potential_dimension']==rank['density_dimension']==2426
 shape=lambda g:(g['j'],g['m'],tuple(g['spec']))
 actual=list(map(shape,raw['generators']));old=list(map(shape,parent['generators']))
 new=[(j,m,('legqs',0,N,4,50)) for j in range(1,4) for m in range(9,16) for N in range(12)]
 assert actual==old+new==list(map(shape,abstract['generators']))
 assert len(actual)==len(set(actual))==2426 and len(old)==2174 and len(new)==252
 assert Q(raw['cl_exact'])==Q(parent['cl_exact'])==Q(abstract['c_exact'])==Q(4076476460239181,2251799813685248)
 rows=[(1,z) if isinstance(z,int) else tuple(z) for z in raw['meta']['pair_k']]
 expected=[(1,K) for K in [0,1,2,3,4,5,6,7,8,12,16,24,32,48,64,96,128,192,256,384,512,768,1024,1536,2048,3072,4096]]+[(n,(n-1)//2+s) for n in range(3,18,2) for s in [0,8,32,128,512]]
 assert rows==expected and len(set(rows))==67
 script=(B/'source/N1_chain020.sh').read_text();lines=[s for s in script.splitlines() if s.startswith('taskset ') and 'run_quot.py' in shlex.split(s)];assert len(lines)==1
 words=shlex.split(lines[0]);args=words[words.index('run_quot.py')+1:]
 launchrows=[tuple(map(int,s.split(':'))) if ':' in s else (1,int(s)) for s in args[9].split(',')]
 assert launchrows==rows and args[0]=='candD2/'+raw['meta']['parent_json'] and raw['meta']['parent_json']=='quot013_legqs25_m9to15_cpu_m16_exact.json'
 assert int(args[1])==raw['meta']['angular_midpoint']==180 and int(args[2])==raw['meta']['steps']==12 and int(args[5])==raw['meta']['middle_order']==16
 assert Q(args[8])==Q(str(raw['meta']['wpair']))==10**12 and args[10]==raw['meta']['pair_mode']=='penalty'
 assert raw['meta']['added_legqs']=='1,2,3:9:15:50:12' and 'export IPM_ADD_LEGQS='+raw['meta']['added_legqs'] in script
 log=(B/'source/N1_020.out').read_text();assert hash(B/'data/candidate020.json') in log and 'pair rows 67' in log and 'generators 2426' in log and 'it  12 ' in log
 ast.parse((B/'source/N1_run_quot.py').read_text())
 probes=[(n,K) for n in [19,23,25,29,31] for K in [600,900,1200,1800,2400]]+[(21,522)]
 assert all(n>max(m for m,k in rows) and K>=(n-1)//2 for n,K in probes)
 peer=read(B/'source/N4_result.json');assert peer['actual_shapes_match_accepted_rank'] and peer['raw_sha256']==hash(B/'data/candidate020.json')
 for p in [B/'PROOF.md',Path(__file__),B/'source/N1_chain020.sh',B/'source/N1_020.out',B/'source/N1_run_quot.py',B/'source/N4_PROOF.md']:inputs[str(p)]=hash(p)
 result={'utc':datetime.now(timezone.utc).isoformat(),'inputs':inputs,'potential_dimension':2426,'density_dimension':2426,'all_actual_shapes_match':True,'parent016_prefix':2174,'appended_R50':252,'recorded_current_objective_rows':rows,'outside_current_analytic_span':probes,'historical_scope':'Current020 metadata, displayed launch and completed log only. Earlier history not independently replayed.','publisher_code_executed':False,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED actual dimension and current analytic objective-span separation'}
 with (B/'verification/result.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
 print(result['utc'],result['verdict'],hash(B/'verification/result.json'))
if __name__=='__main__':main()
