from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
import ast, difflib, hashlib, json, shlex, time
B=Path(__file__).resolve().parents[1]
R=B.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()

def main():
 start=time.monotonic();inputs={}
 def read(p,h=None):
  d=sha(p);assert h is None or d==h,(p,d,h);inputs[str(p)]=d
  return json.loads(p.read_text())
 new=read(B/'data/candidate021.json','c6ed292b9f7129ad236f8441140745ec6accc3918d477ca2268e55bf7efc85c8')
 old=read(B/'data/candidate020.json','bddbd3120852a815cfe850635564cb09ab52a98ec596a4cce3b72c98cf04f7cf')
 prior=read(R/'candidate020_shapes/verification/result.json')
 rank=read(R/'joint_scaled_rank_audit/verification/result.json','0d167869fb0d49e68a7cc2bcbc2a29420629eccf43f3c5c57651d73129755aa9')
 for source in [prior,rank]:
  for p,h in source['inputs'].items():assert sha(Path(p))==h;inputs[p]=h
 assert prior['potential_dimension']==prior['density_dimension']==2426
 assert rank['potential_dimension']==rank['density_dimension']==2426
 shape=lambda g:(g['j'],g['m'],tuple(g['spec']))
 shapes=list(map(shape,new['generators']))
 assert shapes==list(map(shape,old['generators']))
 assert len(shapes)==len(set(shapes))==2426
 assert Q(old['cl_exact'])==Q(new['cl_exact'])==Q(4076476460239181,2251799813685248)
 parse_rows=lambda d:[(1,x) if isinstance(x,int) else tuple(x) for x in d['meta']['pair_k']]
 rows=parse_rows(new);before=parse_rows(old)
 extra=[(n,(n-1)//2+s) for s in [128,512] for n in range(19,32,2)]
 assert rows==before+extra and len(rows)==len(set(rows))==81
 assert before==[tuple(x) for x in prior['recorded_current_objective_rows']]
 script=(B/'source/N1_chain021.sh').read_text()
 lines=[s for s in script.splitlines() if s.startswith('taskset ') and 'run_quot.py' in shlex.split(s)]
 assert len(lines)==1
 words=shlex.split(lines[0]);args=words[words.index('run_quot.py')+1:]
 launch=[tuple(map(int,s.split(':'))) if ':' in s else (1,int(s)) for s in args[9].split(',')]
 assert launch==rows and args[0]=='candD2/'+new['meta']['parent_json']
 assert new['meta']['parent_json']=='quot013_legqs25p50_m9to15_cpu_m16_exact.json'
 assert int(args[1])==new['meta']['angular_midpoint']==180
 assert int(args[2])==new['meta']['steps']==40
 assert int(args[5])==new['meta']['middle_order']==16
 assert Q(args[8])==Q(str(new['meta']['wpair']))==10**12
 assert args[10]==new['meta']['pair_mode']=='penalty'
 assert new['meta']['added_legqs'] is None
 log=(B/'source/N1_021.out').read_text()
 assert sha(B/'data/candidate021.json') in log and 'pair rows 81' in log
 assert 'generators 2426' in log and 'it  40 ' in log
 a=(B/'source/N1_run_quot020.py').read_text()
 b=(B/'source/N1_run_quot.py').read_text()
 trees=[ast.parse(s) for s in [a,b]]
 rowspec=[]
 for tree in trees:
  pair=[node for node in ast.walk(tree) if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='PAIRK' for t in node.targets)]
  parsers=[node for node in ast.walk(tree) if isinstance(node,ast.FunctionDef) and node.name=='_parse']
  assert len(pair)==len(parsers)==1
  rowspec.append([ast.dump(pair[0],include_attributes=False),ast.dump(parsers[0],include_attributes=False)])
  calls=[node for node in ast.walk(tree) if isinstance(node,ast.Call) and isinstance(node.func,ast.Attribute) and node.func.attr=='Problem3']
  assert len(calls)==1
  assert any(k.arg=='pair_k' and isinstance(k.value,ast.Name) and k.value.id=='PAIRK' for k in calls[0].keywords)
 assert rowspec[0]==rowspec[1]
 delta=''.join(difflib.unified_diff(a.splitlines(True),b.splitlines(True),fromfile='frozen_parent020',tofile='inspected_current021'))
 assert delta==(B/'source/current_source_delta.diff').read_text()
 probes=[(n,K) for n in [19,23,25,29,31] for K in [600,900,1200,1800,2400]]
 probes += [(n,(n-1)//2+s) for n in range(19,32,2) for s in [0,8,32]]
 assert len(probes)==len(set(probes))==46
 assert all((n,K) not in rows and K>=(n-1)//2 for n,K in probes)
 assert (21,522) in rows
 peer=read(B/'source/N4_result.json')
 assert peer['actual_shapes_match_accepted_rank'] and peer['raw_sha256']==sha(B/'data/candidate021.json')
 assert [tuple(x) for x in peer['exact_objective_rows']]==rows
 for p in [B/'PROOF.md',Path(__file__),*sorted((B/'source').iterdir())]:inputs[str(p)]=sha(p)
 result={'utc':datetime.now(timezone.utc).isoformat(),'inputs':inputs,'potential_dimension':2426,'density_dimension':2426,
 'all_actual_shapes_match':True,'recorded_current_objective_rows':rows,'outside_current_analytic_span':probes,
 'probe_21_522_in_objective':True,'PAIRK_parser_unchanged':True,'source_delta_reproduced':True,
 'historical_scope':'Current021 metadata, launch and completed output, with accepted020 current-objective and rank evidence. Earlier historical launches not replayed.',
 'publisher_code_executed':False,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED actual dimension and current analytic objective-span separation'}
 with (B/'verification/result.json').open('x') as out:json.dump(result,out,indent=2);out.write('\n')
 print(result['utc'],result['verdict'],sha(B/'verification/result.json'))
if __name__=='__main__':main()
