"""Accept T4-395 with its exact current-objective scope."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
from hashlib import sha256
import ast, difflib, gzip, json, shlex, time
R=Path(__file__).resolve().parents[3];B=R/'research/candidate021_shape_peer';P=R.parent/'c1-t4/research'
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def main():
 start=time.monotonic();target=B/'verification/result.json';assert not target.exists()
 op=R/'research/candidate021_holdout/verification/result.json';own=json.loads(op.read_text());paths=[Path(__file__),B/'PROOF.md',B/'verification/PREPARE.json',op]
 for rel,h in own['inputs'].items():p=R/rel;assert sha(p)==h;paths.append(p)
 known={sha(p):p for p in paths};frozen={};bindings={}
 for pp in [R/'research/candidate021_weak_peer/verification/result.json',R/'research/candidate020_weak_peer/verification/result.json']:
  d=json.loads(pp.read_text())
  for rel,e in d['frozen_or_retained_sources'].items():
   if not e['gzip'] and sha(R/rel)==e['stored_sha256']:known[e['sha256']]=R/rel
 def freeze(p,expected=None):
  p=Path(p);blob=p.read_bytes();h=sha256(blob).hexdigest();assert expected is None or h==expected,(p,h,expected)
  if h in known:dest=known[h];compressed=False
  else:
   dest=B/'source'/p.relative_to(P);compressed=len(blob)>1000000
   if compressed:dest=dest.with_name(dest.name+'.gz')
   dest.parent.mkdir(parents=True,exist_ok=True);stored=gzip.compress(blob,mtime=0) if compressed else blob
   if dest.exists():assert dest.read_bytes()==stored
   else:
    with dest.open('xb') as f:f.write(stored)
   if not compressed:known[h]=dest
  frozen[str(dest.relative_to(R))]={'original':str(p),'sha256':h,'stored_sha256':sha(dest),'gzip':compressed};bindings[str(p)]=h
  return json.loads(blob) if p.suffix=='.json' else blob.decode()
 peer=freeze(P/'candidate021_shapes/verification/result.json','e7da2ceadc102d14013f59776f22f0eeef428edb89659fff6573374188cae652')
 data={p:freeze(p,h) for p,h in peer['inputs'].items()};new=data[str(P/'candidate021_shapes/data/candidate021.json')];old=data[str(P/'candidate021_shapes/data/candidate020.json')]
 checks={};shape=lambda g:(g['j'],g['m'],tuple(g['spec']));shapes=list(map(shape,new['generators']));rows=[(1,x) if isinstance(x,int) else tuple(x) for x in new['meta']['pair_k']];before=[(1,x) if isinstance(x,int) else tuple(x) for x in old['meta']['pair_k']]
 prep=json.loads((B/'verification/PREPARE.json').read_text());checks['proof_binding']=sha(B/'PROOF.md')==prep['proof_sha256'] and sha(P/'candidate021_shapes/PROOF.md')==prep['peer_proof_sha256']
 checks['candidate_hash']=own['raw_sha256']==sha(P/'candidate021_shapes/data/candidate021.json')=='c6ed292b9f7129ad236f8441140745ec6accc3918d477ca2268e55bf7efc85c8'
 checks['all_ordered_shapes']=shapes==list(map(shape,old['generators'])) and len(shapes)==len(set(shapes))==2426 and own['actual_shapes_match_accepted_rank'] and peer['all_actual_shapes_match']
 checks['dimensions']=own['potential_dimension']==own['density_dimension']==peer['potential_dimension']==peer['density_dimension']==2426
 checks['exact_c']=Q(new['cl_exact'])==Q(old['cl_exact'])==Q(4076476460239181,2251799813685248)
 checks['current_rows']=rows==[tuple(x) for x in own['exact_objective_rows']]==[tuple(x) for x in peer['recorded_current_objective_rows']] and len(rows)==len(set(rows))==81
 checks['parent_and_added_rows']=len(before)==67 and rows==before+[(n,(n-1)//2+s) for s in [128,512] for n in range(19,32,2)]
 probes=[tuple(x) for x in peer['outside_current_analytic_span']];ourprobes={(r['n'],r['K']) for r in own['probe_rows'] if r['outside_span']}
 checks['all_46_probes']=len(probes)==len(set(probes))==46 and set(probes)==ourprobes and all((n,K) not in rows and n>0 and n%2 and K>=(n-1)//2 for n,K in probes)
 checks['registered_25']=set((n,K) for n in [19,23,25,29,31] for K in [600,900,1200,1800,2400])=={(r['n'],r['K']) for r in own['probe_rows'] if r['member_of_25_register']}
 checks['heldin_21_522']=(21,522) in rows and peer['probe_21_522_in_objective'] and own['probe_21_522_is_objective_row']
 def text(name):return data[str(P/'candidate021_shapes/source'/name)]
 lines=[s for s in text('N1_chain021.sh').splitlines() if s.startswith('taskset ') and 'run_quot.py' in shlex.split(s)];checks['one_launch']=len(lines)==1;words=shlex.split(lines[0]);args=words[words.index('run_quot.py')+1:]
 launch=[tuple(map(int,s.split(':'))) if ':' in s else (1,int(s)) for s in args[9].split(',')]
 checks['launch_metadata']=launch==rows and args[0]=='candD2/'+new['meta']['parent_json'] and new['meta']['parent_json']=='quot013_legqs25p50_m9to15_cpu_m16_exact.json' and int(args[1])==new['meta']['angular_midpoint']==180 and int(args[2])==new['meta']['steps']==40 and int(args[5])==new['meta']['middle_order']==16 and Q(args[8])==Q(str(new['meta']['wpair']))==10**12 and args[10]==new['meta']['pair_mode']=='penalty' and new['meta']['added_legqs'] is None
 log=text('N1_021.out');checks['completed_log']=own['raw_sha256'] in log and 'pair rows 81' in log and 'generators 2426' in log and 'it  40 ' in log
 sources=[text('N1_run_quot020.py'),text('N1_run_quot.py')];asts=[]
 for i,source in enumerate(sources):
  tree=ast.parse(source);pair=[n for n in ast.walk(tree) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='PAIRK' for t in n.targets)];parsers=[n for n in ast.walk(tree) if isinstance(n,ast.FunctionDef) and n.name=='_parse'];assert len(pair)==len(parsers)==1
  asts.append([ast.dump(pair[0],include_attributes=False),ast.dump(parsers[0],include_attributes=False)])
  calls=[n for n in ast.walk(tree) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=='Problem3'];checks[f'actual_parser_binding_{i}']=len(calls)==1 and any(k.arg=='pair_k' and isinstance(k.value,ast.Name) and k.value.id=='PAIRK' for k in calls[0].keywords)
 checks['parser_unchanged']=asts[0]==asts[1] and peer['PAIRK_parser_unchanged']
 delta=''.join(difflib.unified_diff(sources[0].splitlines(True),sources[1].splitlines(True),fromfile='frozen_parent020',tofile='inspected_current021'));checks['complete_source_diff']=delta==text('current_source_delta.diff') and peer['source_delta_reproduced']
 checks['historical_boundary']='Earlier historical launches not replayed.' in peer['historical_scope'] and not peer['publisher_code_executed'] and not own['publisher_code_executed']
 rank=data[str(P/'joint_scaled_rank_audit/verification/result.json')];prior=data[str(P/'candidate020_shapes/verification/result.json')]
 checks['accepted_rank_graph']=rank['potential_dimension']==rank['density_dimension']==prior['potential_dimension']==prior['density_dimension']==2426 and before==[tuple(r) for r in prior['recorded_current_objective_rows']]
 assert all(checks.values()),{k:v for k,v in checks.items() if not v}
 for rel,e in frozen.items():assert sha(R/rel)==e['stored_sha256']
 out={'utc':datetime.now(timezone.utc).isoformat(),'checks':checks,'check_count':len(checks),'peer_input_bindings':bindings,'frozen_or_retained_sources':frozen,'own_inputs':{str(p.relative_to(R)):sha(p) for p in paths},'generator_count':len(shapes),'potential_dimension':2426,'density_dimension':2426,'current_rows':rows,'outside_current_analytic_span':probes,'historical_scope':peer['historical_scope'],'foreign_code_executed':False,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED N4-315 via T4-395 for all actual021 shapes and current81-row objective,46 absent probes; no new independent audit of earlier007-to013 launches'}
 with target.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print('CONFIRMED',len(checks),'checks',len(bindings),'bindings',sha(target),'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
